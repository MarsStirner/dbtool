#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- добавление столбцов для хранения форматов серий и номеров документов в виде регулярных выражений
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute('''
ALTER TABLE `rbDocumentType`
    ADD COLUMN `serial_regexp` VARCHAR(256) DEFAULT '.*' AFTER `TFOMSCode`,
    ADD COLUMN `number_regexp` VARCHAR(256) DEFAULT '.*' AFTER `serial_regexp`;
''')

    c.execute('''
ALTER TABLE `rbPolicyType`
    ADD COLUMN `serial_regexp` VARCHAR(256) DEFAULT '.*' AFTER `TFOMSCode`,
    ADD COLUMN `number_regexp` VARCHAR(256) DEFAULT '.*' AFTER `serial_regexp`;
''')

    c.execute(u'''
UPDATE `rbDocumentType`
    SET `serial_regexp` = '^[IVXLCDM]+ [а-яА-Я]+$'
    WHERE `serial_format` = 1;
''')

    c.execute(u'''
UPDATE `rbDocumentType`
    SET `number_regexp` = '^[IVXLCDM]+ [а-яА-Я]+$'
    WHERE `number_format` = 1;
''')

    c.execute(u'''
UPDATE `rbDocumentType`
    SET `serial_regexp` = '^\\\\d+ \\\\d+$'
    WHERE `serial_format` = 2;
''')

    c.execute(u'''
UPDATE `rbDocumentType`
    SET `number_regexp` = '^\\\\d+ \\\\d+$'
    WHERE `number_format` = 2;
''')

    c.close()


def downgrade(conn):
    pass