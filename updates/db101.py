#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- ДОБавление столбца cost к таблице PersonEducation
'''


def upgrade(conn):
    global config        
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `PersonEducation` ADD COLUMN `cost` DOUBLE NULL DEFAULT NULL;
'''
    try:
        c.execute(sql)
    except OperationalError:
        pass
    else:
        print(u'column `PersonEducation`.`cost` exists or elsewhy cannot be added')
        
def downgrade(conn):
    pass
