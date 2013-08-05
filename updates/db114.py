#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
- Добавление Направительного диагноза в ActionPropertyType, относящихся к инструментальным исследованиям и консультациям (ВебМИС)
'''

mnems = (u'CONS', u'DIAG')

def upgrade(conn):
    global config    
    c = conn.cursor() 
        
    for mnem in mnems:
        query = u'''SELECT * FROM ActionType where mnem LIKE '%s' and deleted = 0;''' % mnem
        c.execute(query)
        rows = c.fetchall()
        if len(rows) > 0:
            for row in rows:
                addProperty(row[0], conn)
    
def addProperty(recordId, conn):
    c = conn.cursor()
     
    try:
        sql = u'''INSERT INTO ActionPropertyType
            (`deleted`, `actionType_id`, `idx`, `template_id`, `name`, `descr`, `unit_id`, `typeName`, `valueDomain`,`defaultValue`,`code`,`isVector`,`norm`,`sex`,`age`,`age_bu`,`age_bc`,`age_eu`,`age_ec`,`penalty`,`visibleInJobTicket`,`isAssignable`,`test_id`,`defaultEvaluation`,`toEpicrisis`,`mandatory`,`readOnly`)
             VALUES (0, "%s", 99, null, 'Направительный диагноз', '', null, 'MKB', '', '', null, 0, '', 0, '', 0, '000', 0, '000', 0, 0, 0, null, 0, 0, 1, 0);''' %  recordId
        c.execute(sql)
    except:
        traceback.print_exc()
    
        
def downgrade(conn):
    pass

