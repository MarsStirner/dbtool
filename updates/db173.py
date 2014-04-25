#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение длины поля снилс в Client и Person
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
ALTER TABLE `Client` CHANGE COLUMN `SNILS` `SNILS` CHAR(12) NOT NULL COMMENT 'СНИЛС (12 символов, т.к. сюда также записывается ИИН)' ;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `Person` CHANGE COLUMN `SNILS` `SNILS` CHAR(12) NOT NULL COMMENT 'СНИЛС (12 символов, т.к. сюда также записывается ИИН)' ;

'''
    c.execute(sql)


def downgrade(conn):
    pass