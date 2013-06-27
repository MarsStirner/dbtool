#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Обновление поля MNEM для раздела Лечение
'''

def upgrade(conn):
    global config    
    c = conn.cursor()

    #c.execute(u"SET SQL_SAFE_UPDATES=0;")
    
    c.execute(u'SELECT * FROM ActionType where class = 2 and deleted=0')
    rows = c.fetchall()
    if len(rows) > 0:
        for row in rows:
            setMnem(row[0], u'THER' ,conn)

    #c.execute(u"SET SQL_SAFE_UPDATES=1;")     
    c.close()
  
def setMnem(recordId, mnem, conn):
    c = conn.cursor()
    c.execute(u'''SELECT * FROM ActionType where group_id="%s" and deleted=0''', recordId)
    rows = c.fetchall()
    
    if len(rows) > 0:
        for row in rows:
            setMnem(row[0], mnem, conn)
    else:
        try:
            c.execute(u'''UPDATE ActionType SET mnem= '%s' WHERE id = %s and deleted = 0''' % (mnem, recordId))
        except:
            print(u'''Cann't set mnem "%s" for ActionType ID: "%s"''' % (mnem, recordId))
    
        
def downgrade(conn):
    pass
