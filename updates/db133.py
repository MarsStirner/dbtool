#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Изменения для корректировки существующего бизнес-процесса ФНКЦ для работы
с движениями пациента в МИС
'''

# частично выпилено
def upgrade(conn):
    global tools
    c = conn.cursor()
#     # Обновление свойств в Поступлении
#     received_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'received\'')
#     if received_at_id:
#         # Отделение пребывания
#         apt_d = dict(actionType_id=received_at_id,
#                      name=u"'Отделение поступления'",
#                      descr=u"'Отделение поступления'",
#                      typeName=u"'OrgStructure'",
#                      code="'orgStructStay'",
#                      mandatory=1,
#                      )
#         tools.addNewActionProperty(c, **apt_d)
# 
#         # Направлен из
#         apt_d = dict(actionType_id=received_at_id,
#                      name=u"'Направлен из'",
#                      descr=u"'отделение из предыдущей истории болезни'",
#                      typeName=u"'OrgStructure'",
#                      code="'orgStructDirectedFrom'",
#                      )
#         tools.addNewActionProperty(c, **apt_d)
# 
    # Обновление свойств в Движении
    moving_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'moving\'')
    if moving_at_id:
#         # Переведен из отделения
#         sql = u'''
# UPDATE ActionPropertyType SET mandatory=1
# WHERE actionType_id=%d AND code='%s'
# ''' % (moving_at_id, 'orgStructReceived')
#         tools.executeEx(c, sql, modes=['safe_updates_off'])
 
        # Отделение пребывания
        sql = u'''
UPDATE ActionPropertyType SET code='%s'
WHERE actionType_id=%d AND (code='%s' OR name='Отделение пребывания')
''' % ('orgStructStay', moving_at_id, 'hospOrgStruct')
        tools.executeEx(c, sql, modes=['safe_updates_off'])
 
    c.close()


def downgrade(conn):
    pass
