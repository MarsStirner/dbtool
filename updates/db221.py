#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
hotfix для интеграции ядра и 1C Аптеки (увеличить макс размер поля для описания ошибки)
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''ALTER TABLE `Pharmacy` CHANGE COLUMN `error_string` `error_string` TEXT NULL DEFAULT NULL COMMENT 'Строка с ошибкой вернувшейся из 1С' AFTER `result`;
'''
    c.execute(sql)   

    c.close()


def downgrade(conn):
    pass