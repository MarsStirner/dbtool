# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление прав для работы с MediPad.
'''

sqlClientUserRights = [
    ("clientExamCreate",        "Пациенты: осмотры, чтение"),
    ("clientExamCreate",        "Пациенты: осмотры, создание"),
    ("clientExamUpdate",        "Пациенты: осмотры, изменение"),
    ("clientExamDelete",        "Пациенты: осмотры, удаление"),
    ("clientDiagRead",          "Пациенты: диагностика, чтение"),
    ("clientDiagCreate",        "Пациенты: диагностика, создание"),
    ("clientDiagUpdate",        "Пациенты: диагностика, изменение"),
    ("clientDiagDelete",        "Пациенты: диагностика, удаление"),
    ("clientHealRead",          "Пациенты: лечение, чтение"),
    ("clientHealCreate",        "Пациенты: лечение, создание"),
    ("clientHealUpdate",        "Пациенты: лечение, изменение"),
    ("clientHealDelete",        "Пациенты: лечение, удаление"),
    ("clientEventRead",         "Пациенты: обращения, чтение"),
    ("clientEventCreate",       "Пациенты: обращения, создание"),
    ("clientEventUpdate",       "Пациенты: обращения, изменение"),
    ("clientEventDelete",       "Пациенты: обращения, удаление"),
    ("clientActionRead",        "Пациенты: мероприятия, чтение"),
    ("clientActionCreate",      "Пациенты: мероприятия, создание"),
    ("clientActionUpdate",      "Пациенты: мероприятия, изменение"),
    ("clientActionDelete",      "Пациенты: мероприятия, удаление"),
    ("clientRegRead",           "Пациенты: регистрация, чтение"),
    ("clientRegCreate",         "Пациенты: регистрация, создание"),
    ("clientRegUpdate",         "Пациенты: регистрация, изменение"),
    ("clientRegDelete",         "Пациенты: регистрация, удаление"),
    ("existsSeesSelf",          "В списке отделения видит своих пациентов"),
    ("existsSeesStructure",     "В списке отделения видит пациентов своего отделения"),
    ("inflowSeesSelf",          "В поступлениях видит своих поступивших пациентов"),
    ("cardsAccess",             "Видит картотеку"),
    ("inflowSeesApproaching",   "В поступлениях видит пациентов с незакрытым обращением"),
    ("inflowSeesStructure",     "В поступлениях видит пациентов, поступивших в свое отделение"),
]

sqlInsertQuery = '''
    INSERT INTO `rbUserRight` (code, name)
    SELECT "{code}", "{name}" FROM `rbUserRight`
    WHERE NOT EXISTS (
        SELECT * FROM `rbUserRight`
        WHERE code="{code}"
    )
    LIMIT 1
'''

sqlDeleteQuery = '''
    DELETE FROM `rbUserRight`
    WHERE code="{code}"
'''

def upgrade(conn):
    c = conn.cursor()
    for (code, name) in sqlClientUserRights:
        q = sqlInsertQuery.format(code=code, name=name)
        c.execute(q)

def downgrade(conn):
    c = conn.cursor()
    for (code, name) in sqlClientUserRights:
        q = sqlDeleteQuery.format(code=code, name=name)
        c.execute(q)
