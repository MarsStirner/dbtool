#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Настройка отображения раздела назначения лекарственных стредств
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sql = '''ALTER TABLE `ActionType`
ADD COLUMN `hasPrescriptions` TINYINT(1) NOT NULL DEFAULT '0' AFTER `layout`;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass
