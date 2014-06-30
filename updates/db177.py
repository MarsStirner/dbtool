#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Передача в 1С информации об изменении сведений о госпитализации
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sqls = [
        u'''UPDATE DrugChart SET `statusDateTime` = NULL WHERE `statusDateTime` = 0''',
        u'''ALTER TABLE `DrugChart`
            CHANGE COLUMN `statusDateTime` `statusDateTime` DATETIME NULL DEFAULT NULL AFTER `status`''',
        u'''ALTER TABLE `Pharmacy` CHANGE COLUMN `status` `status` 
            ENUM('ADDED','COMPLETE','ERROR','RESEND') NULL DEFAULT 'ADDED' COMMENT 'Текущий статус сообщения' AFTER `attempts`''',
        u'''CREATE TABLE IF NOT EXISTS `Event_FinanceChanges` (
		`id` INT(11) NOT NULL AUTO_INCREMENT,
		`event_id` INT(11) NOT NULL COMMENT 'Идентификатор события {Event}',
		`modifyDatetime` DATETIME NOT NULL COMMENT 'Дата изменения записи',
		`modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор изменения записи {Person}',
		`eventTypeOld_id` INT(11) NOT NULL COMMENT 'Текущий тип события {EventType}',
		`eventTypeNew_id` INT(11) NOT NULL COMMENT 'Новый тип события {EventType}',
		`financeOld_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип финансирования {rbFinance}',
		`financeNew_id` INT(11) NULL DEFAULT NULL COMMENT 'Новый nип финансирования {rbFinance}',
		PRIMARY KEY (`id`),
		CONSTRAINT `FK_Event_FinanceChanges_Event` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`),
		CONSTRAINT `FK_Event_FinanceChanges_Person` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`),
		CONSTRAINT `FK_Event_FinanceChanges_EventType_Old` FOREIGN KEY (`eventTypeOld_id`) REFERENCES `EventType` (`id`),
		CONSTRAINT `FK_Event_FinanceChanges_EventType_New` FOREIGN KEY (`eventTypeNew_id`) REFERENCES `EventType` (`id`),
		CONSTRAINT `FK_Event_FinanceChanges_rbFinance_Old` FOREIGN KEY (`financeOld_id`) REFERENCES `rbFinance` (`id`),
		CONSTRAINT `FK_Event_FinanceChanges_rbFinance` FOREIGN KEY (`financeNew_id`) REFERENCES `rbFinance` (`id`)
		)
	COMMENT='История изменений источников финансирования'
	COLLATE='utf8_general_ci'
	ENGINE=InnoDB'''
    ]
    for sql in sqls:
        c.execute(sql)

    triggerEvent = "Update"
    tableName = "Event"
    sql = u'''CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
		IF NEW.deleted IS NOT NULL
		AND NEW.deleted != OLD.deleted THEN
			UPDATE Action
			SET deleted = NEW.deleted
			WHERE event_id = NEW.id;
		END IF;

		IF (Old.eventType_id != NEW.eventType_id)
		AND (
	        (SELECT `code`
	         FROM rbFinance
	         WHERE id =
	            (SELECT EventType.finance_id
            	     FROM EventType
	             WHERE EventType.id = NEW.eventType_id)) LIKE '4') THEN
			INSERT
			IGNORE INTO `EventsToODVD` (event_id)
			VALUES (NEW.id);
		END IF;

		IF (Old.eventType_id != NEW.eventType_id) THEN
			UPDATE `Pharmacy`
			SET `status`='RESEND'
			WHERE `Pharmacy`.actionId IN
			    (SELECT `Action`.`id`
			     FROM `Action`
			     INNER JOIN `ActionType` ON `Action`.`actionType_id` = `ActionType`.id
			     WHERE `Action`.`event_id` = NEW.`id`
			       AND (`ActionType`.flatCode LIKE 'moving'
			            OR `ActionType`.flatCode LIKE 'received')
			     ORDER BY `Action`.`createDatetime` DESC)
			  AND `status` = 'COMPLETE';
		        INSERT INTO `Event_FinanceChanges` (`event_id`, `modifyDatetime`, `modifyPerson_id`, `eventTypeOld_id`, `eventTypeNew_id`, `financeOld_id`, `financeNew_id`)
			VALUES (NEW.`id`, 
                	        NEW.`modifyDatetime`, 
	                        NEW.`modifyPerson_id`, 
        	                OLD.eventType_id, NEW.`eventType_id`, 
			        (SELECT `rbFinance`.`id` FROM `rbFinance` INNER JOIN `EventType` ON `rbFinance`.`id` = `EventType`.finance_id WHERE `EventType`.`id` = OLD.eventType_id), 
		        	(SELECT `rbFinance`.`id` FROM `rbFinance` INNER JOIN `EventType` ON `rbFinance`.`id` = `EventType`.finance_id WHERE `EventType`.`id` = NEW.eventType_id));
			END IF;
          END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)
    c.execute('''DROP TRIGGER `onUpdateEvent`''')
    c.execute(sql)

    triggerEvent = "Update"
    tableName = "Client"
    sql = u'''CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
		CALL SendClientToHS(NEW.id);
		IF NEW.firstName NOT LIKE OLD.firstName
		OR NEW.patrName NOT LIKE OLD.patrName
		OR NEW.lastName NOT LIKE OLD.lastName THEN
		    UPDATE `Pharmacy`
		    SET `status`='RESEND'
		    WHERE `Pharmacy`.actionId IN
		        (SELECT `Action`.`id`
		         FROM `Action`
		         INNER JOIN `ActionType` ON `Action`.`actionType_id` = `ActionType`.`id`
		         WHERE `Action`.`event_id` IN
		             (SELECT `Event`.`id`
		              FROM `Event`
		              WHERE `Event`.`client_id` = NEW.`id`
                		AND `Event`.`execDate` IS NULL)
			        AND (`ActionType`.flatCode LIKE 'moving'
		                OR `ActionType`.flatCode LIKE 'received')
		         ORDER BY `Action`.`createDatetime` DESC)
		      AND `status` = 'COMPLETE';
		END IF; 
	END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)
    c.execute('''DROP TRIGGER `onUpdateClient`''')
    c.execute(sql)    

def downgrade(conn):
    pass
