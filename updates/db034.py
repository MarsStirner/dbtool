# -*- coding: utf-8 -*-

from __future__ import unicode_literals

__doc__ = '''\
Добавляет тип действия для анализа чувствительности микроорганизма к антибиотикам
'''

def insert(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    sqlLastInsertedId = "SELECT LAST_INSERT_ID()"
    c.execute(sqlLastInsertedId)
    result = c.fetchone()
    return result[0]

def upgrade(conn):
    sql = u'''\
INSERT INTO `ActionType`
(createDatetime, modifyDatetime, deleted, class, group_id, code, name, title, flatCode, sex, age, office, showInForm, genTimetable, context, defaultPlannedEndDate)
VALUES
(NOW(), NOW(), 0, 1, 161, '2_2_99', 'Чувствительность к антибиотикам', 'Чувствительность к антибиотикам', 'bacteriologicalAnalysis', 0, '', '', 1, 0, '', 0)
'''
    at_id = insert(conn, sql)
    sqlInsertApt = u'''\
INSERT INTO `ActionPropertyType`
(actionType_id, name, descr, typeName, valueDomain, defaultValue, norm, sex, age, test_id)
VALUES
({actionTypeId}, '{name}', '{name}', '{typeName}', '', '', '', 0, 0, {testId})
'''
    sql = sqlInsertApt.format(actionTypeId=at_id, name=u'Наименование', typeName='String', testId='NULL')
    c = conn.cursor()
    c.execute(sql)
    sql = sqlInsertApt.format(actionTypeId=at_id, name=u'Антибиотик1', typeName='String', testId=1)
    c = conn.cursor()
    c.execute(sql)

def downgrade(conn):
    sql = "DELETE FROM ActionPropertyType WHERE actionType_id IN (SELECT at.id FROM ActionType at WHERE at.flatCode LIKE 'bacteriologicalAnalysis')"
    c = conn.cursor()
    c.execute(sql)
    sql = "DELETE FROM `ActionType` WHERE flatCode LIKE 'bacteriologicalAnalysis'"
    c = conn.cursor()
    c.execute(sql)