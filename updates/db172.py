#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Создание таблицы для хранения текста автосохранения полей ввода данных
'''

def upgrade(conn):
    c = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS `AutoSaveStorage` (
        id VARCHAR(60) NOT NULL,
        user_id INT(11) NOT NULL,
        modifyDatetime DATETIME NOT NULL,
        text TEXT NOT NULL,
        PRIMARY KEY (id, user_id),
        FOREIGN KEY `autoSaveStorage_user_id_to_Person` (user_id) REFERENCES Person (id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    '''
    c.execute(sql)

def downgrade(conn):
    c = conn.cursor()
    sql = '''
    DROP TABLE IF EXISTS `AutoSaveStorage`;
    '''
    c.execute(sql)