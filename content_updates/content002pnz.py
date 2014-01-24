#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Обновление для выгрузки данных госпитализаций в ТФОМС Пензы
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    # заполнение справочников
    c.execute('TRUNCATE `rbAppointmentOrder`')
    sql = u'''INSERT IGNORE INTO `rbAppointmentOrder`
(`code`,`name`, `TFOMScode_hosp`, `TFOMScode_account`)
VALUES (%s, %s, %s, %s);'''
    data = [(1, 'Плановый', 1, 1),
            (3, 'Экстренный', 3, 2),
            (4, 'Самотёком', '', ''),
            (5, 'Принудительный', '', ''),
            (2, 'Неотложный', 2, 3),
            ]
    c.executemany(sql, data)

    c.execute('TRUNCATE `rbRefusalReason`')
    sql = u'''INSERT IGNORE INTO `rbRefusalReason` (`code`,`name`) VALUES (%s, %s);'''
    data = [(1, 'Направлен не по профилю'),
            (2, 'Не нуждается в госпитализации'),
            (3, 'Отсутствие мест'),
            (4, 'Инициативный отказ от госпитализации пациентом'),
            (5, 'Не согласен на госпитализацию в предложенное МО'),
            (6, 'Не согласен со сроками госпитализации'),
            (7, 'Неявка пациента на госпитализацию'),
            (8, 'Непредоставление необходимого пакета документов (отказ стационара)'),
            (9, 'Смерть'),
            (10, 'Прочие'),
            ]
    c.executemany(sql, data)

    c.execute('''INSERT INTO rbHospitalBedType (`code`, `name`) VALUES ('9', 'платная')''')

    perform_hosp_app_upgrade(c)
    perform_received_upgrade(c)
    perform_moving_upgrade(c)
    perform_leaved_upgrade(c)

    c.close()

