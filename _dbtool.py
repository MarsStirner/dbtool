#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import logging
import os
import re
import MySQLdb
import codecs
from glob import glob
from ConfigParser import ConfigParser, Error as ConfigError
from utils import tools


def get_config(filename):
    p = ConfigParser(defaults={'port': '3306',
                               'develop_version': False})
    with codecs.open(filename, 'r', 'utf-8-sig') as f:
        p.readfp(f)
    return {
        'host': p.get('database', 'host'),
        'port': p.get('database', 'port'),
        'username': p.get('database', 'username'),
        'password': p.get('database', 'password'),
        'dbname': p.get('database', 'dbname'),
        'definer': p.get('database', 'definer'),
        'content': p.get('content', 'content_type'),
        'log_filename': p.get('misc', 'log_filename'),
        'develop_version': p.get('misc', 'develop_version'),
    }


class Session(object):
    _conn = None
    _conf = None

    @classmethod
    def setConf(cls, filename):
        try:
            cls._conf = get_config(filename)
        except ConfigError, e:
            raise ConfigException('config file "{0}": {1}'.format(filename, e))
        if not cls._conf['log_filename']:
            raise ConfigException('в конфигурационном файле должен быть задан путь для файла лога '
                                  ' (параметр log_filename)')

    @classmethod
    def checkConf(cls):
        if not cls._conf:
            raise AttributeError('Set config first')
        if cls._conf['content'] not in ('common', 'fnkc', 'pnz'):
            raise ConfigException('Неверное значение для content_type в конфигурационном файле. '
                                  'Поддерживаемые значения: common, fnkc, pnz')

    @classmethod
    def getConf(cls):
        return cls._conf

    @classmethod
    def getConnection(cls):
        if cls._conn is not None:
            return cls._conn
        if not cls._conf:
            raise AttributeError('Set config first')
        c = MySQLdb.connect(host=cls._conf['host'],
            port=int(cls._conf['port']),
            user=cls._conf['username'],
            passwd=cls._conf['password'],
            db=cls._conf['dbname'],
            charset='utf8',
            use_unicode=True)
        cls._conn = c
        c.autocommit(False)
        return c

    @classmethod
    def closeConnection(cls):
        if cls._conn:
            cls._conn.close()


class DBToolException(Exception): pass

class ConfigException(Exception): pass


