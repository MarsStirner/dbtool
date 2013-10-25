#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sqls = [
        u"""CREATE TABLE `rbFinance1C` (
	      `id` INT(11) NOT NULL AUTO_INCREMENT,
	      `code1C` VARCHAR(127) NOT NULL COMMENT 'Код',
	      `finance_id` INT(11) NOT NULL COMMENT 'тип финансирования {rbFinance}',
	      PRIMARY KEY (`id`),
	      INDEX `FK_rbFinance1C_rbFinance` (`finance_id`),
	      CONSTRAINT `FK_rbFinance1C_rbFinance` FOREIGN KEY (`finance_id`) REFERENCES `rbFinance` (`id`)
            )
            COMMENT='Коды источников финансирования в 1C'
            COLLATE='utf8_general_ci'
            ENGINE=InnoDB""",
    ]

    for sql in sqls:
        c.execute(sql)  	

    c.close()

def downgrade(conn):
    pass