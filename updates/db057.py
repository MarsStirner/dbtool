#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- Добавление таблиц из 6098
- Изменения таблиц из 6098
- Дополнительные изменения для ЗНР по ВМП
'''


def upgrade(conn):
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `rbMedicalAidUnit` ADD COLUMN `regionalCode` VARCHAR(1) NOT NULL AFTER `descr`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise
    
    sql = u'''
ALTER TABLE `rbTempInvalidDocument`
ADD COLUMN `checkingSerial` ENUM('нет', 'мягко', 'жестко') NOT NULL COMMENT 'контроль серии' AFTER `name`,
ADD COLUMN `checkingNumber` ENUM('нет', 'мягко', 'жестко') NOT NULL COMMENT 'контроль номера' AFTER `checkingSerial`,
ADD COLUMN `checkingAmount` ENUM('нет', 'списание') NOT NULL COMMENT 'контроль количества' AFTER `checkingNumber`;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE IF NOT EXISTS `rbBlankActions` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `doctype_id` INT(11) NOT NULL,
    `code` VARCHAR(16) NOT NULL,
    `name` VARCHAR(64) NOT NULL,
    `checkingSerial` TINYINT(3) NOT NULL,
    `checkingNumber` TINYINT(3) NOT NULL,
    `checkingAmount` TINYINT(2) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `ActionType` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE IF NOT EXISTS `rbBlankTempInvalids` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `doctype_id` INT(11) NOT NULL,
    `code` VARCHAR(16) NOT NULL,
    `name` VARCHAR(64) NOT NULL,
    `checkingSerial` TINYINT(3) NOT NULL,
    `checkingNumber` TINYINT(3) NOT NULL,
    `checkingAmount` TINYINT(2) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `rbTempInvalidDocument` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `BlankTempInvalid_Party` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL,
    `createPerson_id` INT(11) NULL DEFAULT NULL,
    `modifyDatetime` DATETIME NOT NULL,
    `modifyPerson_id` INT(11) NULL DEFAULT NULL,
    `deleted` TINYINT(1) NOT NULL DEFAULT '0',
    `date` DATE NOT NULL,
    `doctype_id` INT(11) NOT NULL,
    `person_id` INT(11) NULL DEFAULT NULL,
    `serial` VARCHAR(8) NOT NULL,
    `numberFrom` VARCHAR(16) NOT NULL,
    `numberTo` VARCHAR(16) NOT NULL,
    `amount` INT(4) NOT NULL DEFAULT '0',
    `extradited` INT(4) NOT NULL DEFAULT '0',
    `balance` INT(4) NOT NULL DEFAULT '0',
    `used` INT(4) NOT NULL DEFAULT '0',
    `writing` INT(4) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    INDEX `createPerson_id` (`createPerson_id`),
    INDEX `modifyPerson_id` (`modifyPerson_id`),
    INDEX `doctype_id` (`doctype_id`),
    INDEX `person_id` (`person_id`),
    FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `rbBlankTempInvalids` (`id`),
    FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`),
    FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE IF NOT EXISTS `BlankTempInvalid_Moving` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL,
    `createPerson_id` INT(11) NULL DEFAULT NULL,
    `modifyDatetime` DATETIME NOT NULL,
    `modifyPerson_id` INT(11) NULL DEFAULT NULL,
    `deleted` TINYINT(1) NOT NULL DEFAULT '0',
    `date` DATE NOT NULL,
    `blankParty_id` INT(11) NOT NULL,
    `serial` VARCHAR(8) NOT NULL,
    `orgStructure_id` INT(11) NULL DEFAULT NULL,
    `person_id` INT(11) NULL DEFAULT NULL,
    `received` INT(4) NOT NULL DEFAULT '0',
    `used` INT(4) NOT NULL DEFAULT '0',
    `returnDate` DATE NULL DEFAULT NULL,
    `returnAmount` INT(4) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    INDEX `createPerson_id` (`createPerson_id`),
    INDEX `modifyPerson_id` (`modifyPerson_id`),
    INDEX `blankParty_id` (`blankParty_id`),
    INDEX `orgStructure_id` (`orgStructure_id`),
    INDEX `person_id` (`person_id`),
    CONSTRAINT `blankTempInvalid_Moving_blankParty_id` FOREIGN KEY (`blankParty_id`) REFERENCES `BlankTempInvalid_Party` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_createPerson_id` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_modifyPerson_id` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_orgStructure_id` FOREIGN KEY (`orgStructure_id`) REFERENCES `OrgStructure` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_person_id` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `BlankActions_Party` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL,
    `createPerson_id` INT(11) NULL DEFAULT NULL,
    `modifyDatetime` DATETIME NOT NULL,
    `modifyPerson_id` INT(11) NULL DEFAULT NULL,
    `deleted` TINYINT(1) NOT NULL DEFAULT '0',
    `date` DATE NOT NULL,
    `doctype_id` INT(11) NOT NULL,
    `person_id` INT(11) NULL DEFAULT NULL,
    `serial` VARCHAR(8) NOT NULL,
    `numberFrom` VARCHAR(16) NOT NULL,
    `numberTo` VARCHAR(16) NOT NULL,
    `amount` INT(4) NOT NULL DEFAULT '0',
    `extradited` INT(4) NOT NULL DEFAULT '0',
    `balance` INT(4) NOT NULL DEFAULT '0',
    `used` INT(4) NOT NULL DEFAULT '0',
    `writing` INT(4) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    INDEX `createPerson_id` (`createPerson_id`),
    INDEX `modifyPerson_id` (`modifyPerson_id`),
    INDEX `doctype_id` (`doctype_id`),
    INDEX `person_id` (`person_id`),
    CONSTRAINT `blankActions_Party_createPerson_id` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `blankActions_Party_doctype_id` FOREIGN KEY (`doctype_id`) REFERENCES `rbBlankActions` (`id`),
    CONSTRAINT `blankActions_Party_modifyPerson_id` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `blankActions_Party_person_id` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE IF NOT EXISTS `BlankActions_Moving` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL,
    `createPerson_id` INT(11) NULL DEFAULT NULL,
    `modifyDatetime` DATETIME NOT NULL,
    `modifyPerson_id` INT(11) NULL DEFAULT NULL,
    `deleted` TINYINT(1) NOT NULL DEFAULT '0',
    `date` DATE NOT NULL,
    `blankParty_id` INT(11) NOT NULL,
    `serial` VARCHAR(8) NOT NULL,
    `orgStructure_id` INT(11) NULL DEFAULT NULL,
    `person_id` INT(11) NULL DEFAULT NULL,
    `received` INT(4) NOT NULL DEFAULT '0',
    `used` INT(4) NOT NULL DEFAULT '0',
    `returnDate` DATE NULL DEFAULT NULL,
    `returnAmount` INT(4) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    INDEX `createPerson_id` (`createPerson_id`),
    INDEX `modifyPerson_id` (`modifyPerson_id`),
    INDEX `blankParty_id` (`blankParty_id`),
    INDEX `orgStructure_id` (`orgStructure_id`),
    INDEX `person_id` (`person_id`),
    CONSTRAINT `blankActions_Moving_blankParty_id` FOREIGN KEY (`blankParty_id`) REFERENCES `BlankActions_Party` (`id`),
    CONSTRAINT `blankActions_Moving_createPerson_id` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `blankActions_Moving_modifyPerson_id` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `blankActions_Moving_orgStructure_id` FOREIGN KEY (`orgStructure_id`) REFERENCES `OrgStructure` (`id`),
    CONSTRAINT `blankActions_Moving_person_id` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `MKB_QuotaType_PacientModel` (
`id` INT(11) NOT NULL AUTO_INCREMENT,   
`MKB_id` INT(11) NOT NULL COMMENT 'ref to {MKB}',
`pacientModel_id` INT(11) NOT NULL COMMENT 'ref to {rbPacientModel}',
`quotaType_id` INT(11) NOT NULL COMMENT 'ref to {QuotaType}',
PRIMARY KEY (`id`)
)
COMMENT='Связь таблиц для талонов ВМП'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Action` ADD `hospitalUidFrom` VARCHAR(128)  NOT NULL  DEFAULT '0'  AFTER `coordText`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise


def downgrade(conn):
    pass
