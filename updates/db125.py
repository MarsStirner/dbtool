#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Исправление кода для типа свойства "Диагноз направившего учреждения"
'''

def upgrade(conn):
    global tools        
    c = conn.cursor()
    
    sql = u'''
UPDATE `ActionPropertyType` SET `code` = 'diagReceivedMkb'  WHERE  `code` = 'diagReceived';
'''
    c.execute(sql)
    

def downgrade(conn):
    pass