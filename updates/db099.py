#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Перенос типов действий, связанных с записью между ЛПУ (Направление [на осмотр]...)
из Движения в Медицинские документы (ActionType.class 3 -> 0)
'''

direction_code = '4100'
medDoc_class = 0

def upgrade(conn):
    global config        
    c = conn.cursor()
    
    c.execute(u'''SELECT id FROM ActionType where code="%s" and group_id IS NULL''' % direction_code)
    
    result = c.fetchall()
    if result:
        direction_at_ids = [res[0] for res in result]
        ids_cond = ','.join([str(id_) for id_ in direction_at_ids])
        c.execute(u'''UPDATE ActionType SET class=%s where id IN (%s)''' % (medDoc_class, ids_cond))
        c.execute(u'''UPDATE ActionType SET class=%s where group_id IN (%s)''' % (medDoc_class, ids_cond))
    
        
def downgrade(conn):
    pass
