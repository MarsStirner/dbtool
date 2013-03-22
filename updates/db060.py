#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Исправление для справочника показателей исследований
'''

def upgrade(conn):
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `rbTest`
ADD COLUMN `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Отметка удаления записи' AFTER `name`;
'''
    c.execute(sql)
        

def downgrade(conn):
    pass
