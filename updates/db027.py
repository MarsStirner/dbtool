# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
добавляет результат действия "Отказ в госпитализации"
'''

def upgrade(conn):
    sql0 = [
'''\
INSERT INTO rbResult (eventPurpose_id, code, name, continued) VALUES (8, 15, "Отказ в госпитализации", 0)
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)
        
def downgrade(conn):
    sql0 = [
'''\
DELETE FROM rbResult WHERE code = 15 and eventPurpose_id = 8
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)