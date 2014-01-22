#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Индекс для кодов свойств типов действий
- Исправление для типа свойства ТРФУ
- Столбцы DocumentTable для Contract_Tariff
- Столбцы DocumentTable для ActionPropertyType
- Новое поле для Person - отображать сотрудника в расписании приема или нет
'''

def upgrade(conn):
    global config
    global tools       
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `ActionPropertyType` ADD INDEX `code` (`code` ASC) ;
'''
    tools.executeEx(c, sql, mode=['ignore_duplicates',])
    
    sql = u'''
UPDATE `ActionPropertyType` SET `typeName`="String", `valueDomain` = "'Плановая','Экстренная'"  WHERE  `code` = 'trfuReqBloodCompType';
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Contract_Tariff`
ADD COLUMN `createDatetime` DATETIME NOT NULL COMMENT 'Дата создания записи'  AFTER `rbServiceFinance_id` ,
ADD COLUMN `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор записи {Person}'  AFTER `createDatetime` ,
ADD COLUMN `modifyDatetime` DATETIME NOT NULL COMMENT 'Дата изменения записи'  AFTER `createPerson_id` ,
ADD COLUMN `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор изменения записи {Person}'  AFTER `modifyDatetime` ;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `ActionPropertyType`
ADD COLUMN `createDatetime` DATETIME NOT NULL COMMENT 'Дата создания записи'  AFTER `readOnly` ,
ADD COLUMN `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор записи {Person}'  AFTER `createDatetime` ,
ADD COLUMN `modifyDatetime` DATETIME NOT NULL COMMENT 'Дата изменения записи'  AFTER `createPerson_id` ,
ADD COLUMN `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор изменения записи {Person}'  AFTER `modifyDatetime` ,
ADD INDEX `createDatetime` (`createDatetime` ASC) ;

'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Person` ADD COLUMN `displayInTimeline` TINYINT(1) NOT NULL DEFAULT '1' COMMENT 'Отображать сотрудника в расписании'  AFTER `uuid_id` ;
'''
    c.execute(sql)
            
    
def downgrade(conn):
    pass