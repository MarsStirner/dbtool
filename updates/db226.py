#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
 Связь соцстатуса пациента с записью в ClientWork
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sql = '''ALTER TABLE `ClientWork`
CHANGE COLUMN `rank_id` `rank_id` INT(10) UNSIGNED NULL COMMENT 'Звание военнослужащего. FlatDirectory№7' ,
CHANGE COLUMN `arm_id` `arm_id` INT(10) UNSIGNED NULL COMMENT 'Род войск. FlatDirectory №6',
ADD COLUMN `soc_status_id` INT(11) NOT NULL AFTER `arm_id`;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass
