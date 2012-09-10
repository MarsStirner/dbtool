# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
добавляется тип свойства действия "Канал госпитализации"
'''

actionReceivedTypeId = 112 # действие "поступление"

def upgrade(conn):
    sql0 = [
'''\
INSERT INTO `ActionPropertyType` 
    (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `typeName`, `defaultValue`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `descr`, `valueDomain`) 
VALUES 
    (0, %d, 0, NULL, 'Канал госпитализации', 'Organisation', '', 0, '', 0, '', 0, 000, 0, 000, 0, 0, 0, NULL, 0, 0, 'Канал госпитализации', '');
''' % actionReceivedTypeId
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)
        
def downgrade(conn):
    sql0 = [
'''\
DELETE FROM `ActionPropertyType` WHERE `name` like "Канал госпитализации";
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)