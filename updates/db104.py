#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- ДОБавление столбца `relevant` к таблице rbRequestType
- Расширение кода у rbPolicyType
'''

sqls = [
ur'''
ALTER TABLE `rbRequestType` ADD COLUMN `relevant` TINYINT(1) NOT NULL DEFAULT 1;
''',
ur'''
ALTER TABLE `rbPolicyType`
    ALTER `code` DROP DEFAULT,
    ALTER `name` DROP DEFAULT;
''',
ur'''
ALTER TABLE `rbPolicyType`
    CHANGE COLUMN `code` `code` VARCHAR(50) NOT NULL COMMENT 'Код' AFTER `id`,
    CHANGE COLUMN `name` `name` VARCHAR(256) NOT NULL COMMENT 'Наименование' AFTER `code`,
    DROP INDEX `code`,
    ADD UNIQUE INDEX `code` (`code`);
'''
]


def upgrade(conn):
    global config
    c = conn.cursor()

    for sql in sqls:
        try:
            c.execute(sql)
        except OperationalError, e:
            print(e)

    c.close()

def downgrade(conn):
    pass
