#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление таблицы для интеграции с HealthShare
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
        CREATE TABLE IF NOT EXISTS `HSIntegration` (
	    `event_id` INT(11) NOT NULL COMMENT 'Идентификатор события',
	    `status` ENUM('NEW', 'SENDED', 'ERROR') NOT NULL DEFAULT 'NEW' COMMENT 'Статус отправки в  HS (NEW - для отправки,  SENDED - успешно передан, ERROR - ошибка при передаче)',
	    `info` VARCHAR(1024) NULL DEFAULT NULL COMMENT 'Текстовое описание статуса передачи события (сообщение об ошибке)',
	    PRIMARY KEY (`event_id`),
	    CONSTRAINT `FK__Event` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`)
        )
        COMMENT='Информация об отправке событий в HealthShare'
        COLLATE='utf8_general_ci'
       ENGINE=InnoDB;
    '''
    c.execute(sql)

    sql = u'''
        CREATE TABLE IF NOT EXISTS `PatientsToHS` (
            `client_id` INT(11) NOT NULL COMMENT 'Идентификатор события {Event.event_id}',
            `sendTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Время следующей отсылки в HealthShare',
            `errCount` INT(11) NOT NULL DEFAULT 0 COMMENT 'Количество неудачных попыток',
            `info` VARCHAR(1024) NULL DEFAULT NULL COMMENT 'Сообщение об ошибке',
	    PRIMARY KEY (`client_id`),
	   CONSTRAINT `FK__Client` FOREIGN KEY (`client_id`) REFERENCES `Client` (`id`)
        )
        COMMENT='события для передачи в HealthShare'
        COLLATE='utf8_general_ci'
       ENGINE=InnoDB;
    '''
    c.execute(sql)

    sql = u'''
    	CREATE DEFINER=%s PROCEDURE `SendClientToHS`(IN `aClient` INT)
    	BEGIN
    	   INSERT IGNORE INTO PatientsToHS SET PatientsToHS.client_id = aClient;
	END;''' %config['definer']
    c.execute(sql)

    triggerEvents = ["Insert", "Update"]
    clientInfoTables = ["ClientAddress", "ClientContact", "ClientDocument", "ClientPolicy"] 
    sqlTemplate = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
             CALL SendClientToHS(NEW.client_id);   
          END'''
    for triggerEvent in triggerEvents:
        sql = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
             CALL SendClientToHS(NEW.id);   
          END''' % (config['definer'], triggerEvent, "Client", triggerEvent, "Client")
        c.execute(sql)
        for clientInfoTable in clientInfoTables:
            c.execute(sqlTemplate % (config['definer'], triggerEvent, clientInfoTable, triggerEvent, clientInfoTable))
            
    sql = u'''ALTER TABLE `rlsNomen` ADD COLUMN `version` INT(11) NOT NULL DEFAULT '0' AFTER `disabledForPrescription`;'''
    c.execute(sql)
                       
def downgrade(conn):
    pass
