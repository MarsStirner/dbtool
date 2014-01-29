# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Устанавливает Action.plannedEndDate равным Action.createDatetime в случае если plannedEndDate = NULL
'''

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def execute(conn, sql):
    c = conn.cursor()
    c.execute(sql)

def insert(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    sqlLastInsertedId = "SELECT LAST_INSERT_ID()"
    c.execute(sqlLastInsertedId)
    result = c.fetchone()
    return result[0]

sqlUpdatePlannedEndDate = u'''\
UPDATE Action a
SET a.plannedEndDate = a.createDatetime
WHERE a.plannedEndDate IS NULL
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    for sql in [sqlUpdatePlannedEndDate]:
        tools.executeEx(c, sql, mode=['safe_updates_off',])

def downgrade(conn):
    pass
    


