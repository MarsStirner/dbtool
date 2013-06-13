# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Добавляет во все таблицы, где содержится диапазон возрастов, \
столбцы для хранения диапазона возрастов в структурированном виде. \
Изменяемые таблицы: ActionPropertyType, ActionPropertyTemplate, \
ActionType, ActionTemplate, Contract_Contingent, \
Contract_Tariff, EventType, EventType_Action, \
EventType_Diagnostic, MKB, OrgStructure_HospitalBed \
rbNet, rbService_Profile, rbSpeciality, TempInvalid. \
Изменяемое представление: vHospitalBed
'''

tblActionType = "ActionType"
tblActionPropertyType = "ActionPropertyType"

upgradeTables = ( "ActionPropertyType",
		  "ActionPropertyTemplate",
		  "ActionType",
		  "ActionTemplate",
		  "Contract_Contingent",
		  "Contract_Tariff",
		  "EventType",
		  "EventType_Action",
		  "EventType_Diagnostic",
		  "MKB",
		  "OrgStructure_HospitalBed",
		  "rbNet",
		  "rbService_Profile",
		  "rbSpeciality",
		  "TempInvalid"
		)


AgeSelectorUnits = u'днмг'

sqlDropvHospitalBedView = '''\
DROP VIEW IF EXISTS vHospitalBed
'''

def parseAgeSelectorPart(val):
    if val:
        matchObject = re.match(r'^(\d+)\s*([^\d\s]+)$', val)
        if matchObject:
            strCount, strUnit = matchObject.groups()
	    count = int(strCount) if strCount else 0
            unit  = AgeSelectorUnits.find(strUnit.lower())+1
            if unit == 0:
    		#raise ValueError, u'Неизвестная единица измерения "%s"' % strUnit
    		print(u'Неизвестная единица измерения "%s"' % strUnit)
            return (unit, count)
        else:
            #print(val)
            #raise ValueError, u'Недопустимый синтаксис части селектора возраста "%s"' % val
            print(u'Недопустимый синтаксис части селектора возраста "%s"' % val)
            return 0, 0
    else:
        return 0, 0


def parseAgeSelectorInt(val):
    ageStr = (unicode(val) if val else u'')
    parts = ageStr.split('-')
    if len(parts) == 2:
        begUnit, begCount = ( parseAgeSelectorPart(parts[0].strip()) if parts[0] else (0, 0) )
        endUnit, endCount = ( parseAgeSelectorPart(parts[1].strip()) if parts[1] else (0, 0) )
        return begUnit, begCount, endUnit, endCount
    elif len(parts) == 1:
        if parts[0]:
            begUnit, begCount = parseAgeSelectorPart(parts[0].strip())
        else:
            begUnit, begCount = 0, 0
        return begUnit, begCount, 0, 0

# Код переноса значения диапазона возрастов из строковго
#  значения в новый набор столбцов
def copyAgeFromString(c, tblName):
    sql = '''\
SELECT `id`, `age` FROM {tableName}
'''
    struct_ages = []
    c.execute(sql.format(tableName=tblName))
    for r in c.fetchall():
	#print(r)
	struct_ages.append((r[0], parseAgeSelectorInt(r[1])))
	#print(parseAgeSelectorInt(r[1]))

    sql = '''\
UPDATE {tableName} SET `age_bu` = {a_bu},
     		       `age_bc` = {a_bc},
		       `age_eu` = {a_eu},
		       `age_ec` = {a_ec}
		   WHERE id = {row_id}
'''
    for e in struct_ages:
	c.execute(sql.format(tableName = tblName,
			     a_bu = e[1][0],
			     a_bc = e[1][1],
			     a_eu = e[1][2],
			     a_ec = e[1][3],
			     row_id = e[0]))


def upgrade(conn):
    global tools
    # Код добавления столбцов для структурированного хранения 
    #  диапазонов возрастов
    sqlAddAgeColumns = u'''\
ALTER TABLE {tableName}
    ADD COLUMN `age_ec` SMALLINT(3) UNSIGNED ZEROFILL AFTER `age`,
    ADD COLUMN `age_eu` TINYINT(1) UNSIGNED ZEROFILL AFTER `age`,
    ADD COLUMN `age_bc` SMALLINT(3) UNSIGNED ZEROFILL AFTER `age`,
    ADD COLUMN `age_bu` TINYINT(1) UNSIGNED ZEROFILL AFTER `age`
'''

    sqlCommentAgeColumns = u'''\
ALTER TABLE {tableName}
    CHANGE `age_ec` `age_ec` SMALLINT(3) UNSIGNED ZEROFILL COMMENT 'Величина верхней границы дипазона возраста',
    CHANGE `age_eu` `age_eu` TINYINT(1) UNSIGNED ZEROFILL  COMMENT 'Единица измерения верхней границы дипазона возраста (0 - не задано, \
															       1 - день, \
															       2 - неделя, \
															       3 - месяц, \
															       4 - год)',
    CHANGE `age_bc` `age_bc` SMALLINT(3) UNSIGNED ZEROFILL COMMENT 'Величина нижней границы дипазона возраста',
    CHANGE `age_bu` `age_bu` TINYINT(1) UNSIGNED ZEROFILL COMMENT 'Единица измерения нижней границы дипазона возраста (0 - не задано, \
															       1 - день, \
															       2 - неделя, \
															       3 - месяц, \
															       4 - год)'
