#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление полей в таблицы Action и ActionType (Веб-клиент)
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    # Добавление мнемоники для ActionType
    sql = u'''
    ALTER TABLE ActionType ADD COLUMN mnem VARCHAR(32) NULL DEFAULT '' COMMENT 'Мнемоника'  AFTER jobType_id;'''
    try:
        c.execute(sql)
    except:
            print("Column MNEM already exists.")
    
    #  Добавление признака "Дозаказ" для лабораторных исследований
    sql = u'''
    ALTER TABLE Action ADD COLUMN toOrder TINYINT(1) NULL COMMENT 'Дозаказ в лабораторию'  AFTER version;'''
    try:
        c.execute(sql)
    except:
        print("Column ToORDER already exists.")
    

    #TODO: заполнение поля mnem 
    
def downgrade(conn):
    pass
