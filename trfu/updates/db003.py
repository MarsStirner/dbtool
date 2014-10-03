# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Исправления операционных #2 - Переименование таблицы с настройками операционных
'''

#Переименование таблицы trfu_operational_crew в trfu_operational

def upgrade(conn):
    sql = [
        # 1) Удалить все FK на старое название таблицы
        '''\
ALTER TABLE `trfu_operational_crew_members` DROP FOREIGN KEY `FKC88BD3BAF145EDB3`;
''',
        # 1
        '''\
ALTER TABLE `trfu_blood_donation_requests` DROP FOREIGN KEY `FKD779745AD10439A1`;
''',
        # 2) Переименовываем таблицу
        '''\
RENAME TABLE `trfu_operational_crew` TO `trfu_operational`;
''',
        # 3) Прокидываем (+ переименовываем колонки) новые ключи
        '''\
ALTER TABLE `trfu_operational_crew_members`
	CHANGE COLUMN `crew_id` `operational_id` INT(11) NOT NULL COMMENT 'Ссылка на операционную' FIRST;
''',
        # 3
        '''\
ALTER TABLE `trfu_operational_crew_members` 
	ADD CONSTRAINT `FK_trfu_operational_crew_members_trfu_operational` 
	FOREIGN KEY (`operational_id`) REFERENCES `trfu_operational` (`id`) 
	ON DELETE CASCADE;
''',
        # 3
        '''\
ALTER TABLE `trfu_blood_donation_requests`
	CHANGE COLUMN `operationalCrew_id` `operational_id` INT(11) NULL DEFAULT NULL AFTER `bloodSystem_id`;
''',
        # 3
        '''\
ALTER TABLE `trfu_blood_donation_requests`
	ADD CONSTRAINT `FK_trfu_blood_donation_requests_trfu_operational` FOREIGN KEY (`operational_id`) REFERENCES `trfu_operational` (`id`);
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # 1) Удаляем новые ключи и переименовываем колонки обратно
        '''\
ALTER TABLE `trfu_blood_donation_requests`
DROP FOREIGN KEY `FK_trfu_blood_donation_requests_trfu_operational`;
''',
        '''\
ALTER TABLE `trfu_blood_donation_requests`
	CHANGE COLUMN `operational_id` `operationalCrew_id` INT(11) NULL DEFAULT NULL AFTER `bloodSystem_id`;
''',
        '''\
ALTER TABLE `trfu_operational_crew_members` 
	DROP FOREIGN KEY `FK_trfu_operational_crew_members_trfu_operational`;
''',
        '''\
ALTER TABLE `trfu_operational_crew_members`
	CHANGE COLUMN `operational_id` `crew_id` INT(11) NOT NULL COMMENT 'Ссылка на операционную' FIRST;
''',
        # 2) Переименовываем таблицу обратно
        '''\
RENAME TABLE `trfu_operational` TO `trfu_operational_crew`;
''',
        # 3) Возвращаем старые ключи
        '''\
ALTER TABLE `trfu_operational_crew_members` ADD CONSTRAINT `FKC88BD3BAF145EDB3` FOREIGN KEY (`crew_id`) REFERENCES `trfu_operational_crew` (`id`);
''',
        '''\
ALTER TABLE `trfu_blood_donation_requests` ADD CONSTRAINT 
`FKD779745AD10439A1` FOREIGN KEY (`operationalCrew_id`) REFERENCES `trfu_operational_crew` (`id`);
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

