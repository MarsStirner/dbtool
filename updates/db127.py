#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавлена дата подтверждения оплаты
'''


def upgrade(conn):

    c = conn.cursor()
    sql = u'''ALTER TABLE `Account_Item` ADD COLUMN `paymentConfirmationDate` DATE NOT NULL
    COMMENT 'Дата подтверждения платежа'  AFTER `service_id`;
    '''
    c.execute(sql)
    c.close()


def downgrade(conn):
    pass