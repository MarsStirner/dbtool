#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Передача в 1С информации об изменении сведений о госпитализации
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
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
			            OR `ActionType`.flatCode LIKE 'received'
			 	    OR `ActionType`.flatCode LIKE 'leaved' 
				    OR `ActionType`.flatCode LIKE 'del_received'
				    OR `ActionType`.flatCode LIKE 'del_moving')
			     ORDER BY `Action`.`createDatetime` DESC)
			  AND `status` = 'COMPLETE'
                        ORDER BY `Pharmacy`.actionId DESC 
			LIMIT 1;
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

def downgrade(conn):
    pass
