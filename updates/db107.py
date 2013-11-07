#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление нового свойства действия для поступления: отделение поступления
'''

def upgrade(conn):
    # отключено, будет добавлено в 133
    pass
#     global config
#     c = conn.cursor()
#
#     def checkRecordExists(c, table, cond):
#         c.execute(u'''SELECT id FROM %s where %s ''' % (table, cond))
#         result = c.fetchone()
#         if result:
#             id_ = int(result[0])
#         else:
#             id_ = None
#         return id_
#
#     AT_id = checkRecordExists(c, u'ActionType', u"flatCode='received'")
#
#     if AT_id:
#         APT_id = checkRecordExists(c, u'ActionPropertyType', u"code='hospOrgStruct' and actionType_id=%s"%AT_id)
#         if not APT_id:
#             sql = u'''
#             INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `name`, `descr`, `typeName`, `valueDomain`, `defaultValue`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `defaultEvaluation`, `toEpicrisis`, `code`, `mandatory`, `readOnly`) 
#             VALUES (0, %s, 0, 'Отделение поступления', 'Отделение, откуда поступил пациент, либо Приёмное отделение', 'OrgStructure', '', '', 0, '', 0, '', 0, 000, 0, 000, 0, 0, 0, 0, 0, 'hospOrgStruct', 0, 1);
#         ''' % AT_id
#             c.execute(sql)
#     c.close()

def downgrade(conn):
    pass
