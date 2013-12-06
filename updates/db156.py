#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление признака "Скрыт" для типа действия (http://helpdesk.korusconsulting.ru/browse/FTMISCLIENT-422)
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''
ALTER TABLE `ActionType`
    ADD COLUMN `hidden` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Cкрывать при создании' AFTER `deleted`;
''')

    c.close()


def downgrade(conn):
    pass
