# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Для определения типа обращения создана новая таблица и поле в eventType
Также должно быть добавлено новое правило в таблицу rbUserRight: code=changeFinanceSource name=Имеет возможность изменять источники финансирования
'''

tbl = "Person"


def upgrade(conn):
    sqlAddColumns = u'''\
CREATE TABLE rbRequestType ( id INT(11) NOT NULL AUTO_INCREMENT, 
    code VARCHAR(8) NOT NULL COMMENT 'Код', 
    name VARCHAR(64) NOT NULL COMMENT 'Наименование', 
    PRIMARY KEY (id), INDEX code (code), INDEX name (name) ) COMMENT='Типы обращений' COLLATE='utf8_general_ci';'''

    c = conn.cursor()
    c.execute(sqlAddColumns.format(tableName=tbl))

    sql = '''
ALTER TABLE EventType ADD COLUMN requestType_id INT(11) NULL DEFAULT NULL COMMENT 'тип обращения {rbRequestType}' AFTER age_ec;
'''
    c.execute(sql)

def downgrade(conn):
    pass

    c = conn.cursor()
    c.execute(sqlDropColumns.format(tableName=tbl))