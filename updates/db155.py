#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
- приведение к 'нормальной' структуре
'''


def upgrade(conn):
    upgrade133(conn)
    upgrade143(conn)
    upgrade145(conn)
    upgrade146(conn)
    upgrade151(conn)

    c = conn.cursor()
    c.execute('update `Meta` set `value` = %s where `name` = "schema_version"', 154)
    c.close()


def upgrade133(conn):
    global tools
    c = conn.cursor()
    # Обновление свойств в Поступлении
    received_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'received\'')
    if received_at_id:
        # Отделение пребывания
        apt_d = dict(actionType_id=received_at_id,
                     name=u"'Отделение поступления'",
                     descr=u"'Отделение поступления'",
                     typeName=u"'OrgStructure'",
                     code="'orgStructStay'",
                     mandatory=1,
                     )
        tools.addNewActionProperty(c, **apt_d)
 
        # Направлен из
        apt_d = dict(actionType_id=received_at_id,
                     name=u"'Направлен из'",
                     descr=u"'отделение из предыдущей истории болезни'",
                     typeName=u"'OrgStructure'",
                     code="'orgStructDirectedFrom'",
                     )
        tools.addNewActionProperty(c, **apt_d)
 
    # Обновление свойств в Движении
    moving_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'moving\'')
    if moving_at_id:
        # Переведен из отделения
        sql = u'''
UPDATE ActionPropertyType SET mandatory=1
WHERE actionType_id=%d AND code='%s'
''' % (moving_at_id, 'orgStructReceived')
        tools.executeEx(c, sql, modes=['safe_updates_off'])
 
    c.close()


def upgrade143(conn):
    global tools
    c = conn.cursor()

    # Добавление или обновление  свойства 'профиль койки' в Движении
    moving_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'moving\'')
 
    if moving_at_id:
        hospitalBedProfileId = tools.checkRecordExists(c, 'ActionPropertyType',
                                                       'name=\'Профиль койки\' and actionType_id = {0}'.format(moving_at_id))
        if hospitalBedProfileId:
            sql = u'''
                UPDATE ActionPropertyType
                SET mandatory=1,
                code='hospitalBedProfile'
                WHERE id=%d
                ''' % hospitalBedProfileId
            tools.executeEx(c, sql, modes=['safe_updates_off'])
        else:
            apt_d = dict(actionType_id=moving_at_id,
                         name=u"'Профиль койки'",
                         descr=u"'Профиль койки'",
                         typeName=u"'HospitalBedProfile'",
                         code="'hospitalBedProfile'",
                         mandatory=1,
                         )
            tools.addNewActionProperty(c, **apt_d)

    c.close()


def upgrade145(conn):
    global tools
    c = conn.cursor()

    sql = u'''
SELECT apt.id, at.createDatetime
FROM ActionType at JOIN ActionPropertyType apt ON at.id = apt.actionType_id
WHERE apt.code = '%s' AND at.flatCode = '%s'
''' % ('orgStructStay', 'received')
    num_rows = c.execute(sql)
    if num_rows > 1:
        print('Warning! Not unique APT')
    apt_id, at_datetime = c.fetchone()
    sql = u'''UPDATE ActionPropertyType SET createDatetime = '%s' WHERE id = %d''' % (at_datetime, apt_id)
    c.execute(sql)
 
    sql = u'''UPDATE ActionPropertyType SET deleted = 1 WHERE code = '%s'
AND actionType_id IN (SELECT id FROM ActionType WHERE flatCode = '%s' AND deleted = 0) ''' % ('hospOrgStruct', 'received')
    c.execute(sql)
 
    c.close()


def upgrade146(conn):
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
    

def upgrade151(conn):
    global config
    c = conn.cursor()

    c.execute(u'''INSERT INTO `rbCoreActionProperty` (`actionType_id`, `name`, `actionPropertyType_id`) 
SELECT `actionType_id`, `name`, `id` 
FROM `ActionPropertyType`
WHERE `actionType_id` IN (SELECT `id` FROM `ActionType` WHERE `flatCode` = 'received')
AND `deleted` = 0
AND `id` NOT IN (
SELECT `actionPropertyType_id`
FROM `rbCoreActionProperty`
WHERE `actionType_id` IN (SELECT `id` FROM `ActionType` WHERE `flatCode` = 'received'));''')
    c.close()


def downgrade(conn):
    pass
