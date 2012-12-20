#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Изменения, неоходимые  для работы аналитических отчетов
- Добавлено поле для фильтрации отображаемых оргструктур
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''CREATE  TABLE IF NOT EXISTS `rbAnalyticalReports` ( `id` INT NOT NULL AUTO_INCREMENT,
	      `name` VARCHAR(45) NULL,
	      `PrintTemplate_id` INT(11) NULL DEFAULT NULL COMMENT 'Аналитические отчеты' ,
	      PRIMARY KEY (`id`) )
	      ENGINE = InnoDB
	      DEFAULT CHARSET=utf8
	      COMMENT 'Аналитические отчеты';
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `OrgStructure` ADD COLUMN `show` INT(11) NOT NULL DEFAULT 1  AFTER `uuid_id` ;
'''
    c.execute(sql)
    
    
def downgrade(conn):
    pass
