# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавление права clientTreatmentRead для роли "Медсестра отеделения"
'''

def upgrade(conn):
    sql = [
        '''INSERT INTO rbUserProfile_Right(master_id,userRight_id)
           SELECT rbUserProfile.id, rbUserRight.id FROM rbUserProfile JOIN rbUserRight
           WHERE rbUserProfile.code = 'strNurse' AND rbUserRight.code = 'clientTreatmentRead';''',]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [        
        '''DELETE FROM rbUserProfile_Right where master_id= (SELECT rbUserProfile.id FROM rbUserProfile WHERE rbUserProfile.code='strNurse') AND userRight_id=
           (SELECT rbUserRight.id FROM rbUserRight WHERE rbUserRight.code = 'clientTreatmentRead');''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

