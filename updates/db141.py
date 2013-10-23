#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    alerts = (
       u'''DROP PROCEDURE `SendPrescriptionTo1C`''',
       )

    for sql in alerts:	
       c.execute(sql)

    sql = u'''CREATE DEFINER=%s PROCEDURE `SendPrescriptionTo1C`(IN `id` INT, IN is_prescription INT, IN `old_status` INT, IN `new_status` INT)
              BEGIN
                  DECLARE flag INT(1);   
                  SELECT count(*) INTO @flag FROM PrescriptionsTo1C WHERE PrescriptionsTo1C.interval_id = id;   
                  IF @flag = 0 THEN 
	              INSERT IGNORE INTO PrescriptionsTo1C (PrescriptionsTo1C.interval_id, PrescriptionsTo1C.is_prescription, PrescriptionsTo1C.old_status, PrescriptionsTo1C.new_status) 
                                    VALUES  (id, is_prescription, old_status, new_status); 
                  ELSE 
                      UPDATE `PrescriptionsTo1C` SET PrescriptionsTo1C.is_prescription = is_prescription, 
                                                     PrescriptionsTo1C.old_status = old_status,
                                                     PrescriptionsTo1C.new_status = new_status WHERE  PrescriptionsTo1C.interval_id = id;   
                  END IF; 
              END''' %config['definer']
    c.execute(sql)

    sqls = [
        u"""CREATE TABLE IF NOT EXISTS `PrescriptionSendingRes` (
	  `id` INT(11) NOT NULL AUTO_INCREMENT,
	  `uuid` VARCHAR(100) NULL DEFAULT NULL COMMENT 'идентификатор интервала 1С',
	  `version` INT(11) NULL DEFAULT NULL COMMENT 'текущая версия',
	  `interval_id` INT(11) NULL DEFAULT NULL,
	  `drugComponent_id` INT(11) NULL DEFAULT NULL,
	  PRIMARY KEY (`id`),
	  INDEX `FK_PrescriptionSendingRes_interval_id` (`interval_id`),
	  INDEX `FK_PrescriptionSendingRes_DrugComponent` (`drugComponent_id`),
	  CONSTRAINT `FK_PrescriptionSendingRes_interval_id` FOREIGN KEY (`interval_id`) REFERENCES `DrugChart` (`id`),
	  CONSTRAINT `FK_PrescriptionSendingRes_DrugComponent` FOREIGN KEY (`drugComponent_id`) REFERENCES `DrugComponent` (`id`)
        ) COLLATE='utf8_general_ci'
        ENGINE=InnoDB;""",
       u"""CREATE TABLE IF NOT EXISTS `PrescriptionsTo1C` (
	 `interval_id` INT(11) NOT NULL,
	 `errCount` INT(11) NOT NULL DEFAULT '0' COMMENT 'Количество неудачных попыток',
	 `info` VARCHAR(1024) NULL DEFAULT NULL COMMENT 'Сообщение об ошибке',
	 `is_prescription` TINYINT(1) NULL DEFAULT NULL COMMENT '1 - назначение, 0 - исполнение',
	 `new_status` INT(11) NULL DEFAULT NULL COMMENT 'Новый статус интервала',
	 `old_status` INT(11) NULL DEFAULT NULL COMMENT 'Предыдущий статус интервала',
	 `sendTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Время следующей отсылки в HealthShare',
	PRIMARY KEY (`interval_id`)
       ) COLLATE='utf8_general_ci'
       ENGINE=InnoDB""" 
    ]

    for sql in sqls:
        c.execute(sql)  	

    c.close()

def downgrade(conn):
    pass