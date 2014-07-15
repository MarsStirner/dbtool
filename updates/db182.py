#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Доработка интеграции с 1С Аптека
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    c.execute('''DROP TRIGGER `onInsertAction`''')
    tableName = "Action" 
    triggerEvent = "Insert"
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
              DECLARE flatCode VARCHAR(64);
              IF isPaidAction(NEW.id) AND NEW.status = 2 AND NEW.endDate IS NOT NULL THEN
                 INSERT IGNORE INTO `ActionToODVD` (action_id) VALUES (NEW.id);
              END IF;   
				  SELECT `ActionType`.`flatCode` INTO flatCode FROM `ActionType` WHERE `ActionType`.`id` = NEW.`actionType_id`;
				  IF flatCode LIKE "received" 
				     OR flatCode LIKE "del_received" 
					  OR flatCode LIKE "moving" 
					  OR flatCode LIKE "del_moving"
					  OR flatCode LIKE "leaved" THEN 
					  INSERT IGNORE INTO `Pharmacy` (actionId, flatCode) VALUES (NEW.id, flatCode);
				  END IF;	   
              END'''%(config['definer'], triggerEvent, tableName, triggerEvent, tableName)   
    c.execute(sql) 
           
def downgrade(conn):
    pass
