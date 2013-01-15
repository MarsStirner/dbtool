#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Интеграция с ТФОМС
- Интеграция с DICOM Архивом
'''

simple_queries = \
(
# Интеграция с ТФОМС
u'''
CREATE TABLE IF NOT EXISTS `rbMedicalKind` (
    `id`         INT(11)      NOT NULL AUTO_INCREMENT,
    `code`       VARCHAR(1)   NOT NULL COMMENT 'Код вида помощи',
    `name`       VARCHAR(64)  NOT NULL COMMENT 'Описание вида помощи',
    PRIMARY KEY (`id`)) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Виды медицинской помощи';
''',
'''
ALTER TABLE EventType
ADD `rbMedicalKind_id` INT(11) NULL COMMENT 'Ссылка на вид помощи rbMedicalKind.id' AFTER `age`,
ADD FOREIGN KEY (`rbMedicalKind_id`) REFERENCES `rbMedicalKind`(`id`);
''',
'''
CREATE TABLE IF NOT EXISTS `rbServiceFinance` (
    `id`      INT(11)      NOT NULL AUTO_INCREMENT,
    `code`    VARCHAR(2)   NOT NULL COMMENT 'Код',
    `name`    VARCHAR(64)  NOT NULL COMMENT 'Описание',
    PRIMARY KEY (`id`)) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Источники финансирования услуг';
