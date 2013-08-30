#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback


__doc__ = '''\
Дополнения к структуре БД для интеграции с БАК Лабораторией (CGM)
'''

sqls = [
    # В первую очередь добавляем справочники
    u"""CREATE TABLE `rbAntibiotic` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(128) NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
)
COMMENT='Антибиотики'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `rbBacIndicator` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(128) NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
)
COMMENT='Методики/показатели/микроорганизмы БАК-исследований'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `rbBacLabDoctor` (
    `id` INT(11) NOT NULL,
    `fullName` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
)
COMMENT='Врач БАК Лаборатории'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `rbMicroorganism` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(128) NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
)
COMMENT='Микроорганизмы'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    # Ответы БАК ЛИС
    u"""CREATE TABLE `bbtResponse` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор',
    `action_id` INT(11) NOT NULL COMMENT 'Ид. действия {Action.id}',
    `index` INT(11) NOT NULL DEFAULT '0' COMMENT 'Индекс',
    `final` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Конечный вариант исследования',
    `defects` TEXT NULL COMMENT 'Дефекты биоматериала',
    `doctor_id` INT(11) NOT NULL COMMENT 'Идентификатор доктора в ЛИС',
    `codeLIS` VARCHAR(20) NOT NULL COMMENT 'Код ЛИС',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `action_id_index` (`action_id`, `index`),
    INDEX `FK_bbtResponse_rbBacLabDoctor` (`doctor_id`),
    CONSTRAINT `FK_bbtResponse_Action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`),
    CONSTRAINT `FK_bbtResponse_rbBacLabDoctor` FOREIGN KEY (`doctor_id`) REFERENCES `rbBacLabDoctor` (`id`)
)
COMMENT='Ответ БАК лаборатории с результатами бактериологического анализа крови'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `bbtResult` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор',
    `response_id` INT(11) NOT NULL COMMENT 'Ид. ответа ЛИС',
    `index` INT(11) NOT NULL COMMENT 'Индекс',
    `device` VARCHAR(256) NULL DEFAULT NULL COMMENT 'Название прибора',
    `valueText` TEXT NULL COMMENT 'Текстовое значение результата',
    `indicator_id` INT(11) NOT NULL COMMENT 'Ид. методики/показателя/микроорганизма',
    `normString` VARCHAR(256) NULL DEFAULT NULL COMMENT 'норма, диапазон допустимых значений',
    `normalityIndex` FLOAT NULL DEFAULT NULL COMMENT 'значение результата относительно нормы (число в диапазоне -1 до +1) ',
    `unit` VARCHAR(20) NULL DEFAULT NULL COMMENT 'единица измерения',
    `signDateTime` DATETIME NOT NULL COMMENT 'дата выполнения/утверждения результата',
    `status` TEXT NULL,
    `comment` TEXT NULL,
    PRIMARY KEY (`id`),
    UNIQUE INDEX `response_id_index` (`response_id`, `index`),
    INDEX `indicator_id` (`indicator_id`),
    CONSTRAINT `FK_bbtResult_bbtResponse` FOREIGN KEY (`response_id`) REFERENCES `bbtResponse` (`id`),
    CONSTRAINT `FK_bbtResult_rbBacIndicator` FOREIGN KEY (`indicator_id`) REFERENCES `rbBacIndicator` (`id`)
)
COMMENT='Результат бактериологического анализа крови'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `bbtSensValues` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор',
    `result_id` INT(11) NOT NULL COMMENT 'Ид. результата',
    `index` INT(11) NULL DEFAULT NULL COMMENT 'Индекс',
    `antibiotic_id` INT(11) NULL DEFAULT NULL COMMENT 'Ид. Антибиотика {rbAntibiotic.id}',
    `MIC` VARCHAR(20) NOT NULL COMMENT 'Концентрация',
    `activity` VARCHAR(5) NOT NULL COMMENT 'описание чувствительности в произвольном виде: R,S,I',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `result_id_index` (`result_id`, `index`),
    INDEX `FK_bbtSensValues_rbAntibiotic` (`antibiotic_id`),
    CONSTRAINT `FK_bbtSensValues_bbtResult` FOREIGN KEY (`result_id`) REFERENCES `bbtResult` (`id`),
    CONSTRAINT `FK_bbtSensValues_rbAntibiotic` FOREIGN KEY (`antibiotic_id`) REFERENCES `rbAntibiotic` (`id`)
)
COMMENT='Чувствительности микроорганизма к антибиотикам'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `bbtMicroValues` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор',
    `result_id` INT(11) NOT NULL COMMENT 'Ид. результата {bbtResult.id}',
    `index` INT(11) NOT NULL COMMENT 'Индекс',
    `organism_id` INT(11) NOT NULL COMMENT 'Ид. микроорганизма {rbMicroorganism.id}',
    `concentration` VARCHAR(256) NOT NULL COMMENT 'Концентрация',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `result_id_index` (`result_id`, `index`),
    INDEX `organism_id` (`organism_id`),
    CONSTRAINT `FK_bbtMicroValues_bbtResult` FOREIGN KEY (`result_id`) REFERENCES `bbtResult` (`id`),
    CONSTRAINT `FK_bbtMicroValues_rbMicroorganism` FOREIGN KEY (`organism_id`) REFERENCES `rbMicroorganism` (`id`)
)
COMMENT='Найденные микроорганизмы'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""",

    u"""CREATE TABLE `bbtImageValues` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор',
    `result_id` INT(11) NOT NULL COMMENT 'ид. результата {bbtResult.id}',
    `index` INT(11) NOT NULL COMMENT 'Индекс',
    `description` VARCHAR(256) NULL DEFAULT NULL COMMENT 'Описание изображения',
    `image` LONGBLOB NOT NULL COMMENT 'Изображение',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `result_id_index` (`result_id`, `index`),
    CONSTRAINT `FK_bbtImageValues_bbtResult` FOREIGN KEY (`result_id`) REFERENCES `bbtResult` (`id`)
)
COMMENT='Изображения'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;""",
]


def upgrade(conn):
    c = conn.cursor()

    for query in sqls:
        try:
            c.execute(query)
        except:
            traceback.print_exc()

    c.close()


def downgrade(conn):
    pass