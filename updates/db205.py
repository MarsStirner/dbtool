#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление столбца для хранения id согласовавшего сотрудника в Action (Action.coordPerson_id) для Hippocrates
'''

def upgrade(conn):
    c = conn.cursor()
    sql = '''
    ALTER TABLE `Action`
        ADD COLUMN `coordPerson_id` INT(11) NULL AFTER `coordDate`,
        ADD INDEX `coord_person` (`coordPerson_id` ASC);
    '''
    c.execute(sql)
    sql = '''
    ALTER TABLE `Action`
        ADD CONSTRAINT `fk_coord_person`
        FOREIGN KEY (`coordPerson_id`)
        REFERENCES `Person` (`id`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION;
    '''
    c.execute(sql)

def downgrade(conn):
    c = conn.cursor()
    sql = '''
    ALTER TABLE `Action`
        DROP FOREIGN KEY `fk_coord_person`,
        DROP INDEX `coord_person`,
        DROP COLUMN `coordPerson_id`;
    '''
    c.execute(sql)