#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `Action` ADD `pacientInQueueType` TINYINT DEFAULT 0 AFTER `hospitalUidFrom`;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `Person` ADD `maxOverQueue` TINYINT DEFAULT 0 AFTER `typeTimeLinePerson`;
'''
    c.execute(sql)
    

def downgrade(conn):
    pass
