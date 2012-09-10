# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Вводим таблицу Event_Persons - возможность иметь несколько врачей, ответственных за одно обращение в разное время.
'''


def upgrade(conn):
    sql = [
        # Создаём таблицу для ответственных за обращения врачей
        '''\
create table if not exists `Event_Persons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL COMMENT 'Event {Event}',
  `person_id` int(11) NOT NULL COMMENT 'Person {Person}',
  `begDate` datetime NOT NULL COMMENT 'Starting responsibility date',
  `endDate` datetime COMMENT 'Disclaimer date',
  PRIMARY KEY (`id`),
  KEY `event_id` (`event_id`),
  KEY `person_id` (`person_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Event Responsibility List' AUTO_INCREMENT=13;
''',
        # Переносим имеющуюся информацию об ответственности из Event
        '''\
insert into `Event_Persons` (`event_id`, `person_id`, `begDate`, `endDate`)
select `id`, `execPerson_id`, `setDate`, `execDate` from `Event` where `execPerson_id` is not null
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем таблицу со списком ответственных
        '''\
drop table `Event_Persons`
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
        