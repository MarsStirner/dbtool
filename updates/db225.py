#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
 Увеличение баркодов для ЛИС до 8-ми символов (для новых записей)
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sqls = [
            u"""DROP TRIGGER `TTJ_INSERT`;""",
            u"""
CREATE DEFINER = %s TRIGGER `TTJ_INSERT` BEFORE INSERT ON `TakenTissueJournal` FOR EACH ROW BEGIN
    DECLARE n_period INT;
    DECLARE n_barcode INT;
    IF NEW.barcode is NULL OR NEW.period is NULL THEN
        SELECT
            barcode, period
        INTO
            n_barcode, n_period
        FROM `TakenTissueJournal`
        ORDER BY `period` DESC, `barcode` DESC LIMIT 1;
        SET n_barcode = n_barcode + 1;
        IF n_barcode > 99999999 THEN
            SET n_period = n_period + 1;
            SET n_barcode = 10000000;
        END IF;
        SET NEW.barcode = n_barcode;
        SET NEW.period = n_period;
    END IF;
END;""" % config['definer'],
    ]

    for sql in sqls:
        c.execute(sql)
    
def downgrade(conn):
    pass
