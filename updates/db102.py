#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''
Табличные типы данных свойств действий
'''

sqls = [
ur'''
CREATE TABLE IF NOT EXISTS `rbAPTable` (
    `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(50) NOT NULL COMMENT 'Код для {ActionPropertyType.valueDomain}',
    `name` VARCHAR(256) NOT NULL COMMENT 'Отображаемое наименование таблицы',
    `tableName` VARCHAR(256) NOT NULL COMMENT 'Наименование отображаемой таблицы БД',
    `masterField` VARCHAR(256) NOT NULL COMMENT 'Наименование столбца для выборки отображаемой таблицы БД',
    PRIMARY KEY (`id`),
    UNIQUE INDEX `code` (`code`)
)
COMMENT='Описание выходной таблицы для отображения ActionProperty типа Table'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
''',
'''
CREATE TABLE IF NOT EXISTS `rbAPTableField` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `idx` INT(10) UNSIGNED NOT NULL COMMENT 'Положение столбца в отображенной таблице',
    `master_id` INT(11) UNSIGNED NOT NULL COMMENT '{rbAPTable.id}',
    `name` VARCHAR(256) NOT NULL COMMENT 'Отображаемое название столбца',
    `fieldName` VARCHAR(256) NOT NULL COMMENT 'Наименование столбца отображаемой таблицы БД',
    `referenceTable` VARCHAR(256) NULL DEFAULT NULL COMMENT 'Наименование таблицы справочника',
    PRIMARY KEY (`id`),
    INDEX `FK_rbAPTableField_rbAPTable` (`master_id`),
    CONSTRAINT `FK_rbAPTableField_rbAPTable` FOREIGN KEY (`master_id`) REFERENCES `rbAPTable` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
)
COMMENT='Описание столбца таблицы отображения для свойств действия Table'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
''',
'''
INSERT INTO `rbAPTable` (`id`, `code`, `name`, `tableName`, `masterField`) VALUES
    (1, 'TRFU_OIR', 'Ответ ТРФУ на запрос КК', 'trfuOrderIssueResult', 'action_id'),
    (2, 'TRFU_LM', 'Лабораторные измерения', 'trfuLaboratoryMeasure', 'action_id'),
    (3, 'TRFU_FV', 'Финальные объёмы', 'trfuFinalVolume', 'action_id');
''',
'''INSERT INTO `rbAPTableField` (`id`, `idx`, `master_id`, `name`, `fieldName`, `referenceTable`) VALUES
    (1, 0, 1, 'Ид. компонента', 'trfu_comp_id', NULL),
    (2, 1, 1, 'Номер компонента', 'comp_number', NULL),
    (3, 2, 1, 'Тип компонента', 'comp_type', 'rbBloodComponentType'),
    (4, 3, 1, 'Группа крови', 'blood_type_id', 'rbBloodType'),
    (5, 4, 1, 'Объём', 'volume', NULL),
    (6, 5, 1, 'Кол-во доз', 'dose_count', NULL),
    (7, 6, 1, 'Ид. донора', 'trfu_donor_id', NULL),
    (8, 0, 2, 'Тип лаб. измерений в системе ТРФУ', 'trfu_lab_measure_id', 'rbTrfuLaboratoryMeasureTypes'),
    (9, 1, 2, 'Ид. лабораторного измерения', 'time', NULL),
    (10, 2, 2, 'До процедуры', 'beforeOperation', NULL),
    (11, 3, 2, 'Во время процедуры', 'duringOperation', NULL),
    (12, 4, 2, 'В продукте афереза', 'inProduct', NULL),
    (13, 5, 2, 'После процедуры', 'afterOperation', NULL),
    (14, 0, 3, 'Длительность афереза', 'time', NULL),
    (15, 1, 3, 'Объём антикоагулянта', 'anticoagulantVolume', NULL),
    (16, 2, 3, 'inlet', 'inletVolume', NULL),
    (17, 3, 3, 'plasma', 'plasmaVolume', NULL),
    (18, 4, 3, 'collect', 'collectVolume', NULL),
    (19, 5, 3, 'AC в collect', 'anticoagulantInCollect', NULL),
    (20, 6, 3, 'AC в plasma', 'anticoagulantInPlasma', NULL);
''',]

def upgrade(conn):
    global config
    c = conn.cursor()
    map(c.execute, sqls)
    c.close()

def downgrade(conn):
    pass

