#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, with_statement

__doc__ = '''\
Таблица для хранения подписок пользователей
'''


def upgrade(conn):
    with conn as c:
        sql = '''CREATE TABLE `UserSubscriptions` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `object_id` VARCHAR(256) NOT NULL,
        `person_id` INT(11) NOT NULL,
        PRIMARY KEY (`id`),
        UNIQUE INDEX `object_id_person_id` (`person_id`, `object_id`),
        INDEX `object_id` (`object_id`),
        CONSTRAINT `FK_UserSubscriptions_Person` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
        )
        DEFAULT CHARACTER SET = utf8
        COLLATE = utf8_general_ci
        ENGINE = InnoDB;
        '''
        c.execute(sql)


def downgrade(conn):
    with conn as c:
        c.execute('''DROP TABLE `UserSubscriptions`''')