''',
'''
ALTER TABLE Contract_Tariff
ADD `rbServiceFinance_id` INT(11) NULL COMMENT 'Ссылка на источник финансирования услуги rbServiceFinance.id' AFTER `MKB`,
ADD FOREIGN KEY (`rbServiceFinance_id`) REFERENCES `rbServiceFinance`(`id`);
''',
'''
ALTER TABLE rbService
ADD `rbMedicalKind_id` INT(11) NULL COMMENT 'Ссылка на вид помощи rbMedicalKind.id',
ADD FOREIGN KEY (`rbMedicalKind_id`) REFERENCES `rbMedicalKind`(`id`),
ADD `departCode` VARCHAR(3) NULL COMMENT 'Код отделения, соответствующего услуге (в поликлинике это характеристика отдельной услуги, а не отделения)';
''',
'''
ALTER TABLE rbService
ADD `UET` DOUBLE NOT NULL DEFAULT 0 COMMENT 'УЕТ по умолчанию' AFTER `rbMedicalKind_id`;
''',
'''
CREATE TABLE IF NOT EXISTS `rbServiceUET` (
    `id`           INT(11)      NOT NULL AUTO_INCREMENT,
    `rbService_id` INT(11)      NOT NULL COMMENT 'Ссылка на услугу rbService.id',
    `age`          VARCHAR(10)  NOT NULL COMMENT 'Закодированное значение возраста пациентов, при котором берется значение УЕТ',
    `UET`          DOUBLE       NOT NULL DEFAULT 0 COMMENT 'Число УЕТ, соответствующее выбранному возрасту',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`rbService_id`) REFERENCES `rbService`(`id`)
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Таблица для хранения числа УЕТ, соответствующих услуге в зависимости от возраста пациента';
''',
'''
CREATE TABLE IF NOT EXISTS `rbPayType` (
    `id`                  INT(11)      NOT NULL AUTO_INCREMENT,
    `code`                VARCHAR(2)   NOT NULL COMMENT 'Код способа оплаты',
    `name`                VARCHAR(64)  NOT NULL COMMENT 'Описание способа оплаты',
    PRIMARY KEY (`id`)
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Способы оплаты услуг';
''',
'''
CREATE TABLE IF NOT EXISTS `rbTariffType` (
    `id`                  INT(11)      NOT NULL AUTO_INCREMENT,
    `code`                VARCHAR(2)   NOT NULL COMMENT 'Код вида тарификации',
    `name`                VARCHAR(64)  NOT NULL COMMENT 'Описание вида тарификации',
    PRIMARY KEY (`id`)
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Виды тарификации услуг';
''',
'''
CREATE TABLE IF NOT EXISTS `MedicalKindUnit` (
    `id`                  INT(11)      NOT NULL AUTO_INCREMENT,
    `rbMedicalKind_id`    INT(11)      NOT NULL COMMENT 'Ссылка на категорию помощи rbMedicalKind.id', 
    `eventType_id`        INT(11)      NULL     COMMENT 'Ссылка на тип события EventType.id. Если null - то зависимость только от категории помощи, от типа события - нет',
    `rbMedicalAidUnit_id` INT(11)      NOT NULL COMMENT 'Ссылка на единицу мед.помощи rbMedicalAidUnit.id',
    `rbPayType_id`        INT(11)      NOT NULL COMMENT 'Ссылка на способ оплаты rbPayType.id',
    `rbTariffType_id`     INT(11)      NOT NULL COMMENT 'Ссылка на вид тарификации rbTariffType.id',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`rbMedicalKind_id`) REFERENCES `rbMedicalKind`(`id`), 
    FOREIGN KEY (`eventType_id`) REFERENCES `EventType`(`id`),
    FOREIGN KEY (`rbMedicalAidUnit_id`) REFERENCES `rbMedicalAidUnit`(`id`),
    FOREIGN KEY (`rbPayType_id`) REFERENCES `rbPayType`(`id`),
    FOREIGN KEY (`rbTariffType_id`) REFERENCES `rbTariffType`(`id`)
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Таблица для хранения связи категорий помощи и способов оплаты услуг';
''',
'''
CREATE TABLE IF NOT EXISTS `rbAcheResult` (
    `id`                  INT(11)      NOT NULL AUTO_INCREMENT,
    `eventPurpose_id`     INT(11)      NOT NULL COMMENT 'Ссылка на назначение типа события rbEventTypePurpose.id',
    `code`                VARCHAR(3)   NOT NULL COMMENT 'Код исхода заболевания',
    `name`                VARCHAR(64)  NOT NULL COMMENT 'Описание исхода заболевания',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`eventPurpose_id`) REFERENCES `rbEventTypePurpose`(`id`)
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Исходы заболеваний';
''',
'''
ALTER TABLE Event
ADD `rbAcheResult_id` INT(11) NULL COMMENT 'Ссылка на исход заболевания rbAcheResult.id' AFTER `mesSpecification_id`,
ADD FOREIGN KEY (`rbAcheResult_id`) REFERENCES `rbAcheResult`(`id`);
''',
'''
ALTER TABLE Diagnostic
ADD `rbAcheResult_id` INT(11) NULL COMMENT 'Ссылка на исход заболевания rbAcheResult.id' AFTER `notes`,
ADD FOREIGN KEY (`rbAcheResult_id`) REFERENCES `rbAcheResult`(`id`);
''',
'''
ALTER TABLE rbEventTypePurpose
ADD `codePlace` VARCHAR(2) NULL COMMENT 'Код условий оказания мед.помощи' AFTER `name`;
''',
'''
CREATE TABLE IF NOT EXISTS `rbHospitalBedProfile_Service` (
    `id`                      INT(11)      NOT NULL AUTO_INCREMENT,
    `rbHospitalBedProfile_id` INT(11)      NOT NULL COMMENT 'Ссылка на профиль коек rbHospitalBedProfile.id',
    `rbService_id`            INT(11)      NOT NULL COMMENT 'Ссылка на услугу rbService.id',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`rbHospitalBedProfile_id`) REFERENCES `rbHospitalBedProfile`(`id`),
    FOREIGN KEY (`rbService_id`) REFERENCES `rbService`(`id`)
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Данные об услугах, соответствующих профилю койки';
''',
'''
DROP TABLE IF EXISTS `ActionProperty_HospitalBedProfile`;
CREATE TABLE IF NOT EXISTS `ActionProperty_HospitalBedProfile` (
    `id`                      INT(11)      NOT NULL COMMENT '{ActionProperty.id}',
    `index`                INT(11)      NOT NULL DEFAULT 0 COMMENT 'Индекс элемента векторного значения или 0',
    `value`                 INT(11)     NULL COMMENT 'Значение свойства действия {rbHospitalBedProfile.id}',
    PRIMARY KEY (`id`,`index`),
    INDEX `value` (`value`) 
) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Значение свойства действия типа «Профиль койки»';
''',
# DICOM Архив
'''
ALTER TABLE Action
ADD `dcm_study_uid` VARCHAR(50) NULL DEFAULT NULL COMMENT 'Внешний идентификатор записи в системе DICOM Архив';
'''
)

def upgrade(conn):
    global config    
    c = conn.cursor()
    
    for query in simple_queries:
        c.execute(query)
    
    
def downgrade(conn):
    pass
