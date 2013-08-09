#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение кода полиса ОМС электронного образца для интеграции с УЭК.
Добавление столбца flatCode в таблицу rbPost.
Для должности заведующий заявлением установлен flatCode = 'departmentManager'.
Необходимо для вывода информации о заведующем отделения на печать.
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = u'''ALTER TABLE `rbPolicyType` CHANGE COLUMN `code` `code` VARCHAR(64) NOT NULL COMMENT 'Код';
    '''
    c.execute(sql)

    sql = u'''
UPDATE `rbPolicyType` SET `code`='cmiCommonElectron' WHERE `name` like '%единого образца';
'''
    c.execute(sql)

    c.execute(u'''SELECT * from `rbPolicyType` WHERE `code`='cmiCommonElectron';''')
    result = c.fetchone()
    if not result:
        sql = u'''INSERT INTO `rbPolicyType`
                    (`code`, `name`)
                     VALUES ('cmiCommonElectron','ОМС Электронный полис единого образца');'''
        c.execute(sql)

    sql = u'''ALTER TABLE `rbPost` ADD COLUMN `flatCode` VARCHAR(64) NOT NULL  AFTER `high`;
    '''
    c.execute(sql)

    sql = u'''UPDATE `rbPost` SET `flatCode`='departmentManager' WHERE `name` like 'Заведующий отделением';
    '''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass