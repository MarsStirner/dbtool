#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback


__doc__ = '''\
_ Изменение поля flatCode для справочника rbDiagnosisType и заливка справочника (вебМИС)'''

queries = \
(
u'''UPDATE rbDiagnosisType SET flatCode='mainDiagMkb' WHERE name LIKE 'основной';''',
u'''UPDATE rbDiagnosisType SET flatCode='finalMkb' WHERE name LIKE 'заключительный'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='diagComplMkb' WHERE name LIKE 'осложнение основного'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='mainDiagMkbPat' WHERE name LIKE 'причина смерти';  ''',
u'''UPDATE rbDiagnosisType SET flatCode='admissionMkb' WHERE name LIKE 'Основной предварительный диагноз'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='assocDiagMkb' WHERE name LIKE 'сопутствующий'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='aftereffectMkb' WHERE name LIKE 'Сопутствующий к направительному'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='attendantMkb' WHERE name LIKE 'Осложнения к направительному'; ''',
u'''UPDATE rbDiagnosisType SET flatCode='diagReceivedMkb' WHERE name LIKE 'Направительный диагноз' AND flatCode !=''; ''',
u'''INSERT INTO rbDiagnosisType (code, `name`, `replaceInDiagnosis`, `flatCode`) VALUES 
(LAST_INSERT_ID(), 'Сопутствующий к заключительному клиническому', '1', 'aftereffectFinalMkb'),
(LAST_INSERT_ID(), 'Осложнения к заключительному клиническому', '1', 'attendantFinalMkb'); ''',
)


def upgrade(conn):
    global config 
    c = conn.cursor()
     
    for query in queries:
        try: 
            c.execute(query)
        except:
            traceback.print_exc()

    c.close()
    
    
def downgrade(conn):
    pass
