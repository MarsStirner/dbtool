#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- ДОБавление столбца `relevant` к таблице rbRequestType
- Расширение кода у rbPolicyType
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
ALTER TABLE `rbRequestType` ADD COLUMN `relevant` TINYINT(1) NOT NULL DEFAULT 1;
'''
    try:
        c.execute(sql)
    except OperationalError, e:
        print(e)
        pass
    c.close()

    sql = u'''
ALTER TABLE `rbPolicyType`
    ALTER `code` DROP DEFAULT,
    ALTER `name` DROP DEFAULT;
ALTER TABLE `rbPolicyType`
    CHANGE COLUMN `code` `code` VARCHAR(50) NOT NULL COMMENT 'Код' AFTER `id`,
    CHANGE COLUMN `name` `name` VARCHAR(256) NOT NULL COMMENT 'Наименование' AFTER `code`,
    DROP INDEX `code`,
    ADD UNIQUE INDEX `code` (`code`);
'''
    try:
        c.execute(sql)
    except OperationalError, e:
        print(e)
        pass
    c.close()

def downgrade(conn):
    pass
