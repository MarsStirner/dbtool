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
    
    sql = u'''
UPDATE rbUserProfile SET withDep=1 WHERE id=26;
'''
    c.execute(sql)

    sql = u'''
UPDATE rbUserProfile SET withDep=1 WHERE id=28;
'''
    c.execute(sql)

    sql = u'''
UPDATE rbUserProfile SET withDep=1 WHERE id=33;
'''
    c.execute(sql)
    


    
def downgrade(conn):
    pass
