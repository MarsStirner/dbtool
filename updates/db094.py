#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''
Справочник УФМС
'''
def upgrade(conn):
    global config
    c = conn.cursor()
    sql = u'''
CREATE TABLE IF NOT EXISTS `rbUFMS` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(50) NOT NULL COLLATE 'utf8_unicode_ci',
    `name` VARCHAR(256) NOT NULL COLLATE 'utf8_unicode_ci',
    PRIMARY KEY (`id`)
)
COMMENT='Справочник УФМС'
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB
'''
    c.execute(sql)
    c.close()

def downgrade(conn):
    pass

