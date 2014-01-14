#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''
Добавление таблиц справочников
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
CREATE TABLE IF NOT EXISTS `rbAppointmentOrder` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(16) NOT NULL,
  `name` VARCHAR(128) NOT NULL,
  `TFOMScode_hosp` VARCHAR(16) DEFAULT '',
  `TFOMScode_account` VARCHAR(16) DEFAULT '',
  PRIMARY KEY (`id`),
  INDEX `code` (`code` ASC),
  INDEX `name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = 'Порядок обращения';
'''
    c.execute(sql)

    sql = '''
CREATE TABLE IF NOT EXISTS `rbRefusalReason` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(16) NOT NULL,
  `name` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `code` (`code` ASC),
  INDEX `name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = 'Причина отказа от госпитализации';
'''
    c.execute(sql)

    c.close()

def downgrade(conn):
    pass