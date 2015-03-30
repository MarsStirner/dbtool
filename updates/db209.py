#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление табл. Event_ClientRelation
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
    CREATE TABLE IF NOT EXISTS `Event_ClientRelation` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`event_id` INT(11) NOT NULL COMMENT 'Event {Event}',
	`clientRelation_id` INT(11) NOT NULL COMMENT 'ClientRelation {ClientRelation}',
        `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Отметка удаления записи',
        `note` TEXT NULL DEFAULT NULL COMMENT 'Примечания',
	PRIMARY KEY (`id`),
	INDEX `event_id` (`event_id`),
	INDEX `person_id` (`clientRelation_id`),
	CONSTRAINT `FK_Event_ClientRelation_ClientRelation` FOREIGN KEY (`clientRelation_id`) REFERENCES `ClientRelation` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT `FK_Event_ClientRelation_Event` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
    )
    COMMENT='Event client relation List'
    COLLATE='utf8_general_ci'
    ENGINE=InnoDB    '''
    c.execute(sql)


def downgrade(conn):
    pass