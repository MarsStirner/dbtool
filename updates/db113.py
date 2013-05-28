#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Обновление поля MNEM для медицинских документов
'''

replacements = (
    (0, u'ПЕРВИЧНЫЙ ОСМОТР', u'EXAM',),
    (0, u'ДНЕВНИКОВЫЙ ОСМОТР', u'JOUR'),
    (0, u'ЭПИКРИЗЫ', u'EPI'),
    (0, u'КОНСИЛИУМ', u'EXAM'),
    (0, u'СОВМЕСТНЫЙ ОСМОТР', u'EXAM'),
    (0, u'ИЗВЕЩЕНИЯ', u'NOT'),
    (0, u'ДЕЖУРНЫЙ ВРАЧ ОСМОТР', u'EXAM'),
    (0, u'ПРОЧЕЕ/СОГЛАСИЯ', u'OTH'),
    (3, u'Выписка', u'ORD'),
)

sql = u'''
    SELECT * FROM ActionType
    WHERE class = '%s' AND id IN (
        SELECT data.id FROM (
            SELECT id
            FROM ActionType
            WHERE name LIKE '%s'
            ) 
        as data); '''   

def upgrade(conn):
    global config    
    c = conn.cursor()

    c.execute(u"SET SQL_SAFE_UPDATES=0;")
        
    
    # Установка мнемоники для вложений
    for rep in replacements:
        query = sql % (rep[0], rep[1])
        c.execute(query)
        rows = c.fetchall()
        if len(rows) > 0:
            for row in rows:
                setMnem(row[0], rep[2], conn)

    c.execute(u"SET SQL_SAFE_UPDATES=1;")     
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
            c.execute(u'''UPDATE ActionType SET mnem='%s' WHERE id = %s and deleted = 0''' % (mnem, recordId))
        except:
            print(u'''Cann't set mnem "%s" for ActionType ID: "%s"''' % (mnem, recordId))
    
        
def downgrade(conn):
    pass
