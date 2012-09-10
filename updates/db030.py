# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Переносим Эпикризы в осмотры
'''
def upgrade(conn):
    sql0 = [
'''\
Update `ActionType` SET class=0 WHERE `code` like "45%";
'''
    ] 
    c = conn.cursor()
    for s in sql0:
        c.execute(s)
        
def downgrade(conn):
    sql0 = [
'''\
Update `ActionType` SET class=3 WHERE `code` like "45%";
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)