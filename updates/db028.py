# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
добавляется тип свойства действия "Канал госпитализации"
'''

actionReceivedTypeCode = "4201" # действие "поступление"
actionReceivedTypeFlatCode = "received" # действие "поступление"

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def upgrade(conn):
    rows = query(conn, 'SELECT id FROM ActionType where code="%s" or flatCode="%s"' % (actionReceivedTypeCode, actionReceivedTypeFlatCode))
    if rows:
        at_id = rows[0][0]
        
        sql0 = '''
    INSERT INTO `ActionPropertyType` 
        (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `typeName`, `defaultValue`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `test_id`, `defaultEvaluation`, `toEpicrisis`, `descr`, `valueDomain`) 
    VALUES 
        (0, %d, 0, NULL, 'Канал госпитализации', 'Organisation', '', 0, '', 0, '', 0, 000, 0, 000, 0, 0, 0, NULL, 0, 0, 'Канал госпитализации', '');
    ''' % at_id
        c = conn.cursor()
        c.execute(sql0)
        
def downgrade(conn):
    sql0 = [
'''\
DELETE FROM `ActionPropertyType` WHERE `name` like "Канал госпитализации";
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)