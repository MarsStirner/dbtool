#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление поддержки NULL-значений в таблицах TempInvalid и TempInvalid_Period на столбцах begDate и endDate
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
        ALTER TABLE TempInvalid MODIFY begDate date COMMENT 'Дата начала временной утраты (мин. из периодов)';
    '''
    c.execute(sql)

    sql = u'''
        ALTER TABLE TempInvalid MODIFY endDate date COMMENT 'Дата окончания временной утраты (макс. из периодов)';
    '''
    c.execute(sql)

    sql = u'''
        ALTER TABLE TempInvalid_Period MODIFY begDate date COMMENT 'Дата открытия периода';
    '''
    c.execute(sql)

    sql = u'''
        ALTER TABLE TempInvalid_Period MODIFY endDate date COMMENT 'Дата закрытия периода';
    '''
    c.execute(sql)

def downgrade(conn):
    pass
