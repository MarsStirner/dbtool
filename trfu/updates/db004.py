# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Исправления операционных #3 - Добавление признака для Типов Систем Крови
'''


def upgrade(conn):
    sql = [
        # Добавляем признак возможностей использования системы крови
        '''\
ALTER TABLE `trfu_blood_system_types` 
	ADD COLUMN `type` ENUM('virusinactivation','operational') NULL DEFAULT NULL COMMENT 'Тип операционной (Вирусинактивация/Операционная)' AFTER `unit`;
''',
        # Проставляем признаки
        '''\
UPDATE `trfu_blood_system_types` SET `type` = IF(`id`<=4, 'operational', 'virusinactivation');
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем признак из Типов Систем Крови
        '''\
ALTER TABLE `trfu_blood_system_types` 
	DROP COLUMN `type`;
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

