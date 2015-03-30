#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
ActionPropertyType с типом значения Diagnosis
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
    ALTER TABLE `Diagnostic`
    ADD COLUMN `diagnosis_description` TEXT NULL DEFAULT NULL COMMENT 'Описание диагноза' AFTER `action_id`;
    '''
    c.execute(sql)

    sql = '''
    CREATE TABLE IF NOT EXISTS `ActionProperty_Diagnosis` (
      `id` INT(11) NOT NULL COMMENT '{ActionProperty}',
      `index` INT(11) NOT NULL DEFAULT '0',
      `value` INT(11) NULL DEFAULT NULL,
      PRIMARY KEY (`index`, `id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass