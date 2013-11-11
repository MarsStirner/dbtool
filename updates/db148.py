#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Служебные типы действий
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''
                UPDATE ActionType
                inner join (select min(id) id
                from ActionType
                where code in ('amb', 'home', 'cew', 'exp', 'timeLine', 'queue')
                group by code) AT
                on ActionType.id = AT.id
                SET deleted=0,
                class=-1;
                ''')
    c.close()


def downgrade(conn):
    pass