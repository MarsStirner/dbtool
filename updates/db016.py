# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Вводит версионирование основных таблиц для обеспечения оптимистических блокировок
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

sqlAddVersionColumn = '''\
ALTER TABLE `{tableName}` ADD COLUMN `version` INT(11) NOT NULL DEFAULT 0;
'''

sqlCreateTrigger = '''\
CREATE TRIGGER {triggerName}
BEFORE UPDATE ON {tableName} FOR EACH ROW
BEGIN
    SET NEW.version = OLD.version + 1;
END;
'''

sqlDropVersionColumn = '''\
ALTER TABLE `{tableName}` DROP COLUMN `version` ;
'''

sqlDropTrigger = "DROP TRIGGER IF EXISTS {triggerName}"

tables = ['Event', 'Action', 'ActionProperty']

def createTriggerName(tableName):
    return "INCREMENT_{tableName}_RECORD_VERSION_ON_UPDATE".format(
        tableName=tableName)

def upgrade(conn):
    global tools
    c = conn.cursor()
    for t in tables:
        # Создаем поле версии  для таблицы t
        sql = sqlAddVersionColumn.format(tableName = t)
        tools.executeEx(c, sql, mode=['ignore_dublicates'])
        # Удаляем триггер
        sql = sqlDropTrigger.format(triggerName=createTriggerName(t))
        execute(conn, sql)
        # Создаем триггер для 
        sql = sqlCreateTrigger.format(triggerName=createTriggerName(t), tableName=t)
        execute(conn, sql)

def downgrade(conn):
    for t in tables:
        # Удаляем триггер
        sql = sqlDropTrigger.format(triggerName=createTriggerName(t))
        execute(conn, sql)
        # Удаляем поле версии из таблицы t
        sql = sqlDropVersionColumn.format(tableName = t)
        execute(conn, sql)


