#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Комментарий к записи пациента
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `ScheduleClientTicket`
CHANGE COLUMN `note` `note` TEXT NULL DEFAULT NULL COMMENT 'Примечание' ;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass