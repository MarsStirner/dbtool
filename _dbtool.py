#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import sys
import os
import re
from glob import glob
from contextlib import closing, contextmanager
from ConfigParser import ConfigParser, Error as ConfigError
from utils import tools
import MySQLdb as db

if os.name == 'nt' and sys.stdout.isatty():
    ENCODING = 'CP866'
else:
    try:
        import locale
        ENCODING = locale.getpreferredencoding()
        if not ENCODING or 'ascii' in ENCODING.lower():
            ENCODING = 'UTF-8'
    except locale.Error:
        ENCODING = 'UTF-8'

def warning(msg):
    print('warning: {0}'.format(msg).encode(ENCODING, 'replace'),
          file=sys.stderr)

def info(msg, file=sys.stdout):
    print(msg.encode(ENCODING, 'replace'), file=file)


def get_config(filename):
    p = ConfigParser(defaults={'port': '3306'})
    p.read([filename])
    return {
        'host': p.get(b'database', b'host'),
        'port': p.get(b'database', b'port'),
        'username': p.get(b'database', b'username'),
        'password': p.get(b'database', b'password'),
        'dbname': p.get(b'database', b'dbname'),
        'definer': p.get(b'database', b'definer'),
        'content': p.get(b'content', b'content_type')
    }


class DBToolException(Exception): pass


class DBTool(object):

    def __init__(self):
        self.conf = None
        self.connection = None
        self.db_version = None
        self.content_version = None
        self.schema_updates = None
        self.content_updates = None

    def load(self, filename):
        try:
            self.conf = get_config(filename)
        except ConfigError, e:
            raise DBToolException('config file "{0}": {1}'.format(filename, e))
            return
        self._load_versions()

    def _load_versions(self):
        with self._open_db_connection() as conn:
            try:
                with conn as cursor:
                    cursor.execute('SELECT name, value FROM Meta')
                    d = dict(cursor.fetchall())
                    try:
                        self.db_version = int(d.get('schema_version', 0))
                        self.content_version = int(d.get('content_version', 0))
                    except ValueError:
                        raise DBToolException(u'Неверное значение версий структуры БД и данных в таблице Meta')
            except db.ProgrammingError:
                self.db_version = self.content_version = 0
                warning("database: table 'Meta' not found, assuming schema version {0}".format(0))

    @contextmanager
    def _open_db_connection(self):
        with closing(db.connect(host=self.conf['host'],
                                port=int(self.conf['port']),
                                user=self.conf['username'],
                                passwd=self.conf['password'],
                                db=self.conf['dbname'],
                                charset='utf8',
                                use_unicode=True)) as c:
            self.connection = c
            c.autocommit(False)
            yield c
        self.connection = None

    def update_schema(self, v):
        if not self.schema_updates:
            self.schema_updates = self.get_updates()
        self._perform_update(v)

    def update_content(self, v):
        if not self.content_updates:
            self.content_updates = self.get_updates(type_='content')
        self._perform_update(v, type_='content')

    def _perform_update(self, version, type_='schema'):
        if type_ == 'schema':
            current_version = self.db_version
            updates = self.schema_updates
            table_attr = 'schema_version'
        elif type_ == 'content':
            current_version = self.content_version
            updates = self.content_updates
            table_attr = 'content_version'
        else:
            raise AttributeError

        if version == current_version:
            print('{0} is already up to date'.format(table_attr))
            return

        with self._open_db_connection() as conn:
            # XXX: MySQL не поддерживает транзакации для некоторых выражений
            # DDL, например для "create table", так что транзакции здесь не
            # всегда гарантируют консистентное состояние БД при ошибках
            # обновления
            try:
                if version > current_version:
                    versions = range(current_version + 1, version + 1)
                    for v in versions:
                        try:
                            info('upgrading to {0}...'.format(v), file=sys.stderr)
                            upd = updates.get(v, None)
                            if upd is None:
                                raise DBToolException('update file for version {0} '
                                                      'not found'.format(v))
                            min_schema_version = upd.get('min_schema_version')
                            if min_schema_version and self.db_version < min_schema_version:
                                raise DBToolException(u'Минимальная версия схемы БД: {0}. '
                                                      u'Проведите сначала обновление структур таблиц.'.format(min_schema_version))
                            upgrade = upd['upgrade']
                            print(upd['title'])
                            upgrade(conn)
                        except:
                            raise
                        else:
                            # Записать номер версии базы в случае успешного апдейта
                            with conn as cursor:
