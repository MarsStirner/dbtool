#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Удаление ненужного поля MKB из QuotaType
- Удаление ненужного поля toOrder из Action
- Добавление поля MNEM в таблицу ActionType (Веб-клиент) и заполенение его данными
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''ALTER TABLE `QuotaType` DROP COLUMN `MKB` ;'''
    c.execute(sql)
    
    #  Удаление признака "Дозаказ" для лабораторных исследований
    sql = u'''ALTER TABLE Action DROP COLUMN toOrder ;'''
    try:
        c.execute(sql)
    except:
        pass
    
    # Добавление мнемоники для ActionType
    try:
        c.execute(u'''ALTER TABLE ActionType ADD COLUMN mnem VARCHAR(32) NULL DEFAULT '' COMMENT 'Мнемоника'  AFTER jobType_id;''')
    except:
        print('''Column 'mnem' already exists.''')
    
    # Записываем мнемоники для лабраторных исследований
    c.execute(u'''SELECT * FROM ActionType where name = "ЛАБОРАТОРНЫЕ ИССЛЕДОВАНИЯ";''')
    rows = c.fetchall()
    
    if len(rows) > 0:
        for row in rows:
            setMnem(row[0], conn)
        
  
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
