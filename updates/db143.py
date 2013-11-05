#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
Изменения для формы 007
Тип профиля койки не нужен.
Добавление нового обязательного свойства действия 'Профиль койки' в Движение
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = u"""
    ALTER TABLE `rbHospitalBedProfile` DROP COLUMN `type` ;
    """
    try:
        c.execute(sql)
    except:
        traceback.print_exc()

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


def downgrade(conn):
    pass