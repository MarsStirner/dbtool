# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Вводит таблицу с версиями справочников, добавляет триггеры на добавление,
изменение и удаление таблиц ActionType и ActionPropertyType.
'''

tblActionType = "ActionType"
tblActionPropertyType = "ActionPropertyType"

def createTriggerName(tableName, triggerEvent):
    return "INCREMENT_{tableName}_VERSION_ON_{triggerEvent}".format(
        tableName=tableName, triggerEvent=triggerEvent)    	

def upgrade(conn):
    # Код создания таблицы для хранения версий
    sqlCreateVersionsTable = '''\
CREATE TABLE IF NOT EXISTS `Versions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `table` varchar(64) NOT NULL,
  `version` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `table_UNIQUE` (`table`),
  KEY `tableNameIndex` (`table`)
) DEFAULT CHARSET=utf8 COMMENT='Таблица с версиями справочников'
'''
    
    
    # Удаление триггеров, если они есть
    sqlDropTrigger = "DROP TRIGGER IF EXISTS {triggerName}"
    sql = [
    sqlDropTrigger.format(triggerName=createTriggerName(tblActionType,"INSERT")),
    sqlDropTrigger.format(triggerName=createTriggerName(tblActionType,"UPDATE")),
    sqlDropTrigger.format(triggerName=createTriggerName(tblActionType,"DELETE")),
    sqlDropTrigger.format(triggerName=createTriggerName(tblActionPropertyType,"INSERT")),
    sqlDropTrigger.format(triggerName=createTriggerName(tblActionPropertyType,"UPDATE")),
    sqlDropTrigger.format(triggerName=createTriggerName(tblActionPropertyType,"DELETE")),
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
    
    
    
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
	sqlCreateVersionsTable,
	sqlCreateTrigger.format(
            tableName=tblActionType,
            triggerName=createTriggerName(tblActionType, "INSERT"),
            triggerEvent="INSERT"),
	sqlCreateTrigger.format(
            tableName=tblActionType,
            triggerName=createTriggerName(tblActionType, "UPDATE"),
            triggerEvent="UPDATE"),
	sqlCreateTrigger.format(
            tableName=tblActionType,
            triggerName=createTriggerName(tblActionType, "DELETE"),
            triggerEvent="DELETE"),
	sqlCreateTrigger.format(
            tableName=tblActionPropertyType,
            triggerName=createTriggerName(tblActionPropertyType, "INSERT"),
            triggerEvent="INSERT"),
	sqlCreateTrigger.format(
            tableName=tblActionPropertyType,
            triggerName=createTriggerName(tblActionPropertyType, "UPDATE"), 
            triggerEvent="UPDATE"),
	sqlCreateTrigger.format(
            tableName=tblActionPropertyType,
            triggerName=createTriggerName(tblActionPropertyType, "DELETE"), 
            triggerEvent="DELETE"),
    ]
    c = conn.cursor()
    for s in sql:
	#print(unicode(s))
        c.execute(s)

def downgrade(conn):
    sqlDropVersionsTable = "DROP TABLE IF EXISTS `Versions`"
    sqlDropTrigger = "DROP TRIGGER IF EXISTS {triggerName}"
    sql = [
	sqlDropVersionsTable,
	sqlDropTrigger.format(triggerName=createTriggerName(tblActionType,"INSERT")),
	sqlDropTrigger.format(triggerName=createTriggerName(tblActionType,"UPDATE")),
	sqlDropTrigger.format(triggerName=createTriggerName(tblActionType,"DELETE")),
	sqlDropTrigger.format(triggerName=createTriggerName(tblActionPropertyType,"INSERT")),
	sqlDropTrigger.format(triggerName=createTriggerName(tblActionPropertyType,"UPDATE")),
	sqlDropTrigger.format(triggerName=createTriggerName(tblActionPropertyType,"DELETE")),
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

