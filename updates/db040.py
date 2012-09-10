# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавление столбца comments для таблицы AssignmentHour.
'''

def upgrade(conn):
    sql = [        
        '''ALTER TABLE `AssignmentHour` ADD `comments` VARCHAR(120);''',]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [        
        '''ALTER TABLE `AssignmentHour` DROP `comments`;''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

