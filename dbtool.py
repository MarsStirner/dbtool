#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import sys
import os
import re
from getopt import getopt, GetoptError
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

CONFIG_FILENAME = os.path.join(os.path.dirname(__file__), 'dbtool.conf')


class DBToolException(Exception): pass


def error(msg):
    print('error: {0}'.format(msg).encode(ENCODING, 'replace'),
          file=sys.stderr)


def warning(msg):
    print('warning: {0}'.format(msg).encode(ENCODING, 'replace'),
          file=sys.stderr)


def info(msg, file=sys.stdout):
    print(msg.encode(ENCODING, 'replace'), file=file)


def usage():
    msg = '''\
usage: dbtool [ -u <version> | -l | -h ]

options:
  -u, --update <version>   upgrade database to <version>
  -l, --list               list database versions
  -h, --help               show help message
'''
    info(msg, file=sys.stderr)


def get_config():
    p = ConfigParser(defaults={'port': '3306'})
    p.read([CONFIG_FILENAME])
    return {
        'host': p.get(b'database', b'host'),
        'port': p.get(b'database', b'port'),
        'username': p.get(b'database', b'username'),
        'password': p.get(b'database', b'password'),
        'dbname': p.get(b'database', b'dbname'),
        'definer': p.get(b'database', b'definer'),
    }


def get_db_version(conn):
    DEFAULT_VERSION = 0
    c = conn.cursor()
    try:
        c.execute('select `name`, `value` from `Meta` '
                  'where `name` = "schema_version"')
        row = c.fetchone()
        if not row:
            warning("database: row 'schema_version' in table 'Meta' not found, "
                    "assuming schema version {0}".format(DEFAULT_VERSION))
            return DEFAULT_VERSION
        _, version = row
        # XXX: Значение, хранящееся в виде строки в БД, может не приводиться к
        # числу в случае ошибочного заполнения
        version = int(version)
    except db.ProgrammingError:
        warning("database: table 'Meta' not found, "
                "assuming schema version {0}".format(DEFAULT_VERSION))
        return DEFAULT_VERSION
    return version


def get_updates():
    dirname = os.path.join(os.path.dirname(__file__), 'updates')
    res = {}
    for filename in glob(os.path.join(dirname, 'db*.py')):
        name = re.search(r'db([0-9]+)\.py', filename).group(1)
        try:
            version = int(name)
        except ValueError:
            raise DBToolException(b'file "{0}": bad version '
                                  b'number: "{1}"'.format(filename, name))
        context = {'config': get_config(), 'tools': tools}
        try:
            exec open(filename, 'rb') in context
        except Exception, e:
            raise DBToolException(b'file "{0}": {1}'.format(filename, e))
        try:
            res[version] = {
                'title': context.get('__doc__', '(no docstring)'),
                'upgrade': context['upgrade'],
                'downgrade': context.get('downgrade'),
            }
        except KeyError, e:
            key, = e.args
            raise DBToolException('file "{0}": function "{1}" '
                                  'must be defined'.format(filename, key))
    return res


def change_definers():
    config = get_config()
    current_db_name = config['dbname']
    new_definer = config['definer']
    with open_db_connection() as conn:
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


@contextmanager
def open_db_connection():
    params = get_config()
    with closing(db.connect(host=params['host'],
                            port=int(params['port']),
                            user=params['username'],
                            passwd=params['password'],
                            db=params['dbname'],
                            charset='utf8',
                            use_unicode=True)) as c:
        c.autocommit(False)
        yield c


def list_db_updates():
    with open_db_connection() as conn:
        version = get_db_version(conn)
        updates = get_updates()
        for k, upd in sorted(get_updates().items()):
            info(' {mark} {version:3} {title}'.format(
                mark='*' if k == version else ' ',
                version=k,
                title=upd['title'].splitlines()[0].strip()))


def update_db(version):
    def get_update_exc(updates, key):
        try:
            return updates[v]
        except KeyError:
            raise DBToolException(b'update file for version {0} '
                                  b'not found'.format(v))

    with open_db_connection() as conn:
        current = get_db_version(conn)
        all_updates = get_updates()
        if current not in all_updates:
            raise DBToolException(b'current DB version {0} '
                                  b'not found in updates'.format(current))
        if version == current:
            raise DBToolException(b'DB is already up to date')

        with open_db_connection() as conn:
            # XXX: MySQL не поддерживает транзакации для некоторых выражений
            # DDL, например для "create table", так что транзакции здесь не
            # всегда гарантируют консистентное состояние БД при ошибках
            # обновления
            try:
                if version > current:
                    versions = range(current + 1, version + 1)
                    for v in versions:
                        info('upgrading to {0}...'.format(v),
                             file=sys.stderr)
                        upd = get_update_exc(all_updates, v)
                        upgrade = upd['upgrade']
                        upgrade(conn)
                else:
                    versions = reversed(range(version + 1, current + 1))
                    for v in versions:
                        info('downgrading to {0}...'.format(v),
                             file=sys.stderr)
                        upd = get_update_exc(all_updates, v)
                        try:
                            downgrade = upd['downgrade']
                        except KeyError:
                            raise DBToolException(b'no "downgrade" function '
                                                  b'for version '
                                                  b'"{0}"'.format(v))
                        downgrade(conn)
                if version > 0:
                    c = conn.cursor()
                    c.execute('update `Meta` '
                              'set `value` = %s '
                              'where `name` = "schema_version"',
                              version)
                conn.commit()
                info('updated to {0}'.format(get_db_version(conn)))
            except:
                conn.rollback()
                raise


def main(argv):
    try:
        opts, args = getopt(argv, b'hlcu:', [b'help', b'list', b'change-definers', b'update='])

        if args:
            error('bad command line arguments: "{0}"'.format(' '.join(args)))
            sys.exit(1)

        if not opts:
            usage()
            sys.exit(1)

        for opt, arg in opts:
            if opt in [b'-h', b'--help']:
                usage()
                sys.exit(0)
            elif opt in [b'-l', b'--list']:
                list_db_updates()
            elif opt in [b'-c', b'--change-definers']:
                change_definers()
            elif opt in [b'-u', b'--update']:
                try:
                    version = int(arg)
                except ValueError:
                    error('argument must be a number: "{0}"'.format(arg))
                    sys.exit(1)
                if version < 0:
                    error('argument must be a '
                          'positive number: {0}'.format(version))
                    sys.exit(1)
                update_db(version)
            else:
                usage()
                sys.exit(1)
        sys.exit(0)
    except db.Error, e:
        raise
        errcode, message = e.args
        error('database: {0}'.format(
            message.decode(ENCODING, errors='replace')))
        sys.exit(1)
    except ConfigError, e:
        error('config file "{0}": {1}'.format(
            CONFIG_FILENAME,
            bytes(e).decode(ENCODING, errors='replace')))
        sys.exit(1)
    except (GetoptError, DBToolException), e:
        error(bytes(e).decode(ENCODING, errors='replace'))
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])

