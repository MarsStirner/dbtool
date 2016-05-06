#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- TMIS-1066 - Увеличение размеров полей для Аллергий и Мендикаментозных непереносимостей
'''


def upgrade(conn):
    with conn as c:
        c.execute('''
ALTER TABLE `ClientAllergy`
    ALTER `nameSubstance` DROP DEFAULT;
ALTER TABLE `ClientAllergy`
    CHANGE COLUMN `nameSubstance` `nameSubstance` TEXT NOT NULL COMMENT 'Наименование вещества' AFTER `client_id`,
    CHANGE COLUMN `notes` `notes` TEXT NOT NULL COMMENT 'Примечание' AFTER `createDate`
''')
        c.execute('''
ALTER TABLE `ClientIntoleranceMedicament`
    ALTER `nameMedicament` DROP DEFAULT;
ALTER TABLE `ClientIntoleranceMedicament`
    CHANGE COLUMN `nameMedicament` `nameMedicament` TEXT NOT NULL COMMENT 'Название медикамента' AFTER `client_id`,
    CHANGE COLUMN `notes` `notes` TEXT NOT NULL COMMENT 'Примечание' AFTER `createDate`
''')


def downgrade(conn):
    with conn as c:
        c.execute('''
ALTER TABLE `ClientAllergy`
    CHANGE COLUMN `nameSubstance` `nameSubstance` VARCHAR(128) NOT NULL COMMENT 'Наименование вещества' AFTER `client_id`,
    CHANGE COLUMN `notes` `notes` TINYTEXT NOT NULL COMMENT 'Примечание' AFTER `createDate`
''')
        c.execute('''
ALTER TABLE `ClientIntoleranceMedicament`
    CHANGE COLUMN `nameMedicament` `nameMedicament` VARCHAR(128) NOT NULL COMMENT 'Название медикамента' AFTER `client_id`,
    CHANGE COLUMN `notes` `notes` TINYTEXT NOT NULL COMMENT 'Примечание' AFTER `createDate`
''')





