#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Интеграция с ТГСК
'''

create_queue_table = u'''
CREATE TABLE `queueHsctRequest` (
	`action_id` INT(11) NOT NULL COMMENT 'Ссылка на Action, выступает в качестве первичного ключа',
	`person_id` INT(11) NOT NULL COMMENT 'Ссылка на пользователя, поместившего заявку в очередь',
	`status` ENUM('NEW','IN_PROGRESS','CANCELED','ERROR','FINISHED') NOT NULL DEFAULT 'NEW' COMMENT 'Статус заявки в очереди - NEW{новый}, IN_PROGRESS{отправляется}, ERROR{ошибка при отправке или отказ внешней системы}, FINISHED{Заявка обработана} ',
	`sendDateTime` DATETIME NOT NULL COMMENT 'Дата отправки (планируемая)',
	`attempts` INT(11) NOT NULL DEFAULT '0' COMMENT 'Количество попыток отправки',
	`info` TEXT NULL COMMENT 'ПояснениеСообщение',
	PRIMARY KEY (`action_id`),
	INDEX `FK_queueHsctRequest_Person` (`person_id`),
	INDEX `sendDateTime` (`sendDateTime`),
	INDEX `status` (`status`),
	CONSTRAINT `FK_queueHsctRequest_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`),
	CONSTRAINT `FK_queueHsctRequest_Person` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
)
COMMENT='Таблица с очередью отправки данных в ТГСК'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
'''

delete_old_action_types = u''' UPDATE ActionType SET deleted = 1 WHERE deleted = 0 AND flatCode = 'hsct' '''

insert_new_actionType = u''' 
INSERT INTO ActionType 
    (createDatetime, modifyDatetime, class,  code, 
    name, title, flatCode, sex,
    age, office, showInForm, genTimetable, 
    context, amount, defaultDirectionDate, defaultPlannedEndDate, 
    defaultEndDate, defaultPersonInEvent, defaultPersonInEditor, maxOccursInEvent, 
    showTime, isMES, mnem) 
VALUES 
    (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, 'hsct',
     'Заявка на ТГСК', 'Заявка на ТГСК', 'hsct', 0, 
     '', '', 0, 0, 
     'hsct_request', 1, 2, 2, 
     0, 4, 4, 0, 
     0, 0, 'OTH')
'''

action_properties_query = (
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 0, 'Результат', '', NULL, 'String', '', '', 'result', '', 0, '', 0, 1) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 1, 'Статус рассмотрения заявки', '', NULL, 'String', '', '', 'is_completed', '', 0, '', 0, 1) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 2, 'Статус болезни', '', NULL, 'String', '', '', 'disease_status', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 3, 'Клинический диагноз', '', NULL, 'String', '', '', 'diagnosis', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 4, 'Клинический диагноз по МКБ', '', NULL, 'MKB', '', '', 'diagnosis_icd_code', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 5, 'Дата установки диагноза', '', NULL, 'Date', '', '', 'diagnosis_date', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 6, 'Осложнения', '', NULL, 'String', '', '', 'complications', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 7, 'Сопутствующие диагнозы', '', NULL, 'String', '', '', 'secondary_diagnoses', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 8, 'Анти-CMV IgG', '', NULL, 'String', '\\'Положительный\\',\\'Отрицательный\\'', '', 'anti_cmv_igg_code', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 9, 'Показания к ТГСК', '', NULL, 'String', '', '', 'indications', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 10, 'Дата установления показаний', '', NULL, 'Date', '', '', 'indications_date', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 11, 'Оптимальный срок ТГСК', '', NULL, 'Date', '', '', 'optimal_hsct_date', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 12, 'Вид ТГСК', '', NULL, 'String', '\\'Аутологичная\\',\\'Аллогенная\\'', '', 'hsct_type_code', '', 0, '', 1, 0) ''',
u'''INSERT INTO `ActionPropertyType` (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `mandatory`, `readonly`) 
VALUES ( %s, 13, 'Наличие сиблингов', '', NULL, 'String', '\\'Есть\\',\\'Нет\\'', '', 'has_siblings', '', 0, '', 1, 0) ''',
)

insert_new_diagnosis_type = u'''INSERT INTO `rbDiagnosisType` (`code`, `name`, `replaceInDiagnosis`, `flatCode`) VALUES ('7346', 'Диагноз для отправки в ТГСК', '99', 'diagnosis_icd_code')'''
hotfix_apt_weight_code = u'''UPDATE `ActionPropertyType` SET `code`='WEIGHT' WHERE `id`=3911145'''

def upgrade(conn):
    global config        
    c = conn.cursor()
    
    c.execute(u'''DROP TABLE IF EXISTS `queueHsctRequest`''')
    c.execute(create_queue_table)
    print(u''' QueueTable created''')
    c.execute(delete_old_action_types)
    c.execute(insert_new_actionType)
    actionType_id = c.lastrowid
    print(u'''Inserted ActionType.id = %s''' % actionType_id)
    for q in action_properties_query:
        print(q % actionType_id)
        c.execute(q % actionType_id)
    print(u''' APT inserted''')
    c.execute(insert_new_diagnosis_type)
    c.execute(hotfix_apt_weight_code)
    c.close()

def downgrade(conn):
    pass





