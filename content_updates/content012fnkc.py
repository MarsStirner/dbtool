#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Удаление неверных значений даты из БД
'''


def upgrade(conn):
    global config
    c = conn.cursor()
    global tools
    tools.executeEx(c, u"""
        DELETE FROM ActionProperty_Date WHERE value = '0002-11-30';

    """, mode = ['safe_updates_off'])
    c.close()
