#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Исправления для обновления для выгрузки данных госпитализаций в ТФОМС Пензы
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    perform_hosp_app_upgrade(c)
    perform_received_upgrade(c)
    perform_moving_upgrade(c)

    c.close()

def perform_hosp_app_upgrade(c):
    global tools
    # установка флеткода (и showTime) для направления на госпитализацию
    hosp_app_id = tools.checkRecordExists(c, 'ActionType', 'flatCode = "hosp_appointment" AND deleted = 0')
    if hosp_app_id is None:
        raise Exception('В бд не найден тип действия Направление на госпитализацию. Добавьте его вручную.')
    if c.rowcount > 1:
        raise Exception('В бд найдено несколько версий типа действия Направление на госпитализацию. '
                        'Выберете один актуальный, остальные пометьте удаленными.')
    # настройка свойств
    # Профиль койки
    sql = '''UPDATE ActionPropertyType
SET code = "%s" WHERE actionType_id = %d AND code = "%s"''' % ('hospitalBedProfile', hosp_app_id, 'hosp_bed_profile')
    tools.executeEx(c, sql, mode = ['safe_updates_off',])

def perform_received_upgrade(c):
    # Поступлений в данный момент может быть несколько с одним флеткодом
    # (в некоторых бд существует Поступление в роддом)
    global tools
    c.execute('SELECT id FROM ActionType WHERE flatCode = "received" AND deleted = 0')
    records = c.fetchall()
    if not records:
        raise Exception('В бд не найден тип действия Поступление.')

    records = [int(row[0]) for row in records]
    # настройка свойств
    for rec_id in records:
        # Профиль койки
        sql = '''UPDATE ActionPropertyType
SET code = "%s" WHERE actionType_id = %d AND code = "%s"''' % ('hospitalBedProfile', rec_id, 'hosp_bed_profile')
        tools.executeEx(c, sql, mode = ['safe_updates_off',])

        # № направления
        sql = '''UPDATE ActionPropertyType
SET valueDomain = "%s", mandatory = 1
WHERE actionType_id = %d AND code = "%s"''' % ("'нет направления',*", rec_id, 'direction_num')
        tools.executeEx(c, sql, mode = ['safe_updates_off',])

def perform_moving_upgrade(c):
    global tools
    mov_id = tools.checkRecordExists(c, 'ActionType', 'flatCode = "moving" AND deleted = 0')
    if mov_id is None:
        raise Exception('В бд не найден тип действия Движение.')
    if c.rowcount > 1:
        raise Exception('В бд найдено несколько версий типа действия Движение. '
                        'Необходимо разбираться в этой ситуации.')

    # настройка свойств
    # Профиль койки
    sql = '''UPDATE ActionPropertyType
SET code = "%s" WHERE actionType_id = %d AND code = "%s"''' % ('hospitalBedProfile', mov_id, 'hosp_bed_profile')
    tools.executeEx(c, sql, mode = ['safe_updates_off',])
