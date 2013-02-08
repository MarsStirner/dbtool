#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление мнемоники для давления, температуры и пульса  (Веб-клиент)'''

queries = \
(
u'''
UPDATE ActionPropertyType SET code='PULS' WHERE name LIKE 'ЧСС';''',
u'''
 UPDATE ActionPropertyType SET code='STATE' WHERE valueDomain LIKE '1_2_1_01' OR name LIKE 'Состояние';''',
u'''
UPDATE ActionPropertyType SET code='BPRAD' WHERE name LIKE 'АД нижн%' or name LIKE 'АД диаст%';''',
u'''
UPDATE ActionPropertyType SET code='BPRAS'  WHERE name LIKE 'АД' or name LIKE 'АД верхн%' or name LIKE 'АД сист%';''',
u'''
UPDATE ActionPropertyType SET code='TEMPERATURE' WHERE name LIKE 't' OR name LIKE 't %';''')


def upgrade(conn):
    global config    
    
    for query in queries:
        c = conn.cursor()
        c.execute(query)
        c.close()
    
    
def downgrade(conn):
    pass
