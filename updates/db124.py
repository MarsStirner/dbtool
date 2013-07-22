#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from _mysql import OperationalError

__doc__ = '''\
Увеличение количества вводимых символов
'''

sqls = [
    u"DROP TABLE rlsATCGroup;",
    u"DROP TABLE rlsATCGroupExt;",
    u"DROP TABLE rlsATCGroupToCode;",
    u"DROP TABLE rlsDosage;",
    u"DROP TABLE rlsINPNameToCode;",
    u"DROP TABLE rlsMKBToCode;",
    u"DROP TABLE rlsNomenRaw;",
    u"DROP TABLE rlsPharmGroup;",
    u"DROP TABLE rlsPharmGroupToCode;",
    u"DROP TABLE rlsTradeNameToCode;",
    u"DROP VIEW vNomen",
    u"DROP TABLE rlsNomen",
    u"ALTER TABLE rlsFilling DROP COLUMN `disabledForPrescription`",
    u"""ALTER TABLE rlsINPName
        DROP COLUMN `rawName`,
        CHANGE COLUMN `latName` `name` VARCHAR(255) NULL DEFAULT NULL AFTER `id`,
        CHANGE COLUMN `name` `localName` VARCHAR(255) NULL DEFAULT NULL AFTER `name`;""",
    u"""ALTER TABLE `rlsTradeName`
        CHANGE COLUMN `latName` `name` VARCHAR(255) NULL DEFAULT NULL AFTER `id`,
        CHANGE COLUMN `name` `localName` VARCHAR(255) NULL DEFAULT NULL AFTER `name`;""",
    u"""CREATE TABLE `rlsNomen` (
        `id` INT(11) NOT NULL COMMENT 'РЛС-овский код',
        `version` INT(11) NOT NULL DEFAULT '0' COMMENT 'Версия',
        `tradeName_id` INT(11) NULL DEFAULT NULL COMMENT 'Торговое название {rlsTradeName}',
        `inpName_id` INT(11) NULL DEFAULT NULL COMMENT 'МНН/НДВ {rlsINPName}',
        `form_id` INT(11) NULL DEFAULT NULL COMMENT 'Лекарственная форма {rlsForm}',
        `packing_id` INT(11) NULL DEFAULT NULL COMMENT 'Упаковка {rlsPacking}',
        `filling_id` INT(11) NULL DEFAULT NULL COMMENT 'Фасовка {rlsFilling}',
        `unit_id` INT(11) NULL DEFAULT NULL COMMENT 'Ед.Изм. препарата {rbUnit}',
        `dosageValue` INT(11) NULL DEFAULT NULL COMMENT 'Доза в единице лекарственной формы {rlsDosage}',
        `dosageUnit_id` INT(11) NULL DEFAULT NULL COMMENT 'Ед.Изм. дозировки препарата {rbUnit}',
        `regDate` DATE NULL DEFAULT NULL COMMENT 'Дата регистрации',
        `annDate` DATE NULL DEFAULT NULL COMMENT 'Дата отмены',
        PRIMARY KEY (`id`, `version`),
        INDEX `tradeName_id` (`tradeName_id`),
        INDEX `inpName_id` (`inpName_id`),
        INDEX `FK_rlsNomen_rlsForm` (`form_id`),
        INDEX `FK_rlsNomen_rlsPacking` (`packing_id`),
        INDEX `FK_rlsNomen_rlsFilling` (`filling_id`),
        INDEX `FK_rlsNomen_rbUnit` (`unit_id`),
        INDEX `FK_rlsNomen_rbUnit_2` (`dosageUnit_id`),
        CONSTRAINT `FK_rlsNomen_rbUnit` FOREIGN KEY (`unit_id`) REFERENCES `rbUnit` (`id`),
        CONSTRAINT `FK_rlsNomen_rbUnit_2` FOREIGN KEY (`dosageUnit_id`) REFERENCES `rbUnit` (`id`),
        CONSTRAINT `FK_rlsNomen_rlsFilling` FOREIGN KEY (`filling_id`) REFERENCES `rlsFilling` (`id`),
        CONSTRAINT `FK_rlsNomen_rlsForm` FOREIGN KEY (`form_id`) REFERENCES `rlsForm` (`id`),
        CONSTRAINT `FK_rlsNomen_rlsINPName` FOREIGN KEY (`inpName_id`) REFERENCES `rlsINPName` (`id`),
        CONSTRAINT `FK_rlsNomen_rlsPacking` FOREIGN KEY (`packing_id`) REFERENCES `rlsPacking` (`id`),
        CONSTRAINT `FK_rlsNomen_rlsTradeName` FOREIGN KEY (`tradeName_id`) REFERENCES `rlsTradeName` (`id`)
    )
    COLLATE='utf8_general_ci'
    ENGINE=InnoDB;""",
    u"ALTER TABLE rlsPacking DROP COLUMN `disabledForPrescription`",
    u"""CREATE TABLE `rlsBalanceOfGoods` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `rlsNomen_id` INT(11) NOT NULL,
        `rlsNomen_version` INT(11) NOT NULL,
        `store_id` INT(11) NULL,
        `value` DOUBLE NOT NULL,
        `bestBefore` DATE NOT NULL,
        `disabled` TINYINT(4) NOT NULL DEFAULT '0',
        PRIMARY KEY (`id`),
        CONSTRAINT `FK_rlsBalanceOfGoods_rlsNomen` FOREIGN KEY (`rlsNomen_id`, `rlsNomen_version`) REFERENCES `rlsNomen` (`id`, `version`)
    )
    COLLATE='utf8_general_ci'
    ENGINE=InnoDB;
    """,
    u"""CREATE VIEW `vNomen` AS
    SELECT
        `rlsNomen`.`id` as `id`,
        `rlsNomen`.`version` as `version`,
        `rlsTradeName`.`name` as `tradeName`,
        `rlsTradeName`.`localName` as `tradeLocalname`,
        `rlsINPName`.`name` as `inpName`,
        `rlsINPName`.`localName` as `inpLocalName`,
        `rlsForm`.`name` as `form`,
        `rlsPacking`.`name` as `packing`,
        `rlsFilling`.`name` as `filling`,
        `rbUnit`.`code` as `unitCode`,
        `rbUnit`.`name` as `unitName`,
        `rlsNomen`.`dosageValue` as `dosageValue`,
        `rbUnit2`.`code` as `dosageUnitCode`,
        `rbUnit2`.`name` as `dosageUnitName`,
        `rlsNomen`.`regDate` as `regDate`,
        `rlsNomen`.`annDate` as `annDate`
    FROM
        `rlsNomen`
    LEFT JOIN `rlsTradeName` on `rlsTradeName`.`id` = `rlsNomen`.`tradeName_id`
    LEFT JOIN `rlsINPName` on `rlsINPName`.`id` = `rlsNomen`.`inpName_id`
    LEFT JOIN `rlsForm` on `rlsForm`.`id` = `rlsNomen`.`form_id`
    LEFT JOIN `rlsPacking` on `rlsPacking`.`id` = `rlsNomen`.`packing_id`
    LEFT JOIN `rlsFilling` on `rlsFilling`.`id` = `rlsNomen`.`filling_id`
    LEFT JOIN `rbUnit` on `rbUnit`.`id` = `rlsNomen`.`unit_id`
    LEFT JOIN `rbUnit` as `rbUnit2` on `rbUnit2`.`id` = `rlsNomen`.`dosageUnit_id`""",
]


def upgrade(conn):
    global config
    c = conn.cursor()

    for sql in sqls:
        try:
            c.execute(sql)
        except OperationalError, e:
            print(e)

    c.close()


def downgrade(conn):
    pass