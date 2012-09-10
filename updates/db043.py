# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Добавляет Дозировку в Назначения (с типом данных String). \
Меняет тип данных свойства Доза с String на Double (если такого свойства нет - создает его). \
'''


def upgrade(conn):
    sqlsWithCheck = []
    sqlsWithCheck.append((u"""select id from ActionPropertyType
            where actionType_id=(select id from ActionType at where at.name=\"Назначения\") and
            name = \"Дозировка\" and
            typeName = \"String\" and
            deleted = 0""",
            u"""insert into ActionPropertyType(actionType_id,idx,name,descr,typeName,valueDomain,defaultValue,norm,sex,age)
            values((select id from ActionType at where at.name=\"Назначения\"),
            2,\"Дозировка\", \"Дозировка лекарственного препарата\", \"String\",\"\",\"\",\"\",0,\"\")""",
            u""
        ))
    sqlsWithCheck.append((u"""select id from ActionPropertyType
            where actionType_id=(select id from ActionType at where at.name=\"Назначения\") and
            name = \"Доза\" and
            typeName = \"String\" and
            deleted = 0""",
            u"",
            u"""update ActionPropertyType
            set deleted = 1
            where actionType_id = (select id from ActionType at where at.name=\"Назначения\")
            and name = \"Доза\" and
            typeName = \"String\" """
        ))
    sqlsWithCheck.append((u"""select id from ActionPropertyType
            where actionType_id=(select id from ActionType at where at.name=\"Назначения\") and
            name = \"Доза\" and
            typeName = \"Double\" and
            deleted = 0""",
            u"""insert into ActionPropertyType(actionType_id,idx,name,descr,typeName,valueDomain,defaultValue,norm,sex,age)
            values((select id from ActionType at where at.name=\"Назначения\"),
            2,\"Доза\", \"Количество лекарственного препарата в в единицах измерения\", \"Double\",\"\",\"\",\"\",0,\"\")""",
            u""
        ))



    c = conn.cursor()
    for sqlWithCheck in sqlsWithCheck:
        c.execute(sqlWithCheck[0])
        if len(c.fetchall()) == 0 and sqlWithCheck[1] != u"":
            c.execute(sqlWithCheck[1])
        elif sqlWithCheck[2] != u"":
            c.execute(sqlWithCheck[2])


def downgrade(conn):
    sql = [
        # Удаляем свойства типа действия Доза и Дозировка
        u"""delete from ActionPropertyType
            where actionType_id = (select id from ActionType at where at.name=\"Назначения\") and
            name = \"Дозировка\" and
            typeName = \"String\" """,
        u"""delete from ActionPropertyType
            where actionType_id = (select id from ActionType at where at.name=\"Назначения\") and
            name = \"Доза\" and
            typeName = \"Double\" """,
        u"""update ActionPropertyType
            set deleted = 0
            where actionType_id = (select id from ActionType at where at.name=\"Назначения\")
            and name = \"Доза\" and
            typeName = \"String\" """,
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
