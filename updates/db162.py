#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import traceback

__doc__ = '''
Проставление Action.AppointmenType для уже созданных записей на прием к врачу (portal, otherLPU)
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    try:
        c.execute(u"""UPDATE Action a 
						INNER JOIN ActionType atype ON a.actionType_id = atype.id
						INNER JOIN Event e ON e.id = a.event_id
						INNER JOIN EventType etype ON etype.id = e.eventType_id
						SET a.AppointmentType = 'otherLPU'
						WHERE 
						 atype.code = 'queue'
						AND
						 etype.code = 'queue'
						AND 
						 a.pacientInQueueType = 0
						AND 
						 a.createPerson_id IS NULL
						AND 
						 a.directionDate IS NOT NULL
						AND 
						 a.pacientInQueueType = 0
						AND 
						 (a.hospitalUidFrom <> '' AND a.hospitalUidFrom <> '0');
						 """)
		c.execute(u"""UPDATE Action a 
						INNER JOIN ActionType atype ON a.actionType_id = atype.id
						INNER JOIN Event e ON e.id = a.event_id
						INNER JOIN EventType etype ON etype.id = e.eventType_id
						SET a.AppointmentType = 'portal'
						WHERE 
						 atype.code = 'queue'
						AND
						 etype.code = 'queue'
						AND 
						 a.pacientInQueueType = 0
						AND 
						 a.createPerson_id IS NULL
						AND 
						 a.directionDate IS NOT NULL
						AND 
						 a.pacientInQueueType = 0
						AND 
						 (a.hospitalUidFrom = '' OR a.hospitalUidFrom = '0');
						 """)
		
    except:
         traceback.print_exc()

    c.close()

def downgrade(conn):
    pass