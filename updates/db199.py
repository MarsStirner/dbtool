#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Нотификация ядра при создании и редактировании новых действий заданного типа 
- Обновление синхронизации редактирования документов (ReleaseAppLock)
'''
def upgrade(conn):
    global config
    c = conn.cursor()


    sql = u'''ALTER TABLE `NotificationAction`
	ADD COLUMN `method` ENUM('POST','PUT','GET','DELETE') NOT NULL 
        COMMENT "HTTP метод для уведомления (POST - создание; PUT - редактирование)"
    '''

    c.execute(sql)

    sql = u'''
	CREATE DEFINER=%s TRIGGER `onInsertAction` AFTER INSERT ON `Action` FOR EACH ROW BEGIN
	  DECLARE flatCode VARCHAR(64);
	  SELECT `ActionType`.`flatCode` INTO flatCode FROM `ActionType` WHERE `ActionType`.`id` = NEW.`actionType_id`;
	  IF flatCode LIKE "received"
	     OR flatCode LIKE "del_received"
	     OR flatCode LIKE "moving"
	     OR flatCode LIKE "del_moving"
	     OR flatCode LIKE "leaved" THEN
	    INSERT IGNORE INTO `Pharmacy` (actionId, flatCode) VALUES (NEW.id, flatCode);
	  END IF;
	  IF NEW.actionType_id IN (SELECT NotificationActionType.actionType_id FROM NotificationActionType) THEN
	    INSERT IGNORE INTO `NotificationAction` (action_id, method) VALUES (NEW.id, 'POST');
	  END IF;
	  IF isPaidAction(NEW.id) AND NEW.status = 2 AND NEW.endDate IS NOT NULL THEN
	    INSERT IGNORE INTO `ActionToODVD` (action_id) VALUES (NEW.id);
	  END IF;
	END'''%(config['definer'])

    c.execute(u'''DROP TRIGGER `onInsertAction`''')
    c.execute(sql)

    triggerEvent = "Update"
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `onUpdateAction` AFTER UPDATE ON `Action` FOR EACH ROW BEGIN 
              IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
                 UPDATE ActionProperty
                 SET deleted = NEW.deleted
                 WHERE action_id = NEW.id;
              END IF;
              IF isPaidAction(NEW.id) AND (NEW.status != OLD.status OR (OLD.endDate IS NULL AND NEW.endDate IS NOT NULL)) AND (NEW.status = 2 AND NEW.endDate IS NOT NULL) THEN
                 INSERT IGNORE INTO `ActionToODVD` (action_id) VALUES (NEW.id);
              END IF;          
     	      IF NEW.actionType_id IN (SELECT NotificationActionType.actionType_id FROM NotificationActionType) THEN
	         INSERT IGNORE INTO `NotificationAction` (action_id, method) VALUES (NEW.id, 'PUT');
  	      END IF;
          END'''%(config['definer'])       
    c.execute('''DROP TRIGGER `onUpdateAction`''')
    c.execute(sql)

    proc = u''' CREATE DEFINER=%s PROCEDURE `%s`(IN `aLockId` BIGINT)
		BEGIN
		    DECLARE vLockName VARCHAR(64) CHARSET utf8;
		    SET vLockName = CONCAT(DATABASE(), '_AppLock');
		    IF GET_LOCK(vLockName, 2) THEN
		        DELETE `AppLock_Detail` FROM `AppLock_Detail` INNER JOIN `AppLock` ON `AppLock`.`id` = `AppLock_Detail`.`master_id` WHERE `AppLock`.`id` = aLockId;
		        DELETE FROM AppLock WHERE AppLock.id = aLockId;
		        CALL clearAppLock;        
		        DO RELEASE_LOCK(vLockName);
		    END IF;
		END'''

    name = u'''ReleaseAppLock'''
    c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
    c.execute(proc%(config['definer'],name))                      

def downgrade(conn):
    pass # не требуется, т.к. возможна потеря данных
