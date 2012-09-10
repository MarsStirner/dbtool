# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Вводим таблицу Person_Profiles - 
возможность иметь несколько профилей одной персоны.
'''


def upgrade(conn):
    sql = [
        # Создаём таблицу для списка профилей
        '''\
create table if not exists `Person_Profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL COMMENT 'User {Person}',
  `userProfile_id` int(11) NOT NULL COMMENT 'Profile {rbUserProfile}',
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  KEY `userProfile_id` (`userProfile_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='User Profile List' AUTO_INCREMENT=13;
''',
        # Переносим имеющуюся информацию о профилях из таблицы Person
        '''\
insert into `Person_Profiles` (`person_id`, `userProfile_id`) 
select `id`, `userProfile_id` from `Person` where `userProfile_id` is not null
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем таблицу со списком профилей
        '''\
drop table `Person_Profiles`
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

