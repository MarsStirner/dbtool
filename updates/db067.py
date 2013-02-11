#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление признака наличия отделения у роли (Медипад)
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE rbUserProfile ADD COLUMN withDep TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Признак сопоставления роли с отделением 0-нет, 1-да'  AFTER name; 
'''
    c.execute(sql)
    


    
def downgrade(conn):
    pass
