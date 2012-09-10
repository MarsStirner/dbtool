# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавляет версионирование к справочнику тезауруса.
'''

tblThesaurus = "rbThesaurus"

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
                tableName=tblThesaurus,
                triggerName=createTriggerName(tblThesaurus, "INSERT"),
                triggerEvent="INSERT"),
        sqlCreateTrigger.format(
                tableName=tblThesaurus,
                triggerName=createTriggerName(tblThesaurus, "UPDATE"),
                triggerEvent="UPDATE"),
        sqlCreateTrigger.format(
                tableName=tblThesaurus,
                triggerName=createTriggerName(tblThesaurus, "DELETE"),
                triggerEvent="DELETE"),
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

def downgrade(conn):
    sqlDropTrigger = "DROP TRIGGER IF EXISTS {triggerName}"
    sql = [
        sqlDropTrigger.format(triggerName=createTriggerName(tblThesaurus, "INSERT")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblThesaurus, "UPDATE")),
        sqlDropTrigger.format(triggerName=createTriggerName(tblThesaurus, "DELETE")),
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