class DBTool(object):

    def __init__(self):
        self.conf = None
        self.connection = None
        self.db_version = None
        self.content_version = None
        self.schema_updates = None
        self.content_updates = None

    def load(self):
        self.conf = Session.getConf()
        self._load_versions()
        if self.conf.get('develop_version') and not self.develop_version:
            connection = self._getConnection()
            with connection as cursor:
                cursor.execute('''INSERT INTO `Meta` (`name`, `value`) VALUES (%s, %s) ''', ('develop_version', 'True'))
                connection.commit()

    def _getConnection(self):
        # XXX: MySQL не поддерживает транзакации для некоторых выражений
        # DDL, например для "create table", так что транзакции здесь не
        # всегда гарантируют консистентное состояние БД при ошибках
        # обновления
        return Session.getConnection()

    def _load_versions(self):
        try:
            with self._getConnection() as cursor:
                cursor.execute('SELECT name, value FROM Meta')
                d = dict(cursor.fetchall())
                try:
                    self.db_version = int(d.get('schema_version', 0))
                    self.content_version = int(d.get('content_version', 0))
                    self.develop_version = bool(d.get('develop_version', False))
                except ValueError:
                    raise DBToolException(u'Неверное значение версий схемы и контента БД в таблице Meta')
        except MySQLdb.ProgrammingError:
            self.db_version = self.content_version = 0
            logging.warning("В базе данных не найдена таблица `Meta`, предполагается, что версия бд равна 0")

    def update_schema(self, version):
        if not self.schema_updates:
            self.schema_updates = self.get_updates()

        if version > self.db_version:
            versions = range(self.db_version + 1, version + 1)
        elif version < self.db_version:
            versions = reversed(range(version + 1, self.db_version + 1))
        else:
            logging.info('Схема бд уже обновлена до этой версии')
            return

        try:
            for v in versions:
                try:
                    if version > self.db_version:
                        self._perform_schema_upgrade(v)
                        actual_v = v
                    elif version < self.db_version:
                        self._perform_schema_downgrade(v)
                        actual_v = v - 1
                except Exception:
                    raise
                else:
                    self._perform_meta_update(actual_v, 'schema_version')
        except:
            self._getConnection().rollback()
            raise
        logging.info('Схема бд обновлена до версии {0}'.format(actual_v))
        self._load_versions()

    def update_content(self, version):
        if not self.content_updates:
            self.content_updates = self.get_updates(type_='content')

        if version > self.content_version:
            versions = range(self.content_version + 1, version + 1)
        elif version < self.content_version:
            versions = reversed(range(version + 1, self.content_version + 1))
        else:
            logging.info('Контент бд уже обновлен до этой версии')
            return

        try:
            for v in versions:
                try:
                    if version > self.content_version:
                        self._perform_content_upgrade(v)
                        actual_v = v
                    elif version < self.content_version:
                        self._perform_content_downgrade(v)
                        actual_v = v - 1
                except Exception:
                    raise
                else:
                    self._perform_meta_update(actual_v, 'content_version')
        except:
            self._getConnection().rollback()
            raise
        logging.info('Контент бд обновлен до версии {0}'.format(actual_v))
        self._load_versions()

    def _perform_schema_upgrade(self, v):
        logging.info('Обновление версии схемы до {0}...'.format(v))
        upd = self.schema_updates.get(v, None)
        if upd is None:
            raise DBToolException('Файл обновления для версии {0} не найден'.format(v))
        min_content_version = upd.get('min_content_version')
        if min_content_version and self.content_version < min_content_version:
            raise DBToolException(u'Минимальная версия контента БД: {0}. '
                                  u'Проведите сначала обновление контента базы данных.'.format(min_content_version))
        upd_func = upd['upgrade']
        print(upd['title'])
        upd_func(self._getConnection())

    def _perform_schema_downgrade(self, v):
        logging.info('Сброс версии схемы до {0}...'.format(v - 1))
        upd = self.schema_updates.get(v, None)
        if upd is None:
            raise DBToolException('Файл обновления для версии {0} не найден'.format(v))
        dgrd_func = upd['downgrade']
        dgrd_func(self._getConnection())

    def _perform_content_upgrade(self, v):
        logging.info('Обновление версии контента до {0}...'.format(v))
        update_list = self.content_updates.get(v, None)
        if update_list is None:
            raise DBToolException('Файл обновления для версии {0} не найден'.format(v))
        for upd in update_list:
            min_schema_version = upd.get('min_schema_version')
            if min_schema_version and self.db_version < min_schema_version:
                raise DBToolException(u'Минимальная версия схемы БД: {0}. '
                                      u'Проведите сначала обновление схемы базы данных.'.format(min_schema_version))
            upd_func = upd['upgrade']
            print(upd['title'])
            upd_func(self._getConnection())

    def _perform_content_downgrade(self, v):
        logging.info('Сброс версии контента до {0}...'.format(v - 1))

    def _perform_meta_update(self, v, table_attr):
        # Записать номер версии базы в случае успешного апдейта
        connection = self._getConnection()
        with connection as cursor:
            cursor.execute('update `Meta` set `value` = %s where `name` = %s ', (v, table_attr))
            connection.commit()

    def change_definers(self):
        current_db_name = self.conf['dbname']
        new_definer = self.conf['definer']
        with self._getConnection() as c:
            print('- updating triggers')
            c.execute('SELECT TRIGGER_NAME, DEFINER FROM information_schema.TRIGGERS WHERE TRIGGER_SCHEMA = "%s"' % current_db_name)
            trigger_list = c.fetchall()
            for name, definer in trigger_list:
                definer = '`' + '`@`'.join(definer.split('@')) + '`' # mis@% -> `mis`@`%`
                c.execute('SHOW CREATE TRIGGER %s' % name)
                create_text = c.fetchone()[2]
                create_text = create_text.replace(definer, new_definer)
                c.execute('DROP TRIGGER IF EXISTS %s' % name)
                c.execute(create_text)

            logging.info('- updating procedures')
            c.execute('UPDATE mysql.proc SET definer = "%s" WHERE db="%s"' % (new_definer.replace('`', ''), current_db_name))
            
            logging.info('- updating views')
            c.execute('SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = "VIEW" AND TABLE_SCHEMA = "%s"' % current_db_name)
            views = c.fetchall()
            wrong_views = []
            for view in views:
                try:
                    view_name = view[0]
                    c.execute('SHOW CREATE VIEW %s' % view_name)
                    create_stmt = c.fetchone()[1]
                    create_stmt = re.sub(r'`\w+`@`[\w\.%]+`', new_definer, create_stmt)
                    create_stmt = create_stmt.replace('CREATE', 'CREATE OR REPLACE')
                    c.execute(create_stmt)
                except MySQLdb.OperationalError as e:
                    # Случай, когда вьюха в теле ссылается на другую вьюху, у которой еще
                    # не поменялся дефайнер, может вызвать проблемы, если такого дефайнера
                    # нет в текущей бд. Такие случаи пропускаются
                    if '1449' in str(e):
                        wrong_views.append(view_name)
                        pass
                    else:
                        raise
            if wrong_views:
                logging.info('Возникла проблема изменения дефайнеров для следующих представлений: %s. '
                    'Требуется ручное вмешательство.' % ', '.join(wrong_views))
        return

    def get_updates(self, type_='schema'):
        if type_ == 'schema':
            return SchemaUpdateModulesList(conf=self.conf)
        elif type_ == 'content':
            return ContentUpdateModulesList(conf=self.conf)
        return {}

    def list_db_updates(self):
        if not self.schema_updates:
            self.schema_updates = self.get_updates()
        if not self.content_updates:
            self.content_updates = self.get_updates(type_='content')
        list_schema = []
        for k, upd in sorted(self.schema_updates.items()):
            m = ' {mark} {version:3} {title}'.format(
                mark='*' if k == self.db_version else ' ',
                version=k,
                title=upd['title'].splitlines()[0].strip())
            list_schema.append(m)
        list_content = []
        for k, upd_list in sorted(self.content_updates.items()):
            for upd in upd_list:
                m = ' {mark} {version:3} {title}'.format(
                    mark='*' if k == self.content_version else ' ',
                    version=k,
                    title=upd['title'].splitlines()[0].strip())
                list_content.append(m)

        msg = 'Модули обновления схемы:\n{0}\nМодули обновления контента:\n{1}\n'.format(
            '\n'.join(list_schema),
            '\n'.join(list_content))
        return msg

    def usage(self):
        msg = '''\
использование: dbtool [ -u <version> | -l | -h ]

аргументы:
  -u, --update <version>   обновить схему базы данных до версии <version>
  --update-content         обновить контент базы данных до версии <version>
  -l, --list               вывести список модулей обновлений с указанной текущей версией бд
  -c, --change-definers    изменить все определители (definer) у процедур, триггеров и \
представлений (views) на указанный в конфигурационном файле
  -h, --help               показать это сообщение
'''
        return msg


