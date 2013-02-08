#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- добавляем записи для ActionType = 118 (Выписка) в rbCoreActionProperty'''

def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
    INSERT INTO rbCoreActionProperty VALUES 
    (158, 118, 'Дата следующей госпитализации(в текущем году)', 20174), 
    (159, 118, 'Отделение госпитализации', 36081), 
    (160, 118, 'Источник финансирования следующей госпитализации', 36082),
    (161, 118, 'Исход госпитализации', 1663);'''
    
    c.execute(sql)
    
def downgrade(conn):
    pass
