#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные об инфекционных осложнениях
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute('SET SQL_SAFE_UPDATES=0;')

    sql = u'''
SELECT id FROM LayoutAttribute WHERE code = 'VGROUPROW' AND typeName = 'String';
'''
    c.execute(sql)
    vgroupRowStringId = c.fetchone()[0]

    sql = u'''
SELECT id FROM LayoutAttribute WHERE code = 'VGROUPROW' AND typeName = 'Date';
'''
    c.execute(sql)
    vgroupRowDateId = c.fetchone()[0]


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectCNSComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCNSComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '74' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCNS';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '20' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 76, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectCNSComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '75'),
            ({0}, {1}, '49');
        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 76, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectCNSComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '76'),
            ({0}, {1}, '49');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 76, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectCNSComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '77'),
            ({0}, {1}, '49');
        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEye';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '78' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '20' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectConjunctivitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '79' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectConjunctivitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '80' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectConjunctivitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '81' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectConjunctivitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '82' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeriorbital';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '83' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeriorbital-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '84' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeriorbital-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '85' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeriorbital-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '86' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBlepharitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '87' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBlepharitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '88' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBlepharitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '89' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBlepharitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '90' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectChorioretinitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '91' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectChorioretinitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '92' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectChorioretinitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '93' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectChorioretinitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '94' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectEyeComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEyeComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '95' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 82, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectEyeComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '96'),
            ({0}, {1}, '50');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 82, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectEyeComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '97'),
            ({0}, {1}, '50');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 82, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectEyeComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '98'),
            ({0}, {1}, '50');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkin';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '99' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '12' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinLight';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '100' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinLight-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '101' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinLight-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '102' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinLight-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '103' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinHard';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '104' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinHard-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '105' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinHard-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '106' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinHard-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '107' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectSkinComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectSkinComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '108' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '6' WHERE layoutAttribute_id = 10 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 86, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectSkinComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '109'),
            ({0}, {1}, '51');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 86, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectSkinComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '110'),
            ({0}, {1}, '51');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 86, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectSkinComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '111'),
            ({0}, {1}, '51');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucous';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '112' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '20' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis12';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '113' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis12-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '114' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis12-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '115' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis12-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '116' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis34';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '117' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis34-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '118' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis34-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '119' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucositis34-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '120' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEsophagitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '121' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEsophagitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '122' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEsophagitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '123' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEsophagitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '124' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGingivitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '125' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGingivitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '126' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGingivitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '127' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGingivitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '128' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectMucousComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMucousComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '129' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 92, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMucousComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '130'),
            ({0}, {1}, '52');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 92, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMucousComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '131'),
            ({0}, {1}, '52');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 92, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMucousComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '132'),
            ({0}, {1}, '52');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLOR';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '133' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '20' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectRhinitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '134' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectRhinitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '135' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectRhinitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '136' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectRhinitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '138' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTonsillitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '139' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTonsillitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '140' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTonsillitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '141' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTonsillitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '142' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOtitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '143' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOtitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '144' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOtitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '145' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOtitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '146' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDefeatPPN';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '147' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDefeatPPN-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '148' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDefeatPPN-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '149' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDefeatPPN-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '150' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectLORComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLORComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '151' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 98, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectLORComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '152'),
            ({0}, {1}, '53');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 98, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectLORComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '153'),
            ({0}, {1}, '53');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 98, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectLORComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '154'),
            ({0}, {1}, '53');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLungs';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '155' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '20' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBronchitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '156' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBronchitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '157' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBronchitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '158' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectBronchitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '159' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectInterstitialPneumonia';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '160' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectInterstitialPneumonia-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '161' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectInterstitialPneumonia-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '162' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectInterstitialPneumonia-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '163' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLobarPneumonia';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '164' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLobarPneumonia-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '165' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLobarPneumonia-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '166' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLobarPneumonia-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '167' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPleurisy';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '168' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPleurisy-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '169' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPleurisy-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '170' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPleurisy-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '171' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectLungsComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectLungsComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '172' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 104, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectLungsComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '173'),
            ({0}, {1}, '54');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 104, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectLungsComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '174'),
            ({0}, {1}, '54');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 104, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectLungsComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '175'),
            ({0}, {1}, '54');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectHeart';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '176' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '16' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPericarditis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '177' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPericarditis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '178' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPericarditis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '179' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPericarditis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '180' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMioardit';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '181' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMioardit-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '182' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMioardit-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '183' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMioardit-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '184' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndocarditis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '185' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndocarditis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '186' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndocarditis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '187' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndocarditis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '188' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectHeartComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectHeartComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '189' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 109, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectHeartComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '190'),
            ({0}, {1}, '55');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 109, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectHeartComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '191'),
            ({0}, {1}, '55');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 109, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectHeartComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '192'),
            ({0}, {1}, '55');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAbdomen';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '193' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '44' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGastritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '194' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGastritis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '195' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGastritis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '196' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGastritis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '197' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPancreatitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '198' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPancreatitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '199' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPancreatitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '200' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPancreatitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '201' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCholecystitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '202' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCholecystitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '203' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCholecystitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '204' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCholecystitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '205' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infecThepatitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '206' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infecThepatitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '207' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infecThepatitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '208' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infecThepatitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '209' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGepatolienalnyCandidiasis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '210' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGepatolienalnyCandidiasis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '211' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGepatolienalnyCandidiasis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '212' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGepatolienalnyCandidiasis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '213' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAbscess';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '214' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAbscess-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '215' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAbscess-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '216' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAbscess-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '217' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEnterocolitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '218' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEnterocolitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '219' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEnterocolitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '220' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEnterocolitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '221' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCecitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '222' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCecitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '223' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCecitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '224' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCecitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '225' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAppendicitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '226' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAppendicitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '227' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAppendicitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '228' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAppendicitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '229' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeritonitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '230' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeritonitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '231' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeritonitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '232' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPeritonitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '233' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectAbdomenComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAbdomenComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '234' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 121, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectAbdomenComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '235'),
            ({0}, {1}, '56');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 121, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectAbdomenComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '236'),
            ({0}, {1}, '56');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 121, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectAbdomenComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '237'),
            ({0}, {1}, '56');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectUrogenital';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '238' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '32' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGlomerulonephritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '239' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGlomerulonephritis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '240' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGlomerulonephritis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '241' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectGlomerulonephritis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '242' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPyelonephritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '243' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPyelonephritis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '244' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPyelonephritis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '245' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectPyelonephritis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '246' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCystitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '247' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCystitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '248' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCystitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '249' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectCystitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '250' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectUrethritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '251' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectUrethritis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '252' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectUrethritis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '253' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectUrethritis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '254' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndometritis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '255' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndometritis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '256' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndometritis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '257' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectEndometritis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '258' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAdnexitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '259' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAdnexitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '260' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAdnexitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '261' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectAdnexitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '262' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectVulvovaginitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '263' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectVulvovaginitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '264' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectVulvovaginitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '265' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectVulvovaginitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '266' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectUrogenitalComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectUrogenitalComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '267' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 130, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectUrogenitalComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '268'),
            ({0}, {1}, '57');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 130, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectUrogenitalComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '269'),
            ({0}, {1}, '57');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 130, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectUrogenitalComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '270'),
            ({0}, {1}, '57');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMusculoskeletal';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '271' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '12' WHERE layoutAttribute_id = 77 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOsteomyelitis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '272' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOsteomyelitis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '273' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOsteomyelitis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '274' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectOsteomyelitis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '275' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMyositis';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '276' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMyositis-BeginDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '277' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMyositis-EndDate';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '278' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMyositis-Etiology';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '279' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET name = 'Другое' WHERE code = 'infectMusculoskeletalComment';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectMusculoskeletalComment';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '280' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 134, NULL, 'Дата начала', '', NULL, 'Date', '', '', 'infectMusculoskeletalComment-BeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '281'),
            ({0}, {1}, '58');

        '''.format(actionPropertyTypeId, vgroupRowDateId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 134, NULL, 'Дата окончания', '', NULL, 'Date', '', '', 'infectMusculoskeletalComment-EndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 22, '282'),
            ({0}, {1}, '58');

        '''.format(actionPropertyTypeId, vgroupRowDateId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 134, NULL, 'Этиология', '', NULL, 'String', 'бактериальная, грибковая, вирусная, неясной этиологии', '', 'infectMusculoskeletalComment-Etiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '283'),
            ({0}, {1}, '58');

        '''.format(actionPropertyTypeId, vgroupRowStringId))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE name = 'Противоинфекционная терапия';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '284' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '285' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '285' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '285' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_1';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '285' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '286' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '286' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '286' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_2';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '286' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '287' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '287' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '287' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_3';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '287' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '288' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '288' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '288' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_4';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '288' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '289' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '289' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '289' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_5';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '289' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '290' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '290' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '290' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_6';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '290' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '291' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '291' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '291' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_7';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '291' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapyType_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '292' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugName_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '292' WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '292' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectDrugEndDate_8';
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        UPDATE LayoutAttributeValue SET value = '292' WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0};
        '''.format(actionPropertyTypeId[0]))


    sql = u'''
UPDATE ActionPropertyType SET code = 'infect' WHERE name = 'Данные об инфекционных осложнениях';
'''
    c.execute(sql)

    sql = u'''
UPDATE ActionPropertyType SET code = 'infectTherapy' WHERE name = 'Противоинфекционная терапия';
'''
    c.execute(sql)


    sql = u'''
SELECT id FROM ActionPropertyType WHERE actionType_id = 4219 ORDER BY id DESC LIMIT 1;
'''    
    c.execute(sql)
    firstActionTypeId = c.fetchone()


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
SELECT `deleted`, 4219, `idx`+2, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`
FROM `ActionPropertyType` WHERE `actionType_id` = 4218 AND `idx` > 56;
''' 
    c.execute(sql)

    c.execute('''
        SELECT t1.id, t2.id FROM ActionPropertyType t1, ActionPropertyType t2 WHERE t1.code=t2.code AND t2.id > {0} AND t1.actionType_id = 4218 AND t2.actionType_id = 4219;
        '''.format(firstActionTypeId[0]))

    records = c.fetchall()

    for row in records:
        c.execute('''
INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`) SELECT {0}, `layoutAttribute_id`, `value` FROM `LayoutAttributeValue` WHERE `actionPropertyType_id` = {1}
        '''.format(row[1], row[0]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 2 WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0}
        '''.format(row[1]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 2 WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0}
        '''.format(row[1]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 2 WHERE layoutAttribute_id = 68 AND actionPropertyType_id = {0}
        '''.format(row[1]))


        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
