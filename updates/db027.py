# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
добавляет результат действия "Отказ в госпитализации"
'''

rbEventTypePurpose_code = "7" # Госпитализация

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def upgrade(conn):
    rows = query(conn, 'SELECT id FROM rbEventTypePurpose where code=%s' % rbEventTypePurpose_code)
    if rows:
        et_p_id = rows[0][0]
        sql0 = u'''
    INSERT INTO rbResult (eventPurpose_id, code, name, continued) VALUES (%s, 15, "Отказ в госпитализации", 0)
    ''' % et_p_id
        c = conn.cursor()
        c.execute(sql0)
        
def downgrade(conn):
    rows = query(conn, 'SELECT id FROM rbEventTypePurpose where code=%s' % rbEventTypePurpose_code)
    if rows:
        et_p_id = rows[0][0]
        sql0 = u'''
    DELETE FROM rbResult WHERE code = 15 and eventPurpose_id = %s
    ''' % et_p_id
        c = conn.cursor()
        c.execute(sql0)
        