# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
добавляет столбец isRequiredTissue в таблицу ActionType
'''

def upgrade(conn):
    sql0 = [
'''\
ALTER TABLE `ActionType` ADD COLUMN `isRequiredTissue` TINYINT(1) NOT NULL DEFAULT '0'  AFTER `isRequiredCoordination` ;
'''
    ]
    c = conn.cursor()
    global tools
    for s in sql0:
        tools.executeEx(c, s, mode=['ignore_dublicates'])
        
def downgrade(conn):
    sql0 = [
'''\
ALTER TABLE `ActionType` DROP COLUMN `isRequiredTissue` ;
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)