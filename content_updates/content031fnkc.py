#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import logging
from collections import defaultdict

__doc__ = '''\
Замена типов свойств диагнозов (МКБ+текст) на новый тип Diagnosis для AT поликлиники.
'''


def upgrade(conn):
    convert_diag_apts(conn)


def convert_diag_apts(conn):
    sql_old_props = '''
SELECT AT.id,
    AT.name,
    APT.id,
    APT.name,
    APT.typeName,
    APT.valueDomain
FROM
    ActionType AS AT JOIN ActionPropertyType AS APT ON AT.id = APT.actionType_id
WHERE
    AT.deleted = 0 AND
    APT.deleted = 0 AND (
        -- поликлинические at
        AT.group_id IN (2036, 2037, 2477, 2478, 2872) AND (
            -- выборка типов действий, в которых есть свойства типа МКБ
            APT.typeName = 'MKB' OR (
                -- выборка типов действий, в которых есть свойства типа Text для описания диагноза
                APT.typeName = 'Text' AND
                APT.name LIKE '%диагноз%' AND
                APT.name NOT LIKE '%клиника%' AND -- исключить 'Клиника, где установлен диагноз'
                APT.name NOT LIKE '%реабил%' AND -- исключить 'Диагноз при направлении на реабилитацию' и 'Реабилитационный диагноз и прогноз'
                APT.name NOT LIKE '%диффер%' AND -- исключить 'Дифференциальный диагноз'
                APT.name NOT LIKE '%конкур%' AND -- исключить 'Конкурирующие диагнозы'
                APT.name NOT LIKE '%фонов%' -- исключить 'Фоновые диагнозы'
            ) OR (
                -- выборка типов действий, в которых есть свойство с названием "Дата постановки диагноза"
                APT.typeName='Date' AND APT.name LIKE '%Дата постановки диаг%'
            )
        )
    ) OR (
        -- стоматологические at
        AT.group_id = 3031 AND (
            APT.typeName = 'Constructor' AND
            APT.name LIKE '%диагноз%'
        )
    )
'''
    ats = defaultdict(dict)
    c = conn.cursor()
    c.execute(sql_old_props)
    for at_id, at_name, apt_id, apt_name, apt_type_name, vdom, in c.fetchall():
        ats[(at_id, at_name)][apt_id] = (apt_name, apt_type_name, vdom)

    cur_at_valdom = None
    new_apt_id = None
    removed_apt_info = []
    for (at_id, at_name), apts in ats.iteritems():
        logging.debug('{0}{1}:'.format(at_id, at_name))
        for apt_id, (apt_name, apt_type_name, vdom) in apts.iteritems():
            logging.debug('\t{0} {1}'.format(apt_name, apt_type_name))
            if not cur_at_valdom and apt_type_name == 'Constructor':
                cur_at_valdom = vdom
            removed_apt_info.append((apt_id, apt_type_name))
            delete_apt(conn, apt_id)

        new_apt_id = create_diag_apt(conn, at_id, cur_at_valdom)
        logging.debug('\t\t=>{0}:[{1}]=>{2}'.format(
            at_id,
            ','.join(['{0}_{1}'.format(id_, type_) for id_, type_ in removed_apt_info]),
            new_apt_id)
        )
        cur_at_valdom = None
        removed_apt_info = []

    c.close()


def delete_apt(conn, apt_id):
    sql = '''
UPDATE ActionPropertyType SET deleted = 1, modifyDatetime = CURRENT_TIMESTAMP
WHERE id = {0}'''.format(apt_id)
    c = conn.cursor()
    c.execute(sql)
    c.close()


def create_diag_apt(conn, at_id, vdom):
    global tools
    with conn as cursor:
        value_domain = '{{"thesaurus_code": "{0}"}}'.format(vdom) if vdom else ''
        new_id = tools.addNewActionPropertyType(cursor,
                                                actionType_id=at_id,
                                                typeName="'Diagnosis'",
                                                name="'Диагноз'",
                                                descr="'Диагноз'",
                                                valueDomain="'{0}'".format(value_domain),
                                                isVector=1,
                                                code="'diagnosis'")
    return new_id