#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import uuid
import sys
from _mysql_exceptions import IntegrityError

__doc__ = '''\
- Добавление уникальных идентификаторов UUID для таблиц Action, Client, Event, OrgStructure
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
CREATE TABLE `UUID` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`uuid` varchar(100) NOT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `uuid` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Action` ADD COLUMN `uuid_id` INT(11) NOT NULL DEFAULT 0  AFTER `parentAction_id` 
, ADD INDEX `uuid_id` (`uuid_id` ASC) ;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Client` ADD COLUMN `uuid_id` INT(11) NOT NULL DEFAULT 0  AFTER `birthPlace` 
, ADD INDEX `uuid_id` (`uuid_id` ASC) ;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Event` ADD COLUMN `uuid_id` INT(11) NOT NULL DEFAULT 0  AFTER `orgStructure_id` 
, ADD INDEX `uuid_id` (`uuid_id` ASC) ;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `OrgStructure` ADD COLUMN `uuid_id` INT(11) NOT NULL DEFAULT 0  AFTER `inheritGaps` 
, ADD INDEX `uuid_id` (`uuid_id` ASC) ;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `Pharmacy` (
  `actionId` int(11) NOT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  `flatCode` varchar(255) DEFAULT NULL,
  `result` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`actionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf-8;
'''
    c.execute(sql)
    
    updateExistingRecords(conn)
    

def updateExistingRecords(conn):
    c = conn.cursor()    
    
    sql = u'''SELECT id from Action order by id'''
    c.execute(sql)
    actionIds = [id_[0] for id_ in c.fetchall()]
    numActionRecords = len(actionIds)
    
    sql = u'''SELECT id from Client order by id'''
    c.execute(sql)
    clientIds = [id_[0] for id_ in c.fetchall()]
    numClientRecords = len(clientIds)
    
    sql = u'''SELECT id from Event order by id'''
    c.execute(sql)
    eventIds = [id_[0] for id_ in c.fetchall()]
    numEventRecords = len(eventIds)
    
    sql = u'''SELECT id from OrgStructure order by id'''
    c.execute(sql)
    orgStructureIds = [id_[0] for id_ in c.fetchall()]
    numOrgStructureRecords = len(orgStructureIds)
    
    numRecords = sum([numActionRecords, numClientRecords, numEventRecords, numOrgStructureRecords])    
    print("TOTAL: " + str(numRecords) + '\n', end='')
    sys.stdout.flush()
    
    tableRanges = {'Action': iter(actionIds), 'Client': iter(clientIds),
        'Event': iter(eventIds), 'OrgStructure': iter(orgStructureIds)}
    
    i = 1
    ii = 0 # индекс в tableRanges
    
    while i <= numRecords:
        try:
            curTable = sorted(tableRanges.keys())[ii]
            dst_id = tableRanges[curTable].next()
        except StopIteration:
            ii += 1
            continue
        
        try:
            sql = '''INSERT INTO `UUID` (`uuid`) VALUES ("%s")''' % uuid.uuid4()
            c.execute(sql)
            last_id = conn.insert_id()
            sql = '''UPDATE `%s` SET uuid_id=%s where id=%s''' % (curTable, last_id, dst_id)
            c.execute(sql)
            i += 1
            if i % 100 == 0:
                print(".", end='')
                sys.stdout.flush()
            if i % 1000 == 0:
                print(str(i), end='')
                sys.stdout.flush()
            
        except IntegrityError:
            print('Opa, uuid dublicate!', end='')
    
    
    
    
    
    
    

def downgrade(conn):
    pass
