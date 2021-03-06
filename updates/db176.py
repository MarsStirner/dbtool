#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление таблицы для интеграции с 1С ОДВД
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sqls = [ 
        u'''CREATE TABLE IF NOT EXISTS `EventsToODVD` (
	    `event_id` INT(11) NOT NULL COMMENT 'Идентификатор события {Event.event_id}',
	    `sendTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Время следующей отсылки в 1С ОДВД',
	    `errCount` INT(11) NOT NULL DEFAULT '0' COMMENT 'Количество неудачных попыток',
	    `info` VARCHAR(1024) NULL DEFAULT NULL COMMENT 'Сообщение об ошибке',
	    PRIMARY KEY (`event_id`),
	    CONSTRAINT `FK__Event_id` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`)
          )
          COMMENT='события для передачи в 1С ОДВД'
          COLLATE='utf8_general_ci'
          ENGINE=InnoDB;''',
        u'''CREATE TABLE IF NOT EXISTS `ActionToODVD` (
	    `action_id` INT(11) NOT NULL COMMENT 'Идентификатор события {Action.id}',
	    `sendTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Время следующей отсылки в 1С ОДВД',
	    `errCount` INT(11) NOT NULL DEFAULT '0' COMMENT 'Количество неудачных попыток',
	    `info` VARCHAR(1024) NULL DEFAULT NULL COMMENT 'Сообщение об ошибке',
	    PRIMARY KEY (`action_id`),
	    CONSTRAINT `FK__Action_id` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`)
          )
          COMMENT='события для передачи в 1С ОДВД'
          COLLATE='utf8_general_ci'
          ENGINE=InnoDB;''',
    ]
    for sql in sqls:
        c.execute(sql)

    tableName = "Event"
    triggerEvent = "Insert"
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
              IF (SELECT `code` FROM rbFinance WHERE id = (SELECT EventType.finance_id FROM EventType WHERE EventType.id = NEW.eventType_id)) like '4' THEN
                 INSERT IGNORE INTO `EventsToODVD` (event_id) VALUES (NEW.id);
              END IF;          
          END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)
    c.execute(sql)

    triggerEvent = "Update"
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
              IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
                  UPDATE Action
                  SET deleted = NEW.deleted
                  WHERE event_id = NEW.id;
              END IF;
              IF (Old.eventType_id != NEW.eventType_id) AND ((SELECT `code` FROM rbFinance WHERE id = (SELECT EventType.finance_id FROM EventType WHERE EventType.id = NEW.eventType_id)) like '4') THEN
                 INSERT IGNORE INTO `EventsToODVD` (event_id) VALUES (NEW.id);
              END IF;          
          END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)
    c.execute('''DROP TRIGGER `Delete_Action_ON_UPDATE`''')
    c.execute(sql)

    tableName = "Action" 
    triggerEvent = "Insert"
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
              IF isPaidAction(NEW.id) AND NEW.status = 2 AND NEW.endDate IS NOT NULL THEN
                 INSERT IGNORE INTO `ActionToODVD` (action_id) VALUES (NEW.id);
              END IF;          
          END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)   
    c.execute(sql) 
           
    triggerEvent = "Update"
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN 
              IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
                 UPDATE ActionProperty
                 SET deleted = NEW.deleted
                 WHERE action_id = NEW.id;
              END IF;
              IF isPaidAction(NEW.id) AND (NEW.status != OLD.status OR (OLD.endDate IS NULL AND NEW.endDate IS NOT NULL)) AND (NEW.status = 2 AND NEW.endDate IS NOT NULL) THEN
                 INSERT IGNORE INTO `ActionToODVD` (action_id) VALUES (NEW.id);
              END IF;          
          END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)       
    c.execute('''DROP TRIGGER `Delete_ActionProperty_ON_UPDATE`''')
    c.execute(sql)

    funcSql = u'''CREATE FUNCTION `isPaidAction`(`action_id` INT)
                	RETURNS TINYINT
                	LANGUAGE SQL
                	NOT DETERMINISTIC
                	READS SQL DATA
                	SQL SECURITY DEFINER
                	COMMENT 'Возвращает 1 для платных действий'
                        BEGIN
                           DECLARE finaceCode VARCHAR(10);                           
                           SELECT  rbFinance.code  INTO finaceCode FROM 
                              `Action` INNER JOIN  
                              `Event` ON `Action`.event_id = `Event`.id INNER JOIN
                              `EventType` ON `Event`.eventType_id = `EventType`.id INNER JOIN
                              `rbFinance` ON `EventType`.finance_id = `rbFinance`.id
                             WHERE `Action`.id = action_id;                        
                           IF finaceCode LIKE '4' THEN 
                               RETURN 1; 
                           END IF;
                        RETURN  0;
               END'''
    c.execute(funcSql)

def downgrade(conn):
    pass
