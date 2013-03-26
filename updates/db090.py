#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback


__doc__ = '''\
 _ Добавдение столбца color для справочника rbTestTubeType (ВебМИС)'''

def upgrade(conn):
    global config 
    c = conn.cursor()
     
    # Добавление колонки Color в таблицу rbTestTubeType для хранения цвета пробирки
    try:
        c.execute(u'''ALTER TABLE rbTestTubeType ADD COLUMN color VARCHAR(8) NULL COMMENT 'Храниться 16-ричный код цвета пробирки' AFTER image;''')
    except:
        print('''Column 'color' already exists.''')   
    
    c.close()
    
    
def downgrade(conn):
    pass
