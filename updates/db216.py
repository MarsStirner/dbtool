#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, with_statement

__doc__ = '''\
Таблица для хранения внутренней почты
'''


def upgrade(conn):
    with conn as c:
        sql = '''CREATE TABLE `UserMail` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `sender_id` INT(11) NULL DEFAULT NULL,
        `recipient_id` INT(11) NULL DEFAULT NULL,
        `subject` VARCHAR(256) NOT NULL,
        `text` TEXT NOT NULL,
        `datetime` DATETIME NOT NULL,
        `read` TINYINT(1) NOT NULL,
        `mark` TINYINT(1) NOT NULL,
        `parent_id` INT(11) NULL DEFAULT NULL,
        `folder` VARCHAR(50) NOT NULL DEFAULT 'inbox',
        PRIMARY KEY (`id`),
        INDEX `recipient_id` (`recipient_id`),
        INDEX `FK_UserMail_UserMail` (`parent_id`),
        INDEX `FK_UserMail_Person_sender` (`sender_id`),
        CONSTRAINT `FK_UserMail_Person_sender` FOREIGN KEY (`sender_id`) REFERENCES `Person` (`id`),
        CONSTRAINT `FK_UserMail_Person_recepient` FOREIGN KEY (`recipient_id`) REFERENCES `Person` (`id`),
        CONSTRAINT `FK_UserMail_UserMail` FOREIGN KEY (`parent_id`) REFERENCES `UserMail` (`id`)
        )
        DEFAULT CHARACTER SET = utf8
        COLLATE = utf8_general_ci
        ENGINE = InnoDB;
        '''
        c.execute(sql)


def downgrade(conn):
    with conn as c:
        c.execute('''DROP TABLE `UserMail`''')
