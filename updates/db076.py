#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Изменения, необходимые для работы закрытия обращения
- Изменены коды записей в справочнике типов обращений, на них опирается
правильное функционионирование ТМИС
'''

simple_queries = \
(
u'''
SET SQL_SAFE_UPDATES=0;
''',
u'''
ALTER TABLE `Diagnostic` ADD COLUMN `action_id` INT(11) NULL DEFAULT NULL  AFTER `version` 
, ADD INDEX `action_id` (`action_id` ASC) ;
''',
u'''
ALTER TABLE `rbRequestType` CHANGE COLUMN `code` `code` VARCHAR(16) NOT NULL COMMENT 'Код'  ;
''',
u'''
UPDATE `rbRequestType` SET `code`='clinic' WHERE `id`='1';
''',
u'''
UPDATE `rbRequestType` SET `code`='hospital' WHERE `id`='2';
''',
u'''
UPDATE `rbRequestType` SET `code`='policlinic' WHERE `id`='3';
''',
#u'''
#ALTER TABLE `ActionPropertyType` ADD COLUMN `code` VARCHAR(25) NULL  AFTER `toEpicrisis` ;
#''',

# Выписка

u'''
UPDATE `ActionPropertyType` SET `code`='resort' WHERE `actionType_id`=118 and name="Рекомендовано санаторно-курортное лечение в санатории:";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='hospLength' WHERE `actionType_id`=118 and name="Продолжительность госпитализации";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='nextHospDate' WHERE `actionType_id`=118 and name="Дата следующей госпитализации(в текущем году)";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='hospOrgStruct' WHERE `actionType_id`=118 and name="Отделение госпитализации";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='nextHospFinance' WHERE `actionType_id`=118 and name="Источник финансирования следующей госпитализации";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='hospOutcome' WHERE `actionType_id`=118 and name="Исход госпитализации";
''',

# Поступление

u'''
UPDATE `ActionPropertyType` SET `code`='diagReceived' WHERE `actionType_id`=112 and name="Диагноз направившего учреждения";
''',

# Движение

u'''
UPDATE `ActionPropertyType` SET `code`='timeLeaved' WHERE `actionType_id`=113 and name="Время выбытия";
''',

# Первичные осмотры

u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE `actionType_id` in (select id from ActionType where group_id=28 and deleted=0) and name="Основной клинический диагноз";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE `actionType_id`=139 and name="Клиническое описание";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE `actionType_id`=2456 and name="Клиническое описание диагноза";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiag' WHERE `actionType_id` in (select id from ActionType where group_id=28 and deleted=0) and name="Сопутствующие диагнозы";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='diagCompl' WHERE `actionType_id` in (select id from ActionType where group_id=28 and deleted=0) and name="Осложнения";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='preHospDefect' WHERE `actionType_id` in (select id from ActionType where group_id=28 and deleted=0) and name="Дефекты догоспитального этапа";
''',

# Эпикризы

u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE `actionType_id` in (select id from ActionType where group_id=128 and deleted=0) and name="Основной клинический диагноз";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiagMkb' WHERE `actionType_id` in (select id from ActionType where group_id=128 and deleted=0) and name="Основной клинический диагноз по МКБ";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='diagCompl' WHERE `actionType_id` in (select id from ActionType where group_id=128 and deleted=0) and name="Осложнения";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='diagComplMkb' WHERE `actionType_id` in (select id from ActionType where group_id=128 and deleted=0) and name="Осложнения по МКБ";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiag' WHERE `actionType_id` in (select id from ActionType where group_id=128 and deleted=0) and name="Сопутствующие диагнозы";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiagMkb' WHERE `actionType_id` in (select id from ActionType where group_id=128 and deleted=0) and name="Сопутствующие диагнозы по МКБ";
''',
)
user_queries = \
()

def upgrade(conn):
    global config    
    
    for query in simple_queries:
        c = conn.cursor()
        c.execute(query)
        c.close()

    for query in user_queries:
        c = conn.cursor()
        c.execute(query % (config['username'], config['host']))
        c.close()

def downgrade(conn):
    pass
