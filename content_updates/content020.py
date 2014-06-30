#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные для справочников, связанных с расписанием врача
'''

MIN_SCHEMA_VERSION = 180

def upgrade(conn):
    c = conn.cursor()

    sql = '''
INSERT INTO `rbReceptionType` (`id`,`code`,`name`) VALUES
(1,'amb','Амбулаторно'),
(2,'home','На дому');
'''
    c.execute(sql)

    sql = '''
INSERT INTO `rbAttendanceType` (`id`,`code`,`name`) VALUES
(1,'planned','Нормальный'),
(2,'CITO','Вне очереди'),
(3,'extra','Сверх плана');
'''
    c.execute(sql)

    sql = '''
INSERT INTO `rbAppointmentType` (`id`,`code`,`name`) VALUES
(1,'amb','Амбулаторный'),
(2,'hospital','Приём в стационаре'),
(3,'polyclinic','Приём в поликлинике'),
(4,'diagnostic','Диагностика');
'''
    c.execute(sql)

    c.close()
