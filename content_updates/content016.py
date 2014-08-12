#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные для инфекционных осложнений и противоинфекционной терапии
'''

def upgrade(conn):
    global config
    c = conn.cursor()


    sql = u'''
INSERT INTO `LayoutAttribute` (`title`, `description`, `code`, `typeName`, `measure`, `defaultValue`)
VALUES
    ('В одном ряду вертикальной группы', 'Номер ряда в вертикальной группе', 'VGROUPROW', 'String', 'string', '');
'''
    c.execute(sql)

    vgroupRowStringId = c.lastrowid


    sql = u'''
INSERT INTO `LayoutAttribute` (`title`, `description`, `code`, `typeName`, `measure`, `defaultValue`)
VALUES
    ('В одном ряду вертикальной группы', 'Номер ряда в вертикальной группе', 'VGROUPROW', 'Date', 'string', '');
'''
    c.execute(sql)

    vgroupRowDateId = c.lastrowid


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'isInfect';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectBeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))    


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectEndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId)) 


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectEtiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))    


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectEtiologyBacterial';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))     


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectEtiologyFungal';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))  


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectEtiologyVirus';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))     


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectEtiologyUnknown';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))  


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectTherapyType';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id = '{0}';
        '''.format(actionPropertyTypeId))  


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectType';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '6');
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '17' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 59, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectFever-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '39'),
            ({0}, {1}, '1');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 59, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectFever-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '40'),
            ({0}, {1}, '1');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 59, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectFever-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '41'),
            ({0}, {1}, '1');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectBacteremia';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '42' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 60, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectBacteremia-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '43'),
            ({0}, {1}, '2');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 60, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectBacteremia-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '44'),
            ({0}, {1}, '2');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 60, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectBacteremia-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '45'),
            ({0}, {1}, '2');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectSepsis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '46' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 61, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectSepsis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '47'),
            ({0}, {1}, '3');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 61, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectSepsis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '48'),
            ({0}, {1}, '3');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 61, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectSepsis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '49'),
            ({0}, {1}, '3');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectSepticShok';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '50' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 62, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectSepticShok-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '51'),
            ({0}, {1}, '4');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 62, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectSepticShok-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '52'),
            ({0}, {1}, '4');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 62, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectSepticShok-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '53'),
            ({0}, {1}, '4');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLocal';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '54' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDocumental';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '55' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLocalisation';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '56' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectCNS';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '57' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '16' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectCephalopyosis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '58' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 72, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectCephalopyosis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '59'),
            ({0}, {1}, '5');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 72, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectCephalopyosis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '60'),
            ({0}, {1}, '5');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 72, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectCephalopyosis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '61'),
            ({0}, {1}, '5');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMeningitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '62' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 73, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMeningitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '63'),
            ({0}, {1}, '6');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 73, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMeningitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '64'),
            ({0}, {1}, '6');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 73, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMeningitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '65'),
            ({0}, {1}, '6');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMeningoencephalitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '66' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 74, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMeningoencephalitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '67'),
            ({0}, {1}, '7');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 74, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMeningoencephalitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '68'),
            ({0}, {1}, '7');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 74, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMeningoencephalitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '69'),
            ({0}, {1}, '7');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMeningoencephalitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '70' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 75, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectEncephalitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '71'),
            ({0}, {1}, '8');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 75, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectEncephalitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '72'),
            ({0}, {1}, '8');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 75, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectEncephalitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '73'),
            ({0}, {1}, '8');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectCNSComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '57' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectEye';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '75' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '16' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectConjunctivitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '76' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 78, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectConjunctivitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '77'),
            ({0}, {1}, '9');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 78, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectConjunctivitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '78'),
            ({0}, {1}, '9');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 78, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectConjunctivitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '79'),
            ({0}, {1}, '9');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectPeriorbital';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '80' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 79, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectPeriorbital-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '81'),
            ({0}, {1}, '10');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 79, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectPeriorbital-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '82'),
            ({0}, {1}, '10');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 79, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectPeriorbital-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '83'),
            ({0}, {1}, '10');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectBlepharitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '84' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 80, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectBlepharitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '85'),
            ({0}, {1}, '11');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 80, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectBlepharitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '86'),
            ({0}, {1}, '11');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 80, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectBlepharitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '87'),
            ({0}, {1}, '11');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectChorioretinitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '88' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 81, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectChorioretinitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '89'),
            ({0}, {1}, '12');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 81, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectChorioretinitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '90'),
            ({0}, {1}, '12');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 81, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectChorioretinitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '91'),
            ({0}, {1}, '12');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectEyeComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '75' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectSkin';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '93' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '8' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectSkinLight';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '94' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 84, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectSkinLight-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '95'),
            ({0}, {1}, '13');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 84, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectSkinLight-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '96'),
            ({0}, {1}, '13');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 84, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectSkinLight-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '97'),
            ({0}, {1}, '13');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectSkinHard';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '98' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 85, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectSkinHard-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '99'),
            ({0}, {1}, '14');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 85, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectSkinHard-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '100'),
            ({0}, {1}, '14');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 85, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectSkinHard-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '101'),
            ({0}, {1}, '14');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectSkinComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '93' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMucous';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '103' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '16' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMucositis12';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '104' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 88, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMucositis12-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '105'),
            ({0}, {1}, '15');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 88, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMucositis12-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '106'),
            ({0}, {1}, '15');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 88, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMucositis12-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '107'),
            ({0}, {1}, '15');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMucositis34';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '108' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 89, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMucositis34-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '109'),
            ({0}, {1}, '16');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 89, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMucositis34-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '110'),
            ({0}, {1}, '16');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 89, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMucositis34-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '111'),
            ({0}, {1}, '16');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectEsophagitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '112' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 90, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectEsophagitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '113'),
            ({0}, {1}, '17');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 90, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectEsophagitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '114'),
            ({0}, {1}, '17');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 90, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectEsophagitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '115'),
            ({0}, {1}, '17');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectGingivitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '116' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 91, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectGingivitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '117'),
            ({0}, {1}, '18');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 91, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectGingivitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '118'),
            ({0}, {1}, '18');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 91, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectGingivitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '119'),
            ({0}, {1}, '18');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMucousComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '103' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLOR';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '121' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '16' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectRhinitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '122' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 94, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectRhinitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '123'),
            ({0}, {1}, '19');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 94, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectRhinitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '124'),
            ({0}, {1}, '19');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 94, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectRhinitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '125'),
            ({0}, {1}, '19');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectTonsillitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '126' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 95, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectTonsillitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '127'),
            ({0}, {1}, '20');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 95, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectTonsillitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '128'),
            ({0}, {1}, '20');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 95, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectTonsillitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '129'),
            ({0}, {1}, '20');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectOtitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '130' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 96, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectOtitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '131'),
            ({0}, {1}, '21');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 96, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectOtitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '132'),
            ({0}, {1}, '21');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 96, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectOtitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '133'),
            ({0}, {1}, '21');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDefeatPPN';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '134' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 97, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectDefeatPPN-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '135'),
            ({0}, {1}, '22');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 97, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectDefeatPPN-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '136'),
            ({0}, {1}, '22');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 97, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectDefeatPPN-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '137'),
            ({0}, {1}, '22');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLORComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '121' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLungs';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '139' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '16' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectBronchitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '140' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 100, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectBronchitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '141'),
            ({0}, {1}, '23');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 100, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectBronchitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '142'),
            ({0}, {1}, '23');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 100, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectBronchitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '143'),
            ({0}, {1}, '23');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectInterstitialPneumonia';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '144' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 101, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectInterstitialPneumonia-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '145'),
            ({0}, {1}, '24');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 101, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectInterstitialPneumonia-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '146'),
            ({0}, {1}, '24');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 101, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectInterstitialPneumonia-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '147'),
            ({0}, {1}, '24');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLobarPneumonia';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '148' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 102, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectLobarPneumonia-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '149'),
            ({0}, {1}, '25');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 102, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectLobarPneumonia-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '150'),
            ({0}, {1}, '25');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 102, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectLobarPneumonia-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '151'),
            ({0}, {1}, '25');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectPleurisy';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '152' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 103, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectPleurisy-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '153'),
            ({0}, {1}, '26');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 103, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectPleurisy-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '154'),
            ({0}, {1}, '26');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 103, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectPleurisy-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '155'),
            ({0}, {1}, '26');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectLungsComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '139' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectHeart';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '157' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '12' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectPericarditis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '158' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 106, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectPericarditis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '159'),
            ({0}, {1}, '27');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 106, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectPericarditis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '160'),
            ({0}, {1}, '27');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 106, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectPericarditis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '161'),
            ({0}, {1}, '27');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMioardit';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '162' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 107, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMioardit-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '163'),
            ({0}, {1}, '28');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 107, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMioardit-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '164'),
            ({0}, {1}, '28');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 107, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMioardit-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '165'),
            ({0}, {1}, '28');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectEndocarditis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '166' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 108, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectEndocarditis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '167'),
            ({0}, {1}, '29');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 108, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectEndocarditis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '168'),
            ({0}, {1}, '29');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 108, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectEndocarditis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '169'),
            ({0}, {1}, '29');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectHeartComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '157' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectAbdomen';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '171' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '40' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectGastritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '172' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 111, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectGastritis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '173'),
            ({0}, {1}, '30');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 111, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectGastritis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '174'),
            ({0}, {1}, '30');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 111, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectGastritis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '175'),
            ({0}, {1}, '30');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectPancreatitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '176' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 112, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectPancreatitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '177'),
            ({0}, {1}, '31');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 112, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectPancreatitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '178'),
            ({0}, {1}, '31');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 112, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectPancreatitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '179'),
            ({0}, {1}, '31');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectCholecystitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '180' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 113, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectCholecystitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '181'),
            ({0}, {1}, '32');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 113, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectCholecystitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '182'),
            ({0}, {1}, '32');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 113, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectCholecystitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '183'),
            ({0}, {1}, '32');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infecThepatitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '184' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 114, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infecThepatitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '185'),
            ({0}, {1}, '33');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 114, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infecThepatitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '186'),
            ({0}, {1}, '33');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 114, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infecThepatitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '187'),
            ({0}, {1}, '33');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectGepatolienalnyCandidiasis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '188' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 115, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectGepatolienalnyCandidiasis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '189'),
            ({0}, {1}, '34');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 115, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectGepatolienalnyCandidiasis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '190'),
            ({0}, {1}, '34');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 115, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectGepatolienalnyCandidiasis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '191'),
            ({0}, {1}, '34');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectAbscess';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '192' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 116, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectAbscess-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '193'),
            ({0}, {1}, '35');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 116, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectAbscess-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '194'),
            ({0}, {1}, '35');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 116, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectAbscess-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '195'),
            ({0}, {1}, '35');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectEnterocolitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '196' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 117, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectEnterocolitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '197'),
            ({0}, {1}, '36');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 117, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectEnterocolitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '198'),
            ({0}, {1}, '36');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 117, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectEnterocolitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '199'),
            ({0}, {1}, '36');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectCecitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '200' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 118, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectCecitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '201'),
            ({0}, {1}, '37');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 118, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectCecitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '202'),
            ({0}, {1}, '37');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 118, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectCecitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '203'),
            ({0}, {1}, '37');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectAppendicitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '204' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 119, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectAppendicitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '205'),
            ({0}, {1}, '38');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 119, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectAppendicitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '206'),
            ({0}, {1}, '38');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 119, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectAppendicitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '207'),
            ({0}, {1}, '38');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectPeritonitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '208' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 120, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectPeritonitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '209'),
            ({0}, {1}, '39');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 120, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectPeritonitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '210'),
            ({0}, {1}, '39');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 120, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectPeritonitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '211'),
            ({0}, {1}, '39');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectAbdomenComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '171' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectUrogenital';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '213' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '28' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))

    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectGlomerulonephritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '214' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 123, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectGlomerulonephritis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '215'),
            ({0}, {1}, '40');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 123, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectGlomerulonephritis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '216'),
            ({0}, {1}, '40');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 123, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectGlomerulonephritis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '217'),
            ({0}, {1}, '40');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectPyelonephritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '218' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 124, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectPyelonephritis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '219'),
            ({0}, {1}, '41');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 124, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectPyelonephritis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '220'),
            ({0}, {1}, '41');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 124, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectPyelonephritis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '221'),
            ({0}, {1}, '41');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectCystitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '222' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 125, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectCystitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '223'),
            ({0}, {1}, '42');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 125, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectCystitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '224'),
            ({0}, {1}, '42');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 125, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectCystitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '225'),
            ({0}, {1}, '42');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectUrethritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '226' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 126, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectUrethritis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '227'),
            ({0}, {1}, '43');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 126, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectUrethritis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '228'),
            ({0}, {1}, '43');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 126, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectUrethritis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '229'),
            ({0}, {1}, '43');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectEndometritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '230' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 127, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectEndometritis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '231'),
            ({0}, {1}, '44');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 127, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectEndometritis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '232'),
            ({0}, {1}, '44');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 127, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectEndometritis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '233'),
            ({0}, {1}, '44');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectAdnexitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '234' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 128, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectAdnexitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '235'),
            ({0}, {1}, '45');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 128, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectAdnexitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '236'),
            ({0}, {1}, '45');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 128, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectAdnexitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '237'),
            ({0}, {1}, '45');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectVulvovaginitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '238' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 129, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectVulvovaginitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '239'),
            ({0}, {1}, '46');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 129, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectVulvovaginitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '240'),
            ({0}, {1}, '46');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 129, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectVulvovaginitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '241'),
            ({0}, {1}, '46');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectUrogenitalComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '213' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMusculoskeletal';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '243' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '8' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectOsteomyelitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '244' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 132, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectOsteomyelitis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '245'),
            ({0}, {1}, '47');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 132, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectOsteomyelitis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '246'),
            ({0}, {1}, '47');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 132, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectOsteomyelitis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '247'),
            ({0}, {1}, '47');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMyositis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '248' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 133, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMyositis-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '249'),
            ({0}, {1}, '48');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 133, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMyositis-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '250'),
            ({0}, {1}, '48');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 133, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMyositis-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '251'),
            ({0}, {1}, '48');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectMusculoskeletalComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '243' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE name = 'Противоинфекционная терапия';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '253' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
DELETE FROM ActionPropertyType WHERE code = 'infectTherapyType';
'''    
    c.execute(sql)


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 136, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_1', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '254');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '254' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '254' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '254' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 140, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_2', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '255');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 143, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_3', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '255');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 146, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_4', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '256');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '256' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '256' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '256' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 149, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_5', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '257');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '257' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '257' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '257' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 152, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_6', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '258');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '258' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '258' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '258' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 155, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_7', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '259');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '259' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '259' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '259' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 158, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType_8', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '2'),
            ({0}, 9, '260');
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugName_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '260' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '260' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '2' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))


    sql = u'''
SELECT * FROM ActionPropertyType WHERE code = 'infectDrugEndDate_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '260' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '3' WHERE layoutAttribute_id = 23 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId))

    sql = u'''
UPDATE ActionPropertyType SET idx = '57' WHERE name = 'Данные об инфекционных осложнениях';
'''
    c.execute(sql)

    c.close()