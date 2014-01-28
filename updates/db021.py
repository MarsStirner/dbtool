# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Добавляет тестовые данные в таблицу rbTest и назначает свойству 'Удельный вес' вновь созданный или существующий показатель из таблицы rbTest.
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

sqlInsertRbTest = u'''\
INSERT IGNORE INTO rbTest
(id, code, name)
VALUES
(1, '999', 'Тестовый показатель')
'''

sqlUpdateApt = u'''\
UPDATE ActionPropertyType
SET test_id = 1
WHERE name LIKE 'Удельный вес'
AND actionType_id IN (SELECT at.id FROM ActionType at WHERE at.class = 1)
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    for sql in [sqlInsertRbTest, sqlUpdateApt]:
        tools.executeEx(c, sql, mode=['safe_updates_off',])

def downgrade(conn):
    pass
    


