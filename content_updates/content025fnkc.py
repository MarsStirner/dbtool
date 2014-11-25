#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление к каждому БАК исследованию свойства comment для хранения комментария
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = '''INSERT INTO
  ActionPropertyType (actionType_id, idx, name, descr, typeName, valueDomain, defaultValue, code, norm, sex, age, createDatetime, modifyDatetime, createPerson_id, modifyPerson_id)
  SELECT
      at.id as actionTypeId,
      MAX(p.idx) + 1 as idx,
      'Комментарий' as actionTypeName,
      'Комментарий к результатам лабораторного исследования' as actionTypeDescr,
      'String' as actionTypeTypeName,
      '' as actionTypeValueDomain,
      '' as actionTypeDefaultValue,
      'comment' as actionTypeCode,
      '' actionTypeNorm,
      0 as actionTypeSex,
      '' as actionTypeSexAge,
      NOW() as actionTypeCreateDatetime,
      NOW() as actionTypeModifyDatetime,
      1 as actionTypeCreatePerson_id,
      1 as actionTypeModifyPerson_id
    FROM ActionType at, ActionPropertyType p WHERE
      p.actionType_id=at.id AND
      ((at.group_id = 3900)
       OR EXISTS(SELECT * FROM ActionType WHERE id = at.group_id AND group_id = 3900))
    AND NOT EXISTS(SELECT * FROM ActionType WHERE group_id = at.id)
    GROUP BY
      actionTypeId,
      actionTypeName,
      actionTypeDescr,
      actionTypeTypeName,
      actionTypeValueDomain,
      actionTypeDefaultValue,
      actionTypeCode,
      actionTypeNorm,
      actionTypeSex,
      actionTypeSexAge,
      actionTypeCreateDatetime,
      actionTypeModifyDatetime,
      actionTypeCreatePerson_id,
      actionTypeModifyPerson_id;'''
    c.execute(sql)
    sql = '''INSERT INTO
  ActionPropertyType (actionType_id, idx, name, descr, typeName, valueDomain, defaultValue, code, norm, sex, age, createDatetime, modifyDatetime, createPerson_id, modifyPerson_id)
  SELECT
      at.id as actionTypeId,
      MAX(p.idx) + 1 as idx,
      'Комментарий' as actionTypeName,
      'Комментарий к результатам лабораторного исследования' as actionTypeDescr,
      'String' as actionTypeTypeName,
      '' as actionTypeValueDomain,
      '' as actionTypeDefaultValue,
      'comment' as actionTypeCode,
      '' actionTypeNorm,
      0 as actionTypeSex,
      '' as actionTypeSexAge,
      NOW() as actionTypeCreateDatetime,
      NOW() as actionTypeModifyDatetime,
      1 as actionTypeCreatePerson_id,
      1 as actionTypeModifyPerson_id
    FROM ActionType at, ActionPropertyType p WHERE
      p.actionType_id=at.id AND
      ((at.group_id = 4027)
       OR EXISTS(SELECT * FROM ActionType WHERE id = at.group_id AND group_id = 4027))
    AND NOT EXISTS(SELECT * FROM ActionType WHERE group_id = at.id)
    GROUP BY
      actionTypeId,
      actionTypeName,
      actionTypeDescr,
      actionTypeTypeName,
      actionTypeValueDomain,
      actionTypeDefaultValue,
      actionTypeCode,
      actionTypeNorm,
      actionTypeSex,
      actionTypeSexAge,
      actionTypeCreateDatetime,
      actionTypeModifyDatetime,
      actionTypeCreatePerson_id,
      actionTypeModifyPerson_id;'''
    c.execute(sql)
    c.close()