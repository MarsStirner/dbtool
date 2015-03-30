#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
добавление недостающего FOREIGN KEY EventType->rbRequestType
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
    ALTER TABLE EventType ADD CONSTRAINT `EventType_rbRequestType_FK` FOREIGN KEY (`requestType_id`) REFERENCES `rbRequestType`(`id`);
    '''
    c.execute(sql)
    c.close()

def downgrade(conn):
    c = conn.cursor()

    sql = '''
    ALTER TABLE EventType DROP FOREIGN KEY `EventType_rbRequestType_FK`;
    ALTER TABLE EventType DROP KEY `EventType_rbRequestType_FK`;
    '''
    c.execute(sql)
    c.close()