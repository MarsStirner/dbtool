#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные для инфекционных осложнений
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
INSERT INTO `LayoutAttribute` (`title`, `description`, `code`, `typeName`, `measure`, `defaultValue`)
VALUES
	('Нераскрываемая вертикальная группа', '', 'NONTOGGLABLE', 'String', 'string', 'false');
'''
    c.execute(sql)

    groupAttrId = c.lastrowid

	sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 54, NULL, 'Данные об инфекционных осложнениях', '', NULL, 'String', '\'\'', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
    	INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 67, 'true'),
			(%s, 10, '12'),
			(%s, 76, 'false'),
			(%s, 77, ''),
			(%s, 80, 'false'),
			(%s, 81, ''),
			(%s, 9, '35');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 55, NULL, 'Инфекционные осложнения', '', NULL, 'String', 'Да, Нет', '', 'isInfect', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);

'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
    	INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '36'),
			(%s, 10, '3');

    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 56, NULL, 'Дата начала осложнения', '', NULL, 'Date', '', '', 'infectBeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
    	INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 23, '3'),
			(%s, 22, '36');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 57, NULL, 'Дата окончания осложнения', '', NULL, 'Date', '', '', 'infectEndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);

'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 23, '3'),
			(%s, 22, '36');

    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 58, NULL, 'Тип инфекции', '', NULL, 'String', '', '', 'infectType', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '37'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '5'),
			(%s, 107, 'true');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 59, NULL, 'Лихорадка неясного генеза', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
    	INSERT INTO `LayoutAttributeValue` (`id`, `actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '38'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 60, NULL, 'Бактериемия', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '39'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 61, NULL, 'Сепсис', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '40'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 62, NULL, 'Септический шок', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '41'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 63, NULL, 'Локальная инфекция', '', NULL, 'String', 'Да, Нет', '', 'infectLocal', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '42'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 69, NULL, 'Документированная инфекция', '', NULL, 'Html', '', '', 'infectDocumental', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 68, '43'),
			(%s, 69, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 70, NULL, 'Локализация', '', NULL, 'String', '\'\'', '', 'infectLocalisation', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '44'),
			(%s, 67, 'true');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 71, NULL, 'ЦНС', '', NULL, 'String', '', '', 'infectCNS', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '45'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '4'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 72, NULL, 'Абсцесс головного мозга', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 11, '5'),
			(%s, 9, '46');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 73, NULL, 'Менингит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '47'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 74, NULL, 'Менингоэнцефалит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '48'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 75, NULL, 'Энцефалит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '49'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 76, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '45'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 77, NULL, 'Глаз', '', NULL, 'String', '', '', 'infectEye', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '50'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '4');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 78, NULL, 'Коньюнктивит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '51'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 79, NULL, 'Воспаление параорбитальной клетчатки', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '52'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 80, NULL, 'Блефарит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '53'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 81, NULL, 'Хореоретинит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '54'),
			(%s, 11, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 82, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '50'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 83, NULL, 'Кожа и мягкие ткани (включая место стояния ЦВК)', '', NULL, 'String', '', '', 'infectSkin', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '55'),
			(%s, 10, '6'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '2');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 84, NULL, 'Нетяжелые инфекции кожи и мягких тканей (панариций, фурункул)', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '56'),
			(%s, 10, '6');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 85, NULL, 'Тяжелые инфекции кожи и мягких тканей (целлюлит, абсцесс, некроз)', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '57'),
			(%s, 10, '6');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 86, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '55'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 87, NULL, 'Слизистые', '', NULL, 'String', '', '', 'infectMucous', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '58'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 77, '4'),
			(%s, 76, 'true');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 88, NULL, 'Мукозит 1-2 ст', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '59'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 89, NULL, 'Мукозит 3-4 ст', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '60'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 90, NULL, 'Эзофагит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);

'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '61'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 91, NULL, 'Гингивит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '62'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 92, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '58'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 93, NULL, 'ЛОР', '', NULL, 'String', '', '', 'infectLOR', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '63'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '4');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 94, NULL, 'Ринит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '64'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 95, NULL, 'Тонзиллит/фарингит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '65'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 96, NULL, 'Отит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '66'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 97, NULL, 'Поражение ППН', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '67'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 98, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '63'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 99, NULL, 'Легкие', '', NULL, 'String', '', '', 'infectLungs', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '68'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '4');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 100, NULL, 'Бронхит/бронхопневмония', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '69'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
IINSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 101, NULL, 'Интерстициальная пневмония', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '70'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 102, NULL, 'Очаговая/долевая пневмония', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '71'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 103, NULL, 'Плеврит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '72'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 104, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '68'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 105, NULL, 'Сердце', '', NULL, 'String', '', '', 'infectHeart', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '73'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 106, NULL, 'Перикардит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '74'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 107, NULL, 'Миоардит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '75'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 108, NULL, 'Эндокардит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '76'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 109, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '73'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 110, NULL, 'Брюшная полость', '', NULL, 'String', '', '', 'infectAbdomen', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '77'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '10');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 111, NULL, 'Гастрит/гастродуоденит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '78'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 112, NULL, 'Панкреатит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '79'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 113, NULL, 'Холецистит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '80'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 114, NULL, 'Гепатит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '81'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 115, NULL, 'Гепато-лиенальный кандидоз', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '82'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 116, NULL, 'Абсцесс', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '83'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 117, NULL, 'Энтероколит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '84'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 118, NULL, 'Тифлит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '85'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 119, NULL, 'Аппендицит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '86'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 120, NULL, 'Перитонит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '87'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 121, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '77'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 122, NULL, 'Мочеполовая система', '', NULL, 'String', '', '', 'infectUrogenital', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '88'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '7');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 123, NULL, 'Гломерулонефрит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '89'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 124, NULL, 'Пиелонефрит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '90'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 125, NULL, 'Цистит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '91'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 126, NULL, 'Уретрит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '92'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 127, NULL, 'Эндометрит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '93'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 128, NULL, 'Аднексит (тубоовариальный абсцесс)', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '94'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 129, NULL, 'Вульвовагинит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '95'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 130, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '88'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 131, NULL, 'Костно-мышечная система', '', NULL, 'String', '', '', 'infectMusculoskeletal', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '96'),
			(%s, 10, '5'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '2');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 132, NULL, 'Остеомиелит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '97'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 133, NULL, 'Миозит', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '98'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 134, NULL, 'При отсутствии нужного диагноза напишите комментарий', '', NULL, 'String', '', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '96'),
			(%s, 10, '5');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 135, NULL, 'Противоинфекционная терапия', '', NULL, 'String', '\'\'', '', '', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
VALUES
	(%s, 9, '99'),
	(%s, 67, 'true');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 136, NULL, 'Тип терапии', '', NULL, 'String', 'Профилактика, Эмпирическая, Целенаправленная', '', 'infectTherapyType', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 10, '4'),
			(%s, 9, '100');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 64, NULL, 'Этиология', '', NULL, 'String', '', '', 'infectEtiology', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '37'),
			(%s, 67, 'true'),
			(%s, 76, 'true'),
			(%s, 77, '4'),
			(%s, %s, 'true');
    	''', (actionPropertyTypeId, groupAttrId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 65, NULL, 'Бактериальная', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '38'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 66, NULL, 'Грибковая', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '39'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 67, NULL, 'Вирусная', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '40'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 68, NULL, 'Неясной этиологии', '', NULL, 'String', 'Да, Нет', '', NULL, 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-19 11:16:11', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '41'),
			(%s, 11, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 137, NULL, 'Наименование препарата', '', NULL, 'String', 'Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин', '', 'infectDrugName', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '2013-11-05 18:12:27', 781, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 9, '101'),
			(%s, 10, '4');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 138, NULL, 'Дата назначения', '', NULL, 'Date', '', '', 'infectDrugBeginDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 22, '101'),
			(%s, 23, '3');
    	''', (actionPropertyTypeId))

    sql = '''
INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`, `defaultValue`, `code`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`, `createDatetime`, `createPerson_id`, `modifyDatetime`, `modifyPerson_id`)
VALUES
	(0, 4218, 139, NULL, 'Дата отмены', '', NULL, 'Date', '', '', 'infectDrugEndDate', 0, '', 0, '', NULL, NULL, NULL, NULL, 0, 0, 0, NULL, 0, 0, 0, 0, '0000-00-00 00:00:00', NULL, '2014-03-20 15:38:54', 781);
'''    
	c.execute(sql)
    actionPropertyTypeId = c.lastrowid
    c.execute('''
		INSERT INTO `LayoutAttributeValue` (`actionPropertyType_id`, `layoutAttribute_id`, `value`)
		VALUES
			(%s, 22, '101'),
			(%s, 23, '3');
    	''', (actionPropertyTypeId))


    c.close()