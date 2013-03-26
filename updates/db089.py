#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- http://helpdesk.korusconsulting.ru/browse/MIS-308 - решение гонок при создании новой записи в журнале забора БМ
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sqls = [
            u"""
CREATE TABLE IF NOT EXISTS `Media` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `filename` VARCHAR(256) NOT NULL,
    `file` MEDIUMBLOB NULL,
    PRIMARY KEY (`id`)
)
COMMENT='Файлы изображений и прочего'
COLLATE='utf8_bin'
ENGINE=InnoDB;
""",
    ]

    for sql in sqls:
        c.execute(sql)
    
def downgrade(conn):
    pass
