#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение схемы связывания услуг и типов действий. Для корректной работы необходима миграция из 35 обновления контента.
'''


def upgrade(conn):
    c = conn.cursor()

    c.execute('set sql_safe_updates = 0;')
    # удаление ненужных данных
    sql = '''DELETE FROM ActionType_Service WHERE service_id IS NULL;'''
    c.execute(sql)
    sql = '''DELETE ats FROM ActionType_Service ats LEFT JOIN ActionType at on ats.master_id = at.id WHERE at.id IS NULL;'''
    c.execute(sql)
    sql = '''DELETE ats FROM ActionType_Service ats LEFT JOIN rbService s ON ats.service_id = s.id WHERE s.id IS NULL;'''
    c.execute(sql)
    c.execute('set sql_safe_updates = 1;')

    sql = '''ALTER TABLE `ActionType_Service`
DROP COLUMN `finance_id`,
CHANGE COLUMN `service_id` `service_id` INT(11) NOT NULL COMMENT 'услуга {rbService}',
ADD COLUMN `begDate` DATE NOT NULL AFTER `service_id`,
ADD COLUMN `endDate` DATE NULL DEFAULT NULL AFTER `begDate`,
DROP INDEX `finance_id` ;'''
    c.execute(sql)
    sql = '''ALTER TABLE `ActionType_Service`
ADD CONSTRAINT `fk_actiontype_service_actiontype`
  FOREIGN KEY (`master_id`)
  REFERENCES `ActionType` (`id`)
  ON DELETE CASCADE
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_actiontype_service_rbservice`
  FOREIGN KEY (`service_id`)
  REFERENCES `rbService` (`id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass