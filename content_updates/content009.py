#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Установка значения поля code для ActionPropertyType "Время забора"
'''


def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute(u"""
    UPDATE ActionPropertyType apt, ActionType _at SET apt.code='TAKINGTIME' WHERE apt.name = 'Время забора' AND apt.code IS NULL AND _at.id=apt.actionType_id AND _at.mnem='LAB';
    """)
    c.close()
