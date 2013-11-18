#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Заполнение таблицы rbCoreActionProperty новыми свойствами поступления.
'''

# Выпилено
def upgrade(conn):
    global config
    c = conn.cursor()

#     c.execute(u'''INSERT INTO `rbCoreActionProperty` (`actionType_id`, `name`, `actionPropertyType_id`) 
# 		SELECT `actionType_id`, `name`, `id` 
# 		FROM `ActionPropertyType`
# 		WHERE `actionType_id` IN (SELECT `id` FROM `ActionType` WHERE `flatCode` = 'received')
# 			AND `deleted` = 0
# 			AND `id` NOT IN (
# 				SELECT `actionPropertyType_id`
# 				FROM `rbCoreActionProperty`
# 				WHERE `actionType_id` IN (SELECT `id` FROM `ActionType` WHERE `flatCode` = 'received'));''')
#     c.close()


def downgrade(conn):
    pass