#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
DROP TRIGGER IF EXISTS `INCREMENT_Event_RECORD_VERSION_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
DROP TRIGGER IF EXISTS `Delete_Action_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `INCREMENT_Event_RECORD_VERSION_ON_UPDATE`
BEFORE UPDATE ON `Event`
FOR EACH ROW
BEGIN
    SET NEW.version = OLD.version + 1;
END;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `Delete_Action_ON_UPDATE`
AFTER UPDATE ON `Event`
FOR EACH ROW
BEGIN
    IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
        UPDATE Action
        SET deleted = NEW.deleted
        WHERE event_id = NEW.id;
    END IF;

END;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
DROP TRIGGER IF EXISTS `INCREMENT_Action_RECORD_VERSION_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
DROP TRIGGER IF EXISTS `Delete_ActionProperty_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `INCREMENT_Action_RECORD_VERSION_ON_UPDATE`
BEFORE UPDATE ON `Action`
FOR EACH ROW
BEGIN
    SET NEW.version = OLD.version + 1;
END;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `Delete_ActionProperty_ON_UPDATE`
AFTER UPDATE ON `Action`
FOR EACH ROW
BEGIN
    IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
        UPDATE ActionProperty
        SET deleted = NEW.deleted
        WHERE action_id = NEW.id;
    END IF;
END;
''' % (config['username'], config['host'])

    c.execute(sql)
        

def downgrade(conn):
    pass
