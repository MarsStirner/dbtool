# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Добавлен выбор шаблонизатора в таблице, хранящей шаблоны печати.
'''

def upgrade(conn):
    sql = u'''
ALTER TABLE `rbPrintTemplate` ADD COLUMN `render` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Шаблонизатор' AFTER `dpdAgreement`;'''

    c = conn.cursor()
    c.execute(sql)

def downgrade(conn):
    pass