#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    c.close()
