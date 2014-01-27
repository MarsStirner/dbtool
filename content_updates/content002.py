#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Введение дополнительной мнемоники BAK_LAB для исследований БАК-лаборатории
'''

import traceback

def upgrade(conn):
    global config
    c = conn.cursor()

    try:
        c.execute(u"""UPDATE ActionType SET mnem = 'BAK_LAB' WHERE group_id=659 AND mnem = 'LAB';
						 """)

    except:
         traceback.print_exc()

    c.close()

def downgrade(conn):
    global config
    c = conn.cursor()

    try:
        c.execute(u"""UPDATE ActionType SET mnem = 'LAB' WHERE group_id=659 AND mnem = 'BAK_LAB';
						 """)

    except:
         traceback.print_exc()

    c.close()
