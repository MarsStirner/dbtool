#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Как должна выглядеть таблица rbRequestType
'''

def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute(u"SET SQL_SAFE_UPDATES=0;")
    c.execute("TRUNCATE rbRequestType;")
    c.execute(u"SET SQL_SAFE_UPDATES=1;")
    sql = u'''INSERT INTO rbRequestType(`id`, `code`, `name`) VALUES (%s, %s, %s)'''   
    data = [(1, 'clinic', u'Дневной стационар'),
            (2, 'hospital', u'Круглосуточный стационар'),
            (3, 'policlinic', u'Поликлиника'),
            (4, '4', u'Диагностика'),
            (5, '5', u'Диспансеризация'),
            (6, '6', u'Консультативный'),
            (7, 'stationary', u'Стационар')
            ]
    c.executemany(sql, data)    
    
def downgrade(conn):
    pass

