#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Простановка rbContactType.idx
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    c.execute('''UPDATE rbContactType SET idx=1 WHERE code!='03';''')
    c.close()