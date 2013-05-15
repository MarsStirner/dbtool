#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
- Интеграция с системой ТРФУ. Изменения типа табличных данных ТРФУ на Table.
'''

flat_code_trfu_extracorporeal = "ExtracorporealMethods";

simple_queries = \
(
u'''UPDATE `ActionPropertyType` SET `valueDomain`='TRFU_OIR', typeName = "Table" WHERE `code`='trfuReqBloodCompPasport' ''',
u'''UPDATE `rbAPTableField` SET `fieldName`='trfu_blood_comp' WHERE  `fieldName`='trfu_comp_id' ''',
u'''UPDATE `rbAPTableField` SET `fieldName`='comp_type_id' WHERE  `fieldName`='comp_type' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 1, `mandatory`= 0  WHERE `code` like 'trfu%' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 1  WHERE `code` like 'trfuReqBloodCompDiagnosis' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 1  WHERE `code` like 'trfuReqBloodCompId' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 1  WHERE `code` like 'trfuReqBloodCompType' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 0  WHERE `code` like 'trfuReqBloodCompValue' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 0  WHERE `code` like 'trfuReqBloodCompDose' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 1  WHERE `code` like 'trfuReqBloodCompRootCause' ''',
u'''UPDATE `ActionPropertyType` SET `readOnly`= 0, `mandatory`= 0  WHERE `code` like 'trfuProcedureDonor' '''
)

def upgrade(conn):
    global config        
    c = conn.cursor()
    c.execute(u"SET SQL_SAFE_UPDATES=0;")
    for q in simple_queries:
        try: 
            c.execute(q)
        except:
            traceback.print_exc()
                        
    c.execute(u"SET SQL_SAFE_UPDATES=1;")


def downgrade(conn):
    pass
