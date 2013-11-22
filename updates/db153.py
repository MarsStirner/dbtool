#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''ALTER TABLE `rbPolicyType`
    ADD COLUMN `TFOMSCode` VARCHAR(8) NULL AFTER `name`;
''')
    print(u'Необходимо вручную поставить сопоставления типов полисов с кодами ТФОМС')

    c.close()

def downgrade(conn):
    pass