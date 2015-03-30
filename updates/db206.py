#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление столбца createOnlyActionsWithinPriceList в EventType
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `EventType`
ADD COLUMN `createOnlyActionsWithinPriceList` TINYINT(1) NOT NULL DEFAULT '0'
COMMENT 'Действия внутри такого event должны быть привязаны к актуальному прайсу услуг Contract_Tariff' AFTER `requestType_id`;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass