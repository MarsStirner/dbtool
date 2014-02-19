#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Обеспечение уникальности записей таблицы Person, фукнции для работы с ограничениями на возраст
'''

MIN_CONTENT_VERSION = 4

def upgrade(conn):
    c = conn.cursor()

    sql = '''
ALTER TABLE `Person`
DROP INDEX `uuid_id` ,
ADD UNIQUE INDEX `uuid_id` (`uuid_id` ASC);
'''
    c.execute(sql)


def downgrade(conn):
    pass