#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Начальное состояние - запись в Meta версии content_version
'''

MIN_SCHEMA_VERSION = 16

def upgrade(conn):
    c = conn.cursor()
    c.execute('''INSERT INTO `Meta` (`name`, `value`) VALUES ('content_version', '1')''')
    c.close()
