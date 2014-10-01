#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление недостающего foreignkey от LayoutAttributeValue к ActionPropertyType и удаление избыточных элементов
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
        DELETE FROM LayoutAttributeValue WHERE actionPropertyType_id NOT IN (SELECT id FROM ActionPropertyType);
    '''
    c.execute(sql)

    sql = u'''
        ALTER TABLE LayoutAttributeValue ADD INDEX `actionPropertyType_id` (`actionPropertyType_id`);
    '''
    c.execute(sql)

    sql = u'''
        ALTER TABLE LayoutAttributeValue ADD CONSTRAINT `LayoutAttributeValue_actionPropertyType_id` FOREIGN KEY (`actionPropertyType_id`) REFERENCES `ActionPropertyType` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
    '''
    c.execute(sql)

def downgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
        ALTER TABLE LayoutAttributeValue DROP CONSTRAINT `LayoutAttributeValue_actionPropertyType_id`;
    '''
    c.execute(sql)

    sql = u'''
        ALTER TABLE LayoutAttributeValue DROP INDEX `actionPropertyType_id`;
    '''
    c.execute(sql)