'''


    sqlCreatevHospitalBedView = '''\
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vHospitalBed` AS 
    select `OrgStructure_HospitalBed`.`id` AS `id`,
	`OrgStructure_HospitalBed`.`master_id` AS `master_id`,
	`OrgStructure_HospitalBed`.`idx` AS `idx`,
	`OrgStructure_HospitalBed`.`code` AS `code`,
	`OrgStructure_HospitalBed`.`name` AS `name`,
	`OrgStructure_HospitalBed`.`isPermanent` AS `isPermanent`,
	`OrgStructure_HospitalBed`.`type_id` AS `type_id`,
	`OrgStructure_HospitalBed`.`profile_id` AS `profile_id`,
	`OrgStructure_HospitalBed`.`relief` AS `relief`,
	`OrgStructure_HospitalBed`.`schedule_id` AS `schedule_id`,
	`OrgStructure_HospitalBed`.`begDate` AS `begDate`,
	`OrgStructure_HospitalBed`.`endDate` AS `endDate`,
	`OrgStructure_HospitalBed`.`sex` AS `sex`,
	`isOccupiedTransportable`(`OrgStructure_HospitalBed`.`id`,now()) AS `isTransportable`,
	`OrgStructure_HospitalBed`.`age` AS `age`,
	`OrgStructure_HospitalBed`.`age_bu` AS `age_bu`,
	`OrgStructure_HospitalBed`.`age_bc` AS `age_bc`,
	`OrgStructure_HospitalBed`.`age_eu` AS `age_eu`,
	`OrgStructure_HospitalBed`.`age_ec` AS `age_ec`,
	`OrgStructure_HospitalBed`.`involution` AS `involution`,
	`OrgStructure_HospitalBed`.`begDateInvolute` AS `begDateInvolute`,
	`OrgStructure_HospitalBed`.`endDateInvolute` AS `endDateInvolute`,
	`isHospitalBedBusy`(`OrgStructure_HospitalBed`.`id`,now()) AS `isBusy` from `OrgStructure_HospitalBed`
'''

    c = conn.cursor()
    for tblName in upgradeTables:
        tools.executeEx(c, sqlAddAgeColumns.format(tableName=tblName), mode=['ignore_dublicates'])
        tools.executeEx(c, sqlCommentAgeColumns.format(tableName=tblName), mode=['ignore_dublicates'])

    for tblName in upgradeTables:
        copyAgeFromString(c, tblName)

    c.execute(sqlDropvHospitalBedView)
    c.execute(sqlCreatevHospitalBedView)


def downgrade(conn):
    sqlDropAgeColumns = '''\
ALTER TABLE {tableName}
    DROP COLUMN `age_ec`,
    DROP COLUMN `age_eu`,
    DROP COLUMN `age_bc`,
    DROP COLUMN `age_bu`
'''

    sqlCreatevOldHospitalBedView = '''\
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `vHospitalBed` AS 
    select `OrgStructure_HospitalBed`.`id` AS `id`,
	`OrgStructure_HospitalBed`.`master_id` AS `master_id`,
	`OrgStructure_HospitalBed`.`idx` AS `idx`,
	`OrgStructure_HospitalBed`.`code` AS `code`,
	`OrgStructure_HospitalBed`.`name` AS `name`,
	`OrgStructure_HospitalBed`.`isPermanent` AS `isPermanent`,
	`OrgStructure_HospitalBed`.`type_id` AS `type_id`,
	`OrgStructure_HospitalBed`.`profile_id` AS `profile_id`,
	`OrgStructure_HospitalBed`.`relief` AS `relief`,
	`OrgStructure_HospitalBed`.`schedule_id` AS `schedule_id`,
	`OrgStructure_HospitalBed`.`begDate` AS `begDate`,
	`OrgStructure_HospitalBed`.`endDate` AS `endDate`,
	`OrgStructure_HospitalBed`.`sex` AS `sex`,
	`isOccupiedTransportable`(`OrgStructure_HospitalBed`.`id`,now()) AS `isTransportable`,
	`OrgStructure_HospitalBed`.`age` AS `age`,
	`OrgStructure_HospitalBed`.`involution` AS `involution`,
	`OrgStructure_HospitalBed`.`begDateInvolute` AS `begDateInvolute`,
	`OrgStructure_HospitalBed`.`endDateInvolute` AS `endDateInvolute`,
	`isHospitalBedBusy`(`OrgStructure_HospitalBed`.`id`,now()) AS `isBusy` from `OrgStructure_HospitalBed`
'''


    c = conn.cursor()
    for tblName in upgradeTables:
        c.execute(sqlDropAgeColumns.format(tableName=tblName))

    c.execute(sqlDropvHospitalBedView)
    c.execute(sqlCreatevOldHospitalBedView)
