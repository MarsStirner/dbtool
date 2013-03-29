#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение необходимое для отображения кнопки дежурного врача;
Изменение необходимое для работы справочника 'Орагнизации';
'''


def upgrade(conn):
    global config        
    c = conn.cursor()

    try:
        c.execute(u'''ALTER TABLE Organisation ADD COLUMN isOrganisation TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'является Организацией'  AFTER `miacCode` ;''')
    except:
        print('''Column 'isOrganisation' already exists.''')    

    c.execute(u"SET SQL_SAFE_UPDATES=0;")
    sql = u'''
UPDATE `ActionType`
SET
    flatCode = 'dutyDoctor'
WHERE
    `deleted`= 0 and `title` LIKE 'Осмотр дежурного врача'
'''

    c.execute(sql)
    c.execute(u"SET SQL_SAFE_UPDATES=1;")      


def downgrade(conn):
    pass
