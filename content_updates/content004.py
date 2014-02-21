#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import sys
import uuid
from MySQLdb import IntegrityError

__doc__ = '''\
Установка не создававшихся uuid для записей в таблице Person
'''


def upgrade(conn):
    c = conn.cursor()
    sql = u'''SELECT id from Person WHERE uuid_id = 0 order by id'''
    c.execute(sql)
    personIds = [id_[0] for id_ in c.fetchall()]
    numRecords = len(personIds)
    print("TOTAL: %s" % numRecords, end='\n')
    sys.stdout.flush()

    tableRanges = {'Person': iter(personIds)}

    i = 1
    ii = 0 # индекс в tableRanges

    while i <= numRecords:
        try:
            curTable = sorted(tableRanges.keys())[ii]
            dst_id = tableRanges[curTable].next()
        except StopIteration:
            ii += 1
            continue

        try:
            sql = '''INSERT INTO `UUID` (`uuid`) VALUES ("%s")''' % uuid.uuid4()
            c.execute(sql)
            last_id = conn.insert_id()
            sql = '''UPDATE `%s` SET uuid_id=%s where id=%s''' % (curTable, last_id, dst_id)
            c.execute(sql)
            i += 1
            if i % 100 == 0:
                print(".", end='')
                sys.stdout.flush()
            if i % 1000 == 0:
                print(str(i), end='')
                sys.stdout.flush()

        except IntegrityError:
            print('Opa, uuid duplicate!', end='')

    c.close()
