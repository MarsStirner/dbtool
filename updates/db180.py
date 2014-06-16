#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
функции, индексы, модификации таблиц для выгрузки в ТФОМС
'''

def upgrade(conn):
    c = conn.cursor()
    global tools

#-------------------- Table Modifications -----------------------------------------------------------------------------------------------------------
    sqls = [
	'''ALTER TABLE `Account` ADD COLUMN `begDate` DATE NOT NULL COMMENT 'Дата начала интервала' AFTER `refusedSum`;''',
	'''ALTER TABLE `Account` ADD COLUMN `endDate` DATE NOT NULL COMMENT 'Дата конца интервала' AFTER `begDate`;''',
	'''ALTER TABLE `Account` ADD COLUMN `note` VARCHAR(50) NOT NULL DEFAULT '' COMMENT 'Примечание' AFTER `format_id`;''',
	'''ALTER TABLE `Account_Item` ADD COLUMN `client_id` INT NULL COMMENT 'Пациент {Client}' AFTER `serviceDate`;''',
	'''ALTER TABLE `Account_Item` ADD COLUMN `notUploadAnymore` TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Отметка не выгружать больше' AFTER `note`;''',
	'''ALTER TABLE `Contract_Tariff` ADD INDEX `service_unit_deleted` (`service_id`, `unit_id`, `deleted`);''',
	'''ALTER TABLE `ClientContact`	ADD INDEX `client_id_deleted_contactType` (`client_id`, `deleted`, `contactType_id`);''',
	'''ALTER TABLE `Diagnostic` ADD INDEX `event_id_deleted_diagnosisType` (`event_id`, `deleted`, `diagnosisType_id`);''',
	'''ALTER TABLE `VariablesforSQL` CHANGE COLUMN `label` `label` VARCHAR(255) NOT NULL COMMENT 'метка' AFTER `var_type`;'''
    ]
    for s in sqls:
        tools.executeEx(c, s, mode=['ignore_duplicates',])

    sql = '''
CREATE TABLE IF NOT EXISTS `Account_AktInfo` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`account_id` INT(11) NOT NULL COMMENT 'Ссылка на счет {Account}',
	`file_name` VARCHAR(30) NOT NULL COMMENT 'Имя файла' COLLATE 'utf8_unicode_ci',
	`records_count` INT(11) NOT NULL COMMENT 'Число записей в файле',
	PRIMARY KEY (`id`),
	INDEX `account_aktinfo_ibfk_1` (`account_id`),
	CONSTRAINT `account_aktinfo_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `Account` (`id`) ON DELETE CASCADE
)
COMMENT=''
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0;
'''
    c.execute(sql)

