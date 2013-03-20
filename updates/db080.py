#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Переводим все таблицы в БД из MyISAM в InnoDB
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = [
    u'''
ALTER TABLE `MKB` DROP INDEX `DiagName`, ADD INDEX `DiagName` (`DiagName` ASC) ;
'''
    ]
    for s in sql:
        c.execute(s)
    
    chk_engine_query = u'''
SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema=DATABASE() and TABLE_TYPE="BASE TABLE" and ENGINE="MyISAM";
'''
    c.execute(chk_engine_query)
    tables = [t[0] for t in c.fetchall()]
    
    for table in tables:
        if table == "Meta":
            continue
        print("Changing Engine for table", table)
        sql = u'''ALTER TABLE %s ENGINE=InnoDB;''' % table
        c.execute(sql)
    
    
def downgrade(conn):
    pass
