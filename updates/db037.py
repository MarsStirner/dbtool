# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Переименование ролей для MediPad \
'''

sqlUserRightRenames = {
    "clientExamCreate": "clientAssessmentCreate",
    "clientExamRead":   "clientAssessmentRead",
    "clientExamUpdate": "clientAssessmentUpdate",
    "clientExamDelete": "clientAssessmentDelete",

    "clientDiagCreate": "clientDiagnosticCreate",
    "clientDiagRead":   "clientDiagnosticRead",
    "clientDiagUpdate": "clientDiagnosticUpdate",
    "clientDiagDelete": "clientDiagnosticDelete",

    "clientHealCreate": "clientTreatmentCreate",
    "clientHealRead":   "clientTreatmentRead",
    "clientHealUpdate": "clientTreatmentUpdate",
    "clientHealDelete": "clientTreatmentDelete",
}

sqlQuery = '''
    UPDATE rbUserRight
    SET code = "{newCode}"
    WHERE code = "{oldCode}"
'''

def upgrade(conn):
    c = conn.cursor()
    for key, value in sqlUserRightRenames.items():
        q = sqlQuery.format(oldCode=key, newCode=value)
        c.execute(q)

def downgrade(conn):
    c = conn.cursor()
    for key, value in sqlUserRightRenames.items():
        q = sqlQuery.format(oldCode=value, newCode=key)
        c.execute(q)
