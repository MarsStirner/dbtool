#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Миграция на неверсионный rbService c именами и кодами услуг в Contract_Tariff (версионность через прайсы/тарифы)
'''

def upgrade(conn):
    c = conn.cursor()
    global tools

    # Altering

    c.execute(u'''
ALTER TABLE `Contract_Tariff`
    ADD COLUMN `code` VARCHAR(64) NULL DEFAULT NULL AFTER `service_id`,
    ADD COLUMN `name` VARCHAR(256) NULL DEFAULT NULL AFTER `code`;
''')

    # Non-destructive

    c.execute(u'''
UPDATE Contract_Tariff, rbService SET Contract_Tariff.name = rbService.name
WHERE Contract_Tariff.service_id = rbService.id
''')
    c.execute(u'''
UPDATE Contract_Tariff, rbService SET Contract_Tariff.code = rbService.code
WHERE Contract_Tariff.service_id = rbService.id
''')

    # DESTRUCTIVE

    print(u'Храни вас Господь, если вы не делали резервное копирование БД...')

    c.execute(u'''
UPDATE ActionType, rbService SET service_id = rbService.group_id
WHERE ActionType.service_id = rbService.id AND rbService.id != rbService.group_id
''')
    c.execute(u'''
UPDATE ActionType_Service, rbService SET service_id = rbService.group_id
WHERE ActionType_Service.service_id = rbService.id AND rbService.id != rbService.group_id
''')
    c.execute(u'''
DELETE FROM rbService WHERE id != group_id
''')
    c.execute(u'''
ALTER TABLE `rbService`
  DROP INDEX `group_id_idx`,
  DROP FOREIGN KEY `FK_rbService_rbService`,
  DROP COLUMN `group_id`,
  DROP COLUMN `idx`;
''')

    c.close()


def downgrade(conn):
    pass
