#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Добавление всех прав для работы с назначениями
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = u'''SELECT id FROM rbUserRight WHERE code IN (%s)''' % ','.join(["'clientPrescriptionsCreate'",
                                                                           "'clientPrescriptionsStatusUpdate'"])
    c.execute(sql)
    ids = [int(id_[0]) for id_ in c.fetchall()]
    if ids:
        sql = u'''DELETE FROM rbUserProfile_Right WHERE userRight_id IN (%s)''' % ','.join(map(str, ids))
        c.execute(sql)
 
        sql = u'''DELETE FROM rbUserRight WHERE id IN (%s)''' % ','.join(map(str, ids))
        c.execute(sql)

    rights = [('clientPrescriptionsRead', u'имеет возможность просматривать и печатать лист назначений'),
              ('clientPrescriptionsCreateOwn',  u'имеет возможность создавать новые назначения только в тех обращениях, где пользователь является ответственным'),
              ('clientPrescriptionsCreateAll',  u'имеет возможность создавать новые назначения во всех обращениях'),
              ('clientPrescriptionsEditOwn', u'имеет возможность редактировать, отменять назначения только в тех обращениях, где пользователь является ответственным'),
              ('clientPrescriptionsEditAll', u'имеет возможность редактировать, отменять назначения во всех обращениях'),
              ('clientPrescriptionsExecEditOwn', u'имеет возможность исполнять назначения только в рамках своего отделения ЛПУ'),
              ('clientPrescriptionsExecEditAll', u'имеет возможность исполнять назначения во всех отделениях ЛПУ'),
              ('clientPrescriptionsExecChangeOrgStruct', u'имеет возможность просматривать исполнения назначений в любом отделении ЛПУ в форме листа исполнений'),              
              ]
    sql = u'''INSERT IGNORE INTO `rbUserRight` (`code`,`name`) VALUES (%s, %s);'''
    c.executemany(sql, rights)

    c.close()


def downgrade(conn):
    pass
