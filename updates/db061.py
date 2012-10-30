#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
DROP TRIGGER IF EXISTS `INCREMENT_Event_RECORD_VERSION_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
DROP TRIGGER IF EXISTS `Delete_Action_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `INCREMENT_Event_RECORD_VERSION_ON_UPDATE`
BEFORE UPDATE ON `Event`
FOR EACH ROW
BEGIN
    SET NEW.version = OLD.version + 1;
END;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `Delete_Action_ON_UPDATE`
AFTER UPDATE ON `Event`
FOR EACH ROW
BEGIN
    IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
        UPDATE Action
        SET deleted = NEW.deleted
        WHERE event_id = NEW.id;
    END IF;

END;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
DROP TRIGGER IF EXISTS `INCREMENT_Action_RECORD_VERSION_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
DROP TRIGGER IF EXISTS `Delete_ActionProperty_ON_UPDATE`;
'''
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `INCREMENT_Action_RECORD_VERSION_ON_UPDATE`
BEFORE UPDATE ON `Action`
FOR EACH ROW
BEGIN
    SET NEW.version = OLD.version + 1;
END;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE
DEFINER=`%s`@`%s`
TRIGGER `Delete_ActionProperty_ON_UPDATE`
AFTER UPDATE ON `Action`
FOR EACH ROW
BEGIN
    IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted THEN
        UPDATE ActionProperty
        SET deleted = NEW.deleted
        WHERE action_id = NEW.id;
    END IF;
END;
''' % (config['username'], config['host'])

    c.execute(sql)
    
    sql = u'''
CREATE TABLE `action_document` (
    `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор документа',
    `action_id` INT(11) NOT NULL COMMENT 'Идентификатор Действия {Action}',
    `modify_date` DATETIME NOT NULL COMMENT 'Дата изменения документа',
    `template_id` INT(11) NOT NULL COMMENT 'Шаблон, по которому составлен документ {rbPrintTemplates}',
    `document` MEDIUMBLOB NOT NULL COMMENT 'Документ, сжатый gzip',
    PRIMARY KEY (`id`),
    INDEX `action_id` (`action_id`),
    INDEX `FK_action_document_rbprinttemplate` (`template_id`),
    CONSTRAINT `FK_action_document_action` FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`),
    CONSTRAINT `FK_action_document_rbprinttemplate` FOREIGN KEY (`template_id`) REFERENCES `rbPrintTemplate` (`id`)
)
COMMENT='Таблица отрендеренных документов от Action-ов, версионная. Документы хранятся сжатыми алгоритмом gzip.'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE `rbSpecialVariablesPreferences` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`name` varchar(64) NOT NULL COMMENT 'название',
`query` text NOT NULL COMMENT 'запрос',
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='Специальные переменные';
'''
    c.execute(sql)

    sql = u'''CREATE TABLE `VariablesforSQL` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`specialVarName_id` int(11) NOT NULL COMMENT 'имя специальной переменной',
`name` varchar(64) NOT NULL COMMENT 'наименование',
`var_type` varchar(64) NOT NULL COMMENT 'тип',
`label` varchar(64) NOT NULL COMMENT 'метка',
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='Переменные для получения значений специальных переменных с п';
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE ClientDocument CHANGE COLUMN origin origin VARCHAR(256) NOT NULL COMMENT 'Организация выдавшая документ';
'''
    c.execute(sql)


def downgrade(conn):
    pass
