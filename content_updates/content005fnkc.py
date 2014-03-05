#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Удаление дубликатов документов, удостоверяющих личность
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = """
    UPDATE ClientDocument SET deleted=1 WHERE id IN
        (SELECT id FROM (
            SELECT
            cd.id
            FROM
            ClientDocument cd,
            (
                SELECT min(id) last_id, client_id, documentType_id, serial, number, origin, COUNT(*) num_of_eq
                FROM ClientDocument
                GROUP BY client_id, documentType_id, serial, number, origin HAVING count(*) > 1
            ) sub1
            WHERE
                cd.id <> sub1.last_id AND
                sub1.client_id=cd.client_id AND
                sub1.documentType_id=cd.documentType_id AND
                sub1.serial=cd.serial AND
                sub1.number=cd.number AND
                sub1.origin=cd.origin
            ) x);
"""
    tools.executeEx(c, sql, mode=['safe_updates_off',])

    c.close()
