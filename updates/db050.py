# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
Добавляет в таблицу Person столбец:
    - ученая степень сотрудника
Добавлена таблица-справчник учёных степеней
'''

tbl = "Person"


def upgrade(conn):
    global tools
    c = conn.cursor()
    
    sqlAddColumns = u'''\
ALTER TABLE {tableName}
    ADD COLUMN academicdegree_id INT(11) NULL DEFAULT NULL COMMENT 'Научная степень' AFTER typeTimeLinePerson;
'''
    tools.executeEx(c, sqlAddColumns.format(tableName=tbl), mode=['ignore_duplicates'])

    sql = '''
CREATE TABLE rbAcademicDegree (id INT(11) NOT NULL AUTO_INCREMENT, 
code VARCHAR(8) NOT NULL, name VARCHAR(64) NOT NULL, PRIMARY KEY (id));
'''
    c.execute(sql)

def downgrade(conn):
    pass
