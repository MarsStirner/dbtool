#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import traceback
__doc__ = '''\
-  Создание таблицы "История изменения группы крови" '''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
        CREATE TABLE `BloodHistory` (
            `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор записи',
            `bloodDate` date NOT NULL COMMENT 'Дата установления',
            `client_id` int(11) NOT NULL COMMENT 'Пациент {Client}',
            `bloodType_id` int(11) NOT NULL COMMENT 'Группа крови {rbBloodType}',
            `person_id` int(11) NOT NULL COMMENT 'Сотрудник {Person}',
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='История изменения группы крови'; '''
    try:
        c.execute(sql)
    except:
        pass
    
def downgrade(conn):
    pass
