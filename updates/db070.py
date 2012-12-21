#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Исправлено представление для ВМП
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
CREATE OR REPLACE
    ALGORITHM = UNDEFINED 
    DEFINER = `%s`@`%s` 
    SQL SECURITY DEFINER
VIEW `vClient_Quoting` AS
    select 
        `c0`.`id` AS `id`,
        `c0`.`createDatetime` AS `createDatetime`,
        `c0`.`createPerson_id` AS `createPerson_id`,
        `c0`.`modifyDatetime` AS `modifyDatetime`,
        `c0`.`modifyPerson_id` AS `modifyPerson_id`,
        `c0`.`deleted` AS `deleted`,
        `c0`.`master_id` AS `master_id`,
        `c0`.`identifier` AS `identifier`,
        `c0`.`quotaTicket` AS `quotaTicket`,
        `c0`.`quotaType_id` AS `quotaType_id`,
        `c0`.`stage` AS `stage`,
        `c0`.`directionDate` AS `directionDate`,
        `c0`.`freeInput` AS `freeInput`,
        `c0`.`org_id` AS `org_id`,
        `c0`.`amount` AS `amount`,
        `c0`.`MKB` AS `MKB`,
        `c0`.`status` AS `status`,
        `c0`.`request` AS `request`,
        `c0`.`statment` AS `statment`,
        `c0`.`dateRegistration` AS `dateRegistration`,
        `c0`.`dateEnd` AS `dateEnd`,
        `c0`.`orgStructure_id` AS `orgStructure_id`,
        `c0`.`regionCode` AS `regionCode`,
        `c0`.`pacientModel_id` AS `pacientModel_id`,
        `c0`.`treatment_id` AS `treatment_id`,
        `c0`.`event_id` AS `event_id`,
        `c0`.`prevTalon_event_id` AS `prevTalon_event_id`
    from
        (`Client_Quoting` `c0`
        left join `vClient_Quoting_sub` `c00` ON ((`c0`.`id` = `c00`.`id`)))
    where
        isnull(`c00`.`id`) and (`c0`.`event_id` not in 
            (select `c3`.`prevTalon_event_id`
            from `Client_Quoting` `c3`
            where `c3`.`prevTalon_event_id` is not null and `c3`.`deleted` = 0) 
            or c0.event_id is NULL)    ;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    
def downgrade(conn):
    pass
