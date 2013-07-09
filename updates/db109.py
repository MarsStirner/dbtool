#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback
__doc__ = '''\
-  Добавление кода к свойству действия "Время поступления" '''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
        UPDATE ActionPropertyType 
        SET code='timeArrival' 
        WHERE ActionPropertyType.id in
        (SELECT p.id FROM 
            (SELECT apt.id 
            FROM ActionPropertyType as apt, ActionType as at 
            WHERE apt.actionType_id = at.id 
            AND at.flatCode = 'moving' 
            AND apt.name LIKE 'Время поступления')
        as p); '''

    c.execute(sql)
    
def downgrade(conn):
    pass
