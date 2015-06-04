#!/usr/bin/env python
# -*- coding: utf-8 -*-

__doc__ = '''\
QuotaCatalog для ВМП за прошлый год
'''

MIN_SCHEMA_VERSION = 210


def upgrade(conn):
    c = conn.cursor()

    print(u'Добавляем QuotaCatalog за прошлый год')

    sql = u'''
INSERT INTO `QuotaCatalog` (`finance_id`, `createDatetime`, `modifyDatetime`, `begDate`, `endDate`)
VALUES (7, NOW(), NOW(), '2014-01-01', '2014-12-31')
'''
    c.execute(sql)
    last_id = c.lastrowid

    print(u'Привязываем существующие строки QuotaType к QuotaCatalog за прошлый год')
    sql = u'''UPDATE `QuotaType` SET `catalog_id`=%s''' % last_id
    c.execute(sql)

    sql = u'''
ALTER TABLE `QuotaType` 
DROP FOREIGN KEY `fk_catalog_id`;
ALTER TABLE `QuotaType` 
CHANGE COLUMN `catalog_id` `catalog_id` INT(11) NOT NULL COMMENT 'ссылка на справочник квот' ;
ALTER TABLE `QuotaType` 
ADD CONSTRAINT `fk_catalog_id`
  FOREIGN KEY (`catalog_id`)
  REFERENCES `QuotaCatalog` (`id`);
'''
    c.execute(sql)

    sql = '''
INSERT INTO rbUserProfile (code, name, withDep) VALUES("anestezDoctor", "Врач анестезиолог", 0)
'''
    c.execute(sql)

    sql = '''
INSERT INTO rbUserProfile_Right (master_id, userRight_id) SELECT 41, ur.id FROM rbUserRight ur JOIN rbUserProfile_Right upr ON ur.id = upr.userRight_id AND upr.master_id = 24
'''
    c.execute(sql)

    c.close()
