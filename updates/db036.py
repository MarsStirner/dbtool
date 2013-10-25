# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- Добавление ряда пользователей с соответствующими профилями и ролями
- Удаление столбца academicDegree из старых бах 6098, т.к. в нтк была введена
новая структура степеней/званий врачей (по идее может привести к потере данных)
'''

def insert_one(c, sql):
    c.execute(sql)
    sqlLastInsertedId = "SELECT LAST_INSERT_ID()"
    c.execute(sqlLastInsertedId)
    result = c.fetchone()
    return result[0]

def select_one(c, sql):
    c.execute(sql)
    result = c.fetchone()
    return result[0]


def upgrade(conn):
    c = conn.cursor()
    sql = u'''
ALTER TABLE `Person` DROP COLUMN `academicDegree` ;
'''
    try:
        c.execute(sql)
    except OperationalError:
        pass
    else:
        print(u'column `Person`.`academicDegree` deleted')


    sqlCheck = ['''\
SELECT EXISTS(SELECT id FROM Person where login = "Регистраторова")
''',
'''\
SELECT EXISTS(SELECT id FROM Person where login = "Коечкова")
''',
'''\
SELECT EXISTS(SELECT id FROM Person where login = "Приемников")
''',
'''\
SELECT EXISTS(SELECT id FROM Person where login = "Педиатров")
''']

    sqlPersonAdd = [
'''\
INSERT INTO `Person` (`createDatetime`,`createPerson_id`,`modifyDatetime`,`modifyPerson_id`,`deleted`,`code`,`federalCode`,`regionalCode`,`lastName`,`firstName`,`patrName`,`post_id`,`speciality_id`,`org_id`,`orgStructure_id`,`office`,`office2`,`tariffCategory_id`,`finance_id`,`retireDate`,`ambPlan`,`ambPlan2`,`ambNorm`,`homPlan`,`homPlan2`,`homNorm`,`expPlan`,`expNorm`,`login`,`password`,`userProfile_id`,`retired`,`birthDate`,`birthPlace`,`sex`,`SNILS`,`INN`,`availableForExternal`,`primaryQuota`,`ownQuota`,`consultancyQuota`,`externalQuota`,`lastAccessibleTimelineDate`,`timelineAccessibleDays`,`typeTimeLinePerson`) VALUES ('2011-05-11 14:47:58',1,'2011-05-11 15:03:19',1,0,'1','2','3','Регистраторова','Медсестра','Владимировна',200,66,3479,1,'','',NULL,NULL,NULL,0,0,0,0,0,0,0,0,'Регистраторова','698d51a19d8a121ce581499d7b701668',NULL,0,'2011-05-11','',0,'','',0,100,0,0,0,'2011-05-11',0,0);
''',
'''\
INSERT INTO `Person` (`createDatetime`,`createPerson_id`,`modifyDatetime`,`modifyPerson_id`,`deleted`,`code`,`federalCode`,`regionalCode`,`lastName`,`firstName`,`patrName`,`post_id`,`speciality_id`,`org_id`,`orgStructure_id`,`office`,`office2`,`tariffCategory_id`,`finance_id`,`retireDate`,`ambPlan`,`ambPlan2`,`ambNorm`,`homPlan`,`homPlan2`,`homNorm`,`expPlan`,`expNorm`,`login`,`password`,`userProfile_id`,`retired`,`birthDate`,`birthPlace`,`sex`,`SNILS`,`INN`,`availableForExternal`,`primaryQuota`,`ownQuota`,`consultancyQuota`,`externalQuota`,`lastAccessibleTimelineDate`,`timelineAccessibleDays`,`typeTimeLinePerson`) VALUES ('2011-05-11 14:49:06',1,'2011-05-11 15:03:02',1,0,'1','2','3','Коечкова','Медсестра','Анатольевна',165,67,3479,18,'','',NULL,NULL,NULL,0,0,0,0,0,0,0,0,'Коечкова','698d51a19d8a121ce581499d7b701668',NULL,0,'2011-05-11','',0,'','',0,100,0,0,0,'2011-05-11',0,0);
''',
'''\
INSERT INTO `Person` (`createDatetime`,`createPerson_id`,`modifyDatetime`,`modifyPerson_id`,`deleted`,`code`,`federalCode`,`regionalCode`,`lastName`,`firstName`,`patrName`,`post_id`,`speciality_id`,`org_id`,`orgStructure_id`,`office`,`office2`,`tariffCategory_id`,`finance_id`,`retireDate`,`ambPlan`,`ambPlan2`,`ambNorm`,`homPlan`,`homPlan2`,`homNorm`,`expPlan`,`expNorm`,`login`,`password`,`userProfile_id`,`retired`,`birthDate`,`birthPlace`,`sex`,`SNILS`,`INN`,`availableForExternal`,`primaryQuota`,`ownQuota`,`consultancyQuota`,`externalQuota`,`lastAccessibleTimelineDate`,`timelineAccessibleDays`,`typeTimeLinePerson`) VALUES ('2011-05-11 14:50:53',1,'2011-05-11 15:02:37',1,0,'1','2','3','Приемников','Врач','Александрович',79,52,3479,1,'','',NULL,NULL,NULL,0,0,0,0,0,0,0,0,'Приемников','698d51a19d8a121ce581499d7b701668',NULL,0,'2011-05-11','',0,'','',0,100,0,0,0,'2011-05-11',0,0);
''',
'''
INSERT INTO `Person` (`createDatetime`,`createPerson_id`,`modifyDatetime`,`modifyPerson_id`,`deleted`,`code`,`federalCode`,`regionalCode`,`lastName`,`firstName`,`patrName`,`post_id`,`speciality_id`,`org_id`,`orgStructure_id`,`office`,`office2`,`tariffCategory_id`,`finance_id`,`retireDate`,`ambPlan`,`ambPlan2`,`ambNorm`,`homPlan`,`homPlan2`,`homNorm`,`expPlan`,`expNorm`,`login`,`password`,`userProfile_id`,`retired`,`birthDate`,`birthPlace`,`sex`,`SNILS`,`INN`,`availableForExternal`,`primaryQuota`,`ownQuota`,`consultancyQuota`,`externalQuota`,`lastAccessibleTimelineDate`,`timelineAccessibleDays`,`typeTimeLinePerson`) VALUES ('2011-05-11 14:51:53',1,'2011-05-11 15:02:25',1,0,'1','2','3','Педиатров','Врач','Михайлович',75,52,3479,18,'','',NULL,NULL,NULL,0,0,0,0,0,0,0,0,'Педиатров','698d51a19d8a121ce581499d7b701668',NULL,0,'2011-05-11','',0,'','',0,100,0,0,0,'2011-05-11',0,0);
''']

    sqlProfiles = [
'''\
SELECT id FROM rbUserProfile where code = "admNurse";
''',
'''\
SELECT id FROM rbUserProfile where code = "strNurse";
''',
'''\
SELECT id FROM rbUserProfile where code = "admDoctor";
''',
'''\
SELECT id FROM rbUserProfile where code = "strDoctor";
''']

    sqlPersonProfiles = '''\
INSERT INTO Person_Profiles
(person_id, userProfile_id) VALUES (%d,%d);
'''

    for i in range(0,4):
        if (not select_one(c,sqlCheck[i])):
            p_id = insert_one(c, sqlPersonAdd[i])
            up_id = select_one(c, sqlProfiles[i])
            c.execute(sqlPersonProfiles % (p_id, up_id))
        else:
            print('User already added, skipping...')
    c.close()
   
def downgrade(conn):
    pass

