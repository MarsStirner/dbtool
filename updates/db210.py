#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление таблиц для работы прикрепления файлов
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
CREATE TABLE IF NOT EXISTS `FileGroupDocument` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NULL DEFAULT NULL COMMENT 'Наименование',
  `begDate` DATE NULL DEFAULT NULL COMMENT 'Дата начала действия',
  `endDate` DATE NULL DEFAULT NULL COMMENT 'Дата окончания действия',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Группа файлов, образующих один документ';
'''
    c.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `FileMeta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL COMMENT 'отображаемое имя',
  `mimetype` VARCHAR(128) NOT NULL DEFAULT '' COMMENT 'Internet media type',
  `path` varchar(256) DEFAULT NULL COMMENT 'путь до места нахождения, если храннение осуществляется средствами МИС',
  `external_id` int(11) DEFAULT NULL COMMENT 'идентификатор файла во внешней системе, если храннение осуществляется средствами другой системы, например, ЗХПД',
  `filegroup_id` int(11) NOT NULL COMMENT '{FileGroupDocument}',
  `idx` int(11) NOT NULL DEFAULT '0' COMMENT 'порядковый номер файла в группе файлов',
  `deleted` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Признак удаления',
  PRIMARY KEY (`id`),
  KEY `fk_filemeta_filegroupdocument_idx` (`filegroup_id`),
  CONSTRAINT `fk_filemeta_filegroupdocument`
    FOREIGN KEY (`filegroup_id`)
    REFERENCES `FileGroupDocument` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COMMENT='Информация об абстрактном файле, связанным с данными МИС';
'''
    c.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `ClientFileAttach` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `client_id` INT(11) NOT NULL COMMENT '{Client}',
  `filegroup_id` INT(11) NOT NULL COMMENT '{FileGroupDocument}',
  `deleted` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Признак удаления',
  `attachDate` DATETIME NOT NULL COMMENT 'Дата прикрепления',
  `documentType_id` INT(11) NULL DEFAULT NULL COMMENT '{rbDocumentType} тип документа',
  `relationType_id` INT(11) NULL DEFAULT NULL COMMENT '{rbRelationType} документ относится к родственнику пациента',
  PRIMARY KEY (`id`),
  KEY `fk_clientfileattach_rbdocumenttype_idx` (`documentType_id`),
  KEY `fk_clientfileattach_rbrelationtype_idx` (`relationType_id`),
  KEY `fk_clientfileattach_client` (`client_id`),
  KEY `fk_clientfileattach_filegroupdocument_idx` (`filegroup_id`),
  CONSTRAINT `fk_clientfileattach_filegroupdocument` FOREIGN KEY (`filegroup_id`)
      REFERENCES `FileGroupDocument` (`id`)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT `fk_clientfileattach_client` FOREIGN KEY (`client_id`)
      REFERENCES `Client` (`id`)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
  CONSTRAINT `fk_clientfileattach_rbdocumenttype` FOREIGN KEY (`documentType_id`)
      REFERENCES `rbDocumentType` (`id`)
      ON DELETE SET NULL
      ON UPDATE CASCADE,
  CONSTRAINT `fk_сlientfileattach_rbrelationtype`
      FOREIGN KEY (`relationType_id`)
      REFERENCES `rbRelationType` (`id`)
      ON DELETE SET NULL
      ON UPDATE CASCADE)
ENGINE=INNODB
DEFAULT CHARSET=UTF8
COMMENT='Информация об относящихся к пациенту файлах';
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `ClientDocument`
ADD COLUMN `cfa_id` INT(11) NULL DEFAULT NULL COMMENT '{ClientFileAttach}' AFTER `endDate`,
ADD INDEX `fk_clientdocument_clientfileattach_idx` (`cfa_id` ASC);
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `ClientDocument`
ADD CONSTRAINT `fk_clientdocument_clientfileattach`
  FOREIGN KEY (`cfa_id`)
  REFERENCES `ClientDocument` (`id`)
  ON DELETE SET NULL
  ON UPDATE CASCADE;
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `ClientPolicy`
ADD COLUMN `cfa_id` INT(11) NULL DEFAULT NULL COMMENT '{ClientFileAttach}' AFTER `version`,
ADD INDEX `fk_clientpolicy_clientfileattach_idx` (`cfa_id` ASC);
'''
    c.execute(sql)

    sql = '''
ALTER TABLE `ClientPolicy`
ADD CONSTRAINT `fk_clientpolicy_clientfileattach`
  FOREIGN KEY (`cfa_id`)
  REFERENCES `ClientFileAttach` (`id`)
  ON DELETE SET NULL
  ON UPDATE CASCADE;
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass