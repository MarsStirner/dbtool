#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Интеграция с 1С ОДВД. Модификация таблицы Event_Payment
'''


def upgrade(conn):
    global config    
    c = conn.cursor()    
    sqls = [
          u'''ALTER TABLE `Event_Payment` CHANGE COLUMN `master_id` `master_id` INT(11) NULL COMMENT 'Событие {Event}' ''',
          u'''ALTER TABLE `Event_LocalContract` CHANGE COLUMN `master_id` `master_id` INT(11) NULL COMMENT 'Событие {Event}' ''',
          u'''ALTER TABLE `Event_Payment` ADD COLUMN `sumDisc` DOUBLE NOT NULL COMMENT 'Сумма скидки' ''',
          u'''CREATE TABLE IF NOT EXISTS `Payment_LocalContract` (
        	`id` INT(11) NOT NULL AUTO_INCREMENT,
	        `localContract_id` INT(11) NOT NULL COMMENT 'Договор {Event_LocalContract}',
	        `payment_id` INT(11) NOT NULL COMMENT 'Платеж {Event_Payment}',
	        PRIMARY KEY (`id`),
	        INDEX `localContract_id` (`localContract_id`),
	        INDEX `payment_id` (`payment_id`),
	        UNIQUE (`payment_id`),
                CONSTRAINT `FK_Payment_LocalContract_Event_LocalContract` FOREIGN KEY (`localContract_id`) REFERENCES `Event_LocalContract` (`id`),
            	CONSTRAINT `FK_Payment_LocalContract_Event_Payment` FOREIGN KEY (`payment_id`) REFERENCES `Event_Payment` (`id`)
             ) COMMENT='Связь платежа с договором'
             COLLATE='utf8_general_ci'
             ENGINE=InnoDB''']
    for sql in sqls:
        c.execute(sql)

def downgrade(conn):
    pass
