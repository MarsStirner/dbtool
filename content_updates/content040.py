#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Исправление кривых Action-ов (AppointmentType='')
'''


def upgrade(conn):
    c = conn.cursor()
    sql = '''
UPDATE Action a SET a.AppointmentType = '0' WHERE a.AppointmentType=''
'''
    c.execute(sql)
    c.close()