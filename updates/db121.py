#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Обновление значения поля flatCode для осмотров в приемном отделении
'''

replacements = (
    (u'firstExam', u'1_1_01'),
    (u'firstExamShort', u'1_1_02'),
)

sql = u''' 
    UPDATE ActionType 
        SET flatCode='%s' 
        WHERE ActionType.id in
        (SELECT t.id FROM 
            (SELECT at.id 
            FROM ActionType as at 
            WHERE at.code = '%s' 
            )
        as t);    '''

def upgrade(conn):
    global config    
    c = conn.cursor()
    
    for rep in replacements:
        query = sql % rep
        c.execute(query)
        
    c.close()    
  
def downgrade(conn):
    pass
