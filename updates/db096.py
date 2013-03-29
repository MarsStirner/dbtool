#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
Добавление полей "Обязательное" и "Только для чтения" к типам свойств действия
'''

__author__ = 'viruzzz-kun'

query_template_1 = u'''
UPDATE `ActionPropertyType`
SET
    mandatory = '%s',
    readOnly = '%s'
WHERE 
    `code` LIKE '%s' AND
    `actionType_id` IN (
        SELECT `id`
        FROM `ActionType`
        WHERE `flatCode` LIKE '%s'
    )
'''
replacements_1 = (
    (1, 0, u'orgStructDirection', u'received'),
    (1, 0, u'hospOrgStruct',      u'moving'),
#    (1, 0, u'hospOrgStruct',      u'leaved'),
    (1, 0, u'hospOutcome',        u'leaved'),
)


query_template_2 = u'''
UPDATE `ActionPropertyType`
SET
    code = '%s',
    mandatory = '%s',
    readOnly = '%s'
WHERE 
    `name` LIKE '%s' AND
    `actionType_id` IN (
        SELECT `id`
        FROM `ActionType`
        WHERE `flatCode` LIKE '%s'
    )
'''

replacements_2 = (
    (u'nomen',       1, 0, u'Наименование',  u'prescription'),
    (u'dosage',      0, 1, u'Дозировка',     u'prescription'),
    (u'units',       0, 1, u'Единицы',       u'prescription'),
    (u'hospitalBed', 1, 0, u'койка',         u'moving'),
    (u'patronage',   1, 0, u'Патронаж',      u'moving'),
)


def upgrade(conn):
    global config        
    c = conn.cursor()

    try:
        c.execute(u'''ALTER TABLE `ActionPropertyType` ADD COLUMN `mandatory` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Является обязательным';''')
    except:
        print('''Column `ActionPropertyType`.`mandatory` already exists.''')
        traceback.print_exc()

    try:
        c.execute(u'''ALTER TABLE `ActionPropertyType` ADD COLUMN `readOnly` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Является только для чтения';''')
    except:
        print('''Column `ActionPropertyType`.`readOnly` already exists.''')    
        traceback.print_exc()

    c.execute(u"SET SQL_SAFE_UPDATES=0;")

    for rep in replacements_1:
        query = query_template_1 % rep
        c.execute(query)
        if c.rowcount < 1:
            print (u'Не удалось установить значения для свойства "%s" типа действия "%s". Требуется ручное вмешательство.' % (rep[2], rep[3]))

    for rep in replacements_2:
        query = query_template_2 % rep
        c.execute(query)
        if c.rowcount < 1:
            print (u'Не удалось установить значения для свойства "%s" типа действия "%s". Требуется ручное вмешательство.' % (rep[3], rep[4]))


    c.execute(u"SET SQL_SAFE_UPDATES=1;")

    c.close()


def downgrade(conn):
    pass
