#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import sys
import traceback
sys.path.append(sys.path[0] + "/updates")
from db082 import actiontype_id_query 

__doc__ = '''\
- Интеграция с системой ТРФУ. Дополнение к апдейту 082 - запрос на выдачу КК. Лечебные процедуры ТРФУ.
'''

flat_code_trfu_extracorporeal = "ExtracorporealMethods";

simple_queries = \
(
u'''UPDATE `ActionPropertyType` SET `valueDomain`='rbBloodComponentType', typeName = "Reference" WHERE  `code`='trfuReqBloodCompId' ''',
u'''UPDATE `ActionPropertyType` SET descr='', unit_id = 9 WHERE  `code`='trfuReqBloodCompValue' ''',
u'''ALTER TABLE `rbBloodComponentType` RENAME TO `rbTrfuBloodComponentType` ''',
u'''CREATE VIEW rbBloodComponentType AS SELECT id, code, name FROM rbTrfuBloodComponentType WHERE unused = 0 ''',
u'''CREATE TABLE IF NOT EXISTS `rbTrfuProcedureTypes` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `trfu_id` INT(11) NULL DEFAULT NULL COMMENT 'идентификатор типа лечебной процедуры в системе ТРФУ',
    `name` VARCHAR(255) NULL DEFAULT NULL COMMENT 'наименование лечебной процедуры',
    `unused` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'флаг доступности лечебной процедуры',
    PRIMARY KEY (`id`)
)
COMMENT 'Типы лечебных процедур ТРФУ'
ENGINE=InnoDB
''',
u'''CREATE TABLE IF NOT EXISTS `rbTrfuLaboratoryMeasureTypes` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `trfu_id` INT(11) NULL DEFAULT NULL COMMENT 'идентификатор типа лечебной процедуры в системе ТРФУ',
    `name` VARCHAR(255) NULL DEFAULT NULL COMMENT 'наименование лечебной процедуры',
    PRIMARY KEY (`id`)
)
COMMENT 'Типы лабораторных измерений ТРФУ'
ENGINE=InnoDB
''',
u'''CREATE TABLE IF NOT EXISTS `trfuLaboratoryMeasure` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `action_id` INT(11) NOT NULL COMMENT 'идентификатор в МИС лечебной процедуры трансфузиологии',
    `trfu_lab_measure_id` INT(11) NULL DEFAULT NULL COMMENT 'идентификатор типа лабораторных измерений в системе ТРФУ',
    `time` DOUBLE NULL COMMENT 'идентификатор лабораторного измерения', 
    `beforeOperation` VARCHAR(255) NULL COMMENT 'лабораторные измерения до процедуры',
    `duringOperation` VARCHAR(255) NULL COMMENT 'лабораторные измерения во время процедуры',
    `inProduct` VARCHAR(255) NULL COMMENT 'лабораторные измерения в продукте афереза',
    `afterOperation` VARCHAR(255) NULL COMMENT 'лабораторные измерения после процедуры',
    PRIMARY KEY (`id`),
    CONSTRAINT `FK_trfuLaboratoryMeasure_rbTrfuLaboratoryMeasureTypes` FOREIGN KEY (`trfu_lab_measure_id`) REFERENCES `rbTrfuLaboratoryMeasureTypes` (`id`),
    CONSTRAINT `FK_trfuLaboratoryMeasure_Action` FOREIGN KEY (`action_id`) REFERENCES `action` (`id`)
) 
COMMENT 'Результаты лабораторных измерений для процедур ТРФУ'
ENGINE=InnoDB
''',
u'''CREATE TABLE IF NOT EXISTS `trfuFinalVolume` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `action_id` INT(11) NOT NULL COMMENT 'идентификатор в МИС лечебной процедуры трансфузиологии',
    `time` DOUBLE NULL COMMENT 'длительность афереза', 
    `anticoagulantVolume` DOUBLE NULL COMMENT 'объем антикоагулянта',
    `inletVolume` DOUBLE NULL COMMENT 'inlet',
    `plasmaVolume` DOUBLE NULL COMMENT 'plasma',
    `collectVolume` DOUBLE NULL COMMENT 'collect',
    `anticoagulantInCollect` DOUBLE NULL COMMENT 'AC в collect',
    `anticoagulantInPlasma` DOUBLE NULL COMMENT 'AC в plasma',
    PRIMARY KEY (`id`),
    CONSTRAINT `FK_trfuFinalVolume_Action` FOREIGN KEY (`action_id`) REFERENCES `action` (`id`)
) 
COMMENT 'Финальные объемы (для процедур ТРФУ)'
ENGINE=InnoDB
''',
u'''
INSERT INTO ActionType 
    (createDatetime, modifyDatetime, class,  code, 
    name, title, flatCode, sex,
    age, office, showInForm, genTimetable, 
    context, amount, defaultDirectionDate, defaultPlannedEndDate, 
    defaultEndDate, defaultPersonInEvent, defaultPersonInEditor, maxOccursInEvent, 
    showTime, isMES) 
VALUES 
    (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 2, '3_07',
     'Экстракорпоральные методы', 'Экстракорпоральные методы', '%s', 0, 
     '', '', 0, 0, 
     '', 0, 2, 2, 
     0, 4, 4, 0, 
     0, 0)
''' % flat_code_trfu_extracorporeal,
)

blood_comp_pasport = \
u'''INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( '%s', 10, 'Паспортные данные выданных компонентов крови', '', NULL, 'TRFU', '', '', 'trfuReqBloodCompPasport', '', 0, '')
''' 

def upgrade(conn):
    global config        
    c = conn.cursor()
    for q in simple_queries:
        try: 
            c.execute(q)
        except:
            traceback.print_exc()
            
    c.execute(actiontype_id_query)
    actionType_id = c.fetchall()
    
    c.execute(blood_comp_pasport % actionType_id[0])
            
    c.close()


def downgrade(conn):
    pass
