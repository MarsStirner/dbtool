#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление kell-антиген и фенотипа крови
'''

MIN_SCHEMA_VERSION = 184

def upgrade(conn):
    global config
    c = conn.cursor()
    sql = u'''
	INSERT INTO`rbBloodPhenotype` (`code`, `name`) VALUES 
	("D+C+E+c+e+", "D+ C+ E+ c+ e+"), 
	("D+C+E+c+e-", "D+ C+ E+ c+ e-"),
	("D+C+E+c-e+", "D+ C+ E+ c- e+"), 
	("D+C+E+c-e-", "D+ C+ E+ c- e-"),
	("D+C+E-c+e+", "D+ C+ E- c+ e+"),
	("D+C+E-c-e+", "D+ C+ E- c- e+"), 
	("D+C-E+c+e+", "D+ C- E+ c+ e+"),
	("D+C-E+c+e-", "D+ C- E+ c+ e-"),
	("D+C-E-c+e+", "D+ C- E- c+ e+"), 
	("D-C+E+c+e+", "D- C+ E+ c+ e+"), 
	("D-C+E+c+e-", "D- C+ E+ c+ e-"), 
	("D-C+E+c-e+", "D- C+ E+ c- e+"),
	("D-C+E+c-e-", "D- C+ E+ c- e-"), 
	("D-C+E-c+e+", "D- C+ E- c+ e+"),
	("D-C+E-c-e+", "D- C+ E- c- e+"), 
	("D-C-E+c+e+", "D- C- E+ c+ e+"),
	("D-C-E+c+e-", "D- C- E+ c+ e-"),
	("D-C-E-c+e+", "D- C- E- c+ e+") 
    '''
    c.execute(sql)

    sql = u'''INSERT INTO `rbAPTableField` (`idx`, `master_id`, `name`, `fieldName`) VALUES (7, 1, 'Этикетка', 'stickerUrl')'''
    c.execute(sql)

    c.close()
