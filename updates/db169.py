#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление связи через Foreign key между таблизацами ClientDocument и Client по полям client_id и id
'''

MIN_CONTENT_VERSION = 5

def upgrade(conn):
    c = conn.cursor()

    sql = '''
    ALTER TABLE ClientDocument ADD CONSTRAINT FK__ClientDocument_Client FOREIGN KEY (client_id) references Client(id) ON DELETE CASCADE ON UPDATE CASCADE;
    '''
    c.execute(sql)


def downgrade(conn):
    pass