# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
БД без версионирования схемы

Не важно, что конкретно хранится сейчас в БД. Главное, что в ней нет таблицы
`Meta` для хранения метаданных. По умолчанию считается, что версия базы без
такой таблицы равна "000".
'''


def upgrade(conn):
    pass

def downgrade(conn):
    pass