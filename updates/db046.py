# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Добавляет AUTO_INCREMENT к первичному ключу таблицы Setting\
'''

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows


def downgrade(conn):
    pass


def upgrade(conn):
    sql = [
        # Добавляет AUTO_INCREMENT к первичному ключу таблицы Setting
        u"""ALTER TABLE Setting MODIFY id MEDIUMINT NOT NULL AUTO_INCREMENT;
""",
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)
