#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Таблицы для лекарственных назначений
'''

rbUnitsGroup = '''
CREATE TABLE `rbUnitsGroup` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(16) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `shortname` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
'''

rbUnits = u'''
CREATE TABLE `rbUnits` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(16) NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `shortname` VARCHAR(32) NOT NULL,
    `group_id` INT(11) NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `FK_rbUnits_rbUnitsGroup` (`group_id`),
    CONSTRAINT `FK_rbUnits_rbUnitsGroup` FOREIGN KEY (`group_id`) REFERENCES `rbUnitsGroup` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
'''

MedicalPrescription = u'''
CREATE TABLE `MedicalPrescription` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `createDatetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `modifyDatetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    `createPerson_id` INT(11) NOT NULL,
    `modifyPerson_id` INT(11) NOT NULL,
    `action_id` INT(11) NOT NULL,
    `rls_id` INT(11) NOT NULL,
    `status_id` INT(11) NOT NULL,
    `dose_amount` DOUBLE NOT NULL,
    `dose_unit_id` INT(11) NOT NULL,
    `frequency_value` DOUBLE NOT NULL,
    `frequency_unit_id` INT(11) NOT NULL,
    `duration_value` INT(11) NOT NULL,
    `duration_unit_id` INT(11) NOT NULL,
    `begDate` DATE NULL DEFAULT NULL,
    `methodOfAdministration_id` INT(11) NOT NULL,
    `note` VARCHAR(255) NULL DEFAULT NULL,
    `reasonOfCancel` VARCHAR(255) NULL DEFAULT NULL,
    PRIMARY KEY (`id`),
    INDEX `FK_MedicalPrescription_rlsNomen` (`rls_id`),
    INDEX `FK_MedicalPrescription_rbMethodOfAdministration` (`methodOfAdministration_id`),
    INDEX `FK_MedicalPrescription_Action` (`action_id`),
    INDEX `FK_MedicalPrescription_Person_create` (`createPerson_id`),
    INDEX `FK_MedicalPrescription_Person_modify` (`modifyPerson_id`),
    INDEX `FK_MedicalPrescription_rbUnits_dose` (`dose_unit_id`),
    INDEX `FK_MedicalPrescription_rbUnits_duration` (`duration_unit_id`),
    INDEX `FK_MedicalPrescription_rbUnits_frequency` (`frequency_unit_id`),
    CONSTRAINT `FK_MedicalPrescription_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`),
    CONSTRAINT `FK_MedicalPrescription_Person_create` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `FK_MedicalPrescription_Person_modify` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`),
    CONSTRAINT `FK_MedicalPrescription_rbMethodOfAdministration` FOREIGN KEY (`methodOfAdministration_id`) REFERENCES `rbMethodOfAdministration` (`id`),
    CONSTRAINT `FK_MedicalPrescription_rbUnits_dose` FOREIGN KEY (`dose_unit_id`) REFERENCES `rbUnits` (`id`),
    CONSTRAINT `FK_MedicalPrescription_rbUnits_duration` FOREIGN KEY (`duration_unit_id`) REFERENCES `rbUnits` (`id`),
    CONSTRAINT `FK_MedicalPrescription_rbUnits_frequency` FOREIGN KEY (`frequency_unit_id`) REFERENCES `rbUnits` (`id`),
    CONSTRAINT `FK_MedicalPrescription_rlsNomen` FOREIGN KEY (`rls_id`) REFERENCES `rlsNomen` (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
'''

data = u'''
INSERT INTO `rbUnitsGroup` VALUES (1, 'time', 'Время', 'Время');
INSERT INTO `rbUnitsGroup` VALUES (2, 'weight', 'Вес', 'Вес');
INSERT INTO `rbUnitsGroup` VALUES (3, 'volume', 'Объём', 'Объём');
INSERT INTO `rbUnitsGroup` VALUES (4, 'concentration', 'Концентрация', 'Концентрация');
INSERT INTO `rbUnitsGroup` VALUES (5, 'counted', 'Счётные', 'Счётные');

INSERT INTO `rbUnits` VALUES (1, 'second', 'секунда', 'сек.', 1);
INSERT INTO `rbUnits` VALUES (2, 'minute', 'минута', 'мин.', 1);
INSERT INTO `rbUnits` VALUES (3, 'hour', 'час', 'час', 1);
INSERT INTO `rbUnits` VALUES (4, 'day', 'день', 'день', 1);
INSERT INTO `rbUnits` VALUES (5, 'week', 'неделя', 'нед.', 1);
INSERT INTO `rbUnits` VALUES (6, 'month', 'месяц', 'мес.', 1);
INSERT INTO `rbUnits` VALUES (7, 'year', 'год', 'год', 1);
INSERT INTO `rbUnits` VALUES (8, 'mg', 'миллиграмм', 'мг.', 2);
INSERT INTO `rbUnits` VALUES (9, 'g', 'грамм', 'г.', 2);
INSERT INTO `rbUnits` VALUES (10, 'kg', 'килограмм', 'кг.', 2);
INSERT INTO `rbUnits` VALUES (12, 'ml', 'миллилитр', 'мл.', 3);
INSERT INTO `rbUnits` VALUES (13, 'l', 'литр', 'л.', 3);
INSERT INTO `rbUnits` VALUES (14, 'mg/ml', 'миллиграмм на миллилитр', 'мг/мл', 4);
INSERT INTO `rbUnits` VALUES (15, 'mg/l', 'миллиграмм на литр', 'мг/л', 4);
INSERT INTO `rbUnits` VALUES (16, 'pcs', 'штуки', 'шт.', 5);
INSERT INTO `rbUnits` VALUES (17, 'tab', 'таблетка', 'таб.', 5);
'''


def upgrade(conn):
    with conn as c:
        c.execute(rbUnitsGroup)
        c.execute(rbUnits)
        c.execute(MedicalPrescription)

    with conn as c:
        inserts = filter(None, data.splitlines())
        for insert in inserts:
            print(insert)
            c.execute(insert)


def downgrade(conn):
    with conn as c:
        c.execute('DROP TABLE `MedicalPrescription`')
        c.execute('DROP TABLE `rbUnits`')
        c.execute('DROP TABLE `rbUnitsGroup`')
