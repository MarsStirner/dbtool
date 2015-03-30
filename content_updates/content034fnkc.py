#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Заполнение createOnlyActionsWithinPriceList в EventType
'''

MIN_SCHEMA_VERSION = 207


def upgrade(conn):
    c = conn.cursor()
    sql = '''UPDATE EventType
SET createOnlyActionsWithinPriceList = 1 WHERE code IN ("02", "23")
'''
    c.execute(sql)
    c.close()