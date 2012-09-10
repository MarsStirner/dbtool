# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавление таблицы Setting
'''

def upgrade(conn):
    sql = [
'''\
    CREATE TABLE `Setting` (
            `id` int(11) NOT NULL,
            `path` varchar(255) NOT NULL,
            `value` text NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `path` (`path`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8
''',]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [        
        '''DROP TABLE `Setting`''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

