#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Миграция данных услуг типов действий в ActionType_Service
'''

MIN_SCHEMA_VERSION = 208


def upgrade(conn):
    c = conn.cursor()

    c.execute('set sql_safe_updates = 0;')
    sql = '''UPDATE ActionType_Service SET begDate = "1970-01-01";'''
    c.execute(sql)
    sql = '''INSERT INTO ActionType_Service
(`master_id`, `idx`, `service_id`, `begDate`, `endDate`) (
    SELECT id, 0, service_id, "1970-01-01", NULL
    FROM ActionType
    WHERE deleted = 0 AND service_id IS NOT NULL
)'''
    c.execute(sql)
    c.execute('set sql_safe_updates = 1;')

    c.close()