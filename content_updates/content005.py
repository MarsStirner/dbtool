#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Удаление документов, ссылающихся на несуществующих пациентов
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = """DELETE FROM ClientDocument WHERE client_id NOT IN (SELECT id FROM Client);"""
    tools.executeEx(c, sql, mode=['safe_updates_off',])
    c.close()