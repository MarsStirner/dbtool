# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Добавляет для всех Диагностик новое свойсво действия Штрихкод \
(с типом данных Image). \
'''

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows


def upgrade(conn):
    sqlSelectDiagATIds = u"""select id from ActionType
            where class=1 and
            deleted = 0"""

    sqlWithCheck = (u"""select id from ActionPropertyType
            where actionType_id = %d and
            name = \"Штрихкод\" and
            typeName = \"Image\" and
            deleted = 0""",

            u"""insert into ActionPropertyType 
            (actionType_id, idx, name, descr, typeName, valueDomain, defaultValue, norm, sex, age)
            values
            (%d, 100, \"Штрихкод\", \"Штрихкод для печати на контейнере с биоматериалом\", \"Image\",
            \"\", \"\", \"\", 0, \"\")""",

            u""
        )
    c = conn.cursor()
    ids = query(conn, sqlSelectDiagATIds)
    for row in ids:
        actionTypeId = row[0]

        c.execute(sqlWithCheck[0] % actionTypeId)
        if len(c.fetchall()) == 0 and sqlWithCheck[1] != u"":
            c.execute(sqlWithCheck[1] % actionTypeId)
        elif sqlWithCheck[2] != u"":
            c.execute(sqlWithCheck[2])


def downgrade(conn):
    sql = [
        # Удаляем свойства типа действия Штрихкод для всех диагностик
        u"""delete from ActionPropertyType
            where actionType_id in (select id from ActionType at where class = 1) and
            name = \"Штрихкод\" and
            typeName = \"Image\" """,
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
