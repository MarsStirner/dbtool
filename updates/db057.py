#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    c = conn.cursor()

    sql = u'''
ALTER TABLE `rbMedicalAidUnit` ADD COLUMN `regionalCode` VARCHAR(1) NOT NULL AFTER `descr`;


ALTER TABLE `rbTempInvalidDocument`
ADD COLUMN `checkingSerial` ENUM('нет', 'мягко', 'жестко') NOT NULL COMMENT 'контроль серии' AFTER `name`,
ADD COLUMN `checkingNumber` ENUM('нет', 'мягко', 'жестко') NOT NULL COMMENT 'контроль номера' AFTER `checkingSerial`,
ADD COLUMN `checkingAmount` ENUM('нет', 'списание') NOT NULL COMMENT 'контроль количества' AFTER `checkingNumber`;
'''
    c.execute(sql)
	
    sql = '''
CREATE TABLE `rbBlankActions` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `doctype_id` INT(11) NOT NULL COMMENT 'пїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ {ActionType}',
    `code` VARCHAR(16) NOT NULL COMMENT 'пїЅпїЅпїЅ',
    `name` VARCHAR(64) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `checkingSerial` TINYINT(3) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅ 0-пїЅпїЅпїЅ, 1-пїЅпїЅпїЅпїЅпїЅ, 2-пїЅпїЅпїЅпїЅпїЅпїЅ',
    `checkingNumber` TINYINT(3) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ 0-пїЅпїЅпїЅ, 1-пїЅпїЅпїЅпїЅпїЅ, 2-пїЅпїЅпїЅпїЅпїЅпїЅ',
    `checkingAmount` TINYINT(2) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ 0-пїЅпїЅпїЅ, 1-пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `actiontype` (`id`)
)
COMMENT='пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ Action'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `rbBlankTempInvalids` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `doctype_id` INT(11) NOT NULL COMMENT 'пїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ {rbTempInvalidDocument}',
    `code` VARCHAR(16) NOT NULL COMMENT 'пїЅпїЅпїЅ',
    `name` VARCHAR(64) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `checkingSerial` TINYINT(3) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅ 0-пїЅпїЅпїЅ, 1-пїЅпїЅпїЅпїЅпїЅ, 2-пїЅпїЅпїЅпїЅпїЅпїЅ',
    `checkingNumber` TINYINT(3) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ 0-пїЅпїЅпїЅ, 1-пїЅпїЅпїЅпїЅпїЅ, 2-пїЅпїЅпїЅпїЅпїЅпїЅ',
    `checkingAmount` TINYINT(2) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ 0-пїЅпїЅпїЅ, 1-пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`doctype_id`) REFERENCES `rbtempinvaliddocument` (`id`)
)
COMMENT='пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅ пїЅпїЅпїЅ'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;


CREATE TABLE `BlankTempInvalid_Party` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `modifyDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `date` DATE NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `doctype_id` INT(11) NOT NULL COMMENT 'пїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ {rbBlankTempInvalids}',
    `person_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `serial` VARCHAR(8) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `numberFrom` VARCHAR(16) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅ',
    `numberTo` VARCHAR(16) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅ',
    `amount` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `extradited` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `balance` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `used` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `writing` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
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
COMMENT='пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅ, пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
	
    sql = '''
CREATE TABLE `BlankTempInvalid_Moving` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `modifyDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `date` DATE NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `blankParty_id` INT(11) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅ {BlankTempInvalid_Party}',
    `serial` VARCHAR(8) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `orgStructure_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {OrgStructure}',
    `person_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `received` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `used` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `returnDate` DATE NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅ',
    `returnAmount` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
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
COMMENT='пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅ, пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

CREATE TABLE `BlankActions_Party` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `modifyDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `date` DATE NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `doctype_id` INT(11) NOT NULL COMMENT 'пїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ {rbBlankActions}',
    `person_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `serial` VARCHAR(8) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `numberFrom` VARCHAR(16) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅ',
    `numberTo` VARCHAR(16) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅ',
    `amount` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `extradited` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `balance` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `used` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `writing` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
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
COMMENT='пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅ, пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
	
    sql = '''
CREATE TABLE `BlankActions_Moving` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `modifyDatetime` DATETIME NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `date` DATE NOT NULL COMMENT 'пїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `blankParty_id` INT(11) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅ {BlankActions_Party}',
    `serial` VARCHAR(8) NOT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ',
    `orgStructure_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {OrgStructure}',
    `person_id` INT(11) NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅ {Person}',
    `received` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `used` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
    `returnDate` DATE NULL DEFAULT NULL COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅ',
    `returnAmount` INT(4) NOT NULL DEFAULT '0' COMMENT 'пїЅпїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ',
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
COMMENT='пїЅпїЅпїЅпїЅпїЅпїЅ пїЅпїЅпїЅ, пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ'
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
    c.execute(sql)


def downgrade(conn):
    pass
