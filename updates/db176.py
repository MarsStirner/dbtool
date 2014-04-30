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

    sql = u'''
CREATE TABLE IF NOT EXISTS `EventContractPayer` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `event_id` INT(11) NULL DEFAULT NULL COMMENT '{Event} может быть пустым, когда оплата производится до создания обращения, потом поле обновляется',
  `localContract_id` INT(11) NOT NULL COMMENT '{Event_LocalContract}',
  `lastName` VARCHAR(30) NULL DEFAULT NULL COMMENT 'Фамилия плательщика',
  `firstName` VARCHAR(30) NULL DEFAULT NULL COMMENT 'Имя плательщика',
  `patrName` VARCHAR(30) NULL DEFAULT NULL COMMENT 'Отчество плательщика',
  `birthDate` DATE NULL DEFAULT NULL COMMENT 'Дата рождения плательщика',
  `documentType_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип документа плательщика',
  `serialLeft` VARCHAR(8) NULL DEFAULT NULL COMMENT 'Серия левая часть документа плательщика',
  `serialRight` VARCHAR(8) NULL DEFAULT NULL COMMENT 'Серия правая часть документа плательщика',
  `number` varchar(16) NULL COMMENT 'Номер документа плательщика',
  `regAddress` VARCHAR(64) NULL DEFAULT NULL COMMENT 'Адрес регистрации плательщика',
  `payer_org_id` INT(11) NULL DEFAULT NULL COMMENT '{Organisation} плательщик - организация',
  PRIMARY KEY (`id`),
  INDEX `FK_ECP_Event_LocalContract_idx` (`localContract_id` ASC),
  INDEX `FK_ECP_Event_idx` (`event_id` ASC),
  INDEX `FK_ECP_Organisation_idx` (`payer_org_id` ASC),
  CONSTRAINT `FK_ECP_Event`
    FOREIGN KEY (`event_id`)
    REFERENCES `Event` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `FK_ECP_Event_LocalContract`
    FOREIGN KEY (`localContract_id`)
    REFERENCES `Event_LocalContract` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `FK_ECP_Organisation`
    FOREIGN KEY (`payer_org_id`)
    REFERENCES `Organisation` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
COMMENT = 'Сущность - плательщик платит за услуги обращения по конкретному контракту'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)

    sql = u'''ALTER TABLE `Event_Payment`
ADD COLUMN `sumDiscount` DOUBLE NOT NULL COMMENT 'Сумма скидки' AFTER `cashBox`,
ADD COLUMN `action_id` INT(11) NULL DEFAULT NULL COMMENT 'Услуга {Action}' AFTER `sumDiscount`,
ADD COLUMN `service_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип услуги {rbService}' AFTER `action_id`,
ADD COLUMN `ecp_id` INT(11) NOT NULL COMMENT '{EventContractPayer}' AFTER `service_id`
'''
    c.execute(sql)

    sql = u'''ALTER TABLE `Event_Payment`
ADD CONSTRAINT `FK_Event_Payment_ECP` FOREIGN KEY (`ecp_id`) REFERENCES `EventContractPayer` (`id`)
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