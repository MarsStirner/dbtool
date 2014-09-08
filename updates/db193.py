#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление столбца для указания порядка вывода контактов (rbContactType.idx) для Hippocrates
'''

def upgrade(conn):
    c = conn.cursor()
    sql = '''
    ALTER TABLE `rbContactType`
      ADD COLUMN `idx` INT(11) NOT NULL DEFAULT '0' AFTER `name`;'''
    c.execute(sql)


def downgrade(conn):
    c = conn.cursor()
    sql = '''
    ALTER TABLE `rbContactType`
        DROP COLUMN `idx`;
    '''
    c.execute(sql)