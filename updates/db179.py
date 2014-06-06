#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- добавление столбца для хранения текстов шаблонов
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
ALTER TABLE `rbPrintTemplate`
ADD COLUMN `templateText` LONGTEXT NOT NULL AFTER `render`;
'''
    c.execute(sql)
    c.close()


def downgrade(conn):
    pass