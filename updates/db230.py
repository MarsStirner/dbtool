#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Автосохранения
'''


def upgrade(conn):
    global config        

    with conn as c:
        c.execute('''
CREATE TABLE IF NOT EXISTS `ActionAutoSave` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `action_id` INT(11) NOT NULL,
    `user_id` INT(11) NOT NULL,
    `datetime` DATETIME NOT NULL,
    `data` LONGTEXT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `FK_ActionAutoSave_Action` (`action_id`),
    INDEX `FK_ActionAutoSave_Person` (`user_id`),
    CONSTRAINT `FK_ActionAutoSave_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `FK_ActionAutoSave_Person` FOREIGN KEY (`user_id`) REFERENCES `Person` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
''')
        c.execute('''
CREATE TABLE IF NOT EXISTS `ActionAutoSaveUnsaved` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `actionType_id` INT(11) NOT NULL,
    `event_id` INT(11) NOT NULL,
    `user_id` INT(11) NOT NULL,
    `datetime` DATETIME NOT NULL,
    `data` LONGTEXT NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `FK_ActionAutoSave_Action` (`actionType_id`),
    INDEX `FK_ActionAutoSave_Person` (`user_id`),
    INDEX `FK_ActionAutoSaveUnsaved_Event` (`event_id`),
    CONSTRAINT `FK_ActionAutoSaveUnsaved_ActionType` FOREIGN KEY (`actionType_id`) REFERENCES `ActionType` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `FK_ActionAutoSaveUnsaved_Event` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `FK_ActionAutoSaveUnsaved_Person` FOREIGN KEY (`user_id`) REFERENCES `Person` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
''')
        c.execute('''
ALTER TABLE `Diagnosis`
    CHANGE COLUMN `MKB` `MKB` VARCHAR(8) NULL DEFAULT NULL COMMENT 'Код по МКБ X (с пятым знаком)' AFTER `character_id`,
    CHANGE COLUMN `MKBEx` `MKBEx` VARCHAR(8) NULL DEFAULT NULL COMMENT 'Вторая секция кода по МКБ X (с пятым знаком)' AFTER `MKB`;
''')


def downgrade(conn):
    with conn as c:
        c.execute('''DROP TABLE IF EXISTS ActionAutoSave''')
        c.execute('''DROP TABLE IF EXISTS ActionAutoSaveUnsaved''')





