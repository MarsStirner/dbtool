#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавлено значение по умолчанию для поля embryonalPeriodWeek (неделя эмбрионального периода, в которую рожден пациент)
'''

# Навангованные проблемы сбылись.

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''ALTER TABLE `Client`
	    MODIFY COLUMN `embryonalPeriodWeek` varchar(16) NOT NULL
	    DEFAULT ''
	    COMMENT 'Неделя эмбрионального периода, в которую рожден пациент' AFTER `birthPlace`;''')
    c.close()


def downgrade(conn):
    pass