#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Новые колонки для организации
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `Organisation`
CHANGE COLUMN `isHospital` `isHospital` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Является стационаром (поле могло использоваться также для определения ЛПУ, поэтому его использование нецелесообразно в новых клиентах)' ,
CHANGE COLUMN `isOrganisation` `isOrganisation` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'является Организацией (которая относится к месту работы пациента)' ,
ADD COLUMN `isLPU` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Является лечебным учреждением',
ADD COLUMN `isStationary` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Является стационаром (имеет стационарное отделение)',
ADD INDEX `isLPU` (`isLPU` ASC),
ADD INDEX `isStationary` (`isStationary` ASC);
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass