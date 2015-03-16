#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

__doc__ = '''\
QuotaCatalog для ВМП за прошлый год
'''

MIN_SCHEMA_VERSION = 210


def upgrade(conn):
    c = conn.cursor()

    print(u'Добавляем QuotaCatalog за прошлый год')

    sql = u'''
INSERT INTO `QuotaCatalog` (`finance_id`, `createDatetime`, `modifyDatetime`, `begDate`, `endDate`)
VALUES (7, NOW(), NOW(), '2014-01-01', '2014-12-31')
'''
    c.execute(sql)
    last_id = c.lastrowid

    print(u'Привязываем существующие строки QuotaType к QuotaCatalog за прошлый год')
    sql = u'''UPDATE `QuotaType` SET `catalog_id`=%s''' % last_id
    c.execute(sql)

    c.close()
