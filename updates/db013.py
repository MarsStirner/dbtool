# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Удаляет записи со ссылкой на несуществующие записи из rbThesaurus
'''

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def execute(conn, sql):
    c = conn.cursor()
    c.execute(sql)

def upgrade(conn):
    # Создаём таблицу для списка профилей
    sqlSelectNotExisting = '''\
select t1.id from 
rbThesaurus t1
where
t1.group_id is not null
and
not exists (select * from rbThesaurus t2 where t2.id = t1.group_id)
'''
    sqlDeleteThesaurus = '''\
    delete from rbThesaurus where
    id = {id}
'''
    rows = query(conn, sqlSelectNotExisting)
    for r in rows:
	execute(conn, sqlDeleteThesaurus.format(id=r[0]))

def downgrade(conn):
    pass
