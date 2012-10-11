# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Добавлен выбор шаблонизатора в таблице, хранящей шаблоны печати.
'''

def upgrade(conn):
    sql = u'''
ALTER TABLE ClientDocument CHANGE COLUMN endDate endDate DATE NULL DEFAULT NULL COMMENT 'Срок окончания действия документа'  ;
ALTER TABLE ActionProperty_FlatDirectory RENAME TO  ActionProperty_FDRecord ;
ALTER TABLE FDRecord DROP FOREIGN KEY FK_FDRecord_FlatDictionary ;
ALTER TABLE FDRecord CHANGE COLUMN flatDictionary_id flatDirectory_id INT(10) UNSIGNED NOT NULL COMMENT 'id справочника из таблицы FlatDictionaryID'  , 
ADD CONSTRAINT FK_FDRecord_FlatDirectory
  FOREIGN KEY (flatDirectory_id )
  REFERENCES FlatDirectory (id );
'''

    c = conn.cursor()
    c.execute(sql)

def downgrade(conn):
    pass