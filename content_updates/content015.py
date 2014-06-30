#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Удаление старых расписаний
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    c.execute('''SET foreign_key_checks=0;''')
    names = [
        'Action', 'Time', 'String', 'Date', 'Double', 'FDRecord', 'HospitalBed', 'HospitalBedProfile',
        'Image', 'ImageMap', 'Integer', 'Job_Ticket', 'MKB', 'Organisation', 'OrgStructure', 'OtherLPURecord',
        'Person', 'rbReasonOfAbsence', 'rbBloodComponentType', 'rbFinance'
    ]
    sql_delete_ap_val = '''DELETE FROM ActionProperty_%s WHERE id NOT IN (SELECT id FROM ActionProperty)'''
    print('Events deleted:', c.execute('''
DELETE FROM Event WHERE Event.eventType_id IN (SELECT id FROM EventType WHERE code IN ('queue', '0'))
'''))
    print('Actions deleted:', c.execute('''
DELETE FROM Action WHERE Action.event_id NOT IN (SELECT id FROM Event)
'''))
    print('ActionProperties deleted:', c.execute('''
DELETE FROM ActionProperty WHERE action_id NOT IN (SELECT id FROM Action)
'''))
    for name in names:
        affected = c.execute(sql_delete_ap_val % name)
        print(name, affected)
    c.execute('''SET foreign_key_checks=1;''')
    c.close()