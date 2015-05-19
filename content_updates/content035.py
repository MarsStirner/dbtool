#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

__doc__ = '''\
Обновление MKB CоглаCно TMIS-636
'''

MIN_SCHEMA_VERSION = 208


def upgrade(conn):
    c = conn.cursor()

    print(u'Помечаем удаленные МКБ флагом deleted=1')

    sql = u'''
UPDATE `MKB` SET `deleted`=1
WHERE `DiagID` IN (
'C14.1',
'C83.2',
'C83.4',
'C83.6',
'C84.2',
'C84.3',
'C85.0',
'C91.2',
'C93.2',
'C94.1',
'C94.5',
'C95.2',
'C96.1',
'C96.3',
'I84',
'I84.0',
'I84.1',
'I84.2',
'I84.3',
'I84.4',
'I84.5',
'I84.6',
'I84.7',
'I84.8',
'I84.9',
'K35.0',
'K35.1',
'K35.9',
'L41.2',
'M72.3',
'M72.5',
'Q31.4',
'Q35.0',
'Q35.2',
'Q35.4',
'Q35.6',
'Q35.8',
'R50.0',
'R50.1'
);'''
    c.execute(sql)

    print(u'Добавляем новые МКБ')
    for row in _get_data():
        add_mkb(c, row)

    print(u'Обновляем диапазоны кодов')
    update_blocks(c)

    c.close()


def add_mkb(cursor, data):
    global tools
    _id = tools.checkRecordExists(cursor, 'MKB', 'DiagID = "{0}"'.format(data['DiagID']))
    if _id:
        query = u'''
        UPDATE `MKB` SET {0} WHERE id={1}
        '''.format(
            u', '.join(
                [u"{0}=%s".format(key) for key, value in data.items()]),
            _id)
    else:
        query = u'''
        INSERT INTO `MKB` ({0}) VALUES ({1})
        '''.format(', '.join(data.keys()), ', '.join(['%s'] * len(data)))

    cursor.execute(query, data.values())


def update_blocks(cursor):
    q = u'UPDATE `MKB` SET BlockID="(G10-G14)" WHERE BlockID="(G10-G13)";'
    cursor.execute(q)
    q = u'UPDATE `MKB` SET BlockID="(J09-J18)" WHERE BlockID="(J10-J18)";'
    cursor.execute(q)
    q = u'UPDATE `MKB` SET BlockID="(K55-K64)" WHERE BlockID="(K55-K63)";'
    cursor.execute(q)
    q = u'UPDATE `MKB` SET BlockID="(O94-O99)" WHERE BlockID="(O95-O99)";'
    cursor.execute(q)


def _get_data():
    mapper = ['ClassID', 'ClassName', 'BlockID', 'BlockName', 'DiagID', 'DiagName', 'Prim', 'sex']

    data = []

    with open('content_updates/content035_data.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=str(';'))
        for row in reader:
            _row = {mapper[k]: v.decode('utf-8') for k, v in enumerate(row)}
            if _row['sex']:
                _row['sex'] = int(_row['sex'])
            else:
                _row['sex'] = 0
            _row['age'] = ''
            _row['characters'] = 0
            _row['duration'] = 0
            data.append(_row)

    return data
