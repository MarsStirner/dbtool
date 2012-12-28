#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import sys
import re

__doc__ = '''\
- Перенос базы лекарственных средств в базу ЛПУ
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    c.execute('SHOW DATABASES;')
    if 'rls' in [d[0] for d in c.fetchall()]:
        mergeRLSdb(conn)
    else:
        print('RLS database not found!')
        print('Copying schema...')
        upgradeRLSschema(conn)
    
def mergeRLSdb(conn):
    global config
    c = conn.cursor()
    
    c.execute('USE rls;')
    c.execute('SHOW FULL TABLES WHERE Table_Type = "BASE TABLE";')
    tables = [t[0] for t in c.fetchall()]
    c.execute('USE %s;' % config['dbname'])
    print('Inserting: ', end='')
    sys.stdout.flush()
    for table in tables:
        print('%s...' % table, end='')
        sys.stdout.flush()
        show_stmt = 'SHOW CREATE TABLE rls.%s' % table
        c.execute(show_stmt)
        create_stmt = c.fetchone()[1]
        c.execute(create_stmt)
        insert_stmt = u'INSERT INTO %s SELECT * FROM rls.%s' % (table, table)
        c.execute(insert_stmt)
    
    c.execute('USE rls;')
    c.execute('SHOW FULL TABLES WHERE Table_Type = "VIEW";')
    views = [t[0] for t in c.fetchall()]
    c.execute('USE %s;' % config['dbname'])
    for view in views:
        print('%s...' % view, end='')
        sys.stdout.flush()
        show_stmt = 'SHOW CREATE VIEW rls.%s' % view
        c.execute(show_stmt)
        create_stmt = c.fetchone()[1]
        create_stmt = create_stmt.replace('`rls`.', '')
        replacedDefiner = '`%s`@`%s`' % (config['username'], config['host'])
        create_stmt = re.sub(r'`\w+`@`[\w\.]+`', replacedDefiner, create_stmt)
        c.execute(create_stmt)
        
    print('\n')
    
    
def upgradeRLSschema(conn):
    global config
    c = conn.cursor()    
    
    sql = u'''
CREATE TABLE `rlsATCGroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `code` varchar(8) NOT NULL,
  `name` varchar(512) DEFAULT NULL,
  `nameRaw` varchar(512) NOT NULL,
  `path` varchar(128) NOT NULL,
  `pathx` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `nameRaw` (`nameRaw`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsATCGroupExt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(8) NOT NULL,
  `name` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsATCGroupToCode` (
  `rlsATCGroup_id` int(11) NOT NULL DEFAULT '0',
  `code` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`rlsATCGroup_id`,`code`),
  KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsDosage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsFilling` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `disabledForPrescription` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Скрывать при выборе для рецепта',
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsForm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsINPName` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `latName` varchar(255) DEFAULT NULL,
  `rawName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`,`latName`),
  KEY `rawName` (`rawName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsINPNameToCode` (
  `rlsINPName_id` int(11) NOT NULL DEFAULT '0',
  `code` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`rlsINPName_id`,`code`),
  KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsMKBToCode` (
  `MKB` varchar(16) NOT NULL DEFAULT '',
  `code` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`MKB`,`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsNomen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL COMMENT 'РЛС-овский код',
  `tradeName_id` int(11) DEFAULT NULL COMMENT 'Торговое название {rlsTradeName}',
  `INPName_id` int(11) DEFAULT NULL COMMENT 'МНН/НДВ {rlsINPName}',
  `form_id` int(11) DEFAULT NULL COMMENT 'Лекарственная форма {rlsForm}',
  `dosage_id` int(11) DEFAULT NULL COMMENT 'Доза в единице лекарственной формы {rlsDosage}',
  `filling_id` int(11) DEFAULT NULL COMMENT 'Фасовка {rlsFilling}',
  `packing_id` int(11) DEFAULT NULL COMMENT 'Упаковка {rlsPacking}',
  `regDate` date DEFAULT NULL COMMENT 'Дата регистрации',
  `annDate` date DEFAULT NULL COMMENT 'Дата отмены',
  `disabledForPrescription` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Скрывать при выборе для рецепта',
  PRIMARY KEY (`id`),
  KEY `code` (`code`),
  KEY `tradeName_id` (`tradeName_id`),
  KEY `INPName_id` (`INPName_id`),
  KEY `form_id` (`form_id`),
  KEY `dosage_id` (`dosage_id`),
  KEY `filling_id` (`filling_id`),
  KEY `packing_id` (`packing_id`),
  KEY `regDate` (`regDate`),
  KEY `annDate` (`annDate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsNomenRaw` (
  `code` int(11) NOT NULL,
  `tradeName` varchar(256) NOT NULL,
  `latName` varchar(256) NOT NULL,
  `NDV` varchar(256) NOT NULL,
  `kind` varchar(6) NOT NULL,
  `life` varchar(1) NOT NULL,
  `form` varchar(64) NOT NULL,
  `dosage` varchar(64) NOT NULL,
  `filling` varchar(128) NOT NULL,
  `packing` varchar(64) NOT NULL,
  `manufacturer` varchar(128) NOT NULL,
  `mcountry` varchar(32) NOT NULL,
  `distributor` varchar(128) NOT NULL,
  `dcountry` varchar(32) NOT NULL,
  `packer` varchar(128) NOT NULL,
  `pcountry` varchar(32) NOT NULL,
  `barcode` varchar(16) NOT NULL,
  `regNum` varchar(64) NOT NULL,
  `regDate` varchar(10) NOT NULL,
  `registrator` varchar(128) NOT NULL,
  `rcountry` varchar(32) NOT NULL,
  `price` varchar(64) NOT NULL,
  `age` varchar(256) NOT NULL,
  `group` varchar(512) NOT NULL,
  `MKB` varchar(10240) NOT NULL,
  `ATC` varchar(512) NOT NULL,
  KEY `code` (`code`),
  KEY `tradeName` (`tradeName`(255)),
  KEY `latName` (`latName`(255)),
  KEY `NDV` (`NDV`(255)),
  KEY `kind` (`kind`),
  KEY `life` (`life`),
  KEY `form` (`form`),
  KEY `dosage` (`dosage`),
  KEY `filling` (`filling`),
  KEY `packing` (`packing`),
  KEY `group` (`group`(255)),
  KEY `MKB` (`MKB`(255)),
  KEY `tradeName_2` (`tradeName`(255),`latName`(255)),
  KEY `ATC` (`ATC`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsPacking` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `disabledForPrescription` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Скрывать при выборе для рецепта',
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsPharmGroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `code` varchar(8) DEFAULT NULL,
  `name` varchar(128) DEFAULT NULL,
  `path` varchar(128) DEFAULT NULL,
  `pathx` varchar(128) DEFAULT NULL,
  `nameRaw` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `nameRaw` (`nameRaw`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsPharmGroupToCode` (
  `rlsPharmGroup_id` int(11) NOT NULL DEFAULT '0',
  `code` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`rlsPharmGroup_id`,`code`),
  KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
        
    sql = u'''
CREATE TABLE `rlsTradeName` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `latName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `name` (`name`,`latName`),
  KEY `latName` (`latName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rlsTradeNameToCode` (
  `rlsTradeName_id` int(11) NOT NULL DEFAULT '0',
  `code` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`rlsTradeName_id`,`code`),
  KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
        
    sql = u'''
CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `%s`@`%s` 
    SQL SECURITY DEFINER
VIEW `vNomen` AS
    select 
        `rlsNomen`.`id` AS `id`,
        `rlsNomen`.`code` AS `code`,
        `rlsNomen`.`tradeName_id` AS `tradeName_id`,
        `rlsNomen`.`INPName_id` AS `INPName_id`,
        `rlsNomen`.`form_id` AS `form_id`,
        `rlsNomen`.`dosage_id` AS `dosage_id`,
        `rlsNomen`.`filling_id` AS `filling_id`,
        `rlsNomen`.`packing_id` AS `packing_id`,
        `rlsNomen`.`regDate` AS `regDate`,
        `rlsNomen`.`annDate` AS `annDate`,
        `rlsTradeName`.`name` AS `tradeName`,
        `rlsTradeName`.`latName` AS `tradeNameLat`,
        `rlsINPName`.`name` AS `INPName`,
        `rlsINPName`.`latName` AS `INPNameLat`,
        `rlsForm`.`name` AS `form`,
        `rlsDosage`.`name` AS `dosage`,
        `rlsFilling`.`name` AS `filling`,
        `rlsPacking`.`name` AS `packing`,
        (`rlsNomen`.`disabledForPrescription`
            or if(isnull(`rlsFilling`.`disabledForPrescription`),
            0,
            `rlsFilling`.`disabledForPrescription`)
            or if(isnull(`rlsPacking`.`disabledForPrescription`),
            0,
            `rlsPacking`.`disabledForPrescription`)) AS `disabledForPrescription`
    from
        ((((((`rlsNomen`
        left join `rlsTradeName` ON ((`rlsTradeName`.`id` = `rlsNomen`.`tradeName_id`)))
        left join `rlsINPName` ON ((`rlsINPName`.`id` = `rlsNomen`.`INPName_id`)))
        left join `rlsForm` ON ((`rlsForm`.`id` = `rlsNomen`.`form_id`)))
        left join `rlsDosage` ON ((`rlsDosage`.`id` = `rlsNomen`.`dosage_id`)))
        left join `rlsFilling` ON ((`rlsFilling`.`id` = `rlsNomen`.`filling_id`)))
        left join `rlsPacking` ON ((`rlsPacking`.`id` = `rlsNomen`.`packing_id`)))
''' % (config['username'], config['host'])
    c.execute(sql)
   

def downgrade(conn):
    pass
