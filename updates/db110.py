#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Восстановление целостности бд. В таблице ActionType записи с удаленными
group_id помечаются как удаленные
'''


def upgrade(conn):
    global config        
    c = conn.cursor()
    
    c.execute('SELECT id FROM ActionType WHERE id IN (SELECT DISTINCT group_id FROM ActionType) AND deleted=1')
    ids = [str(rec[0]) for rec in c.fetchall()]
    c.execute('UPDATE ActionType SET deleted=1 WHERE group_id IN (%s)' % ','.join(ids))
        

def downgrade(conn):
    pass