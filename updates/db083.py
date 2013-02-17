#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Изменения, необходимые для записи между ЛПУ, добавляются новые типы действий
'Направление' и 'Направление на консультацию в другое ЛПУ', если их еще нет, и
свойства для последнего
'''


def upgrade(conn):
    global config        
    c = conn.cursor()
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `ActionProperty_OtherLPURecord` (
`id` int(11) NOT NULL COMMENT '{ActionProperty}',
`index` int(11) NOT NULL DEFAULT '0' COMMENT 'Индекс элемента векторного значения или 0',
`value` text COLLATE utf8_unicode_ci NOT NULL COMMENT 'собственно значение',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
'''
    c.execute(sql)
    
    def checkRecordExists(c, table, cond):
        c.execute(u'''SELECT id FROM %s where %s ''' % (table, cond))
        result = c.fetchone()
        if result:
            id_ = int(result[0])
        else:
            id_ = None
        return id_
    
    # Создание общего типа 'Направление'
    parentAT_id = checkRecordExists(c, u'ActionType', u"code='4100' and deleted=0 and group_id IS NULL")
    if not parentAT_id:
        sql = u'''
INSERT INTO ActionType(`createDatetime`, `modifyDatetime`, `class`, `code`, `name`, `title`, 
`flatCode`, `sex`, `age`, `office`, `showInForm`, `genTimetable`, `context`, `amount`, `amountEvaluation`, `defaultStatus`, 
`defaultDirectionDate`, `defaultPlannedEndDate`, `defaultEndDate`, `defaultPersonInEvent`, `defaultPersonInEditor`, 
`maxOccursInEvent`, `showTime`, `isMES`, `isPreferable`, `isRequiredCoordination`, `isRequiredTissue`) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 3, '4100', 'Направление', 'Направление', '', 0, '', '', 0, 0, 
'direction', 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
'''
        c.execute(sql)
        parentAT_id = conn.insert_id()
    
    # Создание 'Направление на консультацию в другое ЛПУ'
    AT_id = checkRecordExists(c, u'ActionType', u"code='4100' and deleted=0 and group_id=%s" % parentAT_id)
    if not AT_id:
        sql = u'''
INSERT INTO ActionType(`createDatetime`, `modifyDatetime`, `class`, `group_id`, `code`, 
`name`, `title`, `flatCode`, `sex`, `age`, `office`, `showInForm`, `genTimetable`, `context`, `amount`, `amountEvaluation`, 
`defaultStatus`, `defaultDirectionDate`, `defaultPlannedEndDate`, `defaultEndDate`, `defaultPersonInEvent`, `defaultPersonInEditor`, 
`maxOccursInEvent`, `showTime`, `isMES`, `isPreferable`, `isRequiredCoordination`, `isRequiredTissue`) 
VALUES ('2013-02-13T11:40:02', '2013-02-13T11:40:02', 3, %s, '4100', 'Направление на консультацию в другое ЛПУ', 
'Направление на консультацию в другое ЛПУ', '', 0, '', '', 0, 0, 'direction', 1.0, 0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0)
''' % parentAT_id
        c.execute(sql)
        AT_id = conn.insert_id()
    
    
    # Свойства для 'Направление на консультацию в другое ЛПУ'
    prop_id = checkRecordExists(c, u'ActionPropertyType', 
        u"name='Куда направляется' and deleted=0 and actionType_id=%s" % AT_id)
    if not prop_id:
        sql = u'''
INSERT INTO ActionPropertyType(`name`, `descr`, `typeName`, `valueDomain`, `penalty`, `actionType_id`, `idx`,
`defaultValue`, `norm`, `sex`, `age`) 
VALUES ('Куда направляется', 'Наименование ЛПУ направления', 'Organisation', 'ЛПУ', 0, %s, 0, '', '', 0, '')
''' % AT_id
        c.execute(sql)

    prop_id = checkRecordExists(c, u'ActionPropertyType', 
        u"name='Порядок направления' and deleted=0 and actionType_id=%s" % AT_id)
    if not prop_id:
        sql = u'''
INSERT INTO ActionPropertyType(`name`, `descr`, `typeName`, `valueDomain`, `penalty`, `defaultValue`, `actionType_id`, 
`idx`, `norm`, `sex`, `age`)
VALUES ('Порядок направления', 'Порядок направления', 'String', "'планово','экстренно'", 0, 'планово', %s, 1, '', 0, '')
''' % AT_id
        c.execute(sql)

    prop_id = checkRecordExists(c, u'ActionPropertyType', 
        u"name='Обоснование направления' and deleted=0 and actionType_id=%s" % AT_id)
    if not prop_id:
        sql = u'''
INSERT INTO ActionPropertyType(`name`, `descr`, `typeName`, `penalty`, `actionType_id`, `idx`,
`defaultValue`, `norm`, `sex`, `age`) 
VALUES ('Обоснование направления', 'Обоснование', 'Text', 0, %s, 2, '', '', 0, '')
''' % AT_id
        c.execute(sql)

    prop_id = checkRecordExists(c, u'ActionPropertyType', 
        u"name='Данные результатов обследования' and deleted=0 and actionType_id=%s" % AT_id)
    if not prop_id:
        sql = u'''
INSERT INTO ActionPropertyType(`name`, `descr`, `typeName`, `penalty`, `actionType_id`, `idx`,
`defaultValue`, `norm`, `sex`, `age`) 
VALUES ('Данные результатов обследования', 'Данные результатов обследования', 'Text', 0, %s, 3, '', '', 0, '')
''' % AT_id
        c.execute(sql)
        
    prop_id = checkRecordExists(c, u'ActionPropertyType', 
        u"name='Время приема' and deleted=0 and actionType_id=%s" % AT_id)
    if not prop_id:
        sql = u'''
INSERT INTO ActionPropertyType(`name`, `descr`, `typeName`, `penalty`, `actionType_id`, `idx`,
`defaultValue`, `norm`, `sex`, `age`)
 VALUES ('Время приема', 'Время приема', 'Запись в др. ЛПУ', 0, %s, 4, '', '', 0, '')
''' % AT_id
        c.execute(sql)


def downgrade(conn):
    pass