class UpdateModulesList(dict):

    def __init__(self, *args, **kwargs):
        self._conf = kwargs.pop('conf', None)
        super(UpdateModulesList, self).__init__(*args, **kwargs)

    def _load(self):
        names = self.get_filenames()
        for version, filename in names.iteritems():
            context = self._get_update_context(filename)
            self._set_update(version, context, filename)

    def _exec_file(self, filename):
        context = {'config': self._conf, 'tools': tools}
        try:
            exec open(filename, 'rb') in context
        except ImportError:
            def _f():
                raise DBToolException('Для проведения этого обновления нужен модуль PyQt4. '
                                      'Установите Qt4 и PyQt4.')
            context['upgrade'] = _f
            context['downgrade'] = _f
        except Exception, e:
            raise DBToolException(b'ошибка в модуле обновления "{0}": {1}'.format(filename, e))
        return context


class SchemaUpdateModulesList(UpdateModulesList):
    directory = 'updates'
    file_template = 'db*.py'

    def __init__(self, *args, **kwargs):
        super(SchemaUpdateModulesList, self).__init__(*args, **kwargs)
        self._load()

    def get_filenames(self):
        result = {}
        dirname = os.path.join(os.path.dirname(__file__), self.directory)
        for filename in glob(os.path.join(dirname, self.file_template)):
            name = re.search(r'db([0-9]+)\.py', filename).group(1)
            try:
                version = int(name)
            except (ValueError, AttributeError):
                raise DBToolException('невозможно определить версию в модуле '
                                      'обновления "{0}"'.format(filename))
            result[version] = filename
        return result

    def _get_update_context(self, filename):
        context = self._exec_file(filename)
        return context

    def _set_update(self, version, context, filename):
        try:
            d = {
                'title': context.get('__doc__', '(no docstring)'),
                'upgrade': context['upgrade'],
                'downgrade': context['downgrade'],
                'min_content_version': context.get('MIN_CONTENT_VERSION', None),
            }
            self[version] = d
        except KeyError, e:
            key, = e.args
            raise DBToolException('в модуле обновления "{0}" должна быть определена '
                                  'функция "{1}"'.format(filename, key))


class ContentUpdateModulesList(UpdateModulesList):
    directory = 'content_updates'
    file_template = 'content*.py'

    def __init__(self, *args, **kwargs):
        super(ContentUpdateModulesList, self).__init__(*args, **kwargs)
        self._content_type = self._conf['content'] # текущий тип контента бд
        self._load()

    def get_filenames(self):
        result = {}
        dirname = os.path.join(os.path.dirname(__file__), self.directory)
        for filename in glob(os.path.join(dirname, self.file_template)):
            try:
                info = re.search(r'content(?P<version>[0-9]+)(?P<type>[a-z]*)\.py',
                                 filename).groupdict()
                version = info.get('version')
                version = int(version)
                content_type = info.get('type') or 'common'
            except (ValueError, AttributeError):
                raise DBToolException('невозможно определить версию в модуле '
                                      'обновления "{0}"'.format(filename))
            if content_type == 'common':
                result.setdefault(version, []).insert(0, filename)
            elif content_type == self._content_type:
                result.setdefault(version, []).append(filename)
        return result

    def _get_update_context(self, filename):
        context = []
        for fn in filename:
            context.append(self._exec_file(fn))
        return context

    def _set_update(self, version, context, filename):
        for con in context:
            try:
                d = {
                    'title': con.get('__doc__', '(no docstring)'),
                    'upgrade': con['upgrade'],
                    'min_schema_version': con.get('MIN_SCHEMA_VERSION', None),
                }
                self.setdefault(version, []).append(d)
            except KeyError, e:
                key, = e.args
                raise DBToolException('в модуле обновления "{0}" должна быть определена '
                                      'функция "{1}"'.format(filename, key))

