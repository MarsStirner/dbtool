#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные для инфекционных осложнений
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
INSERT INTO `LayoutAttribute` (`title`, `description`, `code`, `typeName`, `measure`, `defaultValue`)
VALUES
    ('Нераскрываемая вертикальная группа', '', 'NONTOGGLABLE', 'String', 'string', 'false');
'''
    c.execute(sql)

    groupAttrId = c.lastrowid

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 54, NULL, 'Данные об инфекционных осложнениях', '', NULL, 'String', '\'\'', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 67, 'true'),
            ({0}, 10, '12'),
            ({0}, 76, 'false'),
            ({0}, 77, ''),
            ({0}, 80, 'false'),
            ({0}, 81, ''),
            ({0}, 9, '35');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 55, NULL, 'Инфекционные осложнения', '', NULL, 'String', 'Да, Нет', '', 'isInfect', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '36'),
            ({0}, 10, '3');

        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 56, NULL, 'Дата начала осложнения', '', NULL, 'Date', '', '', 'infectBeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 23, '3'),
            ({0}, 22, '36');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 57, NULL, 'Дата окончания осложнения', '', NULL, 'Date', '', '', 'infectEndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 23, '3'),
            ({0}, 22, '36');

        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 58, NULL, 'Тип инфекции', '', NULL, 'String', '', '', 'infectType', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '37'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '5'),
            ({0}, {1}, 'true');
        '''.format(actionPropertyTypeId, groupAttrId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 59, NULL, 'Лихорадка неясного генеза', '', NULL, 'String', 'Да, Нет', '', 'infectFever', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '38'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 60, NULL, 'Бактериемия', '', NULL, 'String', 'Да, Нет', '', 'infectBacteremia', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '39'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 61, NULL, 'Сепсис', '', NULL, 'String', 'Да, Нет', '', 'infectSepsis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '40'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 62, NULL, 'Септический шок', '', NULL, 'String', 'Да, Нет', '', 'infectSepticShok', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '41'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 63, NULL, 'Локальная инфекция', '', NULL, 'String', 'Да, Нет', '', 'infectLocal', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '42'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 69, NULL, 'Документированная инфекция', '', NULL, 'Html', '', '', 'infectDocumental', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 68, '43'),
            ({0}, 69, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 70, NULL, 'Локализация', '', NULL, 'String', '\'\'', '', 'infectLocalisation', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '44'),
            ({0}, 67, 'true');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 71, NULL, 'ЦНС', '', NULL, 'String', '', '', 'infectCNS', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '45'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '4'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 72, NULL, 'Абсцесс головного мозга', '', NULL, 'String', 'Да, Нет', '', 'infectCephalopyosis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 11, '5'),
            ({0}, 9, '46');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 73, NULL, 'Менингит', '', NULL, 'String', 'Да, Нет', '', 'infectMeningitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '47'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 74, NULL, 'Менингоэнцефалит', '', NULL, 'String', 'Да, Нет', '', 'infectMeningoencephalitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '48'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 75, NULL, 'Энцефалит', '', NULL, 'String', 'Да, Нет', '', 'infectEncephalitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '49'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 76, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectCNSComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '45'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 77, NULL, 'Глаз', '', NULL, 'String', '', '', 'infectEye', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '50'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '4');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 78, NULL, 'Коньюнктивит', '', NULL, 'String', 'Да, Нет', '', 'infectConjunctivitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '51'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 79, NULL, 'Воспаление параорбитальной клетчатки', '', NULL, 'String', 'Да, Нет', '', 'infectPeriorbital', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '52'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 80, NULL, 'Блефарит', '', NULL, 'String', 'Да, Нет', '', 'infectBlepharitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '53'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 81, NULL, 'Хореоретинит', '', NULL, 'String', 'Да, Нет', '', 'infectChorioretinitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '54'),
            ({0}, 11, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 82, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectEyeComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '50'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 83, NULL, 'Кожа и мягкие ткани (включая место стояния ЦВК)', '', NULL, 'String', '', '', 'infectSkin', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '55'),
            ({0}, 10, '6'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '2');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 84, NULL, 'Нетяжелые инфекции кожи и мягких тканей (панариций, фурункул)', '', NULL, 'String', 'Да, Нет', '', 'infectSkinLight', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '56'),
            ({0}, 10, '6');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 85, NULL, 'Тяжелые инфекции кожи и мягких тканей (целлюлит, абсцесс, некроз)', '', NULL, 'String', 'Да, Нет', '', 'infectSkinHard', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '57'),
            ({0}, 10, '6');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 86, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectSkinComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '55'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 87, NULL, 'Слизистые', '', NULL, 'String', '', '', 'infectMucous', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '58'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 77, '4'),
            ({0}, 76, 'true');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 88, NULL, 'Мукозит 1-2 ст', '', NULL, 'String', 'Да, Нет', '', 'infectMucositis12', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '59'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 89, NULL, 'Мукозит 3-4 ст', '', NULL, 'String', 'Да, Нет', '', 'infectMucositis34', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '60'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 90, NULL, 'Эзофагит', '', NULL, 'String', 'Да, Нет', '', 'infectEsophagitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '61'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 91, NULL, 'Гингивит', '', NULL, 'String', 'Да, Нет', '', 'infectGingivitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '62'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 92, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectMucousComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '58'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 93, NULL, 'ЛОР', '', NULL, 'String', '', '', 'infectLOR', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '63'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '4');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 94, NULL, 'Ринит', '', NULL, 'String', 'Да, Нет', '', 'infectRhinitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '64'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 95, NULL, 'Тонзиллит/фарингит', '', NULL, 'String', 'Да, Нет', '', 'infectTonsillitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '65'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 96, NULL, 'Отит', '', NULL, 'String', 'Да, Нет', '', 'infectOtitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '66'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 97, NULL, 'Поражение ППН', '', NULL, 'String', 'Да, Нет', '', 'infectDefeatPPN', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '67'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 98, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectLORComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '63'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 99, NULL, 'Легкие', '', NULL, 'String', '', '', 'infectLungs', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '68'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '4');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 100, NULL, 'Бронхит/бронхопневмония', '', NULL, 'String', 'Да, Нет', '', 'infectBronchitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '69'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 101, NULL, 'Интерстициальная пневмония', '', NULL, 'String', 'Да, Нет', '', 'infectInterstitialPneumonia', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '70'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 102, NULL, 'Очаговая/долевая пневмония', '', NULL, 'String', 'Да, Нет', '', 'infectLobarPneumonia', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '71'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 103, NULL, 'Плеврит', '', NULL, 'String', 'Да, Нет', '', 'infectPleurisy', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '72'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 104, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectLungsComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '68'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 105, NULL, 'Сердце', '', NULL, 'String', '', '', 'infectHeart', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '73'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 106, NULL, 'Перикардит', '', NULL, 'String', 'Да, Нет', '', 'infectPericarditis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '74'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 107, NULL, 'Миоардит', '', NULL, 'String', 'Да, Нет', '', 'infectMioardit', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '75'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 108, NULL, 'Эндокардит', '', NULL, 'String', 'Да, Нет', '', 'infectEndocarditis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '76'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 109, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectHeartComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '73'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 110, NULL, 'Брюшная полость', '', NULL, 'String', '', '', 'infectAbdomen', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '77'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '10');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 111, NULL, 'Гастрит/гастродуоденит', '', NULL, 'String', 'Да, Нет', '', 'infectGastritis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '78'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 112, NULL, 'Панкреатит', '', NULL, 'String', 'Да, Нет', '', 'infectPancreatitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '79'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 113, NULL, 'Холецистит', '', NULL, 'String', 'Да, Нет', '', 'infectCholecystitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '80'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 114, NULL, 'Гепатит', '', NULL, 'String', 'Да, Нет', '', 'infecThepatitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '81'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 115, NULL, 'Гепато-лиенальный кандидоз', '', NULL, 'String', 'Да, Нет', '', 'infectGepatolienalnyCandidiasis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '82'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 116, NULL, 'Абсцесс', '', NULL, 'String', 'Да, Нет', '', 'infectAbscess', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '83'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 117, NULL, 'Энтероколит', '', NULL, 'String', 'Да, Нет', '', 'infectEnterocolitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '84'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 118, NULL, 'Тифлит', '', NULL, 'String', 'Да, Нет', '', 'infectCecitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '85'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 119, NULL, 'Аппендицит', '', NULL, 'String', 'Да, Нет', '', 'infectAppendicitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '86'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 120, NULL, 'Перитонит', '', NULL, 'String', 'Да, Нет', '', 'infectPeritonitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '87'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 121, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectAbdomenComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '77'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 122, NULL, 'Мочеполовая система', '', NULL, 'String', '', '', 'infectUrogenital', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '88'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '7');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 123, NULL, 'Гломерулонефрит', '', NULL, 'String', 'Да, Нет', '', 'infectGlomerulonephritis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '89'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 124, NULL, 'Пиелонефрит', '', NULL, 'String', 'Да, Нет', '', 'infectPyelonephritis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '90'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 125, NULL, 'Цистит', '', NULL, 'String', 'Да, Нет', '', 'infectCystitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '91'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 126, NULL, 'Уретрит', '', NULL, 'String', 'Да, Нет', '', 'infectUrethritis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '92'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 127, NULL, 'Эндометрит', '', NULL, 'String', 'Да, Нет', '', 'infectEndometritis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '93'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 128, NULL, 'Аднексит (тубоовариальный абсцесс)', '', NULL, 'String', 'Да, Нет', '', 'infectAdnexitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '94'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 129, NULL, 'Вульвовагинит', '', NULL, 'String', 'Да, Нет', '', 'infectVulvovaginitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
       VALUES
            ({0}, 9, '95'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 130, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectUrogenitalComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '88'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 131, NULL, 'Костно-мышечная система', '', NULL, 'String', '', '', 'infectMusculoskeletal', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '96'),
            ({0}, 10, '5'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '2');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 132, NULL, 'Остеомиелит', '', NULL, 'String', 'Да, Нет', '', 'infectOsteomyelitis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '97'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 133, NULL, 'Миозит', '', NULL, 'String', 'Да, Нет', '', 'infectMyositis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '98'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 134, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', 'infectMusculoskeletalComment', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '96'),
            ({0}, 10, '5');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 135, NULL, 'Противоинфекционная терапия', '', NULL, 'String', '\'\'', '', '', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
