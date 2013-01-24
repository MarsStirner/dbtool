#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавлен вид приема 
(амбулаторный пациент, пациент из стационара (прием в стационаре), пациент из стационара (прием в поликлинике), диагностика.)
'''

def upgrade(conn):
    global config    
    c = conn.cursor()

    sql = u'''
ALTER TABLE `Action` ADD COLUMN `AppointmentType` ENUM('0','amb','hospital','polyclinic','diagnostics','portal','otherLPU') NOT NULL COMMENT 'amb - амбулаторный пациент, hospital - пациент из стационара (прием в стационаре), polyclinic - пациент из стационара (прием в поликлинике), diagnostics - диагностика.'  AFTER `pacientInQueueType`; 
'''
    c.execute(sql)
    

    
def downgrade(conn):
    pass