#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
добавление столбцов для хранения маски ввода серий и номеров документов и полисов
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
    ALTER TABLE `rbPolicyType`
    ADD COLUMN `serial_mask` VARCHAR(256) NULL AFTER `number_regexp`,
    ADD COLUMN `number_mask` VARCHAR(256) NULL AFTER `serial_mask`;
    '''
    c.execute(sql)

    sql = '''
    ALTER TABLE `rbDocumentType`
    ADD COLUMN `serial_mask` VARCHAR(256) NULL AFTER `number_regexp`,
    ADD COLUMN `number_mask` VARCHAR(256) NULL AFTER `serial_mask`;
    '''
    c.execute(sql)

    c.execute(u'''
UPDATE `rbDocumentType`
    SET `serial_mask` = '99 99'
    WHERE `code` = '1';''')

    c.execute(u'''
UPDATE `rbDocumentType`
    SET `number_mask` = '999999'
    WHERE `code` = '1';
''')
    c.close()


def downgrade(conn):
    pass