VALUES
    ({0}, 9, '99'),
    ({0}, 67, 'true');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 136, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '4'),
            ({0}, 9, '100');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 64, NULL, 'Этиология', '', NULL, 'String', '', '', 'infectEtiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '37'),
            ({0}, 67, 'true'),
            ({0}, 76, 'true'),
            ({0}, 77, '4'),
            ({0}, {1}, 'true');
        '''.format(actionPropertyTypeId, groupAttrId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 65, NULL, 'Бактериальная', '', NULL, 'String', 'Да, Нет', '', 'infectEtiologyBacterial', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '38'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 66, NULL, 'Грибковая', '', NULL, 'String', 'Да, Нет', '', 'infectEtiologyFungal', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '39'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 67, NULL, 'Вирусная', '', NULL, 'String', 'Да, Нет', '', 'infectEtiologyVirus', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '40'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 68, NULL, 'Неясной этиологии', '', NULL, 'String', 'Да, Нет', '', 'infectEtiologyUnknown', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '41'),
            ({0}, 11, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 137, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectDrugName', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '101'),
            ({0}, 10, '4');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 138, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectDrugBeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '101'),
            ({0}, 23, '3');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 139, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectDrugEndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '101'),
            ({0}, 23, '3');
        '''.format(actionPropertyTypeId))


    c.close()
