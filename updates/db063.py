#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Особое поле в таблице Event для связи обращений (поликлинических) с конкретной оргструктурой
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `Event` ADD COLUMN `orgStructure_id` INT(11) NULL DEFAULT NULL;
'''
    c.execute(sql)

def downgrade(conn):
    pass
