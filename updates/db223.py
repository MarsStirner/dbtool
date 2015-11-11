#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление флага deleted в перечисленные справочники
'''

rb_list = ['rbSpeciality', 'rbPost', 'rbFinance', 'rbResult', 'rbEventTypePurpose', 'rbRequestType', 'rbTreatmentType',
           'rbPrintTemplate']


def upgrade(conn):
    with conn as c:
        for rb_name in rb_list:
            sql = '''ALTER TABLE `{table_name}`
ADD COLUMN `deleted` TINYINT(1) NOT NULL DEFAULT '0';'''.format(table_name=rb_name)
            c.execute(sql)


def downgrade(conn):
    with conn as c:
        for rb_name in rb_list:
            sql = '''ALTER TABLE `{table_name}` DROP COLUMN `deleted`;'''.format(table_name=rb_name)
            c.execute(sql)
