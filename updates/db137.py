#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback


__doc__ = '''
Изменения для обновления остатков
'''

sqls = [
    u"""ALTER TABLE `TakenTissueJournal` ADD INDEX `period_barcode` (`period`, `barcode`);""",

    u"""DROP PROCEDURE IF EXISTS `getAppLock_`;""",

    u"""CREATE DEFINER=%s PROCEDURE `getAppLock_`(IN `aTableName` VARCHAR(64) CHARSET utf8, IN `aRecordId` INT, IN `aRecordIndex` INT, IN `aPersonId` INT, IN `aAddress` VARCHAR(255) CHARSET utf8, OUT `aResult` VARCHAR(255) CHARSET utf8)
    LANGUAGE SQL
    DETERMINISTIC
    READS SQL DATA
    SQL SECURITY DEFINER
    COMMENT ''
BEGIN
    DECLARE vLockId INT DEFAULT NULL;
    DECLARE vLockName VARCHAR(64) CHARSET utf8;
    DECLARE vTimeout INT DEFAULT 300;
    SET vLockName = CONCAT(DATABASE(), '_AppLock');
    IF GET_LOCK(vLockName, 1) THEN
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
END
""" % config['definer'],
]


def upgrade(conn):
    global config
    c = conn.cursor()

    for query in sqls:
        try:
            c.execute(query)
        except:
            traceback.print_exc()

    c.close()


def downgrade(conn):
    pass