# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Таблица NotificationOccurred для хранения списка пользователей, прочитавших сигнальные донесения
'''

def upgrade(conn):
    sql = [
        # Создаём таблицу для хранения списка пользователей, прочитавших сигнальные донесения
        '''\

create table if not exists `NotificationOccurred` ( 
    `id` int(11) not null auto_increment, 
    `eventDatetime` datetime not null, 
    `clientId` int(11) not null, 
    `userId` int(11) not null, 
    primary key(`id`),
    constraint `NotificationOccurred_userId_fk`
    foreign key (`userId`) references `Person`(`id`) on update cascade on delete cascade
) engine=InnoDB default charset=utf8 comment='Notificated Users List';
''',]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
        # Удаляем таблицу для хранения 
        # списка пользователей, прочитавших сигнальные донесения
        '''\
drop table `NotificationOccurred`
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

