# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import logging

__doc__ = '''\
Исправления операционных #4 - Таблица операционных
'''


def upgrade(conn):
    sql = [
        # Меняем таблицу настроек операционной
        '''\
ALTER TABLE `trfu_operational`
	CHANGE COLUMN `author_id` `author_id` INT(11) NOT NULL COMMENT 'Пользователь, создавший операционную' AFTER `registered`;
''',
        '''\
ALTER TABLE `trfu_operational`
	CHANGE COLUMN `registered` `createDateTime` DATETIME NOT NULL COMMENT 'Время создания операционной' AFTER `deleted`;
''',
        '''\
ALTER TABLE `trfu_operational`
	CHANGE COLUMN `deleted` `deleted` BIT(1) NOT NULL DEFAULT b'0' COMMENT 'Флаг удаления' AFTER `id`;
''',
        '''\
ALTER TABLE `trfu_operational`
	DROP COLUMN `uuid`;
''',
        '''\
ALTER TABLE `trfu_operational`
	ADD COLUMN `name` VARCHAR(50) NULL DEFAULT NULL COMMENT 'Наименование операционной (кабинет?)' AFTER `author_id`;
''',
        '''\
ALTER TABLE `trfu_operational`
	ADD COLUMN `lot` VARCHAR(50) NULL DEFAULT NULL COMMENT 'Название ЛОТа' AFTER `name`;
''',
        '''\
ALTER TABLE `trfu_operational`
	ADD COLUMN `expirationDate` DATETIME NULL DEFAULT NULL COMMENT 'Дата окончания срока дейтвия ЛОТа' AFTER `lot`;
''',
        '''\
ALTER TABLE `trfu_operational`
	ADD COLUMN `type` ENUM('virusinactivation','operational') NULL DEFAULT NULL COMMENT 'Тип операционной (Вирусинактивация\Операционная)' AFTER `expirationDate`;
''',
        '''\
ALTER TABLE `trfu_operational`
	COMMENT='Операционные';
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Возвращаем старые колонки 
        '''\
ALTER TABLE `trfu_operational`
	CHANGE COLUMN `createDateTime` `registered` DATETIME NOT NULL COMMENT 'Время создания операционной' AFTER `deleted`;
''',
        '''\
ALTER TABLE `trfu_operational`
	ADD COLUMN `uuid` VARCHAR(255) NULL DEFAULT NULL;
''',
        '''\
ALTER TABLE `trfu_operational`
	DROP COLUMN `name`;
''',
        '''\
ALTER TABLE `trfu_operational`
	DROP COLUMN `lot`;
''',
        '''\
ALTER TABLE `trfu_operational`
	DROP COLUMN `expirationDate`;
''',
        '''\
ALTER TABLE `trfu_operational`
	DROP COLUMN `type`;
''',
    ]
    c = conn.cursor()
    logging.warn('Восстановление части данных невозможно')
    for s in sql:
        c.execute(s)
