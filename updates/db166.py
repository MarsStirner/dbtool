# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import traceback

__doc__ = '''\
Добавлен параметр "Возраст" для справочника Групп здоровья
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    try:
        c.execute(u"""ALTER TABLE `rbHealthGroup` ADD COLUMN `age`  varchar(9)
            CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Возраст' AFTER `name`;""")
    except:
        traceback.print_exc()

    c.close()

def downgrade(conn):
    pass