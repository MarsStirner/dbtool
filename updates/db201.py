#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Лист назначений:инфузионная терапия. Добавление более одного интервала назначения
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''CREATE TABLE `DrugIntervalCompParam` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`drugChart_id` INT(11) NOT NULL,
	`drugComponent_id` INT(11) NOT NULL,
	`dose` FLOAT NULL DEFAULT NULL,
	`voa` FLOAT NULL DEFAULT NULL,
	`moa_id` INT(11) NULL DEFAULT NULL,
	PRIMARY KEY (`id`),
	INDEX `FK_DrugIntervalCompParam_DrugChart` (`drugChart_id`),
	INDEX `FK_DrugIntervalCompParam_DrugComponent` (`drugComponent_id`),
	INDEX `FK_DrugIntervalCompParam_rbMethodOfAdministration` (`moa_id`),
	CONSTRAINT `FK_DrugIntervalCompParam_rbMethodOfAdministration` FOREIGN KEY (`moa_id`) REFERENCES `rbMethodOfAdministration` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT `FK_DrugIntervalCompParam_DrugChart` FOREIGN KEY (`drugChart_id`) REFERENCES `DrugChart` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT `FK_DrugIntervalCompParam_DrugComponent` FOREIGN KEY (`drugComponent_id`) REFERENCES `DrugComponent` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
	)
        COLLATE='utf8_general_ci'
        ENGINE=InnoDB'''

    c.execute(sql)

def downgrade(conn):
    sql = u'''
        DROP TABLE IF EXISTS `DrugIntervalCompParam`;
    '''
    c.execute(sql)

    pass
