#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Увеличение длины полей name, template таблицы rbThesaurus до 512 знаков
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `rbThesaurus`
CHANGE COLUMN `name` `name` VARCHAR(512) NOT NULL DEFAULT '' COMMENT 'Наименование' ,
CHANGE COLUMN `template` `template` VARCHAR(512) NOT NULL DEFAULT '' COMMENT 'Шаблон для разворачивания ветки дерева в строку, вместо %s рекурсивно подставлется parent.template';
'''
    c.execute(sql)
    c.close()


def downgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `rbThesaurus`
CHANGE COLUMN `name` `name` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'Наименование' ,
CHANGE COLUMN `template` `template` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'Шаблон для разворачивания ветки дерева в строку, вместо %s рекурсивно подставлется parent.template';
'''
    c.execute(sql)
    c.close()