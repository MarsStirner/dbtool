#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
ТИп обращения стационар
'''
def upgrade(conn):
    global config
    c = conn.cursor()
    sql = u'''
INSERT INTO rbRequestType(`code`, `name`) 
VALUES ('stationary', 'Стационар')
'''   
    c.execute(sql)    
    c.close()
    
def downgrade(conn):
    pass

