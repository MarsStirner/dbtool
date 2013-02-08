#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Исправлена ошибка сохранения значений давления в первичных осмотрах (Веб-клиент)'''

queries = \
(
u'''
DELETE FROM ActionPropertyType WHERE id=112002; ''',
u'''
DELETE FROM ActionPropertyType WHERE id=112003;''',
u'''
INSERT INTO ActionPropertyType VALUES
(112002, 0, 112, 55, null, 'Артериальное давление. Правая рука (Сиаст.)', '', 17, 'Double', '', '', null, 0, '', 0, '', 0, '000', 0, '000', 0, 0, 0, null, 0, 0),
(112003, 0, 112, 55, null, 'Артериальное давление. Правая рука (Диаст.)', '', 17, 'Double', '', '', null, 0, '', 0, '', 0, '000', 0, '000', 0, 0, 0, null, 0, 0);''',
u'''
UPDATE ActionPropertyType SET name='Артериальное давление. Левая рука (Сиаст.)' WHERE id=1600047;''',
u'''
UPDATE ActionPropertyType SET name='Артериальное давление. Левая рука (Диаст.)' WHERE id=1600048;''',
u'''
UPDATE ActionPropertyType SET code='BPRAD' WHERE id='1600048';''',
u'''
UPDATE ActionPropertyType SET code='BPRAD' WHERE id='112003';''',
u'''
UPDATE ActionPropertyType SET code='BPRAS' WHERE id='1600047';''',
u'''
UPDATE ActionPropertyType SET code='BPRAS' WHERE id='112002';''',
u'''
UPDATE ActionPropertyType SET unit_id=17, typeName='Double' WHERE id=1600047;''',
u'''
UPDATE ActionPropertyType SET unit_id=17, typeName='Double' WHERE id=1600048;''',
u'''
UPDATE ActionPropertyType SET name='АД диаст.' WHERE id=22959;''',
u'''
UPDATE ActionPropertyType SET name='АД сист.' WHERE id=22958;''',
u'''
UPDATE ActionPropertyType SET deleted=1 WHERE id=1600054;''',
u'''
UPDATE ActionPropertyType SET deleted=1 WHERE id=1600055;''',
u'''
UPDATE rbCoreActionProperty SET name='Артериальное давление. Левая рука (Сиаст.)' WHERE id=31;''',
u'''
UPDATE rbCoreActionProperty SET name='Артериальное давление. Левая рука (Диаст.)' WHERE id=32;''',
u'''
UPDATE rbCoreActionProperty SET name='Артериальное давление. Правая рука (Сиаст.)', actionPropertyType_id='112002' WHERE id=126;''',
u'''
UPDATE rbCoreActionProperty SET name='Артериальное давление. Правая рука (Диаст.)', actionPropertyType_id='112003' WHERE id=127;'''
)


def upgrade(conn):
    global config    
    
    for query in queries:
        c = conn.cursor()
        c.execute(query)
        c.close()
    
    
def downgrade(conn):
    pass
