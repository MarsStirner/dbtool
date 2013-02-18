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
UPDATE `rbRequestType` SET `code`='clinic' WHERE `code`='1';
''',
u'''
UPDATE `rbRequestType` SET `code`='hospital' WHERE `code`='2';
''',
u'''
UPDATE `rbRequestType` SET `code`='policlinic' WHERE `code`='3';
''',
u'''
UPDATE `EventType` SET `canHavePayableActions`='1' WHERE `code`='02';
''',
#u'''
#ALTER TABLE `ActionPropertyType` ADD COLUMN `code` VARCHAR(25) NULL  AFTER `toEpicrisis` ;
#''',
u'''
ALTER TABLE `TempInvalid` ADD COLUMN `event_id` INT(11) NULL DEFAULT NULL  AFTER `caseBegDate` ;
''',
u'''
ALTER TABLE `Event` ADD COLUMN `lpu_transfer` VARCHAR(100) NULL DEFAULT NULL  AFTER `uuid_id` ;
''',

# Промежуточная выписка
u'''
UPDATE `ActionType` SET `code`='4511' WHERE `code`='4504' and name="Промежуточная выписка";
''',

# Выписка

u'''
UPDATE `ActionPropertyType` SET `code`='resort' 
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4203' and deleted='0')
and name="Рекомендовано санаторно-курортное лечение в санатории:";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='hospLength'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4203' and deleted='0')
and name="Продолжительность госпитализации";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='nextHospDate'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4203' and deleted='0')
and name="Дата следующей госпитализации(в текущем году)";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='hospOrgStruct'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4203' and deleted='0')
and name="Отделение госпитализации";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='nextHospFinance'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4203' and deleted='0')
and name="Источник финансирования следующей госпитализации";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='hospOutcome'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4203' and deleted='0')
and name="Исход госпитализации";
''',

# Поступление

u'''
UPDATE `ActionPropertyType` SET `code`='diagReceived'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4201' and deleted='0')
and name="Диагноз направившего учреждения";
''',

# Движение

u'''
UPDATE `ActionPropertyType` SET `code`='timeLeaved'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4202' and deleted='0')
and name="Время выбытия";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='orgStructTransfer'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4202' and deleted='0')
and name="Переведен в отделение";
''',

# Первичные осмотры

u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE `actionType_id` in 
(select id from ActionType where group_id=(select id from ActionType where code='1_1' and deleted='0') and deleted=0)
and name="Основной клинический диагноз";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_1_01' and deleted='0')
and name="Клиническое описание";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_1_02' and deleted='0')
and name="Клиническое описание диагноза";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiag' WHERE `actionType_id` in 
(select id from ActionType where group_id=(select id from ActionType where code='1_1' and deleted='0') and deleted=0)
and name="Сопутствующие диагнозы";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='diagCompl' WHERE `actionType_id`in
(select id from ActionType where group_id=(select id from ActionType where code='1_1' and deleted='0') and deleted=0)
and name="Осложнения";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='preHospDefect' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='1_1' and deleted='0') and deleted=0)
and name="Дефекты догоспитального этапа";
''',

# Эпикризы

u'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='4500' and deleted='0') and deleted=0)
and name="Основной клинический диагноз";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiagMkb' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='4500' and deleted='0') and deleted=0)
and name="Основной клинический диагноз по МКБ";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='diagCompl' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='4500' and deleted='0') and deleted=0)
and name="Осложнения";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='diagComplMkb' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='4500' and deleted='0') and deleted=0)
and name="Осложнения по МКБ";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiag' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='4500' and deleted='0') and deleted=0)
and name="Сопутствующие диагнозы";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiagMkb' WHERE `actionType_id` in
(select id from ActionType where group_id=(select id from ActionType where code='4500' and deleted='0') and deleted=0)
and name="Сопутствующие диагнозы по МКБ";
''',

# Протокол (карта) патологоанатомического исследования
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiagPat'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_9_02' and deleted='0')
and name="Патологоанатомический диагноз. Основное заболевание.";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainDiagMkbPat'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_9_02' and deleted='0')
and name="Патологоанатомический диагноз. Основное заболевание по МКБ.";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='complDiagPat'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_9_02' and deleted='0')
and name="Патологоанатомический диагноз. Осложнения.";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='complDi1_1_01agMkbPat'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_9_02' and deleted='0')
and name="Патологоанатомический диагноз. Осложнения по МКБ.";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiagPat'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_9_02' and deleted='0')
and name="Патологоанатомический диагноз. Сопутствующие заболевания.";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='assocDiagMkbPat'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_9_02' and deleted='0')
and name="Патологоанатомический диагноз. Сопутствующие заболевания по МКБ.";
''',

# Посмертный эпикриз
u'''
UPDATE `ActionPropertyType` SET `code`='mainReasonOD'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4507' and deleted='0')
and name="Основная причина смерти";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='mainReasonODMkb'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='4507' and deleted='0')
and name="Код МКБ";
''',

# Документы и извещения
u'''
UPDATE `ActionPropertyType` SET `code`='tumorStage'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_8_5' and deleted='0')
and name="Стадия опухолевого процесса";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='tumorStage'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_7_1' and deleted='0')
and name="Стадия опухолевого процесса";
''',
u'''
UPDATE `ActionPropertyType` SET `code`='tumorStage'
WHERE `actionType_id`=(SELECT id FROM ActionType WHERE code='1_7_2' and deleted='0')
and name="Стадия опухолевого процесса";
''',

u'''
SET SQL_SAFE_UPDATES=1;
''',
)
user_queries = \
()

def upgrade(conn):
    global config    
    c = conn.cursor()
    
    for query in simple_queries:
        c.execute(query)

    for query in user_queries:
        c.execute(query % (config['username'], config['host']))
    
    c.close()

def downgrade(conn):
    pass
