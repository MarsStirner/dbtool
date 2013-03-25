#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
- Добавление Направительного диагноза во все ActionPropertyType, относящихся к лабораторным исследованиям (ВебМИС)
'''


def upgrade(conn):
    global config    
       
    labId = input('''Please, input parent ID for laboratory (by default it's 782): ''')
    addProperty(labId, conn)
    
  
def addProperty(recordId, conn):
    c = conn.cursor()
    c.execute(u'''SELECT * FROM ActionType where group_id="%s" and deleted=0''', recordId)
    rows = c.fetchall()
    
    if len(rows) > 0:
        for row in rows:
            addProperty(row[0], conn)
    else: 
        try:
            sql = u'''INSERT INTO ActionPropertyType VALUES ("%s", 0, "%s", 99, null, 'Направительный диагноз', '', null, 'MKB', '', '', null, 0, '', 0, '', 0, '000', 0, '000', 0, 0, 0, null, 0, 0);''' % (str(recordId) + '001', recordId)
            c.execute(sql)
        except:
            traceback.print_exc()
    
        
def downgrade(conn):
    pass

