#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление поля в справочник rbPolicyType, определяющий к какому типу относится полис - ОМС или ДМС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
        ALTER TABLE rbPolicyType ADD (insurance_type ENUM('OMS', 'DMS') NOT NULL);
    '''
    c.execute(sql)

    sql = u'''
        UPDATE rbPolicyType SET insurance_type = 'DMS' WHERE code = '3' OR code = 'vmi';
    '''
    c.execute(sql)

def downgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
        ALTER TABLE rbPolicyType DROP insurance_type;
    '''
    c.execute(sql)
