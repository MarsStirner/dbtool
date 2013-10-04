#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    alerts = (
       u'''DROP PROCEDURE `SendPrescriptionTo1C`''',
       u'''DROP TRIGGER `onUpdateDrugChart`''',
       u'''DROP TRIGGER `onInsertDrugChart`''')

    for sql in alerts:	
       c.execute(sql)

    sql = u'''CREATE DEFINER=%s PROCEDURE `SendPrescriptionTo1C`(IN `id` INT, IN is_prescription INT, IN is_new INT, IN `old_status` INT, IN `new_status` INT)
              BEGIN
                  DECLARE isPrescriptionsTo1C INT(1);   
                  SELECT count(*) INTO @isPrescriptionsTo1C FROM information_schema.TABLES WHERE TABLE_NAME = 'PrescriptionsTo1C';
                  IF @isPrescriptionsTo1C = 1 THEN 
	                  INSERT IGNORE INTO PrescriptionsTo1C (PrescriptionsTo1C.interval_id, PrescriptionsTo1C.is_prescription, PrescriptionsTo1C.is_new, PrescriptionsTo1C.old_status, PrescriptionsTo1C.new_status) 
                                VALUES  (id, is_prescription, is_new, old_status, new_status); 
                  END IF; 
              END''' %config['definer']
    c.execute(sql)
    triggerEvents = [ ""]
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `onInsertDrugChart` AFTER Insert ON `DrugChart` FOR EACH ROW BEGIN
             CALL SendPrescriptionTo1C(NEW.action_id, IF(NEW.master_id IS NULL, 1, 0), 1, NEW.status, NEW.status);   
          END''' %config['definer']
    c.execute(sql)
    sql = u''' 
          CREATE DEFINER=%s TRIGGER `onUpdateDrugChart` AFTER Update ON `DrugChart` FOR EACH ROW BEGIN
             CALL SendPrescriptionTo1C(NEW.action_id, IF(NEW.master_id IS NULL, 1, 0), 0, OLD.status, NEW.status);   
          END'''%config['definer']
    c.execute(sql)
    c.close()

def downgrade(conn):
    pass