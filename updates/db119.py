#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback
__doc__ = '''\
-  Увеличение размерности поля '''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
        ALTER TABLE Diagnostic CHANGE COLUMN `notes` `notes` TEXT NOT NULL COMMENT 'Примечания';'''
    try:
        c.execute(sql)
    except:
        pass
    
def downgrade(conn):
    pass
