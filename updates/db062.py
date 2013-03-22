#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- Потерянные столбцы из функционала 6098
- Таблица для настройки проверяемых действий при закрытии обращений
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `Action` ADD `pacientInQueueType` TINYINT DEFAULT 0 AFTER `hospitalUidFrom`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise

    sql = u'''
ALTER TABLE `Person` ADD `maxOverQueue` TINYINT DEFAULT 0 AFTER `typeTimeLinePerson`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise
    
    sql = u'''
CREATE TABLE `ActionType_EventType_check` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `actionType_id` int(11) NOT NULL,
  `eventType_id` int(11) NOT NULL,
  `related_actionType_id` int(11) DEFAULT NULL,
  `relationType` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_actionType_id` (`actionType_id`),
  KEY `fk_eventType_id` (`eventType_id`),
  KEY `fk_related_ActionType_id` (`related_actionType_id`),
  CONSTRAINT `fk_actionType_id` FOREIGN KEY (`actionType_id`) REFERENCES `ActionType` (`id`),
  CONSTRAINT `fk_eventType_id` FOREIGN KEY (`eventType_id`) REFERENCES `EventType` (`id`),
  CONSTRAINT `fk_related_ActionType_id` FOREIGN KEY (`related_actionType_id`) REFERENCES `ActionType` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='Проверка на наличие типа действия для конкретных типов обращений!'
'''
    c.execute(sql) 

def downgrade(conn):
    pass
