#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные для противоинфекционной терапии
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
SELECT id FROM LayoutAttribute WHERE code = 'NONTOGGLABLE';
'''
    c.execute(sql)
    nontogglable = c.fetchone()

    sql = u'''
SELECT id FROM ActionPropertyType WHERE code = 'infectType';
'''    
    c.execute(sql)
    infectType = c.fetchone()

    c.execute('''
        UPDATE LayoutAttributeValue SET value = 'false' WHERE layoutAttribute_id = {0} AND actionPropertyType_id = {1};
        '''.format(nontogglable[0], infectType[0]))

    c.close()