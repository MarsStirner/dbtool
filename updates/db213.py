#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Доработка таблиц хранения адресов пациентов
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `AddressHouse`
CHANGE COLUMN `KLADRStreetCode` `KLADRStreetCode` VARCHAR(17) NULL DEFAULT NULL COMMENT 'Код улицы по кладр' ,
ADD COLUMN `streetFreeInput` VARCHAR(128) NULL DEFAULT NULL AFTER `KLADRStreetCode`;
'''
    c.execute(sql)

    sql = '''ALTER TABLE `ClientAddress`
CHANGE COLUMN `freeInput` `freeInput` VARCHAR(255) NOT NULL DEFAULT '' ,
CHANGE COLUMN `version` `version` INT(10) UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Версия данных' ;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass