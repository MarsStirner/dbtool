#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Исправление даты создания APT "Отделение поступления" в AT "Поступление". Это
влияет на правильную загрузку действий Поступлений в старых обращениях.
- Исправление факапа 107-133 обновлений
'''

# выпилено
def upgrade(conn):
    global tools
    c = conn.cursor()

#     sql = u'''
# SELECT apt.id, at.createDatetime
# FROM ActionType at JOIN ActionPropertyType apt ON at.id = apt.actionType_id
# WHERE apt.code = '%s' AND at.flatCode = '%s'
# ''' % ('orgStructStay', 'received')
#     num_rows = c.execute(sql)
#     if num_rows > 1:
#         print('Warning! Not unique APT')
#     apt_id, at_datetime = c.fetchone()
#     sql = u'''UPDATE ActionPropertyType SET createDatetime = '%s' WHERE id = %d''' % (at_datetime, apt_id)
#     c.execute(sql)
# 
#     sql = u'''UPDATE ActionPropertyType SET deleted = 1 WHERE code = '%s'
# AND actionType_id IN (SELECT id FROM ActionType WHERE flatCode = '%s' AND deleted = 0) ''' % ('hospOrgStruct', 'received')
#     c.execute(sql)
# 
#     c.close()


def downgrade(conn):
    pass
