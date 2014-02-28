#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Удаление документов, ссылающихся на несуществующих пациентов
'''

def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute(u"""DELETE FROM ClientDocument WHERE client_id NOT IN (SELECT id FROM Client);""")
    c.close()