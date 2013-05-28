#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление таблиц для хранения разметки документов
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
        CREATE TABLE `LayoutAttribute` (
        `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'идентификатор атрибута',
        `title` varchar(255) NOT NULL COMMENT 'название атрибута для отображения в интерфейсе',
        `description` varchar(1023) NOT NULL COMMENT 'описание атрибута и его использования',
        `code` varchar(255) NOT NULL COMMENT 'мнемо код атрибута для сопоставления с соответствующим свойством отображения в интерфейсе',
        `typeName` varchar(255) DEFAULT NULL COMMENT 'название типа поля для которого данный атрибут применяется (прим. ‘Constructor’, ‘Text’ и т.д.)',
        `measure` varchar(255) DEFAULT NULL COMMENT 'единица измерения значения данного атрибута',
        `defaultValue` varchar(1023) DEFAULT NULL COMMENT 'значение по умолчанию',
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
    c.execute(sql)
    
   
    sql = u'''
    CREATE TABLE `LayoutAttributeValue` (
        `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'идентификатор записи',
        `actionPropertyType_id` int(11) NOT NULL COMMENT 'идентификатор свойства действия, к которому относится запись',
        `layoutAttribute_id` int(11) NOT NULL COMMENT 'идентификатор записи, содержащий ссылку на код атрибута',
        `value` varchar(1023) NOT NULL COMMENT 'значение атрибута',
        PRIMARY KEY (`id`),
        KEY `layoutAttribute_id_FK` (`layoutAttribute_id`),
        CONSTRAINT `layoutAttribute_id_FK` FOREIGN KEY (`layoutAttribute_id`) REFERENCES `LayoutAttribute` (`id`) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    '''
    c.execute(sql)
    
           
def downgrade(conn):
    pass
