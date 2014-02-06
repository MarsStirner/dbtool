#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''
Добавление OID организации из справочника 1.2.643.5.1.13.2.1.1.178 (MDR308)
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
ALTER TABLE `Organisation`
	ADD COLUMN `OID` VARCHAR(127) NULL COMMENT 'Код ЛПУ из справочника 1.2.643.5.1.13.2.1.1.178 (MDR308)' AFTER `uuid_id`;
'''
    c.execute(sql)

    c.close()

def downgrade(conn):
    pass