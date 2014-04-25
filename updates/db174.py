#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменения, необходимые для ведения листов нетрудоспособности
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
ALTER TABLE `TempInvalid`
ADD COLUMN `tempInvalidExtraReason_id`  int(11) NULL DEFAULT NULL COMMENT 'Доп.причина нетрудоспособности{rbTempInvalidExtraReason}' AFTER `event_id`,
ADD COLUMN `busyness`  tinyint(4) NOT NULL DEFAULT 0 COMMENT 'Занятость:1- основное,2-совместитель,3-на учете' AFTER `tempInvalidExtraReason_id`,
ADD COLUMN `placeWork`  varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'Место работы' AFTER `busyness`;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `TempInvalid_Period`
ADD COLUMN `numberPermit`  varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'Номер путевки' AFTER `note`,
ADD COLUMN `begDatePermit`  date NULL DEFAULT NULL COMMENT 'Начальная дата путевки ' AFTER `numberPermit`,
ADD COLUMN `endDatePermit`  date NULL DEFAULT NULL COMMENT 'Конечная дата путевки ' AFTER `begDatePermit`,
ADD COLUMN `disability_id`  int(11) NULL DEFAULT NULL COMMENT 'Группа инвалидности{rbTempInvalidRegime}' AFTER `endDatePermit`,
ADD COLUMN `directDateOnKAK`  date NULL DEFAULT NULL COMMENT 'Направлен на КЭК' AFTER `disability_id`,
ADD COLUMN `expert_id`  int(11) NULL DEFAULT NULL COMMENT 'Эксперт {Person}' AFTER `directDateOnKAK`,
ADD COLUMN `dateKAK`  date NULL DEFAULT NULL COMMENT 'Дата КЭК' AFTER `expert_id`;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `TempInvalidDuplicate`
ADD COLUMN `placeWork`  varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'Место работы' AFTER `insuranceOfficeMark`;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `BlankTempInvalid_Moving`
ADD COLUMN `numberFrom`  varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Номер с' AFTER `returnAmount`,
ADD COLUMN `numberTo`  varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Номер по' AFTER `numberFrom`;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `BlankTempInvalid_Party`
ADD COLUMN `returnBlank`  int(11) NOT NULL COMMENT 'Возврат' AFTER `writing`;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `BlankActions_Moving`
ADD COLUMN `numberFrom`  varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Номер с' AFTER `blankParty_id`,
ADD COLUMN `numberTo`  varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Номер по' AFTER `numberFrom`;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `BlankActions_Party`
ADD COLUMN `returnBlank`  int(11) NOT NULL COMMENT 'Возврат' AFTER `writing`;
'''
    c.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `rbTempInvalidExtraReason` (
`id`  int(11) NOT NULL AUTO_INCREMENT ,
`type`  tinyint(2) NOT NULL DEFAULT 0 COMMENT 'Тип 0-ВУТ, 1-инвалидность, 2-ограничение жизнедеятельности' ,
`code`  varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Код' ,
`name`  varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'Наименование' ,
PRIMARY KEY (`id`),
INDEX `code` (`code`),
INDEX `name` (`name`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
COMMENT='Дополнительные причины ВУТ'
'''
    c.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `rbOperationClass` (
`id`  int(11) NOT NULL AUTO_INCREMENT ,
`code`  varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT 'Код' ,
`name`  varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT 'Наименование' ,
PRIMARY KEY (`id`),
INDEX `code` (`code`),
INDEX `name` (`name`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass