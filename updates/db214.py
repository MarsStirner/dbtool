#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Обновление таблицы соцстатусов пациента
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `ClientSocStatus`
CHANGE COLUMN `begDate` `begDate` DATE NULL DEFAULT NULL COMMENT 'Дата начала действия записи' ;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass