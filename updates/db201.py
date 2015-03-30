#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


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

    proc = u'''CREATE DEFINER=%s PROCEDURE `%s`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
             BEGIN
                SELECT rbSpecialVariablesPreferences.`query` INTO @tpl FROM rbSpecialVariablesPreferences WHERE rbSpecialVariablesPreferences.name = 'SpecialVar_%s';
		SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, ":end_date", end_date),":org_str",org_str),":%s",profiles);
		PREPARE sqlQuery FROM  @sqlPrepare;
		EXECUTE sqlQuery;
             END'''

    names =    ( u'''form007front''', u'''FIOinput007''', u'''FIOinpuFrom12''', u'''FIOoutTotal''', u'''FIOoutToOtherUnit''', u'''FIOoutToOtherHospital''' , u'''FIOtotalDeath''')
    profiles = (     u'''profiles''',     u'''profile''',       u'''profile''',     u'''profile''',           u'''profile''',               u'''profile''', u'''profile''')

    for name in names:	
        c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
        index = names.index(name)
        c.execute(proc%(config['definer'],name,name,profiles[index])) 


def downgrade(conn):
    c = conn.cursor()
    sql = u'''
        DROP TABLE IF EXISTS `DrugIntervalCompParam`;
    '''
    c.execute(sql)