def perform_hosp_app_upgrade(c):
    global tools
    # установка флеткода (и showTime) для направления на госпитализацию
    hosp_app_id = tools.checkRecordExists(c, 'ActionType',
        'name LIKE "Направление на госпитализацию%" AND deleted = 0')
    if hosp_app_id is None:
        raise Exception('В бд не найден тип действия Направление на госпитализацию. Добавьте его вручную.')
    if c.rowcount > 1:
        raise Exception('В бд найдено несколько версий типа действия Направление на госпитализацию. '
                        'Выберете один актуальный, остальные пометьте удаленными.')
    c.execute('UPDATE ActionType SET flatCode = "%s", showTime = 1 WHERE id = %d' % ('hosp_appointment', hosp_app_id))

    # настройка свойств
    # Куда направлен
    lpu_to_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "Organisation" AND name LIKE "Куда направ%%" AND deleted = 0' % hosp_app_id)
    if lpu_to_id is None:
        tools.addNewActionProperty(c, actionType_id=hosp_app_id,
                                   name="'Куда направляется'",
                                   descr="'Наименование ЛПУ, в которое идет направление'",
                                   typeName="'Organisation'",
                                   valueDomain="'ЛПУ'",
                                   code="'lpu_to'",
                                   mandatory=1)
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('lpu_to', lpu_to_id),
                        mode = ['safe_updates_off',])

    # Профиль койки
    hbp_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "HospitalBedProfile" AND name LIKE "Профиль койки" AND deleted = 0' % hosp_app_id)
    if hbp_id is None:
        tools.addNewActionProperty(c, actionType_id=hosp_app_id,
                                   name="'Профиль койки'",
                                   descr="'Профиль койки'",
                                   typeName="'HospitalBedProfile'",
                                   code="'hosp_bed_profile'",
                                   mandatory=1)
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_bed_profile', hbp_id),
                        mode = ['safe_updates_off',])

    # Порядок направления
    hosp_order_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "ReferenceRb" AND name LIKE "Порядок направления" AND deleted = 0' % hosp_app_id)
    if hosp_order_id is None:
        tools.addNewActionProperty(c, actionType_id=hosp_app_id,
                                   name="'Порядок направления'",
                                   descr="'Порядок направления'",
                                   typeName="'ReferenceRb'",
                                   valueDomain="'rbAppointmentOrder; 1, 2, 3'",
                                   code="'hosp_order'",
                                   mandatory=1)
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_order', hosp_order_id),
                        mode = ['safe_updates_off',])

    # Плановая дата госпитализации
    planned_hospdate_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "Date" AND name LIKE "Плановая дата госпитализации" AND deleted = 0' % hosp_app_id)
    if planned_hospdate_id is None:
        tools.addNewActionProperty(c, actionType_id=hosp_app_id,
                                   name="'Плановая дата госпитализации'",
                                   descr="'Плановая дата госпитализации'",
                                   typeName="'Date'",
                                   code="'planned_hospdate'",
                                   mandatory=1)
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('planned_hospdate', planned_hospdate_id),
                        mode = ['safe_updates_off',])

    # Причина отказа от госпитализации
    ref_reason_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "ReferenceRb" AND name LIKE "Причина отказа от госпитализации" AND deleted = 0' % hosp_app_id)
    if ref_reason_id is None:
        tools.addNewActionProperty(c, actionType_id=hosp_app_id,
                                   name="'Причина отказа от госпитализации'",
                                   descr="'Причина отказа от госпитализации'",
                                   typeName="'ReferenceRb'",
                                   valueDomain="'rbRefusalReason;'",
                                   code="'refusal_reason'")
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('refusal_reason', ref_reason_id),
                        mode = ['safe_updates_off',])

    # Диагноз основной
    diag_mkb_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "MKB" AND name LIKE "Диагноз основной" AND deleted = 0' % hosp_app_id)
    if diag_mkb_id is None:
        tools.addNewActionProperty(c, actionType_id=hosp_app_id,
                                   name="'Диагноз основной'",
                                   descr="'Диагноз основной'",
                                   typeName="'MKB'",
                                   code="'diag_mkb'")
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('diag_mkb', diag_mkb_id),
                        mode = ['safe_updates_off',])

    print('Проверьте настройки типов свойств для типа действия \'Направление на госпитализацию\'. '
          'При необходимости вручную пометьте удаленными дублирующиеся свойства (те, для которых не установлены коды).')

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
        # Направившее ЛПУ
        lpu_from_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "Organisation" AND name LIKE "Направившее ЛПУ" AND deleted = 0' % rec_id)
        if lpu_from_id is None:
            tools.addNewActionProperty(c, actionType_id=rec_id,
                                       name="'Направившее ЛПУ'",
                                       descr="'Наименование ЛПУ, откуда был направлен пациент'",
                                       typeName="'Organisation'",
                                       valueDomain="'ЛПУ'",
                                       code="'lpu_from'",
                                       mandatory=1)
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('lpu_from', lpu_from_id),
                            mode = ['safe_updates_off',])

        # Профиль койки
        hbp_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "HospitalBedProfile" AND name LIKE "Профиль койки" AND deleted = 0' % rec_id)
        if hbp_id is None:
            tools.addNewActionProperty(c, actionType_id=rec_id,
                                       name="'Профиль койки'",
                                       descr="'Профиль койки'",
                                       typeName="'HospitalBedProfile'",
                                       code="'hosp_bed_profile'",
                                       mandatory=1)
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_bed_profile', hbp_id),
                            mode = ['safe_updates_off',])

        # Причина отказа от госпитализации
        ref_reason_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "ReferenceRb" AND name LIKE "Причина отказа от госпитализации" AND deleted = 0' % rec_id)
        if ref_reason_id is None:
            tools.addNewActionProperty(c, actionType_id=rec_id,
                                       name="'Причина отказа от госпитализации'",
                                       descr="'Причина отказа от госпитализации'",
                                       typeName="'ReferenceRb'",
                                       valueDomain="'rbRefusalReason;'",
                                       code="'refusal_reason'")
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('refusal_reason', ref_reason_id),
                            mode = ['safe_updates_off',])

        # Порядок госпитализации
        hosp_order_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "ReferenceRb" AND name LIKE "Порядок госпитализации" AND deleted = 0' % rec_id)
        if hosp_order_id is None:
            tools.addNewActionProperty(c, actionType_id=rec_id,
                                       name="'Порядок госпитализации'",
                                       descr="'Порядок госпитализации'",
                                       typeName="'ReferenceRb'",
                                       valueDomain="'rbAppointmentOrder; 1, 2, 3'",
                                       code="'hosp_order'")
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_order', hosp_order_id),
                            mode = ['safe_updates_off',])

        # Диагноз приемного отделения
        diag_rec_mkb_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "MKB" AND name LIKE "Диагноз приемного отделения" AND deleted = 0' % rec_id)
        if diag_rec_mkb_id is None:
            tools.addNewActionProperty(c, actionType_id=rec_id,
                                       name="'Диагноз приемного отделения'",
                                       descr="'Диагноз приемного отделения'",
                                       typeName="'MKB'",
                                       code="'received_diag_mkb'")
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('received_diag_mkb', diag_rec_mkb_id),
                            mode = ['safe_updates_off',])

        # Номер ИБ
        ext_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "String" AND (name LIKE "Номер ИБ" OR name LIKE "Номер ИР") AND deleted = 0' % rec_id)
        if ext_id is None:
            print('В поступлении не найдено свойство \'Номер ИБ (ИР)\', но добавлено оно не будет. '
                  'Уточните действительно ли оно необходимо. В текущем обновлении устанавливается код только для существующего свойства.')
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('externalId', ext_id),
                            mode = ['safe_updates_off',])

        # № направления
        direction_num_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "String" AND name LIKE "№ направления" AND deleted = 0' % rec_id)
        if direction_num_id is None:
            tools.addNewActionProperty(c, actionType_id=rec_id,
                                       name="'№ направления'",
                                       descr="'№ направления'",
                                       typeName="'String'",
                                       code="'direction_num'")
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('direction_num', direction_num_id),
                            mode = ['safe_updates_off',])

    print('Проверьте настройки типов свойств для типа действия \'Поступление\'. '
          'При необходимости вручную пометьте удаленными дублирующиеся свойства (те, для которых не установлены коды).')

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
    hbp_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "HospitalBedProfile" AND name LIKE "Профиль койки" AND deleted = 0' % mov_id)
    if hbp_id is None:
        tools.addNewActionProperty(c, actionType_id=mov_id,
                                   name="'Профиль койки'",
                                   descr="'Профиль койки'",
                                   typeName="'HospitalBedProfile'",
                                   code="'hosp_bed_profile'",
                                   mandatory=1)
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_bed_profile', hbp_id),
                        mode = ['safe_updates_off',])

    # Порядок госпитализации в др.отделение/ЛПУ
    hosp_order_id = tools.checkRecordExists(c, 'ActionPropertyType',
        'actionType_id = %d AND typeName = "ReferenceRb" AND name LIKE "Порядок госпитализации%%" AND deleted = 0' % mov_id)
    if hosp_order_id is None:
        tools.addNewActionProperty(c, actionType_id=mov_id,
                                   name="'Порядок госпитализации в др.отделение/ЛПУ'",
                                   descr="'Порядок госпитализации в др.отделение/ЛПУ'",
                                   typeName="'ReferenceRb'",
                                   valueDomain="'rbAppointmentOrder; 1, 2, 3'",
                                   code="'hosp_order'")
    else:
        tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('hosp_order', hosp_order_id),
                        mode = ['safe_updates_off',])

    print('Проверьте настройки типов свойств для типа действия \'Движение\'. '
          'При необходимости вручную пометьте удаленными дублирующиеся свойства (те, для которых не установлены коды).')

