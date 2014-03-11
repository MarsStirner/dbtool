#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Удаление поля в типе действия 'Сведение о родах'
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    chbirthinfo_id = tools.checkRecordExists(c, 'ActionType', 'flatCode = "СhildbirthInfo"')
    if chbirthinfo_id:
        apt_id = tools.checkRecordExists(c, 'ActionPropertyType',
                                         'actionType_id = %d and code = "manipulations"' % chbirthinfo_id)
        if apt_id:
            c.execute('UPDATE ActionPropertyType SET deleted = 1 WHERE id = %d' % apt_id)
    c.close()
