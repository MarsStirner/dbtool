#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Ещё несколько изменений для FlatDirectory
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    sqls = [
            u"ALTER TABLE ClientDocument CHANGE COLUMN origin origin VARCHAR(256) NOT NULL COMMENT 'Организация выдавшая документ';"
            u"ALTER TABLE Client_Quoting ADD COLUMN version INT(11) UNSIGNED NOT NULL COMMENT 'Версия данных' AFTER prevTalon_event_id ;" 
            u"ALTER TABLE rbRequestType CHANGE COLUMN code code VARCHAR(32) NOT NULL COMMENT 'Код';"
            u"ALTER TABLE FDRecord DROP FOREIGN KEY FK_FDRecord_FlatDictionary ;"
            u"ALTER TABLE FDRecord CHANGE COLUMN flatDictionary_id flatDirectory_id INT(10) UNSIGNED NOT NULL COMMENT 'id справочника из таблицы FlatDictionaryID', ADD CONSTRAINT FK_FDRecord_FlatDirectory FOREIGN KEY (flatDirectory_id) REFERENCES FlatDirectory (id);"
            u"ALTER TABLE ActionProperty_FlatDirectory RENAME TO  ActionProperty_FDRecord ;"
            u"ALTER TABLE ClientDocument CHANGE COLUMN endDate endDate DATE NULL DEFAULT NULL COMMENT 'Срок окончания действия документа';"
    ]

    for sql in sqls:
        c.execute(sql)
    
def downgrade(conn):
    pass
