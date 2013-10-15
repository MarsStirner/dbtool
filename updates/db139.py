#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

sqls = (
    u"""ALTER TABLE `bbtOrganism_SensValues`
    DROP INDEX `bbtResult_Organism_id_idx`,
    DROP COLUMN `idx`,
    ADD INDEX `FK_bbtResult_Organism_id` (`bbtResult_Organism_id`);
""",
    u"""ALTER TABLE `bbtResult_Image`
    DROP INDEX `action_id_idx`,
    DROP COLUMN `idx`,
    ADD INDEX `FK_action_id_idx` (`action_id`);
""",
    u"""ALTER TABLE `bbtResult_Table`
    DROP INDEX `action_id_index`,
    DROP COLUMN `idx`,
    ADD INDEX `FK_action_id_idx` (`action_id`);
""",
    u"""ALTER TABLE `bbtResult_Organism`
    DROP INDEX `action_id_index`,
    DROP COLUMN `idx`,
    ADD INDEX `FK_action_id_idx` (`action_id`);
""",
    u"""ALTER TABLE `bbtResult_Text`
    DROP INDEX `action_id_index`,
    DROP COLUMN `idx`,
    ADD INDEX `FK_action_id_idx` (`action_id`);
""",
)

def upgrade(conn):
    global config
    c = conn.cursor()

    for query in sqls:
        try:
            c.execute(query)
        except:
            traceback.print_exc()

    c.close()

def downgrade(conn):
    pass