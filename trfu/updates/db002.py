# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Исправления операционных #1-добавление используемой роли в списках персонала операционных
'''


def upgrade(conn):
    sql = [
        # Добавляем колонку используемой роли (FK) в списках персонала операционных
        '''\
ALTER TABLE `trfu_operational_crew_members` 
	ADD COLUMN `appointment_id` INT NULL COMMENT "Должность при назначении в операционную",
	ADD CONSTRAINT `fk_crew_member_to_appointment` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`id`);
''',
        # Заполняем используемые роли в списках персонала операцинных
        '''\
UPDATE `trfu_operational_crew_members` SET `appointment_id` = (SELECT `appointMent_id` FROM `person` WHERE `person`.`id` = `member_id`);
''',
        # Делаем используемую роль в списках персонала операцинных NOT NULL
        '''\
ALTER TABLE `trfu_operational_crew_members` CHANGE COLUMN `appointment_id` `appointment_id` INT NOT NULL COMMENT "Должность при назначении в операционную";
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем колонку с используемой ролью в списках персонала операционных
        '''\
ALTER TABLE `trfu_operational_crew_members` 
	DROP FOREIGN KEY `fk_crew_member_to_appointment`;
''',
        '''\
ALTER TABLE `trfu_operational_crew_members` 
	DROP COLUMN `appointment_id`;
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

