#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import traceback

__doc__ = '''\
Тип профиля койки. Необходимо для формы 007
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u"""
        ALTER TABLE `rbHospitalBedProfile`
        ADD COLUMN `type` TINYINT NOT NULL COMMENT 'тип профиля койки  0 - общий профиль, 1 - узкий профиль'  AFTER `service_id`;
    """

    try:
        c.execute(sql)
    except:
        traceback.print_exc()

    c.close()


def downgrade(conn):
    c = conn.cursor()
    sql = u"""
    ALTER TABLE `rbHospitalBedProfile` DROP COLUMN `type` ;
    """
    c.execute(sql)
    pass