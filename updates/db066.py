#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Изменение поведения плоских справочников. Переход на мнемонические коды вместо идентификаторов.
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `FlatDirectory` ADD `code` CHAR(128)  NULL  DEFAULT NULL  COMMENT 'Универсальный буквенный код, чтобы не привязываться к id.'  AFTER `name`;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FlatDirectory` ADD INDEX FK_FlatDirectory_code (code);
'''
    c.execute(sql)

    sql = u'''
UPDATE `FlatDirectory` SET `FlatDirectory`.`code` = `FlatDirectory`.`id`;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FDField` ADD `flatDirectory_code` CHAR(128) NULL  DEFAULT  NULL  COMMENT 'code справочника из таблицы FlatDirectory'  AFTER `flatDirectory_id`;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `FDField` ADD INDEX FK_FDField_FlatDirectory_code (`flatDirectory_code`);
'''
    c.execute(sql)

    sql = u'''
UPDATE `FDField` SET `FDField`.`flatDirectory_code` = `FDField`.`flatDirectory_id`;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FDField` ADD CONSTRAINT `FK_FDField_FlatDirectory_code` FOREIGN KEY (`flatDirectory_code`) REFERENCES `FlatDirectory` (`code`);
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FDRecord` ADD `flatDirectory_code` CHAR(128) NULL  DEFAULT  NULL  COMMENT 'code справочника из таблицы FlatDirectory'  AFTER `flatDirectory_id`;
ALTER TABLE `FDRecord` ADD INDEX FK_FDRecord_FlatDirectory_code (`flatDirectory_code`);
UPDATE `FDRecord` SET `FDRecord`.`flatDirectory_code` = `FDRecord`.`flatDirectory_id`;
ALTER TABLE `FDRecord` ADD CONSTRAINT `FK_FDRecord_FlatDirectory_code` FOREIGN KEY (`flatDirectory_code`) REFERENCES `FlatDirectory` (`code`);
ALTER TABLE `FDField` DROP FOREIGN KEY FK_FDField_FlatDirectory;
ALTER TABLE `FDField` DROP INDEX FK_FDField_FlatDirectory;
ALTER TABLE `FDField` DROP flatDirectory_id;
ALTER TABLE `FDRecord` DROP FOREIGN KEY FK_FDRecord_FlatDirectory;
ALTER TABLE `FDRecord` DROP INDEX FK_FDRecord_FlatDictionary;
ALTER TABLE `FDRecord` DROP flatDirectory_id;
'''
    c.execute(sql)

def downgrade(conn):
    pass
