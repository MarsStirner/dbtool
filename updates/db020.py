# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Добавляет записи в таблицу EventType_Action.
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

sqlInsert1 = '''\
INSERT INTO EventType_Action
(id, eventType_id, idx, actionType_id, speciality_id, tissueType_id, sex, age, age_bu, age_bc, age_eu, age_ec, selectionGroup, actuality, expose, payable)
VALUES
(1184, 13, 0, 123, NULL, NULL, 0, '', NULL, NULL, NULL, NULL, 0, 0, 1, 0);
'''
sqlInsert2 = '''\
INSERT INTO EventType_Action
(id, eventType_id, idx, actionType_id, speciality_id, tissueType_id, sex, age, age_bu, age_bc, age_eu, age_ec, selectionGroup, actuality, expose, payable)
VALUES
(1185, 13, 1, 424, NULL, NULL, 0, '', NULL, NULL, NULL, NULL, 0, 0, 1, 0);
'''

sqlDelete = '''\
DELETE FROM EventType_Action WHERE id IN (1184, 1185)
'''

def upgrade(conn):
    # Отключено по причине бессмысленного манипулирования id-шниками    
    
#    for sql in [sqlInsert1, sqlInsert2]:
#        execute(conn, sql)
    pass

def downgrade(conn):
#    execute(conn, sqlDelete)
    pass
    


