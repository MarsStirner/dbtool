# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Добавляет в таблицу TakenTissueJournal столбцы:
    - штрихкод (barcode)
    - номер последовательности штрихкодов (period)
'''

tbl = "TakenTissueJournal"


def upgrade(conn):
    sqlAddColumns = u'''\
ALTER TABLE {tableName}
    ADD COLUMN `barcode` INT NOT NULL DEFAULT '100000',
    ADD COLUMN `period` INT DEFAULT '0';
'''

    c = conn.cursor()
    c.execute(sqlAddColumns.format(tableName=tbl))


def downgrade(conn):
    sqlDropColumns = '''\
ALTER TABLE {tableName}
    DROP COLUMN `barcode`,
    DROP COLUMN `period`
'''

    c = conn.cursor()
    c.execute(sqlDropColumns.format(tableName=tbl))
