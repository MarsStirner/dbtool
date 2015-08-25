#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Отметка удаления записи из плоских справочников
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `FDRecord`
ADD COLUMN `deleted` TINYINT(1) NOT NULL DEFAULT '0'
COMMENT 'Отметка удаления записи';
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass