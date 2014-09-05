#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Раширение поля note таблицы Job_Ticket
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
    ALTER TABLE Job_Ticket MODIFY `note` TEXT DEFAULT NULL;
    '''
    c.execute(sql)

def downgrade(conn):
    pass # не требуется, т.к. возможна потеря данных
