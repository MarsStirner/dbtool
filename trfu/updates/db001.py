# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Системная таблица Meta для хранения версий схемы БД
'''


def upgrade(conn):
    sql = [
        # Создаём таблицу для хранения метаинформации
        '''\
create table if not exists `Meta` (
    `name` varchar(100) not null,
    `value` text,
    primary key (`name`)
)
''',
        # Записываем начальную версию 0 схемы БД
        '''\
insert into `Meta` (`name`, `value`)
values ("schema_version", "0")
on duplicate key update `value` = "0"
''',
        # Записываем тип схемы БД
        '''\
insert into `Meta` (`name`, `value`)
values ("schema_type", "trfu")
on duplicate key update `value` = "trfu"
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем таблицу метаинформации
        '''\
drop table `Meta`
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

