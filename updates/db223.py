#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Привязка источника финансирования к расписанию (Schedule)
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `Schedule`
ADD COLUMN `finance_id` INT(11) NULL DEFAULT NULL AFTER `receptionType_id`,
ADD INDEX `fk_finance_ibfk_3_idx` (`finance_id` ASC);
ALTER TABLE `Schedule`
ADD CONSTRAINT `fk_finance_ibfk_3`
  FOREIGN KEY (`finance_id`)
  REFERENCES `rbFinance` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;'''

    c.execute(sql)
    c.close()


def downgrade(conn):
    c = conn.cursor()
    sql = '''ALTER TABLE `Schedule`
DROP FOREIGN KEY `fk_finance_ibfk_3`;
ALTER TABLE `Schedule`
DROP COLUMN `finance_id`,
DROP INDEX `fk_finance_ibfk_3_idx` ;'''
    c.execute(sql)
    c.close()
