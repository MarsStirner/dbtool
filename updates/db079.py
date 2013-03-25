#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление поля MNEM в таблицу ActionType (Веб-клиент) и заполенение его данными
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    # Добавление мнемоники для ActionType
    try:
        c.execute(u'''ALTER TABLE ActionType ADD COLUMN mnem VARCHAR(32) NULL DEFAULT '' COMMENT 'Мнемоника'  AFTER jobType_id;''')
    except:
            print('''Column 'mnem' already exists.''')
    
    # Записываем мнемоники для лабраторных исследований
    labId = input('''Please, input parent ID for laboratory (by default it's 782): ''')
    setMnem(labId, conn)
    
  
def setMnem(recordId, conn):
    c = conn.cursor()
    c.execute(u'''SELECT * FROM ActionType where group_id="%s" and deleted=0''', recordId)
    rows = c.fetchall()
    
    if len(rows) > 0:
        for row in rows:
            setMnem(row[0], conn)

    try:
        c.execute(u'''UPDATE ActionType SET mnem='LAB' WHERE group_id ="%s" and deleted = 0''', recordId)
    except:
        print("Cann't set mnem for record ID: %s", recordId)
    
        
def downgrade(conn):
    pass
