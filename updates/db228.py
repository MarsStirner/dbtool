#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Правки 226 апдейта на совместимость со стацинаром (ClientWork)
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sql = '''ALTER TABLE `ClientWork` CHANGE COLUMN `soc_status_id` `soc_status_id` INT(11) NOT NULL DEFAULT '0' AFTER `arm_id`;'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass
