#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- добавление столбца для хранения текстов шаблонов
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
ALTER TABLE `rbPrintTemplate`
ADD COLUMN `templateText` LONGTEXT NOT NULL AFTER `render`;
'''
    c.execute(sql)
    sql = '''
CREATE TABLE `rbPrintTemplateMeta` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `template_id` INT(11) NOT NULL,
    `type` ENUM('Integer','Float','String','Boolean','Date','Time','List','Multilist','RefBook','Organisation','OrgStructure','Person','Service','SpecialVariable') NOT NULL,
    `name` VARCHAR(128) NOT NULL,
    `title` TINYTEXT NOT NULL,
    `description` TINYTEXT NOT NULL,
    `arguments` MEDIUMTEXT NULL,
    `defaultValue` TEXT NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `template_id_name` (`template_id`, `name`),
    CONSTRAINT `FK_rbPrintTemplateMeta_rbPrintTemplate` FOREIGN KEY (`template_id`) REFERENCES `rbPrintTemplate` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)
COMMENT='Метаданные шаблона печати'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    c.close()


def downgrade(conn):
    pass