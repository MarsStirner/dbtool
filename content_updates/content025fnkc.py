#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление к каждому ИФА исследованию свойства comment для хранения комментария
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = '''INSERT INTO
  ActionPropertyType (actionType_id, name, descr, typeName, valueDomain, defaultValue, code, norm, sex, age, createDatetime, modifyDatetime)
  SELECT id, 'Комментарий', 'Комментарий к результатам лабораторного исследования', 'String', '','', 'comment', '', 0, '', NOW(), NOW() FROM ActionType at WHERE
  ((at.group_id = 3900)
   OR EXISTS(SELECT * FROM ActionType WHERE id = at.group_id AND group_id = 3900))
AND NOT EXISTS(SELECT * FROM ActionType WHERE group_id = at.id);'''
    c.execute(sql)
    c.close()