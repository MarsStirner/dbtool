# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Добавляет в таблицу ActionType столбцы для связи с:
    - типом пробирки (rbTestTubeType)
    - типом работы (rbJobType)
'''

tblActionType = "ActionType"


def upgrade(conn):
    global tools
    sqlAddColumns = u'''\
ALTER TABLE {tableName}
    ADD COLUMN `testTubeType_id` int(11),
    ADD COLUMN `jobType_id` int(11)
'''

    sqlAddConstraints = u'''\
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
ALTER TABLE {tableName}
    ADD CONSTRAINT `rbTestTubeType_id_fk` foreign key (`testTubeType_id`) references `rbTestTubeType`(`id`) on update cascade,
    ADD CONSTRAINT `rbJobType_id_fk` foreign key (`jobType_id`) references `rbJobType`(`id`) on update cascade;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
'''

    c = conn.cursor()
    tools.executeEx(c, sqlAddColumns.format(tableName=tblActionType), mode=['ignore_duplicates'])
    c.execute(sqlAddConstraints.format(tableName=tblActionType))



def downgrade(conn):

    sqlDropConstraints = '''\
    ALTER TABLE {tableName}
        DROP FOREIGN KEY `rbTestTubeType_id_fk`,
        DROP FOREIGN KEY `rbJobType_id_fk`;
'''
    sqlDropColumns = '''\
ALTER TABLE {tableName}
    DROP COLUMN `testTubeType_id`,
    DROP COLUMN `jobType_id`
'''

    c = conn.cursor()
    c.execute(sqlDropConstraints.format(tableName=tblActionType))
    c.execute(sqlDropColumns.format(tableName=tblActionType))
