#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Исправления для таблицы AppLock и связанных процедур, благодаря чему
решается проблема возникновения дедлоков при блокирвоках.
'''


def upgrade(conn):
    global config        
    c = conn.cursor()
    
    sql = u'''
DROP PROCEDURE IF EXISTS `ProlongAppLock`;
'''
    c.execute(sql)
    
    sql = u'''
CREATE DEFINER=%s PROCEDURE `ProlongAppLock`(IN aLockId BIGINT)
BEGIN
    UPDATE AppLock SET retTime = NOW() WHERE AppLock.connectionId = CONNECTION_ID() AND AppLock.id = aLockId;
END;
''' % config['definer']
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `AppLock` ENGINE = InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
CREATE INDEX `AppLock_connectionId` on `AppLock` (`connectionId`);
'''
    try:
        c.execute(sql)
    except:
        pass
            
    
def downgrade(conn):
    pass