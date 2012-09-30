#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    c = conn.cursor()

    sql = u'''
CREATE TABLE IF NOT EXISTS `rbPacientModel` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(32) NOT NULL COMMENT 'код модели пациента',
    `name` text NOT NULL COMMENT 'название модели пациента',
    `quotaType_id` INT(11) NOT NULL COMMENT 'Квота ВМП',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`quotaType_id`) REFERENCES `QuotaType`(`id`)
)
COMMENT='Модели пациента'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `rbTreatment` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(32) NOT NULL COMMENT 'код',
    `name` text NOT NULL COMMENT 'название',
    `pacientModel_id` INT(11) NOT NULL COMMENT 'ref to {rbPacientModel.id}',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`pacientModel_id`) REFERENCES `rbPacientModel`(`id`)
)
COMMENT='Методы лечения'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

ALTER TABLE `Client_Quoting` ADD `pacientModel_id` INT(11)  NOT NULL COMMENT 'ref to {rbPacientModel}' AFTER `regionCode`;
ALTER TABLE `Client_Quoting` ADD `treatment_id`    INT(11)  NOT NULL COMMENT 'ref to {rbTreatment}'  AFTER `pacientModel_id`;
ALTER TABLE `QuotaType` ADD COLUMN `MKB` VARCHAR(8) NOT NULL AFTER `name`;
ALTER TABLE `Quoting` ADD COLUMN `teenOlder` TINYINT(1) UNSIGNED NOT NULL DEFAULT '0' COMMENT 'Для пациентов старше 18 лет' AFTER `inQueue`;

CREATE TABLE IF NOT EXISTS `LastChanges` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `table` VARCHAR(32) NOT NULL COMMENT 'название таблицы',
    `table_key_id` INT(11) NOT NULL COMMENT 'ref to { table.id }',
    `flags` TEXT NOT NULL COMMENT 'Название полей, которые изменились в таблице { table }',
    PRIMARY KEY (`id`)
)
COMMENT='Хранит изменения таблицы { table }'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;

ALTER TABLE `QuotaType` ADD COLUMN `teenOlder` TINYINT(1) NOT NULL COMMENT "Для пациентов старше 18 лет" AFTER `MKB`;
ALTER TABLE `Quoting` DROP COLUMN `teenOlder`;

ALTER TABLE `Client_Quoting`
ADD COLUMN `event_id` INT(11) NULL DEFAULT NULL COMMENT 'ref to {Event}' AFTER `treatment_id`;
'''
    c.execute(sql)


def downgrade(conn):
    pass
