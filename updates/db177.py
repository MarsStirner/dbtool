#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Создание таблицы для хранения шаблонов отображения полей для заполнения ActionPropertyType для Hippocrates
'''

def upgrade(conn):
    c = conn.cursor()
    sql = '''
    CREATE TABLE IF NOT EXISTS `ActionPropertyTypeLayout` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `actionPropertyType_id` int(11) NOT NULL,
      `template` text NOT NULL,
      PRIMARY KEY (`id`),
      KEY `ix_ActionPropertyTypeLayout_actionPropertyType_id` (`actionPropertyType_id`),
      CONSTRAINT `actionpropertytypelayout_ibfk_1` FOREIGN KEY (`actionPropertyType_id`) REFERENCES `ActionPropertyType` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
    c.execute(sql)

def downgrade(conn):
    c = conn.cursor()
    sql = '''
    DROP TABLE IF EXISTS `ActionPropertyTypeLayout`;
    '''
    c.execute(sql)