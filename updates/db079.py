#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- Добавление полей в таблицы Action (Веб-клиент)
'''

def upgrade(conn):
    global config    
    c = conn.cursor()
    
    #  Добавление признака "Дозаказ" для лабораторных исследований
    sql = u'''
    ALTER TABLE Action ADD COLUMN toOrder TINYINT(1) NULL COMMENT 'Дозаказ в лабораторию'  AFTER version;'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise

    
def downgrade(conn):
    pass
