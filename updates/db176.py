#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение таблиц оплаты
'''


def upgrade(conn):
    c = conn.cursor()

    sql = u'''ALTER TABLE `Event_LocalContract` CHANGE COLUMN `master_id` `master_id` INT(11) NULL COMMENT 'Событие {Event}' '''
    c.execute(sql)

    sql = '''ALTER TABLE `Event_Payment` CHANGE COLUMN `master_id` `master_id` INT(11) NULL COMMENT 'Событие {Event}' '''
    c.execute(sql)

    sql = u'''ALTER TABLE `Event_Payment`
ADD COLUMN `sumDiscount` DOUBLE NOT NULL COMMENT 'Сумма скидки' AFTER `cashBox`,
ADD COLUMN `action_id` INT(11) NULL DEFAULT NULL COMMENT 'Услуга {Action}' AFTER `sumDiscount`,
ADD COLUMN `service_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип услуги {rbService}' AFTER `action_id`,
ADD COLUMN `localContract_id` INT(11) NOT NULL COMMENT '{Event_LocalContract}' AFTER `service_id`
'''
    c.execute(sql)

    sql = u'''ALTER TABLE `Event_Payment`
ADD CONSTRAINT `FK_Event_Payment_ELC` FOREIGN KEY (`localContract_id`) REFERENCES `Event_LocalContract` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
'''
    c.execute(sql)

    sql = u'''ALTER TABLE `Event_Payment`
ADD CONSTRAINT `FK_Event_Payment_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
'''
    c.execute(sql)

    sql = u'''ALTER TABLE `Event_Payment`
ADD CONSTRAINT `FK_Event_Payment_rbService` FOREIGN KEY (`service_id`) REFERENCES `rbService` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `Event`
ADD COLUMN `localContract_id` INT(11) NULL DEFAULT NULL AFTER `lpu_transfer`
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `Event`
ADD CONSTRAINT `FK_Event_Event_LocalContract` FOREIGN KEY (`localContract_id`) REFERENCES `Event_LocalContract` (`id`)
  ON DELETE RESTRICT
  ON UPDATE CASCADE;
'''
    c.execute(sql)


def downgrade(conn):
    pass