# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Добавляет в таблицу Person столбец:
    - ученая степень сотрудника
Добавлена таблица-справчник учёных степеней
'''

tbl = "Person"


def upgrade(conn):
    sqlAddColumns = u'''\
ALTER TABLE {tableName}
    ADD COLUMN academicdegree_id INT(11) NULL DEFAULT NULL COMMENT 'Научная степень' AFTER typeTimeLinePerson;
'''

    c = conn.cursor()
    c.execute(sqlAddColumns.format(tableName=tbl))

    sql = '''
CREATE TABLE rbAcademicDegree (id INT(11) NOT NULL AUTO_INCREMENT, 
code VARCHAR(8) NOT NULL, name VARCHAR(64) NOT NULL, PRIMARY KEY (id));
'''
    c.execute(sql)

def downgrade(conn):
    pass

    c = conn.cursor()
    c.execute(sqlDropColumns.format(tableName=tbl))