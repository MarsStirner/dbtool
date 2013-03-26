#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Ещё несколько изменений из ВебМиса
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    
    sql = u"ALTER TABLE ClientDocument CHANGE COLUMN origin origin VARCHAR(256) NOT NULL COMMENT 'Организация выдавшая документ';"
    try:
        c.execute(sql)
    except:
        pass
    
    sql = u"ALTER TABLE Client_Quoting ADD COLUMN version INT(11) UNSIGNED NOT NULL COMMENT 'Версия данных' AFTER prevTalon_event_id ;"
    try:
        c.execute(sql)
    except:
        pass
    
    sql = u"ALTER TABLE rbRequestType CHANGE COLUMN code code VARCHAR(32) NOT NULL COMMENT 'Код';"
    try:
        c.execute(sql)
    except:
        pass
    
def downgrade(conn):
    pass
