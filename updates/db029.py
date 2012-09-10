# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Убираем номер ИБ из поступления
'''

actionReceivedTypeId = 112 # действие "поступление"

def upgrade(conn):
    sql0 = [
'''\
DELETE FROM `ActionPropertyType` WHERE ActionType_id=%d and `name` like "Номер ИБ";
''' % actionReceivedTypeId
    ] 
    c = conn.cursor()
    for s in sql0:
        c.execute(s)
        
def downgrade(conn):
    sql0 = [
'''\
INSERT INTO `ActionPropertyType` 
    (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `typeName`, `defaultValue`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `descr`, `valueDomain`) 
VALUES 
    (0, %d, 0, NULL, 'Номер ИБ', 'Text', '', 0, '', 0, '', 0, 000, 0, 000, 0, 0, 0, NULL, 0, 0, 'Номер истории болезни', '');
''' % actionReceivedTypeId
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)