#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление кодов для свойств действий типов "Поступление", "Движение", "Выписка"
'''
__author__ = 'viruzzz-kun'

query_template = u'''
UPDATE `ActionPropertyType`
SET
    code = '%s'
WHERE 
    `name` LIKE '%s' AND
    `actionType_id` IN (
        SELECT `id`
        FROM `ActionType`
        WHERE `name` LIKE '%s'
    )
'''

replacements = (
    (u'orgStructDirection', u'Направлен в отделение',       u'Поступление'),
    (u'orgStructTransfer',  u'Переведен в отделение',       u'Движение'),
    (u'orgStructReceived',  u'Переведен из отделения',      u'Движение'),
    (u'hospOrgStruct',      u'Отделение пребывания',        u'Движение'),
    (u'hospOrgStruct',      u'Отделение госпитализации',    u'Выписка'),
)

def upgrade(conn):
    global config
    c = conn.cursor()
    
    print (u"Установка кодов для свойств действий...")
    c.execute(u"SET SQL_SAFE_UPDATES=0;")
    for rep in replacements:
        query = query_template % rep
        c.execute(query)
        if c.rowcount < 1:
            print (u'Не удалось установить код "%s" для свойства "%s" типа действия "%s". Требуется ручное вмешательство.' % rep)
    c.execute(u"SET SQL_SAFE_UPDATES=1;")


def downgrade(conn):
    pass
