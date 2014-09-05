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

    event_num = tools.executeEx(c,
                                '''DELETE FROM Event WHERE Event.eventType_id IN (SELECT id FROM EventType WHERE code IN ('queue', '0'))''',
                                mode=['safe_updates_off'])
    print('Events deleted:', event_num)

    action_num = tools.executeEx(c,
                                 '''DELETE FROM Action WHERE Action.event_id NOT IN (SELECT id FROM Event)''',
                                 mode=['safe_updates_off'])
    print('Actions deleted:', action_num)

    ap_num = tools.executeEx(c,
                             '''DELETE FROM ActionProperty WHERE action_id NOT IN (SELECT id FROM Action)''',
                             mode=['safe_updates_off'])
    print('ActionProperties deleted:', ap_num)

    for name in names:
        affected = tools.executeEx(c, sql_delete_ap_val % name, mode=['safe_updates_off'])
        print(name, affected)
    c.execute('''SET foreign_key_checks=1;''')
    c.close()