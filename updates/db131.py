#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Дополнения к структуре БД для передачи в 1С назначений ЛС
'''

def upgrade(conn):

    c = conn.cursor()
    sql = u'''CREATE DEFINER=%s PROCEDURE `SendPrescriptionTo1C`(IN `action_id` INT, IN `master_id` INT)
              BEGIN
                IF master_id IS NOT NULL THEN
                  INSERT IGNORE INTO PrescriptionsTo1C SET PrescriptionsTo1C.action_id = action_id; 
                END IF;  
              END''' %config['definer']
    c.execute(sql)
    triggerEvents = ["Insert", "Update"]
    tables = ["DrugChart"] 
    sqlTemplate = u''' 
          CREATE DEFINER=%s TRIGGER `on%s%s` AFTER %s ON `%s` FOR EACH ROW BEGIN
             CALL SendPrescriptionTo1C(NEW.action_id, NEW.master_id);   
          END'''
    for triggerEvent in triggerEvents:
        for table in tables:
            c.execute(sqlTemplate % (config['definer'], triggerEvent, table, triggerEvent, table))

    c.close()


def downgrade(conn):
    pass