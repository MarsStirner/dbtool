#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Удаление дубликатов документов, удостоверяющих личность и внесение foreign key
'''


def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute(u"""DELETE FROM ClientDocument WHERE client_id NOT IN (SELECT id FROM Client);""")
    c.execute(u"""ALTER TABLE ClientDocument ADD CONSTRAINT FK__ClientDocument_Client FOREIGN KEY (client_id) references Client(id) ON DELETE CASCADE ON UPDATE CASCADE;""")
    c.execute(u"""
    UPDATE ClientDocument SET deleted=1 WHERE id IN
        (SELECT id FROM (
            SELECT
            cd.id
            FROM
            ClientDocument cd,
            (
                SELECT min(id) last_id, client_id, documentType_id, number, origin, COUNT(*) num_of_eq
                FROM ClientDocument
                GROUP BY client_id, documentType_id, number, origin HAVING count(*) > 1
            ) sub1
            WHERE
                cd.id <> sub1.last_id AND
                sub1.client_id=cd.client_id AND
                sub1.documentType_id=cd.documentType_id AND
                sub1.number=cd.number AND
                sub1.origin=cd.origin
            ) x);
""")

    c.close()
