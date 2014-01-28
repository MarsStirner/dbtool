# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = u'''\
Изменяет тип свойства действия медикаментозное назначение на RLS и добавляет тестовые данные
'''

sqlRLSMedicalPresciption = u'''\
UPDATE ActionPropertyType AS apt
  INNER JOIN ActionType AS at ON apt.actionType_id = at.id
  SET apt.typeName = 'RLS'
  WHERE
at.name like 'Назначения' AND
apt.name like 'Наименование'
'''

sqlRLSCodes = u'''
SELECT Code FROM `rls`.`vNomen` where 
tradeName like '%Аспирин%' OR
tradeName like '%Анальгин%' OR
tradeName like '%Галоперидол%';
'''

sqlMedicalPrescriptionAPS = u'''\
select aps.id from Action a
inner join ActionType at on at.id=a.actionType_id
inner join ActionProperty ap on ap.action_id = a.id
left join ActionPropertyType apt on apt.id=ap.type_id
inner join ActionProperty_String aps on aps.id = ap.id
where at.name="Назначения" and apt.name="Наименование";
'''

sqlInsertRLS = u'''\
INSERT INTO ActionProperty_Integer
(id, value)
VALUES
({id}, {value})
'''

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def execute(conn, sql):
    c = conn.cursor()
    c.execute(sql)

def insert(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    sqlLastInsertedId = "SELECT LAST_INSERT_ID()"
    c.execute(sqlLastInsertedId)
    result = c.fetchone()
    return result[0]

def upgrade(conn):
    global tools
    c = conn.cursor()
    tools.executeEx(c, sqlRLSMedicalPresciption, mode=['safe_updates_off',])
    
    codes = []
    rows = query(conn, sqlRLSCodes)
    for r in rows:
        codes.append(r[0])

    cnt = 0
    rows = query(conn, sqlMedicalPrescriptionAPS)
    for row in rows:
        id = row[0]
        sql = sqlInsertRLS.format(id=id, value=codes[cnt])
        cnt = (cnt + 1) % len(codes)
        execute(conn, sql)
    

def downgrade(conn):
    pass


