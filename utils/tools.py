from __future__ import unicode_literals, print_function

import MySQLdb as db


def execute(cursor, sql):
    cursor.execute(sql)

def ignore_column_dublicates(func):
    def wrap(cursor, sql):
        try:
            func(cursor, sql)
        except db.OperationalError as e:
            if 'Duplicate column name' in unicode(e):
                print(e)
                pass
            else:
                raise
    return wrap

def with_safe_updates_off(func):
    def wrap(cursor, sql):
        cursor.execute('SET SQL_SAFE_UPDATES=0;')
        func(cursor, sql)
        cursor.execute('SET SQL_SAFE_UPDATES=1;')
    return wrap

def tests(func):
    def wrap(cursor, sql):
        print('>>>here is sql: ', sql)
        func(cursor, sql)
    return wrap


def executeEx(*args, **kwargs):
    func = lambda *args: execute(*args)
    modes = kwargs.get('mode')
    if modes:
        if 'ignore_dublicates' in modes:
            func = ignore_column_dublicates(func)
        if 'safe_updates_off' in modes: 
            func = with_safe_updates_off(func)
        if 'tests' in modes:
            func = tests(func)
    
    func(*args)

