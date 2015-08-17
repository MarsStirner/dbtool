#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Порция обновлений для таблиц оплаты для интеграции с 1С (иногда избыточных)
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `Event_Payment`
CHANGE COLUMN `master_id` `master_id` INT(11) NULL COMMENT 'Событие {Event}',
CHANGE COLUMN `sumDiscount` DOUBLE NOT NULL DEFAULT '0' COMMENT 'Сумма скидки'
'''
    c.execute(sql)

    sql = '''ALTER TABLE `Event_LocalContract` CHANGE COLUMN `master_id` `master_id` INT(11) NULL COMMENT 'Событие {Event}' '''
    c.execute(sql)

    sql = '''ALTER TABLE `Event_Payment`
ADD COLUMN `sumDisc` DOUBLE NOT NULL DEFAULT '0' COMMENT 'Сумма скидки',
ADD COLUMN `actionSum` DOUBLE NOT NULL DEFAULT '0' COMMENT 'Сумма платежа за услугу' '''
    c.execute(sql)

    sql = '''CREATE TABLE IF NOT EXISTS `Payment_LocalContract` (
 `id` INT(11) NOT NULL AUTO_INCREMENT,
 `localContract_id` INT(11) NOT NULL COMMENT 'Договор {Event_LocalContract}',
 `payment_id` INT(11) NOT NULL COMMENT 'Платеж {Event_Payment}',
 PRIMARY KEY (`id`),
 INDEX `localContract_id` (`localContract_id`),
 INDEX `payment_id` (`payment_id`),
 UNIQUE (`payment_id`),
 CONSTRAINT `FK_Payment_LocalContract_Event_LocalContract` FOREIGN KEY (`localContract_id`) REFERENCES `Event_LocalContract` (`id`),
 CONSTRAINT `FK_Payment_LocalContract_Event_Payment` FOREIGN KEY (`payment_id`) REFERENCES `Event_Payment` (`id`)
) COMMENT='Связь платежа с договором' COLLATE='utf8_general_ci' ENGINE=InnoDB'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass