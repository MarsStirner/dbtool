#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- http://helpdesk.korusconsulting.ru/browse/MIS-308 - решение гонок при создании новой записи в журнале забора БМ
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sqls = [
            u"""
CREATE DEFINER = %s TRIGGER `TTJ_INSERT` BEFORE INSERT ON `TakenTissueJournal` FOR EACH ROW BEGIN
    DECLARE n_period INT;
    DECLARE n_barcode INT;
    IF NEW.barcode = NULL OR NEW.period = NULL THEN
        SELECT
            barcode, period
        INTO
            n_barcode, n_period
        FROM `TakenTissueJournal`
        ORDER BY `period` DESC, `barcode` DESC LIMIT 1;
        SET n_barcode = n_barcode + 1;
        IF n_barcode > 999999 THEN
            SET n_period = n_period + 1;
            SET n_barcode = 100000;
        END IF;
        SET NEW.barcode = n_barcode;
        SET NEW.period = n_period;
    END IF;
END;""" % config['definer'],
            u"""
ALTER TABLE `TakenTissueJournal`
    CHANGE COLUMN `barcode` `barcode` INT(11) NOT NULL AFTER `note`,
    CHANGE COLUMN `period` `period` INT(11) NOT NULL AFTER `barcode`;""",
    ]

    for sql in sqls:
        c.execute(sql)
    
def downgrade(conn):
    pass
