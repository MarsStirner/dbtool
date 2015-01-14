#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Обновлённые тексты шаблонов печати для ФНКЦ
'''

MIN_SCHEMA_VERSION = 205


def upgrade(conn):
    from .content033 import upgrade as c_upgrade, __doc__ as c_doc
    import json
    import gzip
    print(c_doc)
    c_upgrade(conn)

    print(u'Загонка обновленных текстов шаблонов и метаданных')
    with gzip.open('content033.json.gz', 'rb') as fin:
        result = json.load(fin)
    with conn as cursor:
        for _id, [text, meta] in result.iteritems():
            cursor.execute('''UPDATE rbPrintTemplate SET templateText = %s WHERE id = %s''', (text, _id))
            if not cursor.rowcount:
                cursor.execute('''SELECT COUNT(1) FROM rbPrintTemplate WHERE id = %s''', (_id,))
                if cursor.fetchone()[0]:
                    print(u'Шаблон с id=%s не требует обновления')
                else:
                    print(u'Шаблон с id=%s не был найден в БД, потому пропущен', _id)
                    continue
            for row in meta:
                cursor.execute('''
INSERT INTO rbPrintTemplateMeta
(`template_id`, `type`, `name`, `title`, `description`, `arguments`, `defaultValue`)
VALUES (%s, %s, %s, %s, %s, %s, %s)''', (_id,) + tuple(row))