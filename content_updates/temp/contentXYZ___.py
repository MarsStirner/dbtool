#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
заготовка
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    c.close()
