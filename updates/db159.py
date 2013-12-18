#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Индексы для таблицы Client_Quoting, ускоряющие работу вью vClientQuoting и vClientQuoting_sub
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u"""ALTER TABLE `Client_Quoting`
    ADD INDEX `event_id` (`event_id`),
    ADD INDEX `deleted_prevTalon_event_id` (`deleted`, `prevTalon_event_id`);""")
    c.close()

def downgrade(conn):
    pass