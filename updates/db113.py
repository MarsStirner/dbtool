#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Обновление значения поля MNEM для Консультативных осмотров и инструментальных исследований
'''

replacements = (
                (u'CONS', u'ОСМОТР КОНСУЛЬТАТИВНЫЙ'),
                (u'DIAG', u'ИНСТРУМЕНТАЛЬНЫЕ ИССЛЕДОВАНИЯ'))

def upgrade(conn):
    global config    
    c = conn.cursor()
    
   # c.execute(u"SET SQL_SAFE_UPDATES=0;") 
    
    for rep in replacements:
        query = u''' SELECT * FROM ActionType WHERE class = 1 AND id IN(SELECT data.id FROM (SELECT id FROM ActionType WHERE name LIKE '%s') as data);''' % rep[1]
        c.execute(query)
        rows = c.fetchall()
        if len(rows) > 0:
            for row in rows:
                setMnem(row[0], rep[0], conn)
    
    #c.execute(u"SET SQL_SAFE_UPDATES=1;")     
    c.close()    
  
def setMnem(recordId, mnem, conn):
    c = conn.cursor()
    c.execute(u'''SELECT * FROM ActionType where group_id=%s and deleted=0''', recordId)
    rows = c.fetchall()
    
    if len(rows) > 0:
        for row in rows:
            setMnem(row[0], mnem, conn)
   
    try:
        c.execute(u'''UPDATE ActionType SET mnem='%s' WHERE id =%s''' % (mnem, recordId))
    except:
        print("Cann't set mnem for record ID: %s" % (recordId))
        
def downgrade(conn):
    pass
