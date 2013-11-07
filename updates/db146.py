#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
Изменения для формы 007
Заполнение значений профилей коек в движениях по 'OrgStructure_HospitalBed'
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = u'''SELECT createDatetime
                from ActionType
                where flatCode = "moving"'''
    c.execute(sql)
    create_date = c.fetchone()

    sql = u'''
        UPDATE ActionPropertyType
        SET createDatetime = '{0}'
        WHERE code='hospitalBedProfile'
        '''.format(create_date[0].strftime("%Y-%m-%d %H:%M:%S"))
    tools.executeEx(c, sql)

    sql = u'''SELECT Action.id, Action.createDatetime, OrgStructure_HospitalBed.profile_id
                    FROM Action
                    INNER JOIN ActionType
                        ON Action.actionType_id = ActionType.id
                    INNER JOIN ActionProperty
                        ON ActionProperty.action_id = Action.id
                    INNER JOIN ActionProperty_HospitalBed
                        ON ActionProperty.id = ActionProperty_HospitalBed.id
                    INNER JOIN OrgStructure_HospitalBed
                        ON ActionProperty_HospitalBed.value = OrgStructure_HospitalBed.id
                    WHERE
                    ActionType.flatCode = 'moving' and ActionType.deleted=0
                    AND Action.id not in (SELECT Action.id
                                            FROM Action
                                            INNER JOIN ActionType
                                                ON Action.actionType_id = ActionType.id
                                            INNER JOIN ActionProperty
                                                ON ActionProperty.action_id = Action.id
                                            INNER JOIN ActionPropertyType
                                                ON ActionProperty.type_id = ActionPropertyType.id
                                            WHERE
                                                ActionType.flatCode = 'moving' and ActionType.deleted=0
                                                AND ActionPropertyType.code = 'hospitalBedProfile')'''
    c.execute(sql)
    result = c.fetchall()
    bed_profile_apt_id = tools.checkRecordExists(c, 'ActionPropertyType', 'code=\'hospitalBedProfile\'')
    for row in result:
        if row[2]:
            sql = u'''INSERT INTO `ActionProperty`
                        (`createDatetime`, `modifyDatetime`, `deleted`, `action_id`, `type_id`, `norm`)
                        VALUES ('{0}', '{0}', 0, {1}, {2}, ''); '''.format(row[1].strftime("%Y-%m-%d %H:%M:%S"),
                                                                           row[0],
                                                                           bed_profile_apt_id)
            c.execute(sql)
            new_ap_id = c.lastrowid
            sql = u'''INSERT INTO `ActionProperty_HospitalBedProfile`
                        (`id`, `index`, `value`)
                        VALUES ({0}, '0', {1}); '''.format(new_ap_id, row[2])
            c.execute(sql)
    c.close()


def downgrade(conn):
    pass