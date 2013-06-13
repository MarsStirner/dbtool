#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Удаление типов *Epicrisis* с заменой на Html
- Удаление типов Blank* и Проба с заменой на String
'''

sqls = [
    u'''update ActionPropertyType set typeName = 'Html', valueDomain = '*1' where typeName = 'DiagnosticEpicrisis';''',
    u'''update ActionPropertyType set typeName = 'Html', valueDomain = '*1p' where typeName = 'DiagnosticEpicrisisPartitional';''',
    u'''update ActionPropertyType set typeName = 'Html', valueDomain = '*2' where typeName = 'CureEpicrisis';''',
    u'''update ActionPropertyType set typeName = 'Html', valueDomain = '*2p' where typeName = 'CureEpicrisisPartitional';''',
    u'''update ActionPropertyType set typeName = 'String', code = 'blankSerial' where typeName = 'BlankSerial';''',
    u'''update ActionPropertyType set typeName = 'String', code = 'blankNumber' where typeName = 'BlankNumber';''',
    u'''update ActionPropertyType set typeName = 'String', code = 'sample' where typeName = 'Проба';''',
    u'''INSERT IGNORE INTO ActionProperty_String SELECT * FROM ActionProperty_CureEpicrisis;''',
    u'''INSERT IGNORE INTO ActionProperty_String SELECT * FROM ActionProperty_DiagnosticEpicrisis;''',
    u'''DROP TABLE ActionProperty_CureEpicrisis;''',
    u'''DROP TABLE ActionProperty_DiagnosticEpicrisis;''',

]


def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u"SET SQL_SAFE_UPDATES=0;")
    for sql in sqls:
        c.execute(sql)
    c.execute(u"SET SQL_SAFE_UPDATES=1;")


def downgrade(conn):
    pass
