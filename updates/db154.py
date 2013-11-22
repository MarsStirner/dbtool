#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
добавление поля deleted
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''CREATE OR REPLACE VIEW `vrbPersonWithSpeciality` AS
                    SELECT `Person`.`id` AS `id`,
                    `Person`.`code` AS `code`,
                    `Person`.`deleted` AS `deleted`,
                    concat(`Person`.`lastName`,_utf8' ',if((`Person`.`firstName` = _utf8''),_utf8'',
                    concat(left(`Person`.`firstName`,1),_utf8'.')),
                    if((`Person`.`patrName` = _utf8''),_utf8'',
                    concat(left(`Person`.`patrName`,1),_utf8'.')),
                    if(isnull(`rbSpeciality`.`name`),_utf8'',
                    concat(_utf8', ',`rbSpeciality`.`name`))) AS `name`,
                    `Person`.`speciality_id` AS `speciality_id`,
                    `Person`.`org_id` AS `org_id`,
                    `Person`.`orgStructure_id` AS `orgStructure_id`,
                    `Person`.`retireDate` AS `retireDate`
                    from (`Person` left join `rbSpeciality` on((`rbSpeciality`.`id` = `Person`.`speciality_id`)));
                    ''')

    c.close()


def downgrade(conn):
    pass
