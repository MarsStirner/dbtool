# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавляет версионирование к справочнику МКБ и связанным с ним справочникам.
'''

tblMkb = "MKB"
tblMkbSub = "rbMKBSubclass"
tblMkbSubItem = "rbMKBSubclass_Item"

def createTriggerName(tableName, triggerEvent):
    return "INCREMENT_{tableName}_VERSION_ON_{triggerEvent}".format(
        tableName=tableName, triggerEvent=triggerEvent)     

def upgrade(conn):
    # Код создания триггера на событие triggerEvent.
    # Триггер вставляет нулевую версию для таблицы tableName
    # или увеличивает номер версии для таблицы tableName
    sqlCreateTrigger = '''\
CREATE TRIGGER {triggerName}
AFTER {triggerEvent} ON {tableName} FOR EACH ROW
BEGIN
    INSERT INTO Versions (`table`, `version`)
    VALUES ('{tableName}', 0)
    ON DUPLICATE KEY UPDATE version = version+1;
END;
'''
    sql = [
        sqlCreateTrigger.format(
                tableName=tblMkb,
                triggerName=createTriggerName(tblMkb, "INSERT"),
                triggerEvent="INSERT"),
        sqlCreateTrigger.format(
                tableName=tblMkb,
                triggerName=createTriggerName(tblMkb, "UPDATE"),
                triggerEvent="UPDATE"),
        sqlCreateTrigger.format(
                tableName=tblMkb,
                triggerName=createTriggerName(tblMkb, "DELETE"),
                triggerEvent="DELETE"),

        sqlCreateTrigger.format(
                tableName=tblMkbSub,
                triggerName=createTriggerName(tblMkbSub, "INSERT"),
                triggerEvent="INSERT"),
        sqlCreateTrigger.format(
                tableName=tblMkbSub,
                triggerName=createTriggerName(tblMkbSub, "UPDATE"),
                triggerEvent="UPDATE"),
        sqlCreateTrigger.format(
                tableName=tblMkbSub,
                triggerName=createTriggerName(tblMkbSub, "DELETE"),
                triggerEvent="DELETE"),

        sqlCreateTrigger.format(
                tableName=tblMkbSubItem,
                triggerName=createTriggerName(tblMkbSubItem, "INSERT"),
                triggerEvent="INSERT"),
        sqlCreateTrigger.format(
                tableName=tblMkbSubItem,
                triggerName=createTriggerName(tblMkbSubItem, "UPDATE"),
                triggerEvent="UPDATE"),
        sqlCreateTrigger.format(
                tableName=tblMkbSubItem,
                triggerName=createTriggerName(tblMkbSubItem, "DELETE"),
                triggerEvent="DELETE"),
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

def downgrade(conn):
    sqlDropTrigger = "DROP TRIGGER IF EXISTS {triggerName}"
    sql = [
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkb, "INSERT")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkb, "UPDATE")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkb, "DELETE")),

        sqlDropTrigger.format(triggerName=createTriggerName(tblMkbSub, "INSERT")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkbSub, "UPDATE")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkbSub, "DELETE")),

        sqlDropTrigger.format(triggerName=createTriggerName(tblMkbSubItem, "INSERT")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkbSubItem, "UPDATE")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblMkbSubItem, "DELETE")),
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
