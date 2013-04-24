#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Увеличение количества вводимых символов
'''


def upgrade(conn):
    global config        
    c = conn.cursor()

    sql = u'''ALTER TABLE `OrgStructure` CHANGE 
    COLUMN `code` `code` VARCHAR(255) NOT NULL COMMENT 'Код подразделения'  , 
    CHANGE COLUMN `name` `name` VARCHAR(255) NOT NULL COMMENT 'Наименование'  , 
    CHANGE COLUMN `Address` `Address` VARCHAR(255) NOT NULL COMMENT 'Адрес'  ;
'''
    c.execute(sql)    

    sql = u'''ALTER TABLE `rbThesaurus` 
    CHANGE COLUMN `code` `code` VARCHAR(30) NOT NULL COMMENT 'Код; применяется преимущественно для упорядочивания'  , 
    CHANGE COLUMN `name` `name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'Наименование'  , 
    CHANGE COLUMN `template` `template` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'Шаблон для разворачивания ветки дерева в строку, вместо %s рекурсивно подставлется parent.template'  ;
'''
    c.execute(sql) 
    
    sql = u'''ALTER TABLE `Organisation`
CHANGE COLUMN `fullName` `fullName` VARCHAR(255) NOT NULL COMMENT 'Полное наименование'  , 
CHANGE COLUMN `shortName` `shortName` VARCHAR(255) NOT NULL COMMENT 'Краткое наименование'  , 
CHANGE COLUMN `title` `title` VARCHAR(255) NOT NULL COMMENT 'Наименование для печати'  , 
CHANGE COLUMN `Address` `Address` VARCHAR(255) NOT NULL COMMENT 'Адрес'  , 
CHANGE COLUMN `phone` `phone` VARCHAR(255) NOT NULL COMMENT 'Телефон'  ;
'''
    c.execute(sql) 
    
    c.close()
    
def downgrade(conn):
    pass