#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Изменения, необходимые для интеграции с системой ТРФУ. Запрос на выдачу КК.
'''
flat_code_trfu_action = u'''TransfusionTherapy'''

actiontype_id_query = u'''SELECT id FROM ActionType WHERE flatCode ='%s' LIMIT 1''' % flat_code_trfu_action; 

simple_queries = \
(
# Тип действия: Требований на выдачу компонента крови.
u'''
INSERT INTO ActionType 
    (createDatetime, modifyDatetime, class,  code, 
    name, title, flatCode, sex,
    age, office, showInForm, genTimetable, 
    context, amount, defaultDirectionDate, defaultPlannedEndDate, 
    defaultEndDate, defaultPersonInEvent, defaultPersonInEditor, maxOccursInEvent, 
    showTime, isMES) 
VALUES 
    (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 2, '3_02',
     'Гемотрансфузионная терапия', 'Гемотрансфузионная терапия', '%s', 0, 
     '', '', 0, 0, 
     'protokol_gemotransfusia', 0, 2, 2, 
     0, 4, 4, 0, 
     0, 0)
''' % flat_code_trfu_action,

# Таблица результатов выдачи компонентов крови. Заполняется ядром при вызове сервиса setOrderIssueResult.
u'''
CREATE TABLE IF NOT EXISTS trfuOrderIssueResult (
    id INT(11) NOT NULL AUTO_INCREMENT,
    action_id INT(11) NOT NULL COMMENT 'идентификатор требования на выдачу КК ',
    trfu_blood_comp INT(11) NULL DEFAULT NULL COMMENT 'идентификатор компонента крови',
    comp_number VARCHAR(40) NULL DEFAULT NULL COMMENT 'номер компонента крови (номер, зашитый в ШК)',
    comp_type_id INT(11) NULL DEFAULT NULL COMMENT 'идентификатор типа компонента крови',
    blood_type_id INT(11) NULL DEFAULT NULL COMMENT 'название группы крови',
    volume INT(11) NULL DEFAULT NULL COMMENT 'объем компонента крови',
    dose_count DOUBLE NULL DEFAULT NULL COMMENT 'количество донорских доз',
    trfu_donor_id INT(11) NULL DEFAULT NULL COMMENT 'код донора',
    PRIMARY KEY (id),
    INDEX FK_trfuOrderIssueResult_action (action_id),
    INDEX FK_trfuorderissueresult_rbbloodtype (blood_type_id),
    INDEX FK_trfuorderissueresult_rbbloodcomponenttype (comp_type_id),
    CONSTRAINT FK_trfuOrderIssueResult_action FOREIGN KEY (action_id) REFERENCES Action (id),
    CONSTRAINT FK_trfuOrderIssueResult_rbbloodcomponenttype FOREIGN KEY (comp_type_id) REFERENCES rbBloodComponentType (id),
    CONSTRAINT FK_trfuorderIssueResult_rbbloodtype FOREIGN KEY (blood_type_id) REFERENCES rbBloodType (id)
)
COMMENT='Результаты выдачи компонентов крови'
COLLATE='utf8_general_ci'
ENGINE=InnoDB
''',
)

# Свойства типа действия 'Гемотрансфузионная терапия'
simple_queries_ActionPropertyType = \
(
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 7, 'Основной клинический диагноз', '', NULL, 'String', '', '', 'trfuReqBloodCompDiagnosis', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 2, 'Требуемый компонент крови', '', NULL, 'rbBloodComponentType', '', '', 'trfuReqBloodCompId', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 3, 'Вид трансфузии', '', NULL, 'Constructor', '3_1_04', '', 'trfuReqBloodCompType', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 4, 'Объем требуемого компонента крови (все, кроме тромбоцитов)', '9', NULL, 'Integer', '', '', 'trfuReqBloodCompValue', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 5, 'Количество требуемых донорских доз (тромбоциты)', '', NULL, 'Double', '', '', 'trfuReqBloodCompDose', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 6, 'Показания к проведению трансфузии', '', NULL, 'Constructor', '3_1_05', '', 'trfuReqBloodCompRootCause', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 1, 'Результат передачи требования в систему ТРФУ', '', NULL, 'String', '', '', 'trfuReqBloodCompResult', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 8, 'Дата выдачи КК', '', NULL, 'Date', '', '', 'trfuReqBloodCompDate', '', 0, '')
''' ,
u''' 
INSERT INTO `ActionPropertyType`
    (`actionType_id`, `idx`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`) 
VALUES
    ( %s, 9, 'Время выдачи КК', '', NULL, 'Time', '', '', 'trfuReqBloodCompTime', '', 0, '')
''' ,

 )

def upgrade(conn):
    global config
    c = conn.cursor()
         
    for q in simple_queries:
        c.execute(q)
    
    c.execute(actiontype_id_query)
    actionType_id = c.fetchall()
       
    for q in simple_queries_ActionPropertyType:
        c.execute(q % actionType_id[0])

    c.execute(u'''ALTER TABLE `rbBloodComponentType` CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT FIRST''')
    c.close()


def downgrade(conn):
    pass
