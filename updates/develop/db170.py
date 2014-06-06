# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import traceback

__doc__ = '''\
Новые параметры для справочника типов полиса
логический признак, отвечающий за необходимость ввода серии
логический признак, отвечающий за необходимость проверки длины номера полиса
числовое поле, в котором будет указываться требуемая длина номера полиса
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    try:
        c.execute(u"""ALTER TABLE `rbPolicyType`
                    ADD COLUMN `isPolicySerialRequired`  tinyint(1) NULL DEFAULT 0 AFTER `TFOMSCode`,
                    ADD COLUMN `isPolicyNumberCheckRequired`  tinyint(1) NULL DEFAULT 0 AFTER `isPolicySerialRequired`,
                    ADD COLUMN `policyNumberLength`  int(16) NULL DEFAULT 16 AFTER `isPolicyNumberCheckRequired`;""")
    except:
         traceback.print_exc()

    c.close()

def downgrade(conn):
    pass