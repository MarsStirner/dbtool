# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Для определения типа обращения создана новая таблица и поле в eventType
Также должно быть добавлено новое правило в таблицу rbUserRight: code=changeFinanceSource name=Имеет возможность изменять источники финансирования
'''

tbl = "Person"


def upgrade(conn):
    global tools
    sql = u'''\
CREATE TABLE rbRequestType ( id INT(11) NOT NULL AUTO_INCREMENT, 
    code VARCHAR(8) NOT NULL COMMENT 'Код', 
    name VARCHAR(64) NOT NULL COMMENT 'Наименование', 
    PRIMARY KEY (id), INDEX code (code), INDEX name (name) ) COMMENT='Типы обращений' COLLATE='utf8_general_ci';'''

    c = conn.cursor()
    c.execute(sql.format(tableName=tbl))

    sql = '''
ALTER TABLE EventType ADD COLUMN requestType_id INT(11) NULL DEFAULT NULL COMMENT 'тип обращения {rbRequestType}' AFTER age_ec;
'''
    tools.executeEx(c, sql, mode=['ignore_duplicates'])

def downgrade(conn):
    pass
