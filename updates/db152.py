#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''DROP TRIGGER `onUpdateDrugChart`'''

    c.execute(sql)

    sql = u''' 
          CREATE DEFINER=%s TRIGGER `onUpdateDrugChart` AFTER Update ON `DrugChart` FOR EACH ROW BEGIN
             IF OLD.status != NEW.status THEN
                CALL SendPrescriptionTo1C(NEW.id, IF(NEW.master_id IS NULL, 1, 0), OLD.status, NEW.status);   
             END IF;
          END'''%config['definer']
    c.execute(sql)

    c.close()

def downgrade(conn):
    pass