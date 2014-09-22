#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
fix: Обновление синхронизации редактирования документов (AppLock)
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    proc = u''' CREATE DEFINER=%s PROCEDURE `%s`()
                LANGUAGE SQL
                DETERMINISTIC
                MODIFIES SQL DATA
                SQL SECURITY DEFINER
	        COMMENT 'Удаление протухших записей в таблицах AppLock_Detail и AppLock'
	        BEGIN
                   DECLARE  timeOutMin INT;
                   SET timeOutMin = 10;
	           DELETE FROM `AppLock` WHERE TIMESTAMPDIFF(MINUTE,`AppLock`.retTime, NOW()) >= timeOutMin;
                   DELETE `AppLock_Detail` FROM `AppLock_Detail` WHERE `AppLock_Detail`.master_id NOT IN (SELECT `AppLock`.id FROM `AppLock`); 
                END'''

    name = u'''clearAppLock'''
    c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
    c.execute(proc%(config['definer'],name))                      

    proc = u''' CREATE DEFINER=%s PROCEDURE `%s`(IN `aTableName` VARCHAR(64) CHARSET utf8, IN `aRecordId` INT, IN `aRecordIndex` INT, IN `aPersonId` INT, IN `aAddress` VARCHAR(255) CHARSET utf8, OUT `aResult` VARCHAR(255) CHARSET utf8)
                LANGUAGE SQL
                DETERMINISTIC
                MODIFIES SQL DATA
                SQL SECURITY DEFINER
		BEGIN
		    DECLARE vLockId INT DEFAULT NULL;
		    DECLARE vLockName VARCHAR(64) CHARSET utf8;
		    DECLARE vTimeout INT DEFAULT 300;
		    SET vLockName = CONCAT(DATABASE(), '_AppLock');
		    IF GET_LOCK(vLockName, 1) THEN
			CALL clearAppLock;
		        DELETE FROM _AppLock_Depends WHERE 1;
		        CALL getAppLock_storeDepend(aTableName, aRecordId, aRecordIndex);
		        SELECT DISTINCT AppLock.id INTO vLockId
		            FROM AppLock
		            INNER JOIN AppLock_Detail ON AppLock_Detail.master_id = AppLock.id
		            INNER JOIN _AppLock_Depends ON _AppLock_Depends.tableName = AppLock_Detail.tableName AND _AppLock_Depends.recordId = AppLock_Detail.recordId AND AppLock_Detail.recordIndex = aRecordIndex
		            WHERE AppLock.connectionId != CONNECTION_ID() AND TIMESTAMPDIFF(SECOND, AppLock.retTime, NOW())<=vTimeout
		            LIMIT 1;
		        IF vLockId IS NOT NULL THEN
		            SET aResult = CONCAT('0 ', vLockId);
		        ELSE
		            INSERT INTO AppLock (lockTime, retTime, connectionId, person_id, addr)
		                VALUES ( NOW(), NOW(), CONNECTION_ID(), aPersonId, aAddress );
		            SET vLockId = LAST_INSERT_ID();
		            INSERT INTO AppLock_Detail (master_id, tableName, recordId, recordIndex)
		                SELECT vLockId, tableName, recordId, recordIndex FROM _AppLock_Depends;
		            SET aResult = CONCAT('1 ', vLockId);
		        END IF;
	        	DO RELEASE_LOCK(vLockName);
		    ELSE
		        SET aResult = '';
		    END IF;
		END'''

    name = u'''getAppLock_'''
    c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
    c.execute(proc%(config['definer'],name))                      

    proc = u''' CREATE DEFINER=%s PROCEDURE `%s`(IN `aLockId` BIGINT)
		BEGIN
		    DECLARE vLockName VARCHAR(64) CHARSET utf8;
		    SET vLockName = CONCAT(DATABASE(), '_AppLock');
		    IF GET_LOCK(vLockName, 2) THEN
		        DELETE `AppLock_Detail` FROM `AppLock_Detail` INNER JOIN `AppLock` ON `AppLock`.`id` = `AppLock_Detail`.`master_id` WHERE `AppLock`.`id` = aLockId AND `AppLock`.`connectionId` = CONNECTION_ID();
		        DELETE FROM AppLock WHERE AppLock.id = aLockId AND AppLock.connectionId = CONNECTION_ID();
		        CALL clearAppLock;        
		        DO RELEASE_LOCK(vLockName);
		    END IF;
		END'''

    name = u'''ReleaseAppLock'''
    c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
    c.execute(proc%(config['definer'],name))                      
    c.execute('''CALL clearAppLock''')                      
    c.close()

def downgrade(conn):
    pass