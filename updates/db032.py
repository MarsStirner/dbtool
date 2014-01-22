# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавляем льготность и срочность
'''
def upgrade(conn):
    sql0 = [
'''\
Alter table `Event` add privilege tinyint(1) default 0
''',
'''\
Alter table `Event` add urgent tinyint(1) default 0
'''
    ]
    global tools
    c = conn.cursor()
    for s in sql0:
        tools.executeEx(c, s, mode=['ignore_duplicates'])
        
def downgrade(conn):
    sql0 = [
'''\
Alter table `Event` drop column privilege
''',
'''\
Alter table `Event` drop column urgent
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)