# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Таблица rbTestTubeType для хранения типов пробирок
'''

def upgrade(conn):
    sql = [
        # Создаём таблицу для хранения типов пробирок
        '''\

create table if not exists `rbTestTubeType` (
    `id` int(11) not null auto_increment,
    `code` varchar(64),
    `name` varchar(128) not null,
    `volume` double not null,
    `unit_id` int(11) not null,
    `covCol` varchar(64),
    `image` mediumblob,
    primary key(`id`),
    constraint `rbTestTubeType_unit_id_fk`
    foreign key (`unit_id`) references `rbUnit`(`id`) on update cascade on delete cascade
) engine=InnoDB default charset=utf8 comment='Таблица для хранения описаний типов пробирок';
''',]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем таблицу для хранения типов пробирок
        '''\
drop table `rbTestTubeType`
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
