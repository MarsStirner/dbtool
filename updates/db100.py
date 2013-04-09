#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- Удаление столбца academicDegree из старых бах 6098, т.к. в нтк была введена
новая структура степеней/званий врачей (по идее может привести к потере данных)
'''


def upgrade(conn):
    global config        
    c = conn.cursor()
    
#           /|    -----       -----
#          / |  /       \   /       \
#         /  | |         | |         |
#        /   | |         | |         |
#            | |         | |         |
#            | |         | |         |
#            | |         | |         |
#            | |         | |         | get
#            |  \       /   \       /
#            |    -----       -----
    
    sql = u'''
ALTER TABLE `Person` DROP COLUMN `academicDegree` ;
'''
    try:
        c.execute(sql)
    except OperationalError:
        pass
    else:
        print(u'column `Person`.`academicDegree` deleted')
        
def downgrade(conn):
    pass
