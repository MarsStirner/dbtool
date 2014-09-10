#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Миграция для поддержки обновленной связи обращения и договора
'''

# Event.id<-Event_LocalContract.master_id => Event.localContract_id->Event_LocalContract.id

MIN_SCHEMA_VERSION = 175


def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = '''UPDATE
Event e JOIN Event_LocalContract elc ON e.id = elc.master_id
SET e.localContract_id = elc.id'''
    tools.executeEx(c, sql, mode=['safe_updates_off',])
    c.close()