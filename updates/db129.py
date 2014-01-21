#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import MySQLdb as db

__doc__ = '''
- Добавление таблиц для Листа Назначений
- Деструктивное преобразование БД РЛС
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u"DROP TABLE IF EXISTS rlsATCGroup;"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsATCGroupExt;"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsATCGroupToCode;"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsDosage;"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsINPNameToCode;"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsMKBToCode;"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsNomenRaw;"
    c.execute(sql)

    sql = u"""CREATE TABLE IF NOT EXISTS `DrugChart` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `action_id` INT(11) NOT NULL,
    `master_id` INT(11) NULL DEFAULT NULL,
    `begDateTime` DATETIME NOT NULL,
    `endDateTime` DATETIME NULL DEFAULT NULL,
    `status` TINYINT(1) UNSIGNED NOT NULL,
    `statusDateTime` DATETIME NULL DEFAULT NULL,
    `note` VARCHAR(256) NULL DEFAULT '',
    PRIMARY KEY (`id`),
    INDEX `master_id` (`master_id`),
    INDEX `action_uuid` (`action_id`),
    CONSTRAINT `FK_DrugChart_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`),
    CONSTRAINT `FK_DrugChart_DrugChart` FOREIGN KEY (`master_id`) REFERENCES `DrugChart` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;"""
    c.execute(sql)

    sql = u"""CREATE TABLE IF NOT EXISTS `DrugComponent` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `action_id` INT(11) NOT NULL,
    `nomen` INT(11) NULL DEFAULT NULL,
    `name` VARCHAR(255) NULL DEFAULT NULL,
    `dose` FLOAT NULL DEFAULT NULL,
    `unit` INT(10) NULL DEFAULT NULL,
    `createDateTime` DATETIME NOT NULL,
    `cancelDateTime` DATETIME NULL DEFAULT NULL,
    PRIMARY KEY (`id`),
    INDEX `FK_DrugComponent_rlsNomen` (`nomen`),
    INDEX `FK_DrugComponent_Action` (`action_id`),
    CONSTRAINT `FK_DrugComponent_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;"""
    c.execute(sql)

    # Эти справочники понадобятся в будущем, а я не знаю, откуда их брать.
    # u"DROP TABLE rlsPharmGroup;",
    # u"DROP TABLE rlsPharmGroupToCode;",

    sql = u"DROP TABLE IF EXISTS rlsTradeNameToCode;"
    c.execute(sql)

    sql = u"DROP VIEW IF EXISTS vNomen"
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsNomen"
    c.execute(sql)

    sql = u"TRUNCATE `rlsPacking`"
    c.execute(sql)

    sql = u"TRUNCATE `rlsFilling`"
    c.execute(sql)

    sql = u"TRUNCATE `rlsForm`"
    c.execute(sql)

    sql = u"ALTER IGNORE TABLE rlsFilling DROP COLUMN `disabledForPrescription`"
    try:
        c.execute(sql)
    except db.OperationalError as e:
        if '1091' in unicode(e):
            print(e)
        else:
            raise

    sql = u"ALTER IGNORE TABLE `rlsFilling` DROP INDEX `name`, ADD UNIQUE INDEX `name` (`name`);"
    c.execute(sql)

    sql = u"""ALTER IGNORE TABLE `rbUnit`
    CHANGE COLUMN `code` `code` VARCHAR(256),
    CHANGE COLUMN `name` `name` VARCHAR(256)"""
    c.execute(sql)

    sql = u"DROP TABLE IF EXISTS rlsINPName"
    c.execute(sql)

    sql = u"""CREATE TABLE IF NOT EXISTS `rlsActMatters` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор вещества',
    `name` VARCHAR(255) NULL DEFAULT NULL COMMENT 'Международное наименование',
    `localName` VARCHAR(255) NULL DEFAULT NULL COMMENT 'Локальное наименование',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `name_localName` (`name`, `localName`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;"""
    c.execute(sql)

    sql = u"TRUNCATE `rlsTradeName`"
    c.execute(sql)

    sql = u"""ALTER IGNORE TABLE `rlsTradeName`
    CHANGE COLUMN `latName` `name` VARCHAR(255) NULL DEFAULT NULL AFTER `id`,
    CHANGE COLUMN `name` `localName` VARCHAR(255) NULL DEFAULT NULL AFTER `name`;"""
    c.execute(sql)

    sql = u"""ALTER IGNORE TABLE `rlsTradeName`
    DROP INDEX `name`,
    DROP INDEX `latName`, ADD UNIQUE INDEX `name_localName` (`name`, `localName`);"""
    c.execute(sql)

    sql = u"""CREATE TABLE  IF NOT EXISTS  `rlsNomen` (
    `id` INT(11) NOT NULL COMMENT 'РЛС-овский код',
    `actMatters_id` INT(11) NULL DEFAULT NULL COMMENT 'Действующие вещества {rlsActMatters}',
    `tradeName_id` INT(11) NOT NULL COMMENT 'Торговое название {rlsTradeName}',
    `form_id` INT(11) NULL DEFAULT NULL COMMENT 'Лекарственная форма {rlsForm}',
    `packing_id` INT(11) NULL DEFAULT NULL COMMENT 'Упаковка {rlsPacking}',
    `filling_id` INT(11) NULL DEFAULT NULL COMMENT 'Фасовка {rlsFilling}',
    `unit_id` INT(11) NULL DEFAULT NULL COMMENT 'Ед.Изм. препарата {rbUnit}',
    `dosageValue` VARCHAR(128) NULL DEFAULT NULL COMMENT 'Доза в единице лекарственной формы ',
    `dosageUnit_id` INT(11) NULL DEFAULT NULL COMMENT 'Ед.Изм. дозировки препарата {rbUnit}',
    `drugLifetime` INT(11) NULL DEFAULT NULL COMMENT 'Время жизни препарата в месяцах',
    `regDate` DATE NULL DEFAULT NULL COMMENT 'Дата регистрации',
    `annDate` DATE NULL DEFAULT NULL COMMENT 'Дата отмены',
    PRIMARY KEY (`id`),
    INDEX `tradeName_id` (`tradeName_id`),
    INDEX `FK_rlsNomen_rlsForm` (`form_id`),
    INDEX `FK_rlsNomen_rlsActMatters` (`actMatters_id`),
    INDEX `FK_rlsNomen_rlsPacking` (`packing_id`),
    INDEX `FK_rlsNomen_rlsFilling` (`filling_id`),
    INDEX `FK_rlsNomen_rbUnit` (`unit_id`),
    INDEX `FK_rlsNomen_rbUnit_2` (`dosageUnit_id`),
    CONSTRAINT `FK_rlsNomen_rbUnit` FOREIGN KEY (`unit_id`) REFERENCES `rbUnit` (`id`),
    CONSTRAINT `FK_rlsNomen_rbUnit_2` FOREIGN KEY (`dosageUnit_id`) REFERENCES `rbUnit` (`id`),
    CONSTRAINT `FK_rlsNomen_rlsFilling` FOREIGN KEY (`filling_id`) REFERENCES `rlsFilling` (`id`),
    CONSTRAINT `FK_rlsNomen_rlsForm` FOREIGN KEY (`form_id`) REFERENCES `rlsForm` (`id`),
    CONSTRAINT `FK_rlsNomen_rlsPacking` FOREIGN KEY (`packing_id`) REFERENCES `rlsPacking` (`id`),
    CONSTRAINT `FK_rlsNomen_rlsActMatters` FOREIGN KEY (`actMatters_id`) REFERENCES `rlsActMatters` (`id`),
    CONSTRAINT `FK_rlsNomen_rlsTradeName` FOREIGN KEY (`tradeName_id`) REFERENCES `rlsTradeName` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;"""
    c.execute(sql)

    sql = u"ALTER IGNORE TABLE `rlsPacking` DROP COLUMN `disabledForPrescription`"
    c.execute(sql)

    sql = u"ALTER IGNORE TABLE `rlsPacking` DROP INDEX `name`, ADD UNIQUE INDEX `name` (`name`)"
    c.execute(sql)

    sql = u"ALTER IGNORE TABLE `rlsForm` DROP INDEX `name`, ADD UNIQUE INDEX `name` (`name`);"
    c.execute(sql)

    sql = u"""CREATE TABLE `rlsBalanceOfGoods` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `rlsNomen_id` INT(11) NOT NULL,
    `orgStructure_id` INT(11) NULL,
    `value` DOUBLE NOT NULL,
    `bestBefore` DATE NOT NULL,
    `disabled` TINYINT(4) NOT NULL DEFAULT '0',
    PRIMARY KEY (`id`),
    CONSTRAINT `FK_rlsBalanceOfGoods_OrgStructure` FOREIGN KEY (`orgStructure_id`) REFERENCES `OrgStructure` (`id`),
    CONSTRAINT `FK_rlsBalanceOfGoods_rlsNomen` FOREIGN KEY (`rlsNomen_id`) REFERENCES `rlsNomen` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;"""
    c.execute(sql)

    sql = u"""CREATE OR REPLACE VIEW `vNomen` AS
SELECT
    `rlsNomen`.`id` as `id`,
    `rlsTradeName`.`name` as `tradeName`,
    `rlsTradeName`.`localName` as `tradeLocalName`,
    `rlsNomen`.`tradeName_id` as `tradeName_id`,
    `rlsActMatters`.`name` as `actMattersName`,
    `rlsActMatters`.`localName` as `actMattersLocalName`,
    `rlsNomen`.`actMatters_id` as `actMatters_id`,
    `rlsForm`.`name` as `form`,
    `rlsPacking`.`name` as `packing`,
    `rlsFilling`.`name` as `filling`,
    `rlsNomen`.`unit_id` as `unit_id`,
    `rbUnit`.`code` as `unitCode`,
    `rbUnit`.`name` as `unitName`,
    `rlsNomen`.`dosageValue` as `dosageValue`,
    `rlsNomen`.`dosageUnit_id` as `dosageUnit_id`,
    `rbUnit2`.`code` as `dosageUnitCode`,
    `rbUnit2`.`name` as `dosageUnitName`,
    `rlsNomen`.`regDate` as `regDate`,
    `rlsNomen`.`annDate` as `annDate`,
    `rlsNomen`.`drugLifetime` as `drugLifetime`
FROM
    `rlsNomen`
LEFT JOIN `rlsTradeName` on `rlsTradeName`.`id` = `rlsNomen`.`tradeName_id`
LEFT JOIN `rlsActMatters` on `rlsActMatters`.`id` = `rlsNomen`.`actMatters_id`
LEFT JOIN `rlsForm` on `rlsForm`.`id` = `rlsNomen`.`form_id`
LEFT JOIN `rlsPacking` on `rlsPacking`.`id` = `rlsNomen`.`packing_id`
LEFT JOIN `rlsFilling` on `rlsFilling`.`id` = `rlsNomen`.`filling_id`
LEFT JOIN `rbUnit` on `rbUnit`.`id` = `rlsNomen`.`unit_id`
LEFT JOIN `rbUnit` as `rbUnit2` on `rbUnit2`.`id` = `rlsNomen`.`dosageUnit_id`"""
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass
