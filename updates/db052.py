# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавлен справочник научных званий;
- Добавлено поле научное звание сотрудника;
- Добавлено поле научное звание в таблицу типов событий.
'''

def upgrade(conn):
    global tools
    c = conn.cursor()

    sql = '''
CREATE TABLE `rbAcademicTitle` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(8) NOT NULL COMMENT 'Код',
    `name` VARCHAR(64) NOT NULL COMMENT 'Наименование',
    PRIMARY KEY (`id`),
    INDEX `code` (`code`),
    INDEX `name` (`name`)
    )
    COMMENT='Научное звание'
    COLLATE='utf8_general_ci';'''
    c.execute(sql)
    
    sql = '''
ALTER TABLE `Person` 
    ADD COLUMN `academicTitle_id` INT(11) NULL DEFAULT NULL COMMENT 'Научное звание {rbAcademicTitle}' AFTER `academicdegree_id`;'''
    tools.executeEx(c, sql, mode=['ignore_duplicates'])

    sql = '''
ALTER TABLE `EventType_Action`
    ADD COLUMN `academicDegree_id` INT(11) NULL DEFAULT NULL COMMENT 'Ученая степень {rbAcademicDegree}' AFTER `payable`,
    ADD INDEX `academicDegree_id` (`academicDegree_id`);'''
    c.execute(sql)

def downgrade(conn):
    pass
