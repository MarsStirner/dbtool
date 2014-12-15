#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменения в разделе Противоинфекционная терапия
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute('SET SQL_SAFE_UPDATES=0;')

    for i in range(1, 8):
        c.execute('''
        DELETE FROM ActionPropertyType WHERE code = 'infectTherapyType_{0}';
        '''.format(i))
        c.execute('''
        DELETE FROM ActionPropertyType WHERE code = 'infectDrugName_{0}';
        '''.format(i))
        c.execute('''
        DELETE FROM ActionPropertyType WHERE code = 'infectDrugBeginDate_{0}';
        '''.format(i))
        c.execute('''
        DELETE FROM ActionPropertyType WHERE code = 'infectDrugEndDate_{0}';
        '''.format(i))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapy' AND actionType_id = 4218;
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '12'),
            ({0}, 76, 'true'),
            ({0}, 77, '73'),
            ({0}, 96, 'false');

        '''.format(actionPropertyTypeId))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapy' AND actionType_id = 4219;
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '12'),
            ({0}, 76, 'true'),
            ({0}, 77, '73'),
            ({0}, 96, 'false');

        '''.format(actionPropertyTypeId))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapy' AND actionType_id = 4220;
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '12'),
            ({0}, 76, 'true'),
            ({0}, 77, '73'),
            ({0}, 96, 'false');

        '''.format(actionPropertyTypeId))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapy' AND actionType_id = 4221;
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '12'),
            ({0}, 76, 'true'),
            ({0}, 77, '73'),
            ({0}, 96, 'false');

        '''.format(actionPropertyTypeId))

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectTherapy' AND actionType_id = 4222;
'''    
    c.execute(sql)
    actionPropertyTypeId = c.fetchone()
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 10, '12'),
            ({0}, 76, 'true'),
            ({0}, 77, '73'),
            ({0}, 96, 'false');

        '''.format(actionPropertyTypeId))


    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 200, NULL, 'Профилактика', '', NULL, 'String', 'Да', '', 'infectProphylaxis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '285');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 200, NULL, 'Профилактика', '', NULL, 'String', 'Да', '', 'infectProphylaxis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '286');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 200, NULL, 'Профилактика', '', NULL, 'String', 'Да', '', 'infectProphylaxis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '285');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 200, NULL, 'Профилактика', '', NULL, 'String', 'Да', '', 'infectProphylaxis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '286');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 200, NULL, 'Профилактика', '', NULL, 'String', 'Да', '', 'infectProphylaxis', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '286');
        '''.format(actionPropertyTypeId))


    for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 201, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectProphylaxisName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 286+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 201, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectProphylaxisName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 287+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 201, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectProphylaxisName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 286+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 201, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectProphylaxisName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 287+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 201, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectProphylaxisName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 287+(i*3), 60+(i*1)))


        for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 202, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectProphylaxisBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 287+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 202, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectProphylaxisBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 288+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 202, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectProphylaxisBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 287+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 202, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectProphylaxisBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 288+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 202, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectProphylaxisBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 288+(i*3), 60+(i*1)))


        for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 203, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectProphylaxisEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 288+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 203, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectProphylaxisEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 289+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 203, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectProphylaxisEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 288+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 203, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectProphylaxisEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 289+(i*3), 60+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 203, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectProphylaxisEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 289+(i*3), 60+(i*1)))


        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 204, NULL, 'Эмпирическая', '', NULL, 'String', 'Да', '', 'infectEmpiric', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '310');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 204, NULL, 'Эмпирическая', '', NULL, 'String', 'Да', '', 'infectEmpiric', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '311');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 204, NULL, 'Эмпирическая', '', NULL, 'String', 'Да', '', 'infectEmpiric', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '310');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 204, NULL, 'Эмпирическая', '', NULL, 'String', 'Да', '', 'infectEmpiric', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '311');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 204, NULL, 'Эмпирическая', '', NULL, 'String', 'Да', '', 'infectEmpiric', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '311');
        '''.format(actionPropertyTypeId))


    for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 205, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectEmpiricName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 311+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 205, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectEmpiricName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 312+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 205, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectEmpiricName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 311+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 205, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectEmpiricName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 312+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 205, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectEmpiricName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 312+(i*3), 68+(i*1)))


        for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 206, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectEmpiricBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 312+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 206, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectEmpiricBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 313+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 206, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectEmpiricBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 312+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 206, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectEmpiricBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 313+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 206, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectEmpiricBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 313+(i*3), 68+(i*1)))


        for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 207, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectEmpiricEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 313+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 207, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectEmpiricEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 314+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 207, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectEmpiricEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 313+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 207, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectEmpiricEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 314+(i*3), 68+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 207, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectEmpiricEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 314+(i*3), 68+(i*1)))


        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 208, NULL, 'Целенаправленная', '', NULL, 'String', 'Да', '', 'infectTelic', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '335');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 208, NULL, 'Целенаправленная', '', NULL, 'String', 'Да', '', 'infectTelic', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '336');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 208, NULL, 'Целенаправленная', '', NULL, 'String', 'Да', '', 'infectTelic', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '335');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 208, NULL, 'Целенаправленная', '', NULL, 'String', 'Да', '', 'infectTelic', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '336');
        '''.format(actionPropertyTypeId))

    sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 208, NULL, 'Целенаправленная', '', NULL, 'String', 'Да', '', 'infectTelic', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
    c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
        INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
        VALUES
            ({0}, 9, '336');
        '''.format(actionPropertyTypeId))


    for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 209, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectTelicName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 336+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 209, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectTelicName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 337+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 209, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectTelicName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 336+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 209, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectTelicName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 337+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 209, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectTelicName_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 9, '{1}'),
                ({0}, 97, '{2}');
            '''.format(actionPropertyTypeId, 337+(i*3), 84+(i*1)))


        for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 210, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectTelicBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 337+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 210, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectTelicBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 338+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 210, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectTelicBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 337+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 210, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectTelicBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 338+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 210, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectTelicBeginDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 338+(i*3), 84+(i*1)))


        for i in range(0, 7):
        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4218, 211, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectTelicEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 338+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4219, 211, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectTelicEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 339+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4220, 211, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectTelicEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 338+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4221, 211, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectTelicEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 339+(i*3), 84+(i*1)))

        sql = u'''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
    (0, 4222, 211, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectTelicEndDate_{0}', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
        c.execute(sql.format(i+1))
        actionPropertyTypeId = c.lastrowid
        c.execute('''
            INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
            VALUES
                ({0}, 22, '{1}'),
                ({0}, 98, '{2}');
            '''.format(actionPropertyTypeId, 339+(i*3), 84+(i*1)))

    
    c.execute('SET SQL_SAFE_UPDATES=1;')

    c.close()