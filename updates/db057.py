#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    sql = u'''
ALTER TABLE `rbMedicalAidUnit` ADD COLUMN `regionalCode` VARCHAR(1) NOT NULL AFTER `descr`;


ALTER TABLE `rbTempInvalidDocument`
ADD COLUMN `checkingSerial` ENUM('нет', 'мягко', 'жестко') NOT NULL COMMENT 'контроль серии' AFTER `name`,
ADD COLUMN `checkingNumber` ENUM('нет', 'мягко', 'жестко') NOT NULL COMMENT 'контроль номера' AFTER `checkingSerial`,
ADD COLUMN `checkingAmount` ENUM('нет', 'списание') NOT NULL COMMENT 'контроль количества' AFTER `checkingNumber`;
'''
    c = conn.cursor()
    c.execute(sql)
	
    sql = u'''
CREATE TABLE `rbBlankActions` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `doctype_id` INT(11) NOT NULL,
    `code` VARCHAR(16) NOT NULL,
    `name` VARCHAR(64) NOT NULL,
    `checkingSerial` TINYINT(3) NOT NULL,
    `checkingNumber` TINYINT(3) NOT NULL,
    `checkingAmount` TINYINT(2) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `actiontype` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c = conn.cursor()
    c.execute(sql)

    sql = u'''
CREATE TABLE `rbBlankTempInvalids` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `doctype_id` INT(11) NOT NULL,
    `code` VARCHAR(16) NOT NULL,
    `name` VARCHAR(64) NOT NULL,
    `checkingSerial` TINYINT(3) NOT NULL,
    `checkingNumber` TINYINT(3) NOT NULL,
    `checkingAmount` TINYINT(2) NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `rbtempinvaliddocument` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;


CREATE TABLE `BlankTempInvalid_Party` (
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
    FOREIGN KEY (`createPerson_id`) REFERENCES `person` (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `rbblanktempinvalids` (`id`),
    FOREIGN KEY (`modifyPerson_id`) REFERENCES `person` (`id`),
    FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c = conn.cursor()
    c.execute(sql)
	
    sql = u'''
CREATE TABLE `BlankTempInvalid_Moving` (
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
    CONSTRAINT `blankTempInvalid_Moving_blankParty_id` FOREIGN KEY (`blankParty_id`) REFERENCES `blanktempinvalid_party` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_createPerson_id` FOREIGN KEY (`createPerson_id`) REFERENCES `person` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_modifyPerson_id` FOREIGN KEY (`modifyPerson_id`) REFERENCES `person` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_orgStructure_id` FOREIGN KEY (`orgStructure_id`) REFERENCES `orgstructure` (`id`),
    CONSTRAINT `blankTempInvalid_Moving_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

CREATE TABLE `BlankActions_Party` (
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
    CONSTRAINT `blankActions_Party_createPerson_id` FOREIGN KEY (`createPerson_id`) REFERENCES `person` (`id`),
    CONSTRAINT `blankActions_Party_doctype_id` FOREIGN KEY (`doctype_id`) REFERENCES `rbblankactions` (`id`),
    CONSTRAINT `blankActions_Party_modifyPerson_id` FOREIGN KEY (`modifyPerson_id`) REFERENCES `person` (`id`),
    CONSTRAINT `blankActions_Party_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''

    c = conn.cursor()
    c.execute(sql)
	
    sql = u'''
CREATE TABLE `BlankActions_Moving` (
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
    CONSTRAINT `blankActions_Moving_blankParty_id` FOREIGN KEY (`blankParty_id`) REFERENCES `blankactions_party` (`id`),
    CONSTRAINT `blankActions_Moving_createPerson_id` FOREIGN KEY (`createPerson_id`) REFERENCES `person` (`id`),
    CONSTRAINT `blankActions_Moving_modifyPerson_id` FOREIGN KEY (`modifyPerson_id`) REFERENCES `person` (`id`),
    CONSTRAINT `blankActions_Moving_orgStructure_id` FOREIGN KEY (`orgStructure_id`) REFERENCES `orgstructure` (`id`),
    CONSTRAINT `blankActions_Moving_person_id` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;


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


ALTER TABLE `Action` ADD `hospitalUidFrom` VARCHAR(128)  NOT NULL  DEFAULT '0'  AFTER `coordText`;
'''
    c = conn.cursor()
    c.execute(sql)


def downgrade(conn):
    pass
