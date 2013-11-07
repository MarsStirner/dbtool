#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения структуры БД для фильтрации типов действий при создании действия по пользователю и его профилю
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(
u"""CREATE TABLE `ActionType_User` (
    `id` INT(10) NOT NULL AUTO_INCREMENT,
    `actionType_id` INT(10) NOT NULL,
    `person_id` INT(10) NULL,
    `profile_id` INT(10) NULL,
    PRIMARY KEY (`id`),
    INDEX `person_id_profile_id` (`person_id`, `profile_id`),
    INDEX `profile_id` (`profile_id`),
    INDEX `FK__ActionType` (`actionType_id`),
    CONSTRAINT `FK__ActionType` FOREIGN KEY (`actionType_id`) REFERENCES `ActionType` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `FK__Person` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `FK__rbUserProfile` FOREIGN KEY (`profile_id`) REFERENCES `rbUserProfile` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""")
    c.close()

def downgrade(conn):
    pass