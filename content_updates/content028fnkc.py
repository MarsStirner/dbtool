#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Обновлённые тексты шаблонов печати для ФНКЦ
'''

MIN_SCHEMA_VERSION = 202


def upgrade(conn):
    import json
    import gzip

    print(u'Загонка обновленных текстов шаблонов и метаданных')
    with gzip.open('content_updates/content028.json.gz', 'rb') as fin:
        result = json.load(fin)
    with conn as cursor:
        for _id, [text, meta] in result.iteritems():
            cursor.execute('''UPDATE rbPrintTemplate SET templateText = %s WHERE id = %s''', (text, _id))
            if not cursor.rowcount:
                cursor.execute('''SELECT COUNT(1) FROM rbPrintTemplate WHERE id = %s''', (_id,))
                if cursor.fetchone()[0]:
                    print(u'Шаблон с id=%s не требует обновления' % _id)
                else:
                    print(u'Шаблон с id=%s не был найден в БД, потому пропущен' % _id)
                    continue
            for row in meta:
                cursor.execute('''
INSERT INTO rbPrintTemplateMeta
(`template_id`, `type`, `name`, `title`, `description`, `arguments`, `defaultValue`)
VALUES (%s, %s, %s, %s, %s, %s, %s)''', (_id,) + tuple(row))