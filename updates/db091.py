#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback


__doc__ = '''\
_ Добавление поля flatCode для справочника rbDiagnosisType и заливка справочника (вебМИС)'''

queries = \
(
u'''UPDATE rbDiagnosisType SET flatCode='final' WHERE name LIKE 'заключительный'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='clinical' WHERE name LIKE 'основной'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='complicateToClinical' WHERE name LIKE 'осложнение основного' ; ''',
u'''UPDATE rbDiagnosisType SET flatCode='secondaryToClinical' WHERE name LIKE 'сопутствующий'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='admission' WHERE name LIKE 'Основной предварительный диагноз'; ''',
u'''INSERT INTO rbDiagnosisType (code, `name`, `replaceInDiagnosis`, `flatCode`) VALUES (LAST_INSERT_ID(), 'Направительный диагноз', '9', 'assignment'); ''',
u'''INSERT INTO rbDiagnosisType (code, `name`, `replaceInDiagnosis`, `flatCode`) VALUES (LAST_INSERT_ID(), 'Сопутствующий к направительному', '9', 'aftereffect'); ''',
u'''INSERT INTO rbDiagnosisType (code, `name`, `replaceInDiagnosis`, `flatCode`) VALUES (LAST_INSERT_ID(), 'Осложнения к направительному', '3', 'attendant'); ''',
)


def upgrade(conn):
    global config 
    c = conn.cursor()
     
    # Данные для типа диагноза
    try:
        c.execute(u'''ALTER TABLE rbDiagnosisType ADD COLUMN flatCode VARCHAR(64) NOT NULL COMMENT 'Уникальный строковый идентификатор'  AFTER replaceInDiagnosis;''')
    except:
        print('''Column 'flatCode' already exists.''')   
    
    for query in queries:
        try: 
            c.execute(query)
        except:
            traceback.print_exc()

    c.close()
    
    
def downgrade(conn):
    pass
