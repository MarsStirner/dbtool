# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавлен выбор шаблонизатора в таблице, хранящей шаблоны печати.
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = u'''
ALTER TABLE `rbPrintTemplate` ADD COLUMN `render` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Шаблонизатор' AFTER `dpdAgreement`;'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])

def downgrade(conn):
    pass