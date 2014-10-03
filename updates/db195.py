#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Представление Proced_zapis_queue (Записи на прием в процедурные кабинеты на текущую дату)
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
        CREATE OR REPLACE DEFINER={0} VIEW `Proced_zapis_queue` AS
            select
                `ScheduleClientTicket`.`id` AS `EventID`,
                STR_TO_DATE(CONCAT(`Schedule`.`date`, ' ', `ScheduleTicket`.`begTime`), '%Y-%m-%d %H:%i:%s') AS `Datazapisi`,
                `Office`.`code` AS `Kabinet`,
                `ScheduleClientTicket`.`note` AS `Procedure`,
                `Person`.`lastName` AS `Direction`,
                `Client`.`id` AS `P_id`,
                `Client`.`lastName` AS `P_F`,
                `Client`.`firstName` AS `P_I`,
                `Client`.`patrName` AS `P_O`,
                `ClientContact`.`contact` AS `Tele`
            from
                ((((`ScheduleClientTicket`
                join `ScheduleTicket` ON ((`ScheduleClientTicket`.`ticket_id` = `ScheduleTicket`.`id`)
                    and (`ScheduleTicket`.`deleted` = 0))
                join `Schedule` ON (((`ScheduleTicket`.`schedule_id` = `Schedule`.`id`)
                    and (`Schedule`.`deleted` = 0))))
                join `Office` ON (`Schedule`.`office_id` = `Office`.`id`)
                join `Person` ON (((`Schedule`.`person_id` = `Person`.`id`)
                    and (`Person`.`orgStructure_id` = 26)
                    and ((`Person`.`lastName` = '1')
                    or (`Person`.`lastName` = '2')
                    or (`Person`.`lastName` = '3')
                    or (`Person`.`lastName` = '4')))))
                join `Client` ON ((`ScheduleClientTicket`.`client_id` = `Client`.`id`)))
                left join `ClientContact` ON (((`ClientContact`.`client_id` = `Client`.`id`)
                    and (`ClientContact`.`contactType_id` = 3)
                    and (`ClientContact`.`deleted` = 0))))
            where
                ((`ScheduleClientTicket`.`deleted` = 0)
                    and (cast(`Schedule`.`date` as date) = curdate()))
            group by `ScheduleClientTicket`.`id`;
    '''.format(config['definer'])
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass
