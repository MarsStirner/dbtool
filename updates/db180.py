#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Создание таблиц для хранения информации о зависимостях при отображении одних полей от других
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    sql = u'''
    CREATE TABLE IF NOT EXISTS `ActionPropertyRelations`
    ( `id` INT NOT NULL AUTO_INCREMENT,
    `Subject` INT(11) NOT NULL COMMENT 'Ссылка на родительское свойство
        типа действия.',
    `Object` INT(11) NOT NULL COMMENT 'Ссылка на дочернее свойство типа
        действия',
    `RelationType` ENUM('bool', 'equals', 'in', 'nin', 'lt', 'gt')
        NOT NULL COMMENT
    'bool - для логических условий (True)
    equals - для точного совпадения значений (=)
    lt - меньше чем(<)
    gt - больше чем (>)
    has_value - имеет значение
    in - в каком-то множестве значений
    nin - не в каком-то множестве значений',
    `RelationState` ENUM('show', 'available', 'required') NOT NULL COMMENT '
    show - показать свойство типа действия
    available - сделать доступным свойство типа действия
    Доступность - это подмножество понятия "показать".
    Можно сначала показать, потом сделать доступным (например, для выбора
        или редактирования)
    required - обязательно для заполнения',
    PRIMARY KEY (`id`),
    INDEX `fk_ActionPropertyRelations_ActionPropertyObject_idx`
        (`Object` ASC),
    INDEX `fk_ActionPropertyRelations_ActionPropertySubject_idx`
        (`Subject` ASC),
    INDEX `fk_ActionPropertyRelations_ActionPropertyObjectSubject_idx`
        (`Object` ASC, `Subject` ASC),
    CONSTRAINT `fk_ActionPropertyRelations_ActionPropertyObject`
        FOREIGN KEY(`Object`)
        REFERENCES `ActionPropertyType` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `fk_ActionPropertyRelations_ActionPropertySubject`
        FOREIGN KEY (`Subject`)
        REFERENCES `ActionPropertyType` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE) ENGINE = InnoDB;
    '''
    c.execute(sql)

    sql = u'''
    CREATE TABLE IF NOT EXISTS `APRelations_Value` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `ActionPropertyRelations_id` INT NOT NULL
        COMMENT 'Ссылка на запись в таблице отношений между аттрибутами
        {ActionPropertyRelations}',
    `RefType` ENUM('FlatDirectory', 'Action', 'Event') NULL DEFAULT NULL
        COMMENT 'Тип ссылки на другую таблицу или объект.',
    `valueReference` int(11) NULL DEFAULT NULL
        COMMENT 'Значение ссылки на другую таблицу или объект.',
    `valueDate` DATE NULL DEFAULT NULL
        COMMENT 'Поле, если значение является не ссылкой на
        другой объект и имеет тип - дата.',
    `valueFloat` FLOAT NULL DEFAULT NULL
        COMMENT 'Поле, если значение является не ссылкой на
        другой объект и имеет тип - число.',
    `valueString` VARCHAR(200) NULL DEFAULT NULL
        COMMENT 'Поле, если значение является не ссылкой на
        другой объект и имеет тип - строка.',
    PRIMARY KEY (`id`),
    INDEX `fk_APRelations_Value_ActionPropertyRelations1_idx`
    (`ActionPropertyRelations_id` ASC),
    CONSTRAINT `fk_APRelations_Value_ActionPropertyRelations1`
    FOREIGN KEY (`ActionPropertyRelations_id`)
    REFERENCES `ActionPropertyRelations` (`id`)
    ON DELETE CASCADE ON UPDATE CASCADE) ENGINE = InnoDB;
    '''
    c.execute(sql)

def downgrade(conn):
    pass
