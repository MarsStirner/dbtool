#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление новых привилегий и их привязка к некоторым профилям.
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    # добавление новых привилегий
    sql = u'''INSERT INTO rbUserRight (code, name) VALUES (%s, %s);'''
    data = [
        ('evtPoliclinicOmsCreate', 'Имеет возможность создавать поликлинические обращения ОМС'),
        ('evtPoliclinicOmsClose', 'Имеет возможность закрывать поликлинические обращения ОМС'),
        ('evtPoliclinicDmsCreate', 'Имеет возможность создавать поликлинические обращения ДМС'),
        ('evtPoliclinicDmsClose', 'Имеет возможность закрывать поликлинические обращения ДМС'),
        ('evtPoliclinicPaidCreate', 'Имеет возможность создавать поликлинические обращения платные'),
        ('evtPoliclinicPaidClose', 'Имеет возможность закрывать поликлинические обращения платные'),
        ('evtDiagnosticPaidCreate', 'Имеет возможность создавать диагностические обращения платные'),
        ('evtDiagnosticPaidClose', 'Имеет возможность закрывать диагностические обращения платные'),
        ('evtDiagnosticBudgetCreate', 'Имеет возможность создавать диагностические обращения бюджет'),
        ('evtDiagnosticBudgetClose', 'Имеет возможность закрывать диагностические обращения бюджет')
    ]
    c.executemany(sql, data)

    # присвоение новых привилегий роли врач поликлиники (clinicDoctor)
    prof_id = tools.checkRecordExists(c, 'rbUserProfile', 'code = "{0}"'.format('clinicDoctor'))
    for code in ('evtPoliclinicOmsCreate', 'evtPoliclinicDmsCreate', 'evtPoliclinicPaidClose',
                 'evtPoliclinicOmsClose', 'evtPoliclinicDmsClose'):
        add_right(conn, prof_id, code)
    # убрать возможность редактировать чужие действия (editOtherpeopleAction)
    delete_right(conn, prof_id, 'editOtherpeopleAction')

    # присвоение новых привилегий роли врач диагностики (diagDoctor)
    prof_id = tools.checkRecordExists(c, 'rbUserProfile', 'code = "{0}"'.format('diagDoctor'))
    for code in ('evtDiagnosticPaidCreate', 'evtDiagnosticPaidClose', 'evtDiagnosticBudgetCreate',
                 'evtDiagnosticBudgetClose'):
        add_right(conn, prof_id, code)
    # убрать работу с документами-действиями (clientAssessmentCreate, clientAssessmentUpdate, clientAssessmentDelete)
    for code in ('clientAssessmentCreate', 'clientAssessmentUpdate', 'clientAssessmentDelete'):
        delete_right(conn, prof_id, code)

    # присвоение новых привилегий роли регистратор поликлиники (clinicRegistrator)
    prof_id = tools.checkRecordExists(c, 'rbUserProfile', 'code = "{0}"'.format('clinicRegistrator'))
    for code in ('evtDiagnosticPaidCreate', 'evtPoliclinicDmsCreate', 'evtPoliclinicPaidCreate',
                 'evtPoliclinicDmsClose', 'evtDiagnosticPaidClose'):
        add_right(conn, prof_id, code)

    # обновление профиля медсестры
    prof_id = 38
    sql = '''
UPDATE rbUserProfile
SET code='assistNurse', name='Медсестра (ассистент врача)'
WHERE id={0}'''.format(prof_id)
    c.execute(sql)
    # присвоение новых привилегий роли медсестра (assistNurse)
    for code in ('evtDiagnosticPaidCreate', 'evtPoliclinicOmsCreate', 'evtPoliclinicDmsCreate',
                 'evtPoliclinicPaidClose', 'evtPoliclinicOmsClose', 'evtPoliclinicDmsClose',
                 'evtDiagnosticPaidCreate', 'evtDiagnosticPaidClose', 'evtDiagnosticBudgetCreate',
                 'evtDiagnosticBudgetClose'):
        add_right(conn, prof_id, code)

    c.close()


def add_right(conn, profile_id, right_code):
    sql = '''INSERT INTO rbUserProfile_Right (master_id, userRight_id)
VALUES (
  {0},
  (SELECT id FROM rbUserRight WHERE code = "{1}" LIMIT 1)
);'''.format(profile_id, right_code)
    with conn as cursor:
        cursor.execute(sql)


def delete_right(conn, profile_id, right_code):
    sql = '''DELETE FROM rbUserProfile_Right
WHERE master_id = {0} AND userRight_id = (SELECT id FROM rbUserRight WHERE code = "{1}" LIMIT 1);
'''.format(profile_id, right_code)
    with conn as cursor:
        cursor.execute(sql)