#-------------------- Functions ---------------------------------------------------------------------------------------------------------------------	
    sql = '''
DROP FUNCTION IF EXISTS `num_sunday_days`;
'''
    c.execute(sql)

    sql = '''
CREATE DEFINER=%s FUNCTION `num_sunday_days`(`start_date` DATE, `end_date` DATE)
	RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
	CONTAINS SQL
	SQL SECURITY DEFINER
	COMMENT 'кол-во воскресений между датами'
BEGIN
DECLARE sundays INT;
DECLARE stDate DATE;
DECLARE enDate DATE;
SET stDate = DATE(start_date);
SET enDate = DATE(end_date);
SET sundays = 0;
 
IF enDate >= stDate
THEN
 	WHILE (DAYOFWEEK(stDate) <> 1 AND enDate > stDate)
		DO
   		SET stDate = DATE_ADD(stDate,INTERVAL 1 DAY);
  	END WHILE; 
  		 
  IF DAYOFWEEK(stDate) = 1
  THEN
    SET sundays = sundays + 1;  
  END IF; 
  
  SET sundays = sundays + FLOOR(TIMESTAMPDIFF(DAY,stDate, enDate)  / 7);  

ELSE
    SET sundays = 0;
END IF;
   RETURN(sundays);
END
'''%config['definer']
    c.execute(sql)

    sql = '''
DROP FUNCTION IF EXISTS `checkAge`;
'''
    c.execute(sql)

    sql = '''
CREATE DEFINER=%s FUNCTION `checkAge`(`age` VARCHAR(50), `birthDate` DATE, `checkDate` DATE)
	RETURNS tinyint(4)
	LANGUAGE SQL
	DETERMINISTIC
	NO SQL
	SQL SECURITY DEFINER
	COMMENT 'Ограничение на возраст'
BEGIN
DECLARE RESULT TINYINT;
SET RESULT =
(age ='' OR (
-- Проверяем левую часть селектора возраста
(
  SUBSTRING_INDEX(age, '-', 1) = ''
  -- Год ли это
  OR (INSTR(SUBSTRING_INDEX(age, '-', 1), 'Г') AND REPLACE(SUBSTRING_INDEX(age, '-', 1), 'Г', '') <= TIMESTAMPDIFF(YEAR, birthDate, checkDate ) )
  -- А может месяц
  OR (INSTR(SUBSTRING_INDEX(age, '-', 1), 'М') AND REPLACE(SUBSTRING_INDEX(age, '-', 1), 'М', '') <= TIMESTAMPDIFF(MONTH, birthDate, checkDate) )
  -- А еще оказывается бывает в неделях
  OR (INSTR(SUBSTRING_INDEX(age, '-', 1), 'Н') AND REPLACE(SUBSTRING_INDEX(age, '-', 1), 'Н', '') <= TIMESTAMPDIFF(WEEK, birthDate, checkDate) )
  -- Или вдруг день
  OR (INSTR(SUBSTRING_INDEX(age, '-', 1), 'Д') AND REPLACE(SUBSTRING_INDEX(age, '-', 1), 'Д', '') <= TIMESTAMPDIFF(DAY, birthDate, checkDate) )
)
AND
(
  SUBSTRING_INDEX(age, '-', -1) = ''
  -- Год ли это
  OR (INSTR(SUBSTRING_INDEX(age, '-', -1), 'Г') AND REPLACE(SUBSTRING_INDEX(age, '-', -1), 'Г', '') > TIMESTAMPDIFF(YEAR, birthDate, checkDate ) )
  -- А может месяц
  OR (INSTR(SUBSTRING_INDEX(age, '-', -1), 'М') AND REPLACE(SUBSTRING_INDEX(age, '-', -1), 'М', '') > TIMESTAMPDIFF(MONTH, birthDate, checkDate) )
  -- А еще оказывается бывает в неделях
  OR (INSTR(SUBSTRING_INDEX(age, '-', -1), 'Н') AND REPLACE(SUBSTRING_INDEX(age, '-', -1), 'Н', '') > TIMESTAMPDIFF(WEEK, birthDate, checkDate) )
  -- Или вдруг день
  OR (INSTR(SUBSTRING_INDEX(age, '-', -1), 'Д') AND REPLACE(SUBSTRING_INDEX(age, '-', -1), 'Д', '') > TIMESTAMPDIFF(DAY, birthDate, checkDate) )
)
)
);
RETURN RESULT;
END
'''%config['definer']
    c.execute(sql)

    sql = '''
DROP FUNCTION IF EXISTS `search_CSG`;
'''	
    c.execute(sql)

    sql = '''
CREATE DEFINER=%s FUNCTION `search_CSG`(`CSG_enable` VARCHAR(5) charset utf8, `MO_level` VARCHAR(2) charset utf8, `contract_id` INT, `action_endDate` DATETIME, `serv_id` INT, `diag_id` VARCHAR(10) charset utf8, `oper_id` VARCHAR(20))
	RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
	READS SQL DATA
	SQL SECURITY DEFINER
	COMMENT 'Поиск КСГ-группы'
BEGIN
DECLARE var_result int;

IF CSG_enable IS NULL OR CSG_enable = 'да' THEN BEGIN
IF oper_id IS NOT NULL and oper_id <> '' THEN BEGIN
set var_result =
(SELECT rbCSG.id FROM rbCSG
WHERE rbCSG.rbOperationType_TFOMSCode = oper_id
AND   EXISTS(SELECT * FROM rbCSG_Service
             WHERE  rbCSG_Service.rbCSG_id = rbCSG.id
             AND    rbCSG_Service.rbService_id = serv_id LIMIT 1)

/*AND   (FIND_IN_SET(diag_id,rbCSG.MKBlist) > 0 OR (FIND_IN_SET(SUBSTRING(diag_id,1,3), rbCSG.MKBlist) > 0 AND LOCATE(CONCAT(SUBSTRING(diag_id,1,3), '.'), rbCSG.MKBlist) = 0))  */
AND   (EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id
            AND    rbCSG_MKB.MKB_diagId   = diag_id
            )
OR
(EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id
            AND    substring(rbCSG_MKB.MKB_diagId,1,3)   = substring(diag_id,1,3)
            )
AND not EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id
            AND    substring(rbCSG_MKB.MKB_diagId,1,4)   = concat(substring(diag_id,1,3),'.')
            ))
)
AND   FIND_IN_SET(MO_level, rbCSG.MO_levels) > 0
AND  EXISTS(SELECT * FROM Contract_Tariff
            WHERE Contract_Tariff.master_id  = contract_id
            AND   Contract_Tariff.service_id = serv_id
            AND   Contract_Tariff.rbCSG_id   = rbCSG.id
            AND   Contract_Tariff.begDate <= date(action_endDate)
            AND   Contract_Tariff.endDate >= date(action_endDate)
            AND   Contract_Tariff.deleted = 0
           )
LIMIT 1);
IF var_result IS NULL THEN BEGIN
set var_result = 
(SELECT rbCSG.id FROM rbCSG
WHERE rbCSG.rbOperationType_TFOMSCode = oper_id
AND   EXISTS(SELECT * FROM rbCSG_Service
             WHERE  rbCSG_Service.rbCSG_id = rbCSG.id
             AND    rbCSG_Service.rbService_id = serv_id LIMIT 1)

/*AND  rbCSG.MKBlist = '' */
AND   NOT EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id    
            )
AND   FIND_IN_SET(MO_level, rbCSG.MO_levels) > 0
AND  EXISTS(SELECT * FROM Contract_Tariff
            WHERE Contract_Tariff.master_id  = contract_id
            AND   Contract_Tariff.service_id = serv_id
            AND   Contract_Tariff.begDate <= date(action_endDate)
            AND   Contract_Tariff.endDate >= date(action_endDate)
            AND   Contract_Tariff.rbCSG_id   = rbCSG.id
           )
LIMIT 1);
END;
END IF;
END;
END IF;
IF var_result IS NULL or var_result = 0 THEN BEGIN
set var_result = 
(SELECT rbCSG.id FROM rbCSG
WHERE rbCSG.rbOperationType_TFOMSCode IS NULL
AND   EXISTS(SELECT * FROM rbCSG_Service
             WHERE  rbCSG_Service.rbCSG_id = rbCSG.id
             AND    rbCSG_Service.rbService_id = serv_id LIMIT 1)

/*AND   (FIND_IN_SET(diag_id,rbCSG.MKBlist) > 0 OR (FIND_IN_SET(SUBSTRING(diag_id,1,3), rbCSG.MKBlist) > 0 AND LOCATE(CONCAT(SUBSTRING(diag_id,1,3), '.'), rbCSG.MKBlist) = 0)) */
AND   (EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id
            AND    rbCSG_MKB.MKB_diagId   = diag_id
            )
OR
(EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id
            AND    substring(rbCSG_MKB.MKB_diagId,1,3)   = substring(diag_id,1,3)
            )
AND not EXISTS(SELECT * FROM rbCSG_MKB
            WHERE  rbCSG_MKB.rbCSG_id = rbCSG.id
            AND    substring(rbCSG_MKB.MKB_diagId,1,4)   = concat(substring(diag_id,1,3),'.')
            ))
)
AND   FIND_IN_SET(MO_level, rbCSG.MO_levels) > 0
AND  EXISTS(SELECT * FROM Contract_Tariff
            WHERE Contract_Tariff.master_id  = contract_id
            AND   Contract_Tariff.service_id = serv_id
            AND   Contract_Tariff.begDate <= date(action_endDate)
            AND   Contract_Tariff.endDate >= date(action_endDate)
            AND   Contract_Tariff.rbCSG_id   = rbCSG.id
           )
LIMIT 1);
END;
END IF;
END;
END IF;
IF var_result IS NULL THEN SET var_result = 0; END IF;
RETURN var_result;
END
'''%config['definer']
    c.execute(sql)

    sql = '''
DROP FUNCTION IF EXISTS `search_Treatment`;
'''	
    c.execute(sql)

    sql = '''
CREATE DEFINER=%s FUNCTION `search_Treatment`(`contract_id` INT, `action_endDate` DATETIME, `serv_id` INT, `diag_code` VARCHAR(10) charset utf8, `treatment_id` INT)
	RETURNS int(11)
	LANGUAGE SQL
	DETERMINISTIC
	READS SQL DATA
	SQL SECURITY DEFINER
	COMMENT 'поиск ВМП'
BEGIN
DECLARE var_result int;


set var_result =
(SELECT rbTreatment.id FROM rbTreatment, rbPacientModel
WHERE rbTreatment.id = treatment_id
AND   rbPacientModel.id = rbTreatment.pacientModel_id
AND   EXISTS(SELECT * FROM rbTreatment_Service
             WHERE  rbTreatment_Service.rbTreatment_id = rbTreatment.id
             AND    rbTreatment_Service.rbService_id = serv_id LIMIT 1)


AND   (EXISTS(SELECT * FROM MKB_QuotaType_PacientModel, MKB
            WHERE  MKB_QuotaType_PacientModel.pacientModel_id = rbPacientModel.id
            AND    MKB.id = MKB_QuotaType_PacientModel.MKB_id   
            AND    MKB.diagId = diag_code
            )
OR
(EXISTS(SELECT * FROM MKB_QuotaType_PacientModel, MKB
            WHERE  MKB_QuotaType_PacientModel.pacientModel_id = rbPacientModel.id
            AND    MKB.id = MKB_QuotaType_PacientModel.MKB_id   
            AND    substring(MKB.diagId, 1, 3) = substring(diag_code, 1, 3)
            )
AND not EXISTS(SELECT * FROM MKB_QuotaType_PacientModel, MKB
            WHERE  MKB_QuotaType_PacientModel.pacientModel_id = rbPacientModel.id
            AND    MKB.id = MKB_QuotaType_PacientModel.MKB_id   
            AND    substring(MKB.diagId, 1, 4) = concat(substring(diag_code, 1, 3), '.')
            ))
)

AND  EXISTS(SELECT * FROM Contract_Tariff
            WHERE Contract_Tariff.master_id  = contract_id
            AND   Contract_Tariff.service_id = serv_id
            AND   Contract_Tariff.rbTreatment_id   = rbTreatment.id
            AND   Contract_Tariff.begDate <= date(action_endDate)
            AND   Contract_Tariff.endDate >= date(action_endDate) 
            AND   Contract_Tariff.deleted = 0
           )
LIMIT 1);

IF var_result IS NULL THEN SET var_result = 0; END IF;
RETURN var_result;
END
'''%config['definer']
    c.execute(sql)

    sql = '''
DROP FUNCTION IF EXISTS `search2P_Extended`;
'''
    c.execute(sql)

    sql = '''
CREATE DEFINER=%s FUNCTION `search2P_Extended`(`client_id` INT, `action_endDate` DATETIME, `contract_id` INT, `service_infis` VARCHAR(10), `eventType_id` INT, `orgStructureIdList` VARCHAR(255))
	RETURNS varchar(5) CHARSET utf8
	LANGUAGE SQL
	NOT DETERMINISTIC
	CONTAINS SQL
	SQL SECURITY DEFINER
	COMMENT ''
BEGIN

DECLARE var_result varchar(10);

set var_result =
(SELECT CONCAT(rbMedicalAidUnit.code, rbMedicalKind.code, rbResult.code)
FROM Action
INNER JOIN Event ON Event.id = Action.event_id
LEFT JOIN EventType			ON EventType.id = Event.eventType_id
LEFT JOIN Diagnostic			ON (Diagnostic.event_id = Event.id AND   (Diagnostic.diagnosisType_id = 2 OR Diagnostic.diagnosisType_id = 1)  AND   Diagnostic.deleted  = 0)
LEFT JOIN rbResult 			ON rbResult.id               = IF(Diagnostic.result_id  IS NOT NULL,  Diagnostic.result_id, Event.result_id)
INNER JOIN ActionType		        ON ActionType.id = Action.actionType_id AND ActionType.service_id IS NOT NULL  
INNER JOIN rbService			ON rbService.id = ActionType.service_id
LEFT JOIN rbMedicalKind		        ON   ((rbMedicalKind.id = rbService.rbMedicalKind_id  and EventType.rbMedicalKind_id IS NULL)
   or ( rbMedicalKind.id = EventType.rbMedicalKind_id AND EventType.rbMedicalKind_id IS NOT NULL ) )


LEFT JOIN MedicalKindUnit 		ON  (MedicalKindUnit.rbMedicalKind_id = rbMedicalKind.id
AND (MedicalKindUnit.eventType_id = EventType.id  OR (MedicalKindUnit.eventType_id IS NULL
AND NOT EXISTS(SELECT * FROM MedicalKindUnit bMedicalKindUnit   WHERE bMedicalKindUnit.eventType_id =  EventType.id  AND bMedicalKindUnit.rbMedicalKind_id = rbMedicalKind.id) )  ) )

LEFT JOIN rbMedicalAidUnit		ON rbMedicalAidUnit.id = MedicalKindUnit.rbMedicalAidUnit_id
LEFT JOIN Person ON Person.id = Action.person_id
WHERE    Event.client_id     = client_id  AND      Event.deleted     = 0
AND      Event.contract_id = contract_id
AND      Event.eventType_id =  eventType_id
AND      Action.deleted    = 0
AND      SUBSTRING(rbService.infis, 1, 5) = SUBSTRING(service_infis , 1, 5)
AND      Action.endDate     < action_endDate
AND        rbMedicalKind.code = 'P'
AND 	 (FIND_IN_SET(Person.orgStructure_id, orgStructureIdList) OR orgStructureIdList = '')
 ORDER BY Action.endDate DESC, Action.id DESC
limit 1);

IF var_result IS NULL THEN SET var_result = ''; END IF;
RETURN var_result;

END
'''%config['definer']
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass
