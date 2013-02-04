#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Перенос данных для работы типа CReferenceActionPropertyValueType из кучи таблиц в ActionProperty_Reference
- Создание видов для обратной совместимости
'''
__author__ = 'viruzzz-kun'

# Эти записи выпилены, потому как слишком опасны.

simple_queries = \
(
u'''
CREATE TABLE IF NOT EXISTS `ActionProperty_Reference`
(`id` INT(11) UNSIGNED NOT NULL COMMENT "{ActionProperty}",
 `index` INT(11) UNSIGNED NOT NULL DEFAULT 0 COMMENT "Индекс элемента векторного значения или 0",
 `value` INT(11) UNSIGNED NULL DEFAULT NULL COMMENT "Собственно значение {ActionPropertyType.valueDomain}",
 PRIMARY KEY (`id`, `index`)
 COMMENT "Значение свойства действия типа Reference"
)
''',
u'''
INSERT `ActionProperty_Reference` (`id`, `index`, `value`)
SELECT `id`, `index`, `value` FROM `ActionProperty_Action`;
''',
'''
INSERT `ActionProperty_Reference` (`id`, `index`, `value`)
SELECT `id`, `index`, `value` FROM `ActionProperty_rbFinance`;
''',
'''
INSERT `ActionProperty_Reference` (`id`, `index`, `value`)
SELECT `id`, `index`, `value` FROM `ActionProperty_rbReasonOfAbsence`;
''',
'''
DROP TABLE `ActionProperty_Action`;
''',
'''
DROP TABLE `ActionProperty_rbReasonOfAbsence`;
''',
'''
DROP TABLE `ActionProperty_rbFinance`;
''',
'''
DELETE
    FROM `ActionProperty_Reference`
    WHERE `id` NOT IN (SELECT `id` FROM `ActionProperty`);
''',
)
user_queries = \
('''
CREATE OR REPLACE
    ALGORITHM = TEMPTABLE
    DEFINER = `%s`@`%s` 
    SQL SECURITY DEFINER
    VIEW `ActionProperty_Action` (`id`, `index`, `value`)
    AS SELECT
            `ActionProperty_Reference`.`id`,
            `ActionProperty_Reference`.`index`,
            `ActionProperty_Reference`.`value`
        FROM `ActionProperty_Reference`
        INNER JOIN `ActionProperty` on `ActionProperty`.`id` = `ActionProperty_Reference`.`id`
        INNER JOIN `ActionPropertyType` on `ActionProperty`.`type_id` = `ActionPropertyType`.`id`
        WHERE `ActionPropertyType`.`typeName` = 'Reference' and `ActionPropertyType`.`valueDomain` = 'Action';
''',
'''
CREATE
    ALGORITHM = TEMPTABLE
    DEFINER = `%s`@`%s` 
    SQL SECURITY DEFINER
    VIEW `ActionProperty_rbReasonOfAbsence` (`id`, `index`, `value`)
    AS SELECT
            `ActionProperty_Reference`.`id`,
            `ActionProperty_Reference`.`index`,
            `ActionProperty_Reference`.`value`
        FROM `ActionProperty_Reference`
        INNER JOIN `ActionProperty` on `ActionProperty`.`id` = `ActionProperty_Reference`.`id`
        INNER JOIN `ActionPropertyType` on `ActionProperty`.`type_id` = `ActionPropertyType`.`id`
        WHERE `ActionPropertyType`.`typeName` = 'Reference' and `ActionPropertyType`.`valueDomain` = 'rbReasonOfAbsence';
''',
'''
CREATE
    ALGORITHM = TEMPTABLE
    DEFINER = `%s`@`%s` 
    SQL SECURITY DEFINER
    VIEW `ActionProperty_rbFinance` (`id`, `index`, `value`)
    AS SELECT
            `ActionProperty_Reference`.`id`,
            `ActionProperty_Reference`.`index`,
            `ActionProperty_Reference`.`value`
        FROM `ActionProperty_Reference`
        INNER JOIN `ActionProperty` on `ActionProperty`.`id` = `ActionProperty_Reference`.`id`
        INNER JOIN `ActionPropertyType` on `ActionProperty`.`type_id` = `ActionPropertyType`.`id`
        WHERE `ActionPropertyType`.`typeName` = 'Reference' and `ActionPropertyType`.`valueDomain` = 'rbFinance';
''',
)

def upgrade(conn):
    global config    
    
#    for query in simple_queries:
#        c = conn.cursor()
#        c.execute(query)
#        c.close()
#
#    for query in user_queries:
#        c = conn.cursor()
#        c.execute(query % (config['username'], config['host']))
#        c.close()

    c = conn.cursor()
    c.execute(u'''
CREATE TABLE IF NOT EXISTS `rbBloodComponentType` (
    `id`         INT(11)      NOT NULL AUTO_INCREMENT,
    `code`       VARCHAR(64)   NOT NULL COMMENT 'Код типа компонента крови',
    `name`       VARCHAR(128)  NOT NULL COMMENT 'Описание типа компонента крови',
    PRIMARY KEY (`id`)) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='Виды медицинской помощи'
''')
    c.execute(u'''
CREATE TABLE IF NOT EXISTS `ActionProperty_rbBloodType` (
    `id`         INT(11)      NOT NULL AUTO_INCREMENT,
    `index`      INT(11)      NOT NULL COMMENT 'Индекс векторного значения',
    `value`      INT(64)      NOT NULL COMMENT 'Указатель на запись rbBloodComponentType',
    PRIMARY KEY (`id`, `index`)) 
COLLATE='utf8_unicode_ci' ENGINE=InnoDB COMMENT='rbBloodComponentType'
''')
    c.close()



def downgrade(conn):
    pass
