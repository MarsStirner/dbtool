#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление kell-антиген и фенотипа крови 
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
    CREATE TABLE IF NOT EXISTS `rbBloodPhenotype` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`code` VARCHAR(32) NOT NULL COMMENT 'код фенотипа крови',
	`name` VARCHAR(64) NOT NULL COMMENT 'название фенотипа крови',
	PRIMARY KEY (`id`)
    )
    COMMENT='Фенотип крови'
    COLLATE='utf8_general_ci'
    ENGINE=InnoDB
    '''
    c.execute(sql)

    sql = u'''
    ALTER TABLE `Client`
	ADD COLUMN `bloodPhenotype_id` INT(11) NULL DEFAULT NULL COMMENT 'Фенотип крови{rbBloodPhenotype}' AFTER `bloodType_id`,
	ADD COLUMN `bloodKell` ENUM('NOT_DEFINED', 'POSITIVE', 'NEGATIVE') NOT NULL DEFAULT 'NOT_DEFINED' COMMENT 'kell антиген' AFTER `bloodPhenotype_id`,
	ADD CONSTRAINT `FK_Client_rbBloodPhenotype` FOREIGN KEY (`bloodPhenotype_id`) REFERENCES `rbBloodPhenotype` (`id`);
    '''
    c.execute(sql)

    sql = u'''
    ALTER TABLE `trfuOrderIssueResult`
	ADD COLUMN `stickerUrl` VARCHAR(2083) NULL DEFAULT NULL COMMENT 'URL этикетки' AFTER `trfu_donor_id`;
    '''
    c.execute(sql)

    c.close()

def downgrade(conn):
    c = conn.cursor()

    sql = u'''
    DROP TABLE `rbBloodPhenotype`;
    '''
    c.execute(sql)
    c.close()