SELECT `deleted`, 4220, `idx`+3, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`
FROM `ActionPropertyType` WHERE `actionType_id` = 4218 AND `idx` > 56;
''' 
    c.execute(sql)

    c.execute('''
        SELECT t1.id, t2.id FROM ActionPropertyType t1, ActionPropertyType t2 WHERE t1.code=t2.code AND t2.id > {0} AND t1.actionType_id = 4218 AND t2.actionType_id = 4220;
        '''.format(firstActionTypeId[0]))

    records = c.fetchall()

    for row in records:
        c.execute('''
INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`) SELECT {0}, `layoutAttribute_id`, `value` FROM `LayoutAttributeValue` WHERE `actionPropertyType_id` = {1}
        '''.format(row[1], row[0]))


        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
SELECT `deleted`, 4221, `idx`+1, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`
FROM `ActionPropertyType` WHERE `actionType_id` = 4218 AND `idx` > 56;
''' 
    c.execute(sql)

    c.execute('''
        SELECT t1.id, t2.id FROM ActionPropertyType t1, ActionPropertyType t2 WHERE t1.code=t2.code AND t2.id > {0} AND t1.actionType_id = 4218 AND t2.actionType_id = 4221;
        '''.format(firstActionTypeId[0]))

    records = c.fetchall()

    for row in records:
        c.execute('''
INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`) SELECT {0}, `layoutAttribute_id`, `value` FROM `LayoutAttributeValue` WHERE `actionPropertyType_id` = {1}
        '''.format(row[1], row[0]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 1 WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0}
        '''.format(row[1]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 1 WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0}
        '''.format(row[1]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 1 WHERE layoutAttribute_id = 68 AND actionPropertyType_id = {0}
        '''.format(row[1]))


        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
SELECT `deleted`, 4222, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`
FROM `ActionPropertyType` WHERE `actionType_id` = 4218 AND `idx` > 56;
''' 
    c.execute(sql)

    c.execute('''
        SELECT t1.id, t2.id FROM ActionPropertyType t1, ActionPropertyType t2 WHERE t1.code=t2.code AND t2.id > {0} AND t1.actionType_id = 4218 AND t2.actionType_id = 4222;
        '''.format(firstActionTypeId[0]))

    records = c.fetchall()

    for row in records:
        c.execute('''
INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`) SELECT {0}, `layoutAttribute_id`, `value` FROM `LayoutAttributeValue` WHERE `actionPropertyType_id` = {1}
        '''.format(row[1], row[0]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 1 WHERE layoutAttribute_id = 22 AND actionPropertyType_id = {0}
        '''.format(row[1]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 1 WHERE layoutAttribute_id = 9 AND actionPropertyType_id = {0}
        '''.format(row[1]))
        c.execute('''
UPDATE LayoutAttributeValue SET value = value + 1 WHERE layoutAttribute_id = 68 AND actionPropertyType_id = {0}
        '''.format(row[1]))
    
    c.execute('SET SQL_SAFE_UPDATES=1;')

    c.close()