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
    
    c.execute('SELECT id, group_id, deleted FROM ActionType') 
    all_records = [(int(id_), gr_id, d) for id_, gr_id, d in c.fetchall()]
    all_groups = [gr_id for id_, gr_id, d in all_records]
    deleted_groups = set([id_ for id_, gr_id, d in all_records if id_ in all_groups and d == 1])

    ids_to_delete = set()
    while deleted_groups:
        check_id = deleted_groups.pop()
        for id_, gr_id, d in all_records:
            if gr_id == check_id:
                ids_to_delete.add(id_)
                deleted_groups.add(id_)
    ids_str = [str(id_) for id_ in list(ids_to_delete)]
    print(ids_str)
    if ids_str:
        c.execute('UPDATE ActionType SET deleted=1 WHERE id IN (%s)' % ','.join(ids_str))
            
    
def downgrade(conn):
    pass