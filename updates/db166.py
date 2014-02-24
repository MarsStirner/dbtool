#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Исправление поля ед. измерения дозы в таблице компонентов назначения
'''

def upgrade(conn):
    global config
    global tools
    c = conn.cursor()
    sql = '''
ALTER TABLE `DrugComponent`
CHANGE COLUMN `unit` `unit` INT(11) NOT NULL ,
ADD INDEX `fk_DrugComponent_rbUnit_idx` (`unit` ASC);
'''
    tools.executeEx(c, sql, mode=['empty_sql_mode',])

    sql = '''
ALTER TABLE `DrugComponent`
ADD CONSTRAINT `fk_DrugComponent_rbUnit`
  FOREIGN KEY (`unit`)
  REFERENCES `rbUnit` (`id`)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;
'''
    tools.executeEx(c, sql, mode=['disable_fk', 'empty_sql_mode',])
    c.close()

def downgrade(conn):
    pass