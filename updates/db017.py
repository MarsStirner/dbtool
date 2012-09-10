# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Операции с новыми правами.
1. Добавляем права clientTabxAccessy, inflow, Exists.
2. Добавляем роли.
- Врач отделения
- Медсестра отделения
- Врач приемного отделения
- Медсестра приемного отделения
- Заведующий отделения
- Дежурный врач отделения
- Главный врач
'''
tabs = {
    u'Reg': u'регистрация',
    u'Event': u'обращения',
    u'Diag': u'диагностика', 
    u'Exam': u'осмотры', 
    u'Heal': u'лечение',
    u'Action': u'мероприятия' # Общего плана, поступление-движение-выписка
}
accesses = {
    u'Create': u'создание', 
    u'Delete': u'удаление', 
    u'Read': u'чтение', 
    u'Update': u'изменение'
}
codenames = {
    u'cardsAccess': u'Видит картотеку',
    u'inflowSeesSelf': u'В поступлениях видит своих поступивших пациентов',
    u'inflowSeesStructure': u'В поступлениях видит пациентов, поступивших в свое отделение',
    u'inflowSeesApproaching': u'В поступлениях видит пациентов с незакрытым обращением',
    u'existsSeesSelf': u'В списке отделения видит своих пациентов',
    u'existsSeesStructure': u'В списке отделения видит пациентов своего отделения'
}
roles = {
    (u'admNurse', u'Медсестра приемного отделения'): [
        u'cardsAccess', 
        u'inflowSeesApproaching', 
        u'clientRegCreate', u'clientRegRead', u'clientRegUpdate', 
        u'clientEventCreate', u'clientEventRead',
        u'clientActionCreate', u'clientActionRead', u'clientActionUpdate'
    ],
    (u'admDoctor', u'Врач приемного отделения'): [
        u'cardsAccess', 
        u'inflowSeesSelf',
        u'clientEventRead', u'clientEventUpdate',
        u'clientExamCreate', u'clientExamDelete', u'clientExamRead', u'clientExamUpdate',
        u'clientDiagCreate', u'clientDiagRead', u'clientDiagUpdate',
        u'clientHealCreate', u'clientHealRead',
        u'clientActionRead'
    ],
    (u'strNurse', u'Медсестра отделения'): [
        u'inflowSeesStructure',
        u'existsSeesStructure',
        u'clientRegRead',
        u'clientEventRead',
        u'clientActionCreate', u'clientActionRead', u'clientActionUpdate'
    ],
    (u'strDoctor', u'Врач отделения'): [
        u'cardsAccess', 
        u'existsSeesSelf',
        u'clientEventRead', u'clientEventUpdate',
        u'clientExamCreate', u'clientExamDelete', u'clientExamRead', u'clientExamUpdate',
        u'clientDiagCreate', u'clientDiagRead', u'clientDiagUpdate',
        u'clientHealCreate', u'clientHealRead', u'clientHealUpdate',
        u'clientActionRead'
    ],
    (u'strHead', u'Заведующий отделения'): [
        u'cardsAccess', 
        u'inflowSeesStructure',
        u'existsSeesStructure',
        u'clientEventRead', u'clientEventUpdate',
        u'clientExamCreate', u'clientExamDelete', u'clientExamRead', u'clientExamUpdate',
        u'clientDiagCreate', u'clientDiagRead', u'clientDiagUpdate',
        u'clientHealCreate', u'clientHealRead', u'clientHealUpdate',
        u'clientActionCreate', u'clientActionRead', u'clientActionUpdate'
    ],
    (u'strDuty', u'Дежурный врач отделения'): [
        u'inflowSeesStructure',
        u'existsSeesStructure',
        u'clientEventRead',
        u'clientExamCreate', u'clientExamDelete', u'clientExamRead', u'clientExamUpdate',
        u'clientHealCreate', u'clientHealRead',
        u'clientActionRead'
    ],
    (u'chief', u'Главный врач'): [
        u'cardsAccess', 
        u'clientRegCreate', u'clientRegRead', u'clientRegUpdate', 
        u'clientEventCreate', u'clientEventRead', u'clientEventUpdate',
        u'clientExamCreate', u'clientExamDelete', u'clientExamRead', u'clientExamUpdate',
        u'clientDiagCreate', u'clientDiagRead', u'clientDiagUpdate',
        u'clientHealCreate', u'clientHealRead', u'clientHealUpdate',
        u'clientActionCreate', u'clientActionRead', u'clientActionUpdate'
    ]       
}


def upgrade(conn):
    # Добавляем новые права
    sql = []
    for tab in tabs.keys():
        for access in accesses.keys():
            sql.append(u"INSERT INTO rbUserRight (code, name) VALUES ('client" +
            tab + access + u"', 'Пациенты: " + tabs[tab] + u", " + accesses[access] + u"')")
    for code in codenames.keys():
        sql.append(u"INSERT INTO rbUserRight (code, name) VALUES ('" +
        code + u"', '" + codenames[code] + u"')")
    # Добавляем новые роли
    for codename in roles.keys():
        code = codename[0]
        name = codename[1]
        sql.append(u"INSERT INTO rbUserProfile (code, name) VALUES ('" +
        code + u"', '" + name + u"')")
        rightList = roles[codename]
        for right in rightList:
            sql.append(u"INSERT INTO rbUserProfile_Right (master_id, userRight_id) " +
            u"SELECT rbUserProfile.id, rbUserRight.id FROM rbUserProfile JOIN rbUserRight " +
            u"WHERE rbUserProfile.code = '" + code + u"' AND rbUserRight.code = '" +
            right + u"'") 
    # Исполнение 
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = []
    # Удаляем права
    for tab in tabs.keys():
        for access in accesses.keys():
            sql.append(u"DELETE FROM rbUserRight WHERE code = 'client" +
            tab + access + u"'")
    for code in codenames.keys():       
        sql.append(u"DELETE FROM rbUserRight WHERE code = '" +
        code + u"'")
    # Удаляем роли
    for codename in roles.keys():
        code = codename[0]
        sql.append(u"DELETE rbUserProfile_Right, rbUserProfile " +
        u"FROM rbUserProfile_Right, rbUserProfile WHERE " +
        u"rbUserProfile_Right.master_id = rbUserProfile.id AND " +
        u"rbUserProfile.code = '" + code + u"'")
        sql.append(u"DELETE FROM rbUserProfile WHERE code = '" +
        code + u"'")
    # Исполнение
    c = conn.cursor()
    for s in sql:
        c.execute(s)
