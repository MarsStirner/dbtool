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
    ADD COLUMN `group_id` INT(11) NULL COMMENT 'Первая версия записи справочника' AFTER `departCode`,
    ADD INDEX `group_id` (`group_id`),
    ADD CONSTRAINT `FK_rbService_rbService_2` FOREIGN KEY (`group_id`) REFERENCES `rbService` (`id`),

    ADD COLUMN `child_id` INT(11) NULL COMMENT 'Следующая версия записи справочника' AFTER `group_id`,
    ADD INDEX `child_id` (`child_id`),
    ADD CONSTRAINT `FK_rbService_rbService_1` FOREIGN KEY (`child_id`) REFERENCES `rbService` (`id`);""")

    # Предполагается, что версионности никакой нет
    c.execute(u"""UPDATE rbService SET group_id = id;""")

    c.close()

def downgrade(conn):
    pass