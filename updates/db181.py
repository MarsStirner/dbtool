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

    # Меняем данные в внешне-зависимых таблицах

    c.execute(u'''
UPDATE Contract_Tariff, rbService SET service_id = rbService.group_id
WHERE Contract_Tariff.service_id = rbService.id AND rbService.id != rbService.group_id
''')
    c.execute(u'''
UPDATE ActionType, rbService SET service_id = rbService.group_id
WHERE ActionType.service_id = rbService.id AND rbService.id != rbService.group_id
''')
    c.execute(u'''
UPDATE ActionType_Service, rbService SET service_id = rbService.group_id
WHERE ActionType_Service.service_id = rbService.id AND rbService.id != rbService.group_id
''')

    # Удаляем данные из внутренне-зависимых таблиц

    c.execute(u'''
DELETE FROM `rbServiceGroup`
USING `rbServiceGroup`, rbService
WHERE (
  `rbServiceGroup`.group_id = rbService.id OR
  `rbServiceGroup`.service_id = rbService.id
) AND rbService.id != rbService.group_id
''')
    c.execute(u'''
DELETE FROM `rbServiceUET`
USING `rbServiceUET`, rbService
WHERE `rbServiceUET`.rbService_id = rbService.id AND rbService.id != rbService.group_id
''')

    c.execute(u'''
DELETE FROM `rbServiceGroup`
WHERE (
  `rbServiceGroup`.group_id NOT IN (SELECT id FROM rbService) OR
  `rbServiceGroup`.service_id NOT IN (SELECT id FROM rbService)
)''')
    c.execute(u'''
DELETE FROM `rbServiceUET`
WHERE `rbServiceUET`.rbService_id NOT IN (SELECT id FROM rbService)''')

    # Переделываем FK, ибо нехер

    c.execute(u'''
ALTER TABLE `rbServiceUET`
  DROP FOREIGN KEY `rbServiceUET_ibfk_1`;
  ''')
    c.execute(u'''
ALTER TABLE `rbServiceUET`
  ADD CONSTRAINT `rbServiceUET_ibfk_1` FOREIGN KEY (`rbService_id`) REFERENCES `rbService` (`id`) ON UPDATE CASCADE ON DELETE CASCADE;
''')
    c.execute(u'''
ALTER TABLE `rbServiceGroup`
  ADD CONSTRAINT `FK_rbServiceGroup_rbService` FOREIGN KEY (`group_id`) REFERENCES `rbService` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
  ADD CONSTRAINT `FK_rbServiceGroup_rbService_2` FOREIGN KEY (`service_id`) REFERENCES `rbService` (`id`) ON UPDATE CASCADE ON DELETE CASCADE;
''')

    # Удаляем из rbService

    c.execute(u'''
DELETE FROM rbService WHERE id != group_id
''')

    # Дропаем более не нужные столбцы

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