def perform_leaved_upgrade(c):
    # И Выписок тоже может быть несколько с одним флеткодом
    # (в некоторых бд существует Выписка из травматологии)
    global tools
    c.execute('SELECT id FROM ActionType WHERE flatCode = "leaved" AND deleted = 0')
    records = c.fetchall()
    if not records:
        raise Exception('В бд не найден тип действия Выписка.')

    records = [int(row[0]) for row in records]
    # настройка свойств
    for leaved_id in records:
        # ЛПУ, куда переводится пациент
        hbp_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "Organisation" AND name LIKE "ЛПУ, куда переводится пациент" AND deleted = 0' % leaved_id)
        if hbp_id is None:
            tools.addNewActionProperty(c, actionType_id=leaved_id,
                                       name="'ЛПУ, куда переводится пациент'",
                                       descr="'ЛПУ, куда переводится пациент'",
                                       typeName="'Organisation'",
                                       valueDomain="'ЛПУ'",
                                       code="'lpu_direct_to'")
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('lpu_direct_to', hbp_id),
                            mode = ['safe_updates_off',])

        # Рекомендуемый профиль койки при переводе в другое ЛПУ
        hbp_id = tools.checkRecordExists(c, 'ActionPropertyType',
            'actionType_id = %d AND typeName = "HospitalBedProfile" AND name LIKE '
            '"Рекомендуемый профиль койки при переводе в другое ЛПУ" AND deleted = 0' % leaved_id)
        if hbp_id is None:
            tools.addNewActionProperty(c, actionType_id=leaved_id,
                                       name="'Рекомендуемый профиль койки при переводе в другое ЛПУ'",
                                       descr="'Рекомендуемый профиль койки при переводе в другое ЛПУ'",
                                       typeName="'HospitalBedProfile'",
                                       code="'planned_hosp_bed_profile'")
        else:
            tools.executeEx(c, 'UPDATE ActionPropertyType SET code = "%s" WHERE id = %d' % ('planned_hosp_bed_profile', hbp_id),
                            mode = ['safe_updates_off',])

    print('Проверьте настройки типов свойств для типа действия \'Выписка\'. '
          'При необходимости вручную пометьте удаленными дублирующиеся свойства (те, для которых не установлены коды).')
