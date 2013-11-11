#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавлена неделя эмбрионального периода, в которую рожден пациент
'''

# Не спрашивайте, почему неделя измеряется в VARCHAR(16), а не INT, и почему столбец NOT NULL.
# Вангую серьёзные проблемы с этим.

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''ALTER TABLE `Client`
    ADD COLUMN `embryonalPeriodWeek`  varchar(16) NOT NULL
        COMMENT 'Неделя эмбрионального периода, в которую рожден пациент' AFTER `birthPlace`;''')
    c.close()


def downgrade(conn):
    pass