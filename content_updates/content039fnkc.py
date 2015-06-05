#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление роли врача анестезиолога
'''

MIN_SCHEMA_VERSION = 206


def upgrade(conn):
    c = conn.cursor()
    sql = '''
INSERT INTO rbUserProfile (code, name, withDep) VALUES("anestezDoctor", "Врач анестезиолог", 0)
'''
    c.execute(sql)

    sql = '''
INSERT INTO rbUserProfile_Right (master_id, userRight_id) SELECT 42, ur.id FROM rbUserRight ur JOIN rbUserProfile_Right upr ON ur.id = upr.userRight_id AND upr.master_id = 24
'''
    c.execute(sql)
    
    c.close()