#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback


__doc__ = '''
Изменения для обновления остатков
'''

sqls = [
    # В первую очередь добавляем справочники
    u"""CREATE TABLE `rbStorage` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `uuid` VARCHAR(50) NOT NULL,
    `name` VARCHAR(256) NULL,
    `orgStructure_id` INT(11) NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `uuid` (`uuid`),
    CONSTRAINT `FK__OrgStructure` FOREIGN KEY (`orgStructure_id`) REFERENCES `OrgStructure` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""ALTER TABLE `rlsBalanceOfGoods`
    ADD COLUMN `storage_id` INT(11) NULL AFTER `updateDateTime`,
    DROP COLUMN `storage_uuid`,
    DROP INDEX `FK_rlsBalanceOfGoods_OrgStructure`,
    ADD INDEX `storage_id` (`storage_id`),
    ADD CONSTRAINT `FK_rlsBalanceOfGoods_rbStorage` FOREIGN KEY (`storage_id`) REFERENCES `rbStorage` (`id`);
""",

    u"""CREATE OR REPLACE DEFINER=%s VIEW `vNomen` AS
    SELECT
    `rlsBalanceOfGoods`.`id`,
    `rlsBalanceOfGoods`.`rlsNomen_id`,
    `rlsBalanceOfGoods`.`value`,
    `rlsBalanceOfGoods`.`bestBefore`,
    `rlsBalanceOfGoods`.`disabled`,
    `rlsBalanceOfGoods`.`updateDateTime`,
    `rbStorage`.`orgStructure_id`
FROM
    `rlsBalanceOfGoods`
JOIN
    `rbStorage`;
""" % config['definer']
    ,

]


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