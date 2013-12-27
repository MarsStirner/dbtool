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
    ADD INDEX `group_id_idx` (`group_id`, `idx`),
    ADD CONSTRAINT `FK_rbService_rbService` FOREIGN KEY (`group_id`) REFERENCES `rbService` (`id`),

    ADD COLUMN `idx` INT(11) NOT NULL DEFAULT '0' COMMENT 'Номер версии' AFTER `group_id`;""")

    # Предполагается, что версионности никакой нет
    c.execute(u"""UPDATE rbService SET group_id = id;""")

    c.close()

def downgrade(conn):
    pass