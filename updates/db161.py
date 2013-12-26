#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''
Добавление версионности справочнику услуг rbService
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u"""ALTER TABLE `rbService`
    ADD COLUMN `child_id` INT(11) NULL COMMENT 'Следующая версия записи справочника' AFTER `departCode`,
    ADD INDEX `child_id` (`child_id`),
    ADD CONSTRAINT `FK_rbService_rbService` FOREIGN KEY (`child_id`) REFERENCES `rbService` (`id`);""")
    c.close()

def downgrade(conn):
    pass