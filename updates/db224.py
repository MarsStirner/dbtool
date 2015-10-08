#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавляет таблицу PriceList и связь ContractTariff с PriceList
'''


def upgrade(conn):
    with conn as c:
        sql = '''CREATE TABLE IF NOT EXISTS `PriceList` (
  `id` INT(11) NOT NULL,
  `deleted` TINYINT(1) NOT NULL DEFAULT '0',
  `createDatetime` DATETIME NOT NULL COMMENT 'Дата создания записи',
  `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор записи {Person}',
  `modifyDatetime` DATETIME NULL COMMENT 'Дата изменения записи',
  `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор изменения записи {Person}',
  `finance_id` INT(11) NOT NULL COMMENT 'Тип финансирование прайса.',
  PRIMARY KEY (`id`),
  INDEX `fk_PriceList_rbFinance1_idx` (`finance_id` ASC),
  CONSTRAINT `fk_PriceList_rbFinance1`
    FOREIGN KEY (`finance_id`)
    REFERENCES `rbFinance` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = 'Прайс лист услуг и их тарифов.'
'''
        c.execute(sql)
        sql = '''
        ALTER TABLE `Contract_Tariff`
ADD COLUMN `priceList_id` INT(11) NULL DEFAULT NULL,
ADD INDEX `fk_Contract_Tariff_PriceList1_idx` (`PriceList_id` ASC),
ADD CONSTRAINT `fk_Contract_Tariff_PriceList1`
    FOREIGN KEY (`priceList_id`)
    REFERENCES `PriceList` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;'''
        c.execute(sql)


def downgrade(conn):
    with conn as c:
        sql = '''
        ALTER TABLE `Contract_Tariff`
DROP FOREIGN KEY `fk_Contract_Tariff_PriceList1`;
ALTER TABLE `Contract_Tariff`
DROP COLUMN `priceList_id`,
DROP INDEX `fk_Contract_Tariff_PriceList1_idx` ;'''
        c.execute(sql)
        sql = '''DROP TABLE `PriceList`;'''
        c.execute(sql)
