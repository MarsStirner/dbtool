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

    sql = u'''
ALTER TABLE `Event_Payment`
ADD COLUMN `sumDiscount` DOUBLE NOT NULL COMMENT 'Сумма скидки' AFTER `cashBox`,
ADD COLUMN `action_id` INT(11) NULL DEFAULT NULL COMMENT 'Услуга {Action}' AFTER `sumDiscount`,
ADD COLUMN `service_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип услуги {rbService}' AFTER `action_id`,
ADD COLUMN `event_localContract_id` INT(11) NULL DEFAULT NULL COMMENT '{Event_LocalContract}' AFTER `service_id`,
ADD COLUMN `lastName` VARCHAR(30) NULL DEFAULT NULL COMMENT 'Фамилия плательщика' AFTER `event_localContract_id`,
ADD COLUMN `firstName` VARCHAR(30) NULL DEFAULT NULL COMMENT 'Имя плательщика' AFTER `lastName`,
ADD COLUMN `patrName` VARCHAR(30) NULL DEFAULT NULL COMMENT 'Отчество плательщика' AFTER `firstName`,
ADD COLUMN `birthDate` DATE NULL DEFAULT NULL COMMENT 'Дата рождения плательщика' AFTER `patrName`,
ADD COLUMN `documentType_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип документа плательщика' AFTER `birthDate`,
ADD COLUMN `serialLeft` VARCHAR(8) NULL DEFAULT NULL COMMENT 'Серия левая часть документа плательщика' AFTER `documentType_id`,
ADD COLUMN `serialRight` VARCHAR(8) NULL DEFAULT NULL COMMENT 'Серия правая часть документа плательщика' AFTER `serialLeft`,
ADD COLUMN `regAddress` VARCHAR(64) NULL DEFAULT NULL COMMENT 'Адрес регистрации плательщика' AFTER `serialRight`
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `Event_Payment`
ADD CONSTRAINT `FK_Event_Payment_Event_LocalContract` FOREIGN KEY (`event_localContract_id`) REFERENCES `Event_LocalContract` (`id`);
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