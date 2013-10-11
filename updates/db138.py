#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''DROP PROCEDURE `SendPrescriptionTo1C`''')

    sql = u'''CREATE DEFINER=%s PROCEDURE `SendPrescriptionTo1C`(IN `id` INT, IN is_prescription INT, IN `old_status` INT, IN `new_status` INT)
              BEGIN
                  DECLARE flag INT(1);   
                  SELECT count(*) INTO @flag FROM information_schema.TABLES WHERE TABLE_NAME = 'PrescriptionsTo1C';
                  IF @flag = 1 THEN 
                      SELECT count(*) INTO @flag FROM PrescriptionsTo1C WHERE PrescriptionsTo1C.interval_id = id;   
                      IF @flag = 0 THEN 
	                  INSERT IGNORE INTO PrescriptionsTo1C (PrescriptionsTo1C.interval_id, PrescriptionsTo1C.is_prescription, PrescriptionsTo1C.old_status, PrescriptionsTo1C.new_status) 
                                VALUES  (id, is_prescription, old_status, new_status); 
                      ELSE 
                          UPDATE `PrescriptionsTo1C` SET PrescriptionsTo1C.is_prescription = is_prescription, 
                                                         PrescriptionsTo1C.old_status = old_status,
                                                         PrescriptionsTo1C.new_status = new_status WHERE  PrescriptionsTo1C.interval_id = id;   
                      END IF; 
                  END IF; 
              END''' %config['definer']
    c.execute(sql)
    c.close()

def downgrade(conn):
    pass