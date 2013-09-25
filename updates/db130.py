#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Дополнения к структуре БД для получения оперативных данных по остаткам лексредств на складах
'''


def upgrade(conn):

    c = conn.cursor()
    sql = u'''ALTER TABLE `rlsBalanceOfGoods` ADD COLUMN `updateDateTime` DATETIME DEFAULT NULL
    COMMENT 'Датавремя крайней синхронизации с Аптекой'  AFTER `disabled`;
    '''
    c.execute(sql)
    c.close()


def downgrade(conn):
    pass