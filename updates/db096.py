#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
Добавление полей "Обязательное" и "Только для чтения" к типам свойств действия
'''


def upgrade(conn):
    global config        
    c = conn.cursor()

    try:
        c.execute(u'''ALTER TABLE `ActionPropertyType` ADD COLUMN `mandatory` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Является обязательным';''')
    except:
        print('''Column `ActionPropertyType`.`mandatory` already exists.''')
        traceback.print_exc()

    try:
        c.execute(u'''ALTER TABLE `ActionPropertyType` ADD COLUMN `readOnly` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Является только для чтения';''')
    except:
        print('''Column `ActionPropertyType`.`readOnly` already exists.''')    
        traceback.print_exc()

    c.close()


def downgrade(conn):
    pass
