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
u'''UPDATE `rbAPTableField` SET `fieldName`='comp_type_id' WHERE  `fieldName`='comp_type' '''
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
