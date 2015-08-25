#!/usr/bin/env python
# -*- coding: utf-8 -*-

__doc__ = '''\

'''

MIN_SCHEMA_VERSION = 212


def upgrade(conn):
    c = conn.cursor()
    c.close()
