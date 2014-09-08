#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Настраиваемые лейауты в ActionType
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
ALTER TABLE `ActionType`
ADD COLUMN `layout` TEXT NULL DEFAULT NULL AFTER `mnem`;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass