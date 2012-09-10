# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Удаляет ActionPropertyType со значениями "Время приема" и "Количество раз в день" для \
назначений и создает ActionPropertyType "Скорость введения" и "Примечания". \
Создает таблицу AssignmentHours для хранения почасовых назначений.\
'''


def upgrade(conn):
    sql = [
        u"""delete from ActionProperty_String where id in
           (select id from ActionProperty where type_id in ((select id from ActionPropertyType where name=\"Время приема\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\")),
           (select id from ActionPropertyType where name=\"Количество раз в день\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\"))))""",
        u"""delete from ActionPropertyType where name=\"Время приема\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\")""",
        u"""delete from ActionPropertyType where name=\"Количество раз в день\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\")""",
        u"""CREATE TABLE if not exists `AssignmentHour` (
              `action_id` int(11) NOT NULL,
              `createDatetime` datetime NOT NULL,
              `hour` int(11) DEFAULT NULL,
              `complete` tinyint(1) DEFAULT '0'
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""",]
    sqlsWithCheck = []
    sqlsWithCheck.append((u"""select id from ActionPropertyType
            where actionType_id=(select id from ActionType at where at.name=\"Назначения\") and
            name = \"Скорость введения\" and
            typeName = \"String\" """,
            u"""insert into ActionPropertyType(actionType_id,idx,name,descr,typeName,valueDomain,defaultValue,norm,sex,age)
           values((select id from ActionType at where at.name=\"Назначения\"),
           3,\"Скорость введения\", \"Скорость введения лекарственного препарата\", \"String\",\"\",\"\",\"\",0,\"\")"""
        ))
    sqlsWithCheck.append((u"""select id from ActionPropertyType
            where actionType_id=(select id from ActionType at where at.name=\"Назначения\") and
            name = \"Примечания\" and
            typeName = \"String\" """,
            u"""insert into ActionPropertyType(actionType_id,idx,name,descr,typeName,valueDomain,defaultValue,norm,sex,age)
           values((select id from ActionType at where at.name=\"Назначения\"),
           4,\"Примечания\", \"Дополнительный указания по применению препарата\", \"String\",\"\",\"\",\"\",0,\"\")"""
        ))

    c = conn.cursor()
    for sqlWithCheck in sqlsWithCheck:
        c.execute(sqlWithCheck[0])
        if len(c.fetchall()) == 0: c.execute(sqlWithCheck[1])
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем таблицу для хранения 
        # списка пользователей, прочитавших сигнальные донесения
        u"""\
            drop table `AssignmentHour`
        """,
        u"""delete from ActionProperty_String where id in 
           (select id from ActionProperty where type_id in ((select id from ActionPropertyType where name=\"Скорость введения\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\")),
           (select id from ActionPropertyType where name=\"Примечания\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\"))))""",
        u"""delete from ActionPropertyType where name=\"Скорость введения\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\")""",
        u"""delete from ActionPropertyType where name=\"Примечания\" and actionType_id=(select id from ActionType at where at.name=\"Назначения\")""",
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
