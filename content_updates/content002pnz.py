#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Обновление для выгрузки данных в ТФОМС Пензы
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    # установка флеткода для направления на госпитализацию
    hosp_app_id = tools.checkRecordExists(c, 'ActionType',
        'name LIKE "Направление на госпитализацию%" AND deleted = 0')
    if hosp_app_id is None:
        raise Exception('В бд не найден тип действия Направление на госпитализацию. Добавьте его вручную.')
    if c.rowcount > 1:
        raise Exception('В бд найдено несколько версий типа действия Направление на госпитализацию. '
                        'Выберете один актуальный, остальные пометьте удаленными.')
    c.execute('UPDATE ActionType SET flatCode = "%s" WHERE id = %d' % ('hosp_appointment', hosp_app_id))

    # настройка свойств
    # Куда направлен
    lpu_to_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'typeName = "Organisation" AND name LIKE "Куда направлен%" AND deleted = 0')
    if lpu_to_id is None:
        tools.addNewActionProperty(actionType_id=hosp_app_id,
                                   name="'Куда направ%'",
                                   descr="'Наименование ЛПУ, в которое идет направление'",
                                   typeName="'Organisation'",
                                   valueDomain="'ЛПУ'",
                                   code="'lpu_to'",
                                   mandatory=1)
    else:
        tools.executeEx('UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('lpu_to', lpu_to_id),
                        mode = ['safe_updates_off',])

    # Профиль койки
    hbp_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'typeName = "HospitalBedProfile" AND name LIKE "Профиль койки" AND deleted = 0')
    if hbp_id is None:
        tools.addNewActionProperty(actionType_id=hosp_app_id,
                                   name="'Профиль койки'",
                                   descr="'Профиль койки'",
                                   typeName="'HospitalBedProfile'",
                                   code="'hosp_bed_profile'",
                                   mandatory=1)
    else:
        tools.executeEx('UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_bed_profile', hbp_id),
                        mode = ['safe_updates_off',])

    # Порядок направления
    hosp_order_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'typeName = "ReferenceRb" AND name LIKE "Порядок направления" AND deleted = 0')
    if hosp_order_id is None:
        tools.addNewActionProperty(actionType_id=hosp_app_id,
                                   name="'Порядок направления'",
                                   descr="'Порядок направления'",
                                   typeName="'ReferenceRb'",
                                   valueDomain="'rbAppointmentOrder'",
                                   code="'hosp_order'",
                                   mandatory=1)
    else:
        tools.executeEx('UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_order', hosp_order_id),
                        mode = ['safe_updates_off',])

    # Плановая дата госпитализации
    planned_hospdate_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'typeName = "Date" AND name LIKE "Плановая дата госпитализации" AND deleted = 0')
    if planned_hospdate_id is None:
        tools.addNewActionProperty(actionType_id=hosp_app_id,
                                   name="'Плановая дата госпитализации'",
                                   descr="'Плановая дата госпитализации'",
                                   typeName="'Date'",
                                   code="'planned_hospdate'",
                                   mandatory=1)
    else:
        tools.executeEx('UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('planned_hospdate', planned_hospdate_id),
                        mode = ['safe_updates_off',])

    # Причина отказа от госпитализации
    ref_reason_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'typeName = "ReferenceRb" AND name LIKE "Причина отказа от госпитализации" AND deleted = 0')
    if ref_reason_id is None:
        tools.addNewActionProperty(actionType_id=hosp_app_id,
                                   name="'Причина отказа от госпитализации'",
                                   descr="'Причина отказа от госпитализации'",
                                   typeName="'ReferenceRb'",
                                   valueDomain="'rbRefusalReason'",
                                   code="'refusal_reason'")
    else:
        tools.executeEx('UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('refusal_reason', ref_reason_id),
                        mode = ['safe_updates_off',])

    # Диагноз основной
    diag_mkb_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'typeName = "MKB" AND name LIKE "Диагноз основной" AND deleted = 0')
    if diag_mkb_id is None:
        tools.addNewActionProperty(actionType_id=hosp_app_id,
                                   name="'Диагноз основной'",
                                   descr="'Диагноз основной'",
                                   typeName="'MKB'",
                                   code="'diag_mkb'")
    else:
        tools.executeEx('UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('diag_mkb', diag_mkb_id),
                        mode = ['safe_updates_off',])

    

    c.close()