#                                 cursor.execute('update `Meta` set `value` = %s where `name` = %s ', (v, table_attr))
                                conn.commit()
                else:
                    versions = reversed(range(version + 1, current_version + 1))
                    for v in versions:
                        try:
                            v_becomes = v - 1
                            info('downgrading to {0}...'.format(v_becomes), file=sys.stderr)
                            upd = updates.get(v, None)
                            if upd is None:
                                raise DBToolException('update file for version {0} '
                                                      'not found'.format(v))
                            downgrade = upd['downgrade']
                            downgrade(conn)
                        except:
                            raise
                        else:
                            v -= 1
                            with conn as cursor:
                                cursor.execute('update `Meta` set `value` = %s where `name` = %s ', (v, table_attr))
                                conn.commit()
            except:
                conn.rollback()
                raise
        info('updated {0} to {1}'.format(table_attr, v))
        self._load_versions()

    def change_definers(self):
        current_db_name = self.conf['dbname']
        new_definer = self.conf['definer']
        with self._open_db_connection() as conn:
            c = conn.cursor()
            
            print('- updating triggers')
            c.execute('SELECT TRIGGER_NAME, DEFINER FROM information_schema.TRIGGERS WHERE TRIGGER_SCHEMA = "%s"' % current_db_name)
            trigger_list = c.fetchall()
            for name, definer in trigger_list:
                definer = '`' + '`@`'.join(definer.split('@')) + '`' # mis@% -> `mis`@`%`
                c.execute('SHOW CREATE TRIGGER %s' % name)
                create_text = c.fetchone()[2]
    #             print (name, ' : ', definer, ' -> ', new_definer)
                create_text = create_text.replace(definer, new_definer)
                c.execute('DROP TRIGGER IF EXISTS %s' % name)
                c.execute(create_text)
             
            print('- updating procedures')
            c.execute('UPDATE mysql.proc SET definer = "%s" WHERE db="%s"' % (new_definer.replace('`', ''), current_db_name))
            
            print('- updating views')
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
                except db.OperationalError as e:
                    # Случай, когда вьюха в теле ссылается на другую вьюху, у которой еще
                    # не поменялся дефайнер, может вызвать проблемы, если такого дефайнера
                    # нет в текущей бд. Такие случаи пропускаются
                    if '1449' in str(e):
                        wrong_views.append(view_name)
                        pass
                    else:
                        raise
            if wrong_views:
                print('Возникла проблема изменения дефайнеров для следующих представлений: %s. '
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
        for k, upd in sorted(self.content_updates.items()):
            m = ' {mark} {version:3} {title}'.format(
                mark='*' if k == self.content_version else ' ',
                version=k,
                title=upd['title'].splitlines()[0].strip())
            list_content.append(m)

        msg = 'Schema updates:\n{0}\nContent updates:\n{1}\n'.format(
            '\n'.join(list_schema),
            '\n'.join(list_content))
        return msg

    def usage(self):
        msg = '''
usage: dbtool [ -u <version> | -l | -h ]

options:
  -u, --update <version>   upgrade database to <version>
  -l, --list               list database versions
  -h, --help               show help message
'''
        return msg


class UpdateModulesList(dict):

    def __init__(self, *args, **kwargs):
        self._conf = kwargs.pop('conf', None)
        super(UpdateModulesList, self).__init__(*args, **kwargs)

    def _load(self):
        names = self.get_filenames()
        for version, filename in names.iteritems():
            context = {'config': self._conf, 'tools': tools}
            try:
                exec open(filename, 'rb') in context
            except Exception, e:
                raise DBToolException(b'file "{0}": {1}'.format(filename, e))
            try:
                self[version] = {
                    'title': context.get('__doc__', '(no docstring)'),
                    'upgrade': context['upgrade'],
                    'downgrade': context.get('downgrade', lambda c: None),
                    'min_schema_version': context.get('MIN_SCHEMA_VERSION', None),
                }
            except KeyError, e:
                key, = e.args
                raise DBToolException('file "{0}": function "{1}" '
                                      'must be defined'.format(filename, key))


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
            except ValueError:
                raise DBToolException(b'file "{0}": bad version '
                                      b'number: "{1}"'.format(filename, name))
            result[version] = filename
        return result


class ContentUpdateModulesList(UpdateModulesList):
    directory = 'content_updates'
    file_template = 'content*.py'

    def __init__(self, *args, **kwargs):
        super(ContentUpdateModulesList, self).__init__(*args, **kwargs)
        self._content_type = self._conf['content']
        self._load()

    def get_filenames(self):
        result = {}
        dirname = os.path.join(os.path.dirname(__file__), self.directory)
        for filename in glob(os.path.join(dirname, self.file_template)):
            try:
                info = re.search(r'content(?P<version>[0-9]+)(?P<type>[a-z]*)\.py', filename).groupdict()
                version = info.get('version')
                version = int(version)
                content_type = info.get('type') or 'ref'
            except (ValueError, AttributeError):
                raise DBToolException(b'file "{0}": bad version '
                                      b'number: "{1}"'.format(filename, version))
            if content_type == 'ref' and version not in result:
                result[version] = filename
            elif content_type == self._content_type:
                result[version] = filename
        return result