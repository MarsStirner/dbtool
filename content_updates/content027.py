#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Fixes for WEBMIS-177
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
SELECT id FROM ActionPropertyType WHERE idx > 199 AND actionType_id = 4219;
'''
    c.execute(sql)

    rows = c.fetchall()

    for row in rows:
        c.execute('''
        UPDATE LayoutAttributeValue SET value = value + 1 WHERE actionPropertyType_id = {0} AND (layoutAttribute_id = 9 OR layoutAttribute_id = 22);
        '''.format(row[0]))

    c.close()
