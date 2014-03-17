#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Форма 007
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    proc = u'''CREATE DEFINER=%s PROCEDURE `%s`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
             BEGIN
                SELECT rbSpecialVariablesPreferences.`query` INTO @tpl FROM rbSpecialVariablesPreferences WHERE rbSpecialVariablesPreferences.name = 'SpecialVar_%s';
		SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@%s",profiles);
		PREPARE sqlQuery FROM  @sqlPrepare;
		EXECUTE sqlQuery;
             END'''

    name = u'''FIOtotalDeath'''
    profile = u'''profile'''

    c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
    c.execute(proc%(config['definer'],name,name,profile))                      
    c.close()

def downgrade(conn):
    pass