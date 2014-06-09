#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Свободные переменные для выгрузки в ТФОМС
'''


def upgrade(conn):
    c = conn.cursor()
#-------------------- SpecialVariables --------------------------------------------------------------------------------------------------------------
    variables = {
	'@contractId': 'Идентификатор контракта',
	'@beginInterval' : 'Дата начала интервала выгрузки',
	'@endInterval' : 'Дата окончания интервала выгрузки',
	'@orgStructureIdList' : 'Список подразделений по которым происходит выгрузка',
	'@levelMO' : 'Уровень МО',
	'@obsoleteInfisCode' : 'Устаревший инфис-код',
	'@organisationId' : 'Идентификатор ЛПУ, в котором проводилось лечение',
	'@SMOArea' : 'Код области страховых компаний',
	
	'@actionId': 'Идентификатор действия',
	'@clientId': 'Идентифкатор пациента',
	'@eventTypeId': 'Идентифкатор типа обращения',
	'@InsurerArea' : 'Код области страховщика пациента',
	'@serviceInfisCode' : 'Инфис-код основной услуги',
	'@checkDate' : 'Дата+Время оказания основной услуги',

	'@movingActionTypeId' : 'Идентификатор движения',
	'@stationaryMainDiagnosisActionPropertyTypeId' : 'Идентификатор свойства действия \"Основной диагноз\"',
	'@stationarySecondaryDiagnosisActionPropertyTypeId' : 'Идентификатор свойства действия \"Сопутствующий диагноз\"',
	'@stationaryIshodActionPropertyTypeId' : 'Идентификатор свойства действия \"Исход заболевания\"',
	'@stationaryResultActionPropertyTypeId' : 'Идентификатор свойства действия \"Результат заболевания\"',
	'@stationaryCSGActionPropertyTypeId' : 'Идентификатор свойства действия \"Лечение по КСГ\"',
	'@stationaryStageActionPropertyTypeId' : 'Идентификатор свойства действия \"Стадия заболевания\"',
	'@stationaryHospitalBedProfileActionPropertyTypeId' : 'Идентификатор свойства действия \"Профиль койки\"',
	
	'@multipleBirthContactTypeId' : 'Идетификатор типа контакта \"Номер ребенка при многоплодных родах\"'
    }
	
    specialvar = {
	'SpecialVar_getMovingActionTypeId' : '''
SELECT 
ActionType.id 
FROM ActionType 
WHERE 
ActionType.flatCode = 'moving' 
AND 
ActionType.deleted = 0;
''',
	'SpecialVar_getStationaryDiagnosisActionPropertyTypeId' : '''
SELECT 
ActionPropertyType.id 
FROM 
ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.name = 'Диагноз при выписке (переводе)';
''',
	'SpecialVar_getStationarySecondaryDiagnosisActionPropertyTypeId' : '''
SELECT 
ActionPropertyType.id 
FROM 
ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.name = 'Сопутствующий диагноз при выписке (переводе)';
''',
	'SpecialVar_getStationaryIshodActionPropertyTypeId': '''
SELECT 
ActionPropertyType.id 
FROM 
ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.name = 'Исход при выписке (переводе)';
''',
	'SpecialVar_getStationaryResultActionPropertyTypeId': '''
SELECT 
ActionPropertyType.id 
FROM 
ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.name = 'Результат при выписке (переводе)';
''',
	'SpecialVar_getStationaryCSGActionPropertyTypeId': '''
SELECT 
ActionPropertyType.id 
FROM 
ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.name = 'Разрешить оплату по КСГ при наличии тарифа';
''',
	'SpecialVar_getStationaryStageActionPropertyTypeId': '''
SELECT 
ActionPropertyType.id 
FROM ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.name = 'Стадия при выписке (переводе)';
''',
	'SpecialVar_getStationaryHospitalBedProfileActionPropertyTypeId': '''
SELECT 
ActionPropertyType.id 
FROM ActionPropertyType 
WHERE 
ActionPropertyType.actionType_id = ::@movingActionTypeId 
AND 
ActionpropertyType.deleted = 0 
AND 
ActionPropertyType.code = 'hospitalBedProfile';
''',
	'SpecialVar_getMultipleBirthContactTypeId': '''
SELECT rbContactType.id
FROM rbContactType  
WHERE rbContactType.name = 'Номер ребенка при многоплодных родах
''',
	'SpecialVar_TFOMS_Policlinic': '''
SELECT 
-- ID обращения
Event.id as 'EventId',
-- Тип обращения
EventType.id as 'EventTypeId',
-- ID действия
Action.id as 'ActionId',
-- ID источника финансирования
rbServiceFinance.id as 'rbServiceFinanceId',
-- Данные пациента --------------------------------------------------
-- ID пациента
Client.id as 'ClientId',
-- Фамилия пациента
IF(Client.lastName = '', 'НЕТ',	UCASE(Client.lastName))	AS 'FAM',
-- Имя пациента
UCASE(Client.firstName)	AS 'IM',
-- Отчество пациента
IF(Client.patrName = '', 'НЕТ', UCASE(Client.patrName))	AS 'OT',
-- Пол пациента
Client.sex	AS 'W',
-- Дата рождения пациента 
Client.birthDate AS 'DR',
-- место рождения пациента
Client.birthPlace AS 'MR',
-- СНИЛС пациента
IF(Client.SNILS <> '',  INSERT(INSERT(INSERT(Client.SNILS, 4, 0, '-'), 8, 0,  '-'), 12,0, ' ' ), '') AS 'SNILS', 
-- Вес пациента
'0' AS 'VNOV_D',
-- Прдеставитель пациента -------------------------------------------
-- ID представителя
Spokesman.id as 'spokesmanId',
-- Фамилия представителя 
IF(Spokesman.id IS NOT NULL, IF(Spokesman.lastName = '', 'НЕТ', UCASE(Spokesman.lastName)), '')  AS 'FAM_P',
-- Имя представителя
IF(Spokesman.id IS NOT NULL, UCASE(Spokesman.firstName), '') AS 'IM_P',
-- Отчество представителя
IF(Spokesman.id IS NOT NULL, IF(Spokesman.patrName = '', 'НЕТ', UCASE(Spokesman.patrName)), '') AS 'OT_P',
-- Пол представителя
IF(Spokesman.id IS NOT NULL, cast(Spokesman.sex as char), '') AS 'W_P',
-- Дата рождения представителя
IF(Spokesman.id IS NOT NULL, cast(Spokesman.birthDate as char), '')	AS 'DR_P',
-- Документы --------------------------------------------------------
-- ID документа
IF(ClientDocument.id IS NULL, SpokesmanDocument.id, ClientDocument.id) AS 'DocumentId',
-- Код типа документа
IF(SpokesmanDocument.id IS NULL,
	IF(ClientDocumentType.code IS NOT NULL, 
		TRIM(LEADING '0' FROM  ClientDocumentType.code),
		''
	),
	TRIM(LEADING '0'  FROM SpokesmanDocumentType.code)
)  AS 'DOCTYPE', 
-- Серия документа
 IF(SpokesmanDocumentType.code IS NULL,
	IF(ClientDocumentType.code IS NOT NULL, 
		IF(TRIM(LEADING '0' FROM  ClientDocumentType.code) = '3', 
			REPLACE(ClientDocument.serial, ' ', '-'), 
			ClientDocument.serial
		),
		''
	),
	IF(TRIM(LEADING '0'  FROM SpokesmanDocumentType.code) = '3',
		REPLACE(SpokesmanDocument.serial, ' ', '-'), 
		SpokesmanDocument.serial
	)
) AS 'DOCSER',
-- Номер документа
 IF(SpokesmanDocumentType.code IS NULL, 
	IF(ClientDocumentType.code IS NOT NULL, ClientDocument.number, ''),
	SpokesmanDocument.number
) AS 'DOCNUM',
-- Полисы -----------------------------------------------------------
-- ID полиса
IF(ClientPolicy.id IS NULL, SpokesmanPolicy.id, ClientPolicy.id) AS 'PolicyId',
-- Тип полиса
IF(ClientPolicy.id IS NULL, 
	IF(SpokesmanPolicy.id IS NULL, '', SpokesmanPolicyType.TFOMSCode),
	rbPolicyType.TFOMSCode
) AS 'VPOLIS',
-- Серия полиса
 IF(ClientPolicy.id IS NULL, 
	IF(SpokesmanPolicy.id IS NULL, '', SpokesmanPolicy.serial),
	ClientPolicy.serial
) AS 'SPOLIS',
-- Номер полиса
IF(ClientPolicy.id IS NULL, 
	IF(SpokesmanPolicy.id IS NULL, '', SpokesmanPolicy.number),
	ClientPolicy.number
) AS 'NPOLIS', 
-- Инфис-код страховой
COALESCE(Insurer.infisCode, '') AS 'SMO',
COALESCE(Insurer.fullName, '') AS 'SMO_NAM',
COALESCE(Insurer.OGRN, '') AS 'SMO_OGRN',
COALESCE(Insurer.OKATO, '') AS 'SMO_OK',
COALESCE(Insurer.area, '') AS 'SMO_AREA',
-- Свойства оказанной услуги ----------------------------------------
-- Признак новорожденного (нету своего полиса и возраст на момент оказания услуги менее 2-х месяцев)
IF( ClientPolicy.id IS NULL 
	AND
	TIMESTAMPDIFF(MONTH, Client.birthDate, Action.endDate) < 2,
	CONCAT(
		CAST(Client.sex AS CHAR),
		CAST(DATE_FORMAT(Client.birthDate, '%d%m%y') AS CHAR),
		IF(ClientContact.id IS NOT NULL, ClientContact.contact, '1')
	),
    '0'
) AS 'NOVOR',  
-- Условия оказания мед помощи
rbEventTypePurpose.codePlace AS 'USL_OK',
-- Вид помощи
rbMedicalAidType.code AS 'VIDPOM',
-- TODO не помню что значит тег
IF(Event.order = 2, 2, 1) AS 'FOR_POM',
-- Признак экстренного случая
IF(Event.order = 2, 2, 1) AS 'EXTR',
-- TODO
IF(OrgStructure.infisInternalCode IS NOT NULL AND OrgStructure.infisInternalCode <> '', OrgStructure.infisInternalCode, ::@obsoleteInfisCode) AS 'LPU_1', 
-- Подразделение МО в котором оказывается помощь
rbService.departCode AS 'PODR',
-- Профиль помощи
rbMedicalAidProfile.code AS 'PROFIL',
-- Признак десткого случая (на момент оказания услуги нету 18 лет)
IF(TIMESTAMPDIFF(YEAR, Client.birthDate, Action.endDate) < 18, 1, 0)  AS 'DET',
-- Номер истории болезни
IF(APS_NHISTORY.id IS NULL, cast(Client.id as char), APS_NHISTORY.value)  AS 'NHISTORY', 
DATE(Action.endDate) AS 'DATE_1', 
DATE(Action.endDate) AS 'DATE_2',  
IF(AP_DS0.value IS NOT NULL, SUBSTRING_INDEX(AP_DS0.value,'-',1), IF(rbDiseasePhases.code IS NOT NULL, rbDiseasePhases.code, '0'))  AS 'DS0', 
IF(AP_DS1.diagId IS NOT NULL, AP_DS1.diagId, Diagnosis.MKB)  AS 'DS1', 
IF(AP_DS2.diagId IS NOT NULL, AP_DS2.diagId,IF(Diagnosis2.MKB IS NOT NULL, Diagnosis2.MKB, '') )   AS 'DS2',
IF(rbService.code like  'А%' AND rbService.infis <> '', rbService.code, '') AS 'CODE_MES1',
IF((rbMedicalKind.code = 'H' OR rbMedicalKind.code = 'C' OR rbMedicalKind.code = 'V' OR rbMedicalKind.code = 'Z') AND rbHealthGroup.code IS NOT NULL, rbHealthGroup.code, '') AS 'CODE_MES2', 
IF(AP_RSLT.value IS NOT NULL, SUBSTRING_INDEX(AP_RSLT.value,'-',1),rbResult.code)  AS 'RSLT', 
IF(AP_ISHOD.value IS NOT NULL, SUBSTRING_INDEX(AP_ISHOD.value,'-',1),rbAcheResult.code)  AS 'ISHOD',
rbSpeciality.code AS 'PRVS', 
IF(Person.SNILS <> '', insert(insert(insert(Person.SNILS, 4, 0, '-'), 8, 0,  '-'), 12,0, ' ' ), '') AS 'IDDOKT',
IF(TIMESTAMPDIFF(MONTH, Client.birthDate, DATE(Action.endDate)) < 2 and ClientPolicy.id IS NULL, IF(ClientContact.id IS NOT NULL,   '1', IF((Spokesman.id IS NULL AND Client.patrName = '') OR (Spokesman.id IS NOT NULL AND Client.patrName = '' AND Spokesman.patrName = ''),  '2', '0')), '0')  AS 'OS_SLUCH', 
rbPayType.code  AS 'IDSP',
IF(rbMedicalAidUnit.code = '5', CT.uet,  1) AS 'ED_COL', 
CONCAT(
	rbMedicalAidUnit.code,
	rbMedicalKind.code,
	IF(LOCATE(rbMedicalKind.code, 'HCVZ') AND rbMedicalAidUnit.code = '2' AND MKU.stageCode <> '2',  
		CONCAT(rbDispInfo.code, SUBSTRING(rbService.infis, 3, 5)),  
		CONCAT('0', 
			IF(LOCATE(rbMedicalKind.code ,'PHCVZ') AND (rbMedicalAidUnit.code = '3' OR MKU.stageCode = '2') AND SUBSTRING(rbService.infis, 1, 2) <> '06', 
				INSERT(rbService.infis, 1, 2, '04'),
				rbService.infis
			)
		)
	),
	IF(TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.endDate)) >= 18, 1, 2), 
	rbServiceFinance.code
)  AS 'CODE_USL', 
IF(rbServiceFinance.code = '2', 0, IF(CT.uet > 0, CT.price / CT.uet, CT.price) )	AS 'TARIF',
CT.id as 'tariffId',
rbMedicalAidUnit.id as 'rbMedicalAidUnitId',
rbMedicalAidUnit.code as 'rbMedicalAidUnitCode',
rbMedicalKind.code as  'rbMedicalKindCode',
Action.amount as 'ActionAmount',
rbService.id as 'rbServiceId',
rbService.infis as 'rbServiceInfis', 
rbResult.regionalCode as 'rbResultRegionalCode' ,
-- Вид ВМП
'' AS 'VID_HMP',
-- Метод ВПМ
'' AS 'METOD_HMP'
-- END OF FIELDS ---------------------------------------------------- 
FROM 
--  Дейтсвие
Action 
-- Обращение
INNER JOIN Event on Event.id = Action.event_id 
-- Тип дествия
INNER JOIN ActionType ON ActionType.id = Action.actionType_id AND ActionType.service_id IS NOT NULL
-- Пациент
INNER JOIN Client ON Client.id = Event.client_id 
-- Полис пациента
LEFT JOIN ClientPolicy ON ClientPolicy.id =  (
	SELECT MAX(c.id) 
	FROM ClientPolicy c 
	WHERE  c.client_id = Client.id  
	AND c.deleted <> 1
	AND c.policyType_id <> 3
	AND 
	(
		 c.begDate IS NOT NULL  
		 AND 
		 c.begDate <> '0000-00-00' 
		 AND 
		 c.begDate <= Action.endDate
		 AND 
		 (c.endDate IS NULL OR c.endDate = '0000-00-00' OR c.endDate >= DATE(Action.endDate)) 
		 OR		 
		 (c.begDate IS NULL OR c.begDate = '0000-00-00') 
		 AND 
		 c.endDate IS NOT NULL 
		 AND 
		 c.endDate <> '0000-00-00' 
		 AND 
		 c.endDate >= DATE(Action.endDate)
		 OR 
		 (
		 	(c.begDate IS NULL OR c.begDate = '0000-00-00') 
			 AND 
			 (c.endDate IS NULL OR c.endDate = '0000-00-00')  
			 AND NOT EXISTS(
					SELECT * 
					FROM ClientPolicy d 
					WHERE d.client_id = Client.id
					AND d.policyType_id <> 3 
					AND d.id <> c.id 
					AND d.deleted <> 1 
					AND 
					( 
						(
							d.begDate IS NOT NULL AND d.begDate <> '0000-00-00'  AND d.begDate <= Action.endDate 
							AND 
							(d.endDate IS NULL OR d.endDate = '0000-00-00' OR d.endDate >= DATE(Action.endDate))  
						) 
						OR 
						(
							(d.begDate IS NULL OR d.begDate = '0000-00-00') 
							AND 
							d.endDate IS NOT NULL 
							AND 
							d.endDate <> '0000-00-00' 
							AND 
							d.endDate >= DATE(Action.endDate)  
				  		) 
					)
					LIMIT 1				  
			) /*not exists*/ 
		) /*OR*/ 
	) /*AND*/
)
-- Тип полиса пацеинта
LEFT JOIN rbPolicyType ON rbPolicyType.id = ClientPolicy.policyType_id  
-- Контакт пациента(для определения номера новорожденного)  
LEFT JOIN ClientContact	ON (ClientContact.client_id = Client.id  AND ClientContact.deleted = 0  AND ClientContact.ContactType_id = ::@multipleBirthContactTypeId  ) 
-- Документ пациента
LEFT JOIN ClientDocument ON ClientDocument.id  =  (
		SELECT MAX(b.id)  
		FROM  ClientDocument b
		INNER JOIN rbDocumentType bType ON bType.id = b.documentType_id
		WHERE  b.client_id = Client.id 
		AND    b.deleted <> 1  
		AND    bType.group_id = 1  
		AND   (
			(b.date IS NOT NULL AND b.date <> '0000-00-00' AND b.date <= DATE(Action.endDate))
			OR 
			(
				(b.date IS NULL OR b.date = '0000-00-00')
				AND
				NOT EXISTS (
					SELECT c.id 
					FROM ClientDocument c
					INNER JOIN rbDocumentType cType ON cType.id = c.documentType_id
					WHERE c.client_id = Client.id
					AND   c.id <> b.id
					AND   c.deleted <> 1
					AND   cType.group_id = 1
					AND (c.date IS NOT NULL AND c.date <> '0000-00-00' AND c.date <= DATE(Action.endDate))
					LIMIT 1
				)
			)
		)
)
-- Тип документа пациента
LEFT JOIN rbDocumentType ClientDocumentType ON ClientDocumentType.id = ClientDocument.documentType_id 
-- Отношения пациента (для определения представителя) 
LEFT JOIN ClientRelation ON (
	ClientRelation.relative_id = Client.id  
	AND 
	ClientRelation.deleted = 0  
	AND 
	(ClientPolicy.id IS NULL AND TIMESTAMPDIFF(MONTH, Client.birthDate, DATE(Action.endDate)) < 2)
)
-- Представитель пациента
LEFT JOIN Client Spokesman	ON Spokesman.id = ClientRelation.client_id 
-- Документы представителя
LEFT JOIN ClientDocument  SpokesmanDocument  ON SpokesmanDocument.id  =  (
		SELECT MAX(b.id)  
		FROM  ClientDocument b
		INNER JOIN rbDocumentType bType ON bType.id = b.documentType_id
		WHERE  b.client_id = Spokesman.id 
		AND    b.deleted <> 1  
		AND    bType.group_id = 1  
		AND   (
			(b.date IS NOT NULL AND b.date <> '0000-00-00' AND b.date <= DATE(Action.endDate))
			OR 
			(
				(b.date IS NULL OR b.date = '0000-00-00')
				AND
				NOT EXISTS (
					SELECT c.id 
					FROM ClientDocument c
					INNER JOIN rbDocumentType cType ON cType.id = c.documentType_id
					WHERE c.client_id = Spokesman.id
					AND   c.id <> b.id
					AND   c.deleted <> 1
					AND   cType.group_id = 1
					AND (c.date IS NOT NULL AND c.date <> '0000-00-00' AND c.date <= DATE(Action.endDate))
					LIMIT 1
				)
			)
		)
)
-- Тип документа представителя 
LEFT JOIN rbDocumentType SpokesmanDocumentType  ON SpokesmanDocumentType.id = SpokesmanDocument.documentType_id  
-- Полис представителя
LEFT JOIN ClientPolicy SpokesmanPolicy  ON SpokesmanPolicy.id = (
	SELECT MAX(c.id) 
	FROM ClientPolicy c 
	WHERE  c.client_id = Spokesman.id  
	AND c.deleted <> 1
	AND c.policyType_id <> 3
	AND 
	(
		 c.begDate IS NOT NULL  
		 AND 
		 c.begDate <> '0000-00-00' 
		 AND 
		 c.begDate <= Action.endDate 
		 AND 
		 (c.endDate IS NULL OR c.endDate = '0000-00-00' OR c.endDate >= DATE(Action.endDate)) 
		 OR		 
		 (c.begDate IS NULL OR c.begDate = '0000-00-00') 
		 AND 
		 c.endDate IS NOT NULL 
		 AND 
		 c.endDate <> '0000-00-00' 
		 AND 
		 c.endDate >= DATE(Action.endDate)
		 OR 
		 (
			(c.begDate IS NULL OR c.begDate = '0000-00-00') 
			 AND 
			 (c.endDate IS NULL OR c.endDate = '0000-00-00')  
			 AND NOT EXISTS(
					SELECT * 
					FROM ClientPolicy d 
					WHERE d.client_id = Spokesman.id
					AND d.policyType_id <> 3 
					AND d.id <> c.id 
					AND d.deleted <> 1 
					AND 
					( 
						(
							d.begDate IS NOT NULL AND d.begDate <> '0000-00-00'  AND d.begDate <= Action.endDate 
							AND 
							(d.endDate IS NULL OR d.endDate = '0000-00-00' OR d.endDate >= DATE(Action.endDate))  
						) 
						OR 
						(
							(d.begDate IS NULL OR d.begDate = '0000-00-00') 
							AND 
							d.endDate IS NOT NULL 
							AND 
							d.endDate <> '0000-00-00' 
							AND 
							d.endDate >= DATE(Action.endDate)  
						) 
					)
					LIMIT 1
			) /*not exists*/ 
		) /*OR*/ 
	) /*AND*/
)
-- Тип полиса представителя 
LEFT JOIN rbPolicyType SpokesmanPolicyType ON SpokesmanPolicyType.id = SpokesmanPolicy.policyType_id  
-- Страховщик пациента
LEFT JOIN Organisation Insurer ON Insurer.id = COALESCE(SpokesmanPolicy.insurer_id, ClientPolicy.insurer_id)
-- Тип обращения
INNER JOIN EventType ON EventType.id = Event.eventType_id
-- Назначение типа обращения  
LEFT JOIN rbEventTypePurpose ON rbEventTypePurpose.id = EventType.purpose_id 
-- тип мед помощи
LEFT JOIN rbMedicalAidType ON rbMedicalAidType.id = EventType.medicalAidType_id 
-- Основная диагностика из обращения 
LEFT JOIN Diagnostic ON (
	Diagnostic.event_id = Event.id 
	AND   
	(Diagnostic.diagnosisType_id = 2 OR Diagnostic.diagnosisType_id = 1)  
	AND   
	Diagnostic.deleted  = 0
)  
-- Группа здоровья
LEFT JOIN rbHealthGroup ON rbHealthGroup.id = Diagnostic.healthGroup_id  
-- Основной диагноз из основной диагностики
LEFT JOIN Diagnosis	ON (Diagnosis.id = Diagnostic.diagnosis_id AND Diagnosis.deleted = 0)  
-- Сопуствующая диагностика
LEFT JOIN Diagnostic Diagnostic2 ON Diagnostic2.id = (
	SELECT MIN(Diagnostic3.id)
	FROM Diagnostic Diagnostic3
	WHERE Diagnostic3.event_id = Event.id  
	AND Diagnostic3.deleted = 0  
	AND (Diagnostic3.diagnosisType_id = 3  OR Diagnostic3.diagnosisType_id = 5)
)
-- Сопутствующий диагноз из сопутствующей диагностики  
LEFT JOIN Diagnosis Diagnosis2	ON (Diagnosis2.id = Diagnostic2.diagnosis_id AND Diagnosis2.deleted = 0)
-- Результат обращения
LEFT JOIN rbResult ON rbResult.id = COALESCE(Diagnostic.result_id, Event.result_id)  
-- Исход из обращения   
LEFT JOIN rbAcheResult ON rbAcheResult.id = COALESCE(Diagnostic.rbAcheResult_id,Event.rbAcheResult_id)
-- Стадия заболевания из основной диагностики     
LEFT JOIN rbDiseasePhases ON rbDiseasePhases.id = Diagnostic.phase_id 
-- Оказанная услуга
INNER JOIN rbService ON rbService.id = ActionType.service_id 
-- профиль помощи
LEFT JOIN rbMedicalAidProfile ON rbMedicalAidProfile.id = rbService.medicalAidProfile_id  
-- категория помощи
INNER JOIN rbMedicalKind  ON rbMedicalKind.id = IF(EventType.rbMedicalKind_id IS NULL OR rbService.infis = '0607801', rbService.rbMedicalKind_id, EventType.rbMedicalKind_id) 
--  Таблица-связка 
INNER JOIN MedicalKindUnit MKU ON (
	MKU.rbMedicalKind_id = rbMedicalKind.id  
	AND (
		MKU.eventType_id = EventType.id   
		OR (
			MKU.eventType_id IS NULL 
			AND NOT EXISTS(
				SELECT bMKU.id 
				FROM MedicalKindUnit bMKU 
				WHERE bMKU.eventType_id = EventType.id 
				AND bMKU.rbMedicalKind_id = rbMedicalKind.id
			)
		)
	) 
	AND 
	LOCATE(rbMedicalKind.code, 'PTIFGRHCVZ')   
)  
-- единица измерения помощи
INNER JOIN rbMedicalAidUnit ON rbMedicalAidUnit.id =  
	IF(rbMedicalKind.code = 'P' 
		AND MKU.rbMedicalAidUnit_id = 2 
		AND rbResult.code <> '304'  
		AND (search2P_Extended(Client.id, Action.endDate, ::@contractId, rbService.infis, Event.eventType_id, ::@orgStructureIdList) <> '2P304'),
					1,
					MKU.rbMedicalAidUnit_id
) 
-- категория оплаты 
LEFT JOIN rbPayType  ON rbPayType.id = MKU.rbPayType_id 
-- врач, выполнивший услугу 
LEFT JOIN Person ON Person.id = Action.person_id  
-- подразделение в котором работает врач, выполнивший услугу
LEFT JOIN OrgStructure ON OrgStructure.id = Person.orgStructure_id  
-- Специальность врача
LEFT JOIN rbSpeciality ON rbSpeciality.id = Person.speciality_id 
-- Свойство 'Номер исследования для ТФОМС'
LEFT JOIN ActionProperty AP_NHISTORY ON (AP_NHISTORY.action_id = Action.id   
	AND EXISTS(
		SELECT ActionPropertyType.id 
		FROM ActionPropertyType  
		WHERE ActionPropertyType.id = AP_NHISTORY.type_id  
		AND ActionPropertyType.name =  'Номер исследования для ТФОМС'
		LIMIT 1
	)
)
-- Значение свойства 'Номер исследования для ТФОМС' 
LEFT JOIN ActionProperty_String APS_NHISTORY ON APS_NHISTORY.id = AP_NHISTORY.id  
-- Значение основного диагноза из свойств Action
LEFT JOIN MKB AP_DS1 ON AP_DS1.id = (
	SELECT AP_MKB.value
	FROM ActionProperty AP
	INNER JOIN ActionProperty_MKB AP_MKB ON AP.id = AP_MKB.id
	INNER JOIN ActionPropertyType APT ON AP.type_id = APT.id
	WHERE AP.action_id = Action.id
	AND APT.code = 'MainDiagnosis'
	AND AP_MKB.index = 0
	AND AP.deleted = 0
	LIMIT 1
)
-- Значение сопутствующего диагноза из свойств дивжения
LEFT JOIN MKB AP_DS2 ON AP_DS2.id = (
	SELECT AP_MKB.value
	FROM ActionProperty AP
	INNER JOIN ActionProperty_MKB AP_MKB ON AP.id = AP_MKB.id
	INNER JOIN ActionPropertyType APT ON AP.type_id = APT.id
	WHERE AP.action_id = Action.id
	AND APT.code = 'ConcomitantDiagnosis'
	AND AP_MKB.index = 0
	AND AP.deleted = 0
	LIMIT 1
)  
-- Значение исхода из свойств движения
LEFT JOIN ActionProperty_String AP_ISHOD ON AP_ISHOD.id = (
	SELECT AP.id
	FROM ActionProperty AP
	INNER JOIN ActionPropertyType APT ON AP.type_id = APT.id
	WHERE AP.action_id = Action.id
	AND APT.code = 'AcheResult'
	AND AP.deleted = 0
	LIMIT 1
) AND AP_ISHOD.index = 0
-- Значение результата из свойств движения
LEFT JOIN ActionProperty_String AP_RSLT ON AP_RSLT.id = (
	SELECT AP.id
	FROM ActionProperty AP
	INNER JOIN ActionPropertyType APT ON AP.type_id = APT.id
	WHERE AP.action_id = Action.id
	AND APT.code = 'Result'
	AND AP.deleted = 0
	LIMIT 1
) AND AP_RSLT.index = 0
-- Значение Стадии заболевания из свойств движения
LEFT JOIN ActionProperty_String AP_DS0 ON AP_DS0.id = (
	SELECT AP.id
	FROM ActionProperty AP
	INNER JOIN ActionPropertyType APT ON AP.type_id = APT.id
	WHERE AP.action_id = Action.id
	AND APT.code = 'OnkoStage'
	AND AP.deleted = 0
	LIMIT 1
) AND AP_DS0.index = 0
-- Тарифы
LEFT JOIN Contract_Tariff CT ON (
												-- Тариф не был удален
												CT.deleted = 0
												-- Совпадает пол или пол не определен
												AND
												(CT.sex = 0 OR CT.sex = Client.sex)
												-- Совпадает контракт
												AND
												CT.master_id = ::@contractId
												AND
												-- Совпадает услуга
												CT.service_id = rbService.id
												AND 
												-- Совпадает тип обращения
 												(
													(
														CT.eventType_id = EventType.id 
														AND 
														LOCATE(rbMedicalKind.code, 'HCVZ')
													)
													OR 
													(
														CT.eventType_id IS NULL 
														AND 
														NOT LOCATE(rbMedicalKind.code, 'HCVZ')
													)
												)
												AND
												-- Тариф действовал до оказания услуги
												CT.begDate  <= DATE(Action.endDate)
												AND
												-- Тариф не был прекращен на момент оказания услуги
												(CT.endDate IS NULL OR CT.endDate >= DATE(Action.endDate) OR CT.endDate = '0000-00-00')
												AND 
												-- единица учета совпадает с найденной
												CT.unit_id = rbMedicalAidUnit.id
												AND
												-- возраст пациента подходит
												checkAge(
													CT.age, 
													Client.birthDate, 
													IF( LOCATE(rbMedicalKind.code, 'HVZ') 
														AND 
														rbMedicalAidUnit.code = '2'  
														AND 
														NOT (rbMedicalKind.code = 'H' AND TIMESTAMPDIFF(YEAR, Client.birthDate, Action.endDate) < 3 ) 
														AND 
														TIMESTAMPDIFF(YEAR, Client.birthDate, Action.endDate) <> 17, 
															CONCAT(YEAR(Action.endDate), '-12-31'),
															Action.endDate
													)
												)
												-- Нужен ли тариф вообще
												AND NOT 
												(
													(
														SUBSTRING(Insurer.area, 1, 2) = ::@SMOArea 
														OR 
														Insurer.area IS NULL
													) 
													AND 
													(
														rbMedicalKind.code = 'F' 
														OR  
														rbMedicalKind.code = 'R' 
														OR 
														(
															rbMedicalKind.code = 'P' 
															AND 
															(rbMedicalAidUnit.code = '2' OR rbMedicalAidUnit.code = '1') 
															AND 
															SUBSTRING(rbService.infis, 3, 3) IN('026','076','081')
														) 
													)
												)
)
-- Группа диспансеризации
LEFT JOIN rbDispInfo ON LOCATE(rbMedicalKind.code, 'HCVZ') AND rbDispInfo.sex = CT.sex AND rbDispInfo.age = CT.age AND rbDispInfo.rbMedicalKind_id = rbMedicalKind.id
-- Источник финансирования   
INNER JOIN rbServiceFinance	ON (  
	(
		NOT (
			(SUBSTRING(Insurer.area, 1, 2) = ::@SMOArea OR Insurer.area IS NULL) 
			AND (
				rbMedicalKind.code = 'F' 
				OR 
				rbMedicalKind.code = 'R' 
				OR 
				(
					rbMedicalKind.code = 'P' 
					AND 
					(rbMedicalAidUnit.code = '2' OR rbMedicalAidUnit.code = '1') 
					AND 
					SUBSTRING(rbService.infis, 3, 3) IN('026','076','081')
				) 
			)
		) 
		AND 
		rbServiceFinance.id = CT.rbServiceFinance_id
	)  
	OR  
	(
		(
			(SUBSTRING(Insurer.area, 1, 2) = ::@SMOArea OR Insurer.area IS NULL) 
			AND (
				rbMedicalKind.code = 'F' 
				OR 
				rbMedicalKind.code = 'R' 
				OR 
				(
					rbMedicalKind.code = 'P' 
					AND 
					(rbMedicalAidUnit.code = '2' or rbMedicalAidUnit.code = '1') 
					AND 
					SUBSTRING(rbService.infis, 3, 3) IN('026','076','081')
				) 
			)
		) 
		AND 
		rbServiceFinance.code = '2'
	) 
) 
-- WHERE PHRASE ------------------------------------------------------
WHERE 
-- Обращение не удалено
Event.deleted = 0
-- Контракт совпадает с указанным
AND 
Event.contract_id = ::@contractId 
-- Действие не удалено
AND 
Action.deleted = 0  
-- этот случай подходит под первичную(повторную) выгрузку
AND 
NOT EXISTS(SELECT * FROM Account_Item ac_i  WHERE ac_i.action_id =  Action.id AND ac_i.deleted=0) 
-- WMIS-22
AND 
NOT(rbResult.code = '304' AND rbMedicalKind.code = 'P' AND rbMedicalAidUnit.code = '2')  
-- Действие попадает в указанный диапозон выгрузки
AND  
Action.endDate BETWEEN TIMESTAMP(::@beginInterval) AND TIMESTAMP(::@endInterval)  
AND 
NOT(rbMedicalKind.code = 'I' AND rbEventTypePurpose.codePlace <> '3')  
-- Услуга оказана в заданном списке подразделений или по всем подразделениям
AND
( ::@orgStructureIdList = '' OR FIND_IN_SET(OrgStructure.id, ::@orgStructureIdList) )  
AND 
-- WMIS-40
NOT (
	rbPayType.code IN('94','95','96','98','11') 
	AND (
			(
				NOT SUBSTRING(rbService.infis, 3, 3) IN('026','076','081','031') 
				AND rbMedicalKind.code <> 'P'
			) 
			OR (
				rbResult.regionalCode <> '2' AND rbMedicalKind.code = 'P'
			) 
	)  
)  
-- Сортировка -------------------------------------------------------
ORDER BY Client.id, Event.id, Action.id, rbServiceFinance.id; 
''',
	'SpecialVar_TFOMS_FlatStationar': '''
SELECT 
-- ID обращения
Event.id as 'EventId',
-- ID типа обращения
EventType.id as 'EventTypeId',
-- ID действия
Action.id as 'ActionId',
-- ID источника финансирования
rbServiceFinance.id as 'rbServiceFinanceId',
-- Данные пациента --------------------------------------------------
-- ID пациента
Client.id as 'ClientId',
-- Фамилия пациента
IF(Client.lastName = '', 'НЕТ',	UCASE(Client.lastName))	AS 'FAM',
-- Имя пациента
UCASE(Client.firstName)	AS 'IM',
-- Отчество пациента
IF(Client.patrName = '', 'НЕТ', UCASE(Client.patrName))	AS 'OT',
-- Пол пациента
Client.sex	AS 'W',
-- Дата рождения пациента 
Client.birthDate AS 'DR',
-- Место рождения пациента
Client.birthPlace AS 'MR',
-- СНИЛС пациента
IF(Client.SNILS <> '',  INSERT(INSERT(INSERT(Client.SNILS, 4, 0, '-'), 8, 0,  '-'), 12,0, ' ' ), '') AS 'SNILS', 
-- Вес пациента
IF(rbCSG.id IS NOT NULL AND rbCSG.TFOMSCode IN('067','068') AND TIMESTAMPDIFF(YEAR, Client.birthDate, Action.begDate) < 18, CAST(Client.weight AS CHAR), '') AS 'VNOV_D',
-- Прдеставитель пациента -------------------------------------------
-- ID представителя
Spokesman.id as 'spokesmanId',
-- Фамилия представителя 
IF(Spokesman.id IS NOT NULL, IF(Spokesman.lastName = '', 'НЕТ', UCASE(Spokesman.lastName)), '')  AS 'FAM_P',
-- Имя представителя
IF(Spokesman.id IS NOT NULL, UCASE(Spokesman.firstName), '') AS 'IM_P',
-- Отчество представителя
IF(Spokesman.id IS NOT NULL, IF(Spokesman.patrName = '', 'НЕТ', UCASE(Spokesman.patrName)), '') AS 'OT_P',
-- Пол представителя
IF(Spokesman.id IS NOT NULL, Spokesman.sex, '') AS 'W_P',
-- Дата рождения представителя
IF(Spokesman.id IS NOT NULL, Spokesman.birthDate, '')	AS 'DR_P',
-- Документы --------------------------------------------------------
-- ID документа
IF(ClientDocument.id IS NULL, SpokesmanDocument.id, ClientDocument.id) AS 'DocumentId',
-- Код типа документа
IF(SpokesmanDocument.id IS NULL,
	IF(ClientDocumentType.code IS NOT NULL, 
		TRIM(LEADING '0' FROM  ClientDocumentType.code),
		''
	),
	TRIM(LEADING '0'  FROM SpokesmanDocumentType.code)
)  AS 'DOCTYPE', 
-- Серия документа
 IF(SpokesmanDocumentType.code IS NULL,
	IF(ClientDocumentType.code IS NOT NULL, 
		IF(TRIM(LEADING '0' FROM  ClientDocumentType.code) = '3', 
			REPLACE(ClientDocument.serial, ' ', '-'), 
			ClientDocument.serial
		),
		''
	),
	IF(TRIM(LEADING '0'  FROM SpokesmanDocumentType.code) = '3',
		REPLACE(SpokesmanDocument.serial, ' ', '-'), 
		SpokesmanDocument.serial
	)
) AS 'DOCSER',
-- Номер документа
 IF(SpokesmanDocumentType.code IS NULL, 
	IF(ClientDocumentType.code IS NOT NULL, ClientDocument.number, ''),
	SpokesmanDocument.number
) AS 'DOCNUM',
-- Полисы -----------------------------------------------------------
-- ID полиса
IF(ClientPolicy.id IS NULL, SpokesmanPolicy.id, ClientPolicy.id) AS 'PolicyId',
-- Тип полиса
IF(ClientPolicy.id IS NULL, 
	IF(SpokesmanPolicy.id IS NULL, '', SpokesmanPolicyType.TFOMSCode),
	rbPolicyType.TFOMSCode
) AS 'VPOLIS',
-- Серия полиса
 IF(ClientPolicy.id IS NULL, 
	IF(SpokesmanPolicy.id IS NULL, '', SpokesmanPolicy.serial),
	ClientPolicy.serial
) AS 'SPOLIS',
-- Номер полиса
IF(ClientPolicy.id IS NULL, 
	IF(SpokesmanPolicy.id IS NULL, '', SpokesmanPolicy.number),
	ClientPolicy.number
) AS 'NPOLIS', 
-- Инфис-код страховой
COALESCE(Insurer.infisCode, '') AS 'SMO',
COALESCE(Insurer.fullName, '') AS 'SMO_NAM',
COALESCE(Insurer.OGRN, '') AS 'SMO_OGRN',
COALESCE(Insurer.OKATO, '') AS 'SMO_OK',
-- Свойства оказанной услуги ----------------------------------------
-- Признак новорожденного (нету своего полиса и возраст на момент оказания услуги менее 2-х месяцев)
IF( ClientPolicy.id IS NULL 
	AND
	TIMESTAMPDIFF(MONTH, Client.birthDate,  DATE(Action.begDate)) < 2,
	CONCAT(
		CAST(Client.sex AS CHAR),
		CAST(DATE_FORMAT(Client.birthDate, '%d%m%y') AS CHAR),
		IF(ClientContact.id IS NOT NULL, ClientContact.contact, '1')
	),
    '0'
) AS 'NOVOR',  
-- Условия оказания мед помощи
rbEventTypePurpose.codePlace AS 'USL_OK',
-- Вид помощи
rbMedicalAidType.code AS 'VIDPOM',
-- TODO не помню что значит тег
IF(Event.order = 2, 2, 1) AS 'FOR_POM',
-- Признак экстренного случая
IF(Event.order = 2, 2, 1) AS 'EXTR',
-- TODO
IF(OrgStructure.infisInternalCode IS NOT NULL AND OrgStructure.infisInternalCode <> '', OrgStructure.infisInternalCode, ::@obsoleteInfisCode) AS 'LPU_1', 
-- Подразделение МО в котором оказывается помощь
rbService.departCode AS 'PODR',
-- Профиль помощи
rbMedicalAidProfile.code AS 'PROFIL',
-- Признак десткого случая (на момент оказания услуги нету 18 лет)
IF(TIMESTAMPDIFF(YEAR, Client.birthDate,  DATE(Action.begDate)) < 18, 1, 0)  AS 'DET',
-- Номер истории болезни
IF(Event.externalId IS NULL OR Event.externalId = '', 
		prop_history_value.value,
		Event.externalId
)  AS 'NHISTORY',
-- Дата начала оказания услуги
DATE(Action.endDate) AS 'DATE_1',
-- Дата окончания оказания услуги
DATE(Action.endDate) AS 'DATE_2', 
-- Стадия заболевания 
IF(AP_S_STAGE.value IS NOT NULL,
	SUBSTRING_INDEX(AP_S_STAGE.value,'-',1),
	IF(rbDiseasePhases.id IS NOT NULL, rbDiseasePhases.code , '0')
)  AS 'DS0',
-- Основной диагноз DS1
IF(anotherMovingAction.id IS NULL, 
	IF(MKB.diagID IS NOT NULL, MKB.diagID, Diagnosis.MKB), 
	IF(MKB.diagID IS NOT NULL, MKB.diagID, '')
) AS 'DS1', 
-- Сопутствующий диагноз
IF(anotherMovingAction.id IS NULL,
	IF(MKB2.diagID IS NOT NULL, MKB2.diagID, IF(Diagnosis2.id IS NOT NULL, Diagnosis2.MKB, '')),
	IF(MKB2.diagID IS NOT NULL, MKB2.diagID, '')
)    AS 'DS2',
-- CODE_MES1
IF(rbService.code LIKE 'А%' AND rbService.infis <> '', 
	rbService.code,
	IF(rbOperationType.id IS NOT NULL 
		AND 
		NOT(rbCSG.id IS NOT NULL 
			AND 
			rbCSG.rbOperationType_TFOMSCode IS NULL
		),
		SUBSTRING_INDEX(rbOperationType.name, ' ', 1),
		''
	)
)  AS 'CODE_MES1',
-- CODE_MES2
'' AS 'CODE_MES2',
-- Результат обращения
IF(AP_S_RLST.value IS NOT NULL, SUBSTRING_INDEX(AP_S_RLST.value, '-', 1), rbResult.code)  AS 'RSLT',
-- Исход обращения
IF(AP_S_ISHOD.value IS NOT NULL, SUBSTRING_INDEX(AP_S_ISHOD.value,'-', 1), rbAcheResult.code)  AS 'ISHOD',
-- Код специальности лечащего врача
rbSpeciality.code AS 'PRVS',
-- Снилс лечашего врача
IF(Person.SNILS <> '', INSERT(INSERT(INSERT(Person.SNILS, 4, 0, '-'), 8, 0,  '-'), 12,0, ' ' ), '') AS 'IDDOKT', 
-- Признаки особых случаев
IF( TIMESTAMPDIFF(MONTH, Client.birthDate, DATE(Action.begDate)) < 2 
	AND
	ClientPolicy.id IS NULL,
	IF(ClientContact.id IS NOT NULL, 
		'1',
		IF((Spokesman.id IS NULL AND Client.patrName = '') OR (Spokesman.id IS NOT NULL AND Client.patrName = '' AND Spokesman.patrName = ''),  
			'2', 
			'0'
		)
	),
	'0'
)  AS 'OS_SLUCH',
-- Категория оплаты
IF(rbCSG.id IS NOT NULL, 
	'16',
	IF(operationAction.id IS NOT NULL OR rbHospitalBedProfile.code = 'ХИР_1Д', '2', rbPayType.code)
)  AS 'IDSP', 
-- Количество единиц оказанной мед помощи
IF(rbMedicalAidUnit.code = '5', 
	CT.uet * Action.amount,
	IF(rbMedicalAidUnit.code = '1',
		IF(rbMedicalKind.code = 'S', 
			IF(DATE(Action.begDate) = DATE(Action.endDate), 1, TIMESTAMPDIFF(DAY, DATE(Action.begDate), DATE(Action.endDate))),
			IF(DATE(Action.begDate) = DATE(Action.endDate), 1, TIMESTAMPDIFF(DAY, DATE(Action.begDate), DATE(Action.endDate)) + 1 - num_sunday_days(DATE(Action.begDate), DATE(Action.endDate)))
		),
		1
	)
) AS 'ED_COL',
-- Код оказнной услуги для ТФОМС
CONCAT(
	rbMedicalAidUnit.code,
	rbMedicalKind.code,
	IF(rbMedicalKind.code = 'S' AND rbCSG.id IS NOT NULL, '02', '00'),
	IF(rbTreatment.id IS NULL,
		IF(rbCSG.id IS NULL, '000', rbCSG.TFOMSCode),
		rbTreatment.code
	),
	SUBSTRING(rbService.infis, 5, 3),
	IF(TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.begDate) ) >= 18, 1, 2),
	rbServiceFinance.code
)  AS 'CODE_USL',
-- Тариф
IF(anotherMovingAction.id IS NOT NULL
	AND 
	MKB.diagID IS NULL,
	0,
	IF(rbServiceFinance.code = '2',
		0,
		IF(CT.uet > 0, CT.price / CT.uet, CT.price)
	)
)	AS 'TARIF',
-- Ид тарифа
CT.id AS 'tariffId',
-- Единица измерения мед помощи
rbMedicalAidUnit.id as 'rbMedicalAidUnitId',
-- Код единицы измерения
rbMedicalAidUnit.code as 'rbMedicalAidUnitCode',
-- Код категории помощи
rbMedicalKind.code as  'rbMedicalKindCode',
-- Количество в действии
Action.amount as 'ActionAmount',
-- ID услуги
rbService.id as 'rbServiceId',
-- ИНФИС-код услуги
rbService.infis as 'rbServiceInfis',
-- Региональный код результата
rbResult.regionalCode as 'rbResultRegionalCode',
-- Вид ВМП
QuotaType.code AS 'VID_HMP',
-- Метод ВПМ
rbTreatment.code AS 'METOD_HMP'
-- END OF FIELDS ----------------------------------------------------
FROM 
-- Обращение  
Event  
-- Действие
INNER JOIN Action ON Action.event_id = Event.id 
-- Поступление пациента
LEFT JOIN Action act_received ON 
	act_received.event_id = Action.event_id  
	AND 
	act_received.deleted  = 0  
	AND 
	act_received.actionType_id 
	IN (SELECT ActionType.id FROM ActionType WHERE ActionType.flatCode = 'received')
-- Номер истории болезни из поступления	
LEFT JOIN ActionProperty_String prop_history_value ON prop_history_value.id =  (
	SELECT prop_history.id
	FROM ActionProperty prop_history 
	WHERE 
	prop_history.action_id = act_received.id 
	AND  
	EXISTS(SELECT * FROM ActionPropertyType  WHERE ActionPropertyType.id = prop_history.type_id  AND     ActionPropertyType.name  IN  ('Номер ИБ','Номер ИР')) AND 
	prop_history.deleted = 0 
	LIMIT 1
)  AND prop_history_value.index = 0  
-- Пациент
INNER JOIN Client ON Client.id = Event.client_id  
-- Полис пациента
LEFT JOIN ClientPolicy ON ClientPolicy.id =  (
	SELECT MAX(c.id) 
	FROM ClientPolicy c 
	WHERE  c.client_id = Client.id  
	AND c.deleted <> 1
	AND c.policyType_id <> 3
	AND 
	(
		 c.begDate IS NOT NULL  
		 AND 
		 c.begDate <> '0000-00-00' 
		 AND 
		 c.begDate <= Event.execDate 
		 AND 
		 (c.endDate IS NULL OR c.endDate = '0000-00-00' OR c.endDate >= DATE(Event.execDate)) 
		 OR		 
		 (c.begDate IS NULL OR c.begDate = '0000-00-00') 
		 AND 
		 c.endDate IS NOT NULL 
		 AND 
		 c.endDate <> '0000-00-00' 
		 AND 
		 c.endDate >= DATE(Event.execDate)
		 OR 
		 (
		 	(c.begDate IS NULL OR c.begDate = '0000-00-00') 
			 AND 
			 (c.endDate IS NULL OR c.endDate = '0000-00-00')  
			 AND NOT EXISTS(
					SELECT * 
				 	FROM ClientPolicy d 
				 	WHERE d.client_id = Client.id
				 	AND d.policyType_id <> 3 
				  	AND d.id <> c.id 
				  	AND d.deleted <> 1 
				  	AND 
					( 
				  		(
					  		d.begDate IS NOT NULL AND d.begDate <> '0000-00-00'  AND d.begDate <= Event.execDate 
					  		AND 
					  		(d.endDate IS NULL OR d.endDate = '0000-00-00' OR d.endDate >= DATE(Event.execDate))  
				  		) 
				  		OR 
				  		(
				  	  		(d.begDate IS NULL OR d.begDate = '0000-00-00') 
					  		AND 
					  		d.endDate IS NOT NULL 
							AND 
							d.endDate <> '0000-00-00' 
							AND 
							d.endDate >= DATE(Event.execDate)  
				  		) 
					)
					LIMIT 1					
			) /*not exists*/ 
		) /*OR*/ 
	) /*AND*/
)
-- Тип полиса пацеинта
LEFT JOIN rbPolicyType ON rbPolicyType.id = ClientPolicy.policyType_id  
-- Контакт пациента(для определения номера новорожденного)  
LEFT JOIN ClientContact	ON (
	ClientContact.client_id = Client.id  
	AND 
	ClientContact.deleted = 0  
	AND 
	ClientContact.ContactType_id = ::@multipleBirthContactTypeId
) 
-- Документ пациента
LEFT JOIN ClientDocument ON ClientDocument.id  =  (
		SELECT MAX(b.id)  
		FROM  ClientDocument b
		INNER JOIN rbDocumentType bType ON bType.id = b.documentType_id
		WHERE  b.client_id = Client.id 
		AND    b.deleted <> 1  
		AND    bType.group_id = 1  
		AND   (
			(b.date IS NOT NULL AND b.date <> '0000-00-00' AND b.date <= DATE(Event.execDate))
			OR 
			(
				(b.date IS NULL OR b.date = '0000-00-00')
				AND
				NOT EXISTS (
					SELECT c.id 
					FROM ClientDocument c
					INNER JOIN rbDocumentType cType ON cType.id = c.documentType_id
					WHERE c.client_id = Client.id
					AND   c.id <> b.id
					AND   c.deleted <> 1
					AND   cType.group_id = 1
					AND (c.date IS NOT NULL AND c.date <> '0000-00-00' AND c.date <= DATE(Event.execDate))
					LIMIT 1
				)
			)
		)
)
-- Тип документа пациента
LEFT JOIN rbDocumentType ClientDocumentType ON ClientDocumentType.id = ClientDocument.documentType_id 
-- Отношения пациента (для определения представителя) 
LEFT JOIN ClientRelation ON (
	ClientRelation.relative_id = Client.id  
	AND 
	ClientRelation.deleted = 0  
	AND 
	(ClientPolicy.id IS NULL AND TIMESTAMPDIFF(MONTH, Client.birthDate, DATE(Action.begDate)) < 2)
)
-- Представитель пациента
LEFT JOIN Client Spokesman	ON Spokesman.id = ClientRelation.client_id 
-- Документы представителя
LEFT JOIN ClientDocument  SpokesmanDocument ON SpokesmanDocument.id  =  (
		SELECT MAX(b.id)  
		FROM  ClientDocument b
		INNER JOIN rbDocumentType bType ON bType.id = b.documentType_id
		WHERE  b.client_id = Spokesman.id 
		AND    b.deleted <> 1  
		AND    bType.group_id = 1  
		AND   (
			(b.date IS NOT NULL AND b.date <> '0000-00-00' AND b.date <= DATE(Event.execDate))
			OR 
			(
				(b.date IS NULL OR b.date = '0000-00-00')
				AND
				NOT EXISTS (
					SELECT c.id 
					FROM ClientDocument c
					INNER JOIN rbDocumentType cType ON cType.id = c.documentType_id
					WHERE c.client_id = Spokesman.id
					AND   c.id <> b.id
					AND   c.deleted <> 1
					AND   cType.group_id = 1
					AND (c.date IS NOT NULL AND c.date <> '0000-00-00' AND c.date <= DATE(Event.execDate))
					LIMIT 1
				)
			)
		)
)
-- Тип документа представителя 
LEFT JOIN rbDocumentType SpokesmanDocumentType  ON SpokesmanDocumentType.id = SpokesmanDocument.documentType_id  
-- Полис представителя
LEFT JOIN ClientPolicy SpokesmanPolicy  ON SpokesmanPolicy.id = (
	SELECT MAX(c.id) 
	FROM ClientPolicy c 
	WHERE  c.client_id = Spokesman.id  
	AND c.deleted <> 1
	AND c.policyType_id <> 3
	AND 
	(
		 c.begDate IS NOT NULL  
		 AND 
		 c.begDate <> '0000-00-00' 
		 AND 
		 c.begDate <= Event.execDate 
		 AND 
		 (c.endDate IS NULL OR c.endDate = '0000-00-00' OR c.endDate >= DATE(Event.execDate)) 
		 OR		 
		 (c.begDate IS NULL OR c.begDate = '0000-00-00') 
		 AND 
		 c.endDate IS NOT NULL 
		 AND 
		 c.endDate <> '0000-00-00' 
		 AND 
		 c.endDate >= DATE(Event.execDate)
		 OR 
		 (
		 	(c.begDate IS NULL OR c.begDate = '0000-00-00') 
			 AND 
			 (c.endDate IS NULL OR c.endDate = '0000-00-00')  
			 AND NOT EXISTS(
					SELECT * 
				 	FROM ClientPolicy d 
				 	WHERE d.client_id = Spokesman.id
				 	AND d.policyType_id <> 3 
				  	AND d.id <> c.id 
				  	AND d.deleted <> 1 
				  	AND 
					( 
				  		(
					  		d.begDate IS NOT NULL AND d.begDate <> '0000-00-00'  AND d.begDate <= Event.execDate 
					  		AND 
					  		(d.endDate IS NULL OR d.endDate = '0000-00-00' OR d.endDate >= DATE(Event.execDate))  
				  		) 
				  		OR 
				  		(
				  	  		(d.begDate IS NULL OR d.begDate = '0000-00-00') 
					  		AND 
					  		d.endDate IS NOT NULL 
							AND 
							d.endDate <> '0000-00-00' 
							AND 
							d.endDate >= DATE(Event.execDate)  
				  		) 
					)
					LIMIT 1
			) /*not exists*/ 
		) /*OR*/ 
	) /*AND*/
)
-- Тип полиса представителя 
LEFT JOIN rbPolicyType SpokesmanPolicyType ON SpokesmanPolicyType.id = SpokesmanPolicy.policyType_id  
-- Страховщик представителя
LEFT JOIN Organisation Insurer ON Insurer.id = COALESCE(SpokesmanPolicy.insurer_id, ClientPolicy.insurer_id)  
-- Тип обращения
INNER JOIN EventType ON EventType.id = Event.eventType_id
-- Назначение типа обращения  
LEFT JOIN rbEventTypePurpose ON rbEventTypePurpose.id = EventType.purpose_id 
-- тип мед помощи
LEFT JOIN rbMedicalAidType ON rbMedicalAidType.id = EventType.medicalAidType_id 
-- Основная диагностика из обращения 
LEFT JOIN Diagnostic ON (Diagnostic.event_id = Event.id AND   (Diagnostic.diagnosisType_id = 2 OR Diagnostic.diagnosisType_id = 1)  AND   Diagnostic.deleted  = 0)  
-- Основной диагноз из основной диагностики
LEFT JOIN Diagnosis	ON (Diagnosis.id = Diagnostic.diagnosis_id AND Diagnosis.deleted = 0)  
-- Сопуствующая диагностика
LEFT JOIN Diagnostic Diagnostic2 ON Diagnostic2.id = (
	SELECT MIN(Diagnostic3.id)
	FROM Diagnostic Diagnostic3
	WHERE Diagnostic3.event_id = Event.id  
	AND Diagnostic3.deleted = 0  
	AND (Diagnostic3.diagnosisType_id = 3  OR Diagnostic3.diagnosisType_id = 5)
)
-- Сопутствующий диагноз из сопутствующей диагностики  
LEFT JOIN Diagnosis Diagnosis2	ON Diagnosis2.id = Diagnostic2.diagnosis_id
-- Результат из обращения 
LEFT JOIN rbResult ON rbResult.id = Event.result_id
-- Исход из обращения  
LEFT JOIN rbAcheResult ON rbAcheResult.id = Event.rbAcheResult_id
-- Стадия заболевания из основной диагностики  
LEFT JOIN rbDiseasePhases ON rbDiseasePhases.id  = Diagnostic.phase_id  
-- Протокол операции за время 'движения'и в рамках этого-же обращения
LEFT JOIN Action operationAction ON operationAction.id = (
	SELECT bAction.id 
	FROM Action bAction  
	INNER JOIN ActionType bActionType ON bActionType.id = bAction.actionType_id
	WHERE 
	bAction.event_id = Event.id  
	AND bAction.deleted = 0 
	AND bAction.endDate >= Action.begDate 
	AND bAction.endDate <= Action.endDate 
	AND (bActionType.name = 'Протокол операции' OR bActionType.flatCode = 'operation')
	LIMIT 1
)  
-- Свойство 'тип операции' для протокола операции
LEFT JOIN ActionProperty_Integer AP_I_operationAction ON AP_I_operationAction.id = (
	SELECT bActionProperty.id  
	FROM ActionProperty bActionProperty  
	WHERE  
	bActionProperty.action_id = operationAction.id  
	AND  bActionProperty.type_id IN (7472) 
	AND bActionProperty.deleted = 0
	LIMIT 1
)  AND  AP_I_operationAction.index = 0  
-- Тип операции для протокла операции
LEFT JOIN rbOperationType ON rbOperationType.id = AP_I_operationAction.value  
-- Основной диагноз из свойств 'движения'
LEFT JOIN MKB ON MKB.id = (
	SELECT AP_MKB.value
	FROM ActionProperty AP
	INNER JOIN ActionProperty_MKB AP_MKB ON AP.id = AP_MKB.id
	WHERE AP.action_id = Action.id
	AND AP.type_id = ::@stationaryMainDiagnosisActionPropertyTypeId
	AND AP_MKB.`index` = 0
	LIMIT 1
) 
-- Сопутствующий диагноз из свойств 'движения' 
LEFT JOIN MKB MKB2 ON MKB2.id = (
	SELECT AP_MKB.value
	FROM ActionProperty AP
	INNER JOIN ActionProperty_MKB AP_MKB ON AP.id = AP_MKB.id
	WHERE AP.action_id = Action.id
	AND AP.type_id = ::@stationarySecondaryDiagnosisActionPropertyTypeId
	AND AP_MKB.`index` = 0
	LIMIT 1
)
-- 'Исход' из свойств 'движения'
LEFT JOIN ActionProperty_String AP_S_ISHOD ON AP_S_ISHOD.id = (
	SELECT AP.id 
	FROM  ActionProperty AP
	WHERE  AP.action_id = Action.id  
	AND AP.type_id = ::@stationaryIshodActionPropertyTypeId
	AND AP.deleted = 0
	LIMIT 1
	)  AND AP_S_ISHOD.index = 0  
-- 'Результат' из свойств 'движения'
LEFT JOIN ActionProperty_String AP_S_RLST ON AP_S_RLST.id = (
	SELECT AP.id 
	FROM  ActionProperty AP
	WHERE  AP.action_id = Action.id  
	AND AP.type_id = ::@stationaryResultActionPropertyTypeId
	AND AP.deleted = 0
	LIMIT 1
	)  AND AP_S_RLST.index = 0  
-- 'Оплата по КСГ' из свойств 'движения'
LEFT JOIN ActionProperty_String AP_S_CSG ON AP_S_CSG.id = (
	SELECT AP.id 
	FROM  ActionProperty AP
	WHERE  AP.action_id = Action.id  
	AND AP.type_id = ::@stationaryCSGActionPropertyTypeId
	AND AP.deleted = 0
	LIMIT 1
	)  AND AP_S_CSG.index = 0  
-- 'Стадия при выписке (переводе)' из свойств 'движения'
LEFT JOIN ActionProperty_String AP_S_STAGE ON AP_S_STAGE.id = (
	SELECT AP.id 
	FROM  ActionProperty AP
	WHERE  AP.action_id = Action.id  
	AND AP.type_id = ::@stationaryStageActionPropertyTypeId
	AND AP.deleted = 0
	LIMIT 1
	)	AND AP_S_STAGE.index = 0  
-- 'Профиль койки' из свойств 'движения'
LEFT JOIN ActionProperty_HospitalBedProfile  ON ActionProperty_HospitalBedProfile.id = (
	SELECT AP.id  
	FROM ActionProperty AP 
	WHERE  AP.deleted = 0 
	AND AP.action_id = Action.id  
	AND AP.type_id = ::@stationaryHospitalBedProfileActionPropertyTypeId
	LIMIT 1
	)  AND ActionProperty_HospitalBedProfile.index = 0  
-- Сам профиль койки
LEFT JOIN rbHospitalBedProfile  ON rbHospitalBedProfile.id = ActionProperty_HospitalBedProfile.value 
-- Перечень услуг для этого профиля койки 
LEFT JOIN rbHospitalBedProfile_Service  ON rbHospitalBedProfile_Service.rbHospitalBedProfile_id = rbHospitalBedProfile.id  
-- Услуга
INNER JOIN rbService ON rbService.id = rbHospitalBedProfile_Service.rbService_id  
	AND (
			(
				NOT rbService.code LIKE 'А%' 
				AND (
						(  
							SUBSTRING(rbService.code, 9, 1) = '1' 
							AND 
							TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.begDate) ) >= 18
						)  
						OR (   
							SUBSTRING(rbService.code, 9, 1) = '2' 
							AND 
							TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.begDate) ) < 18  
						)  
				) /*AND*/ 
			)  
			OR 
			rbService.code LIKE 'А%'				   
	) /*AND*/ 
	AND (
		rbService.rbMedicalKind_id = EventType.rbMedicalKind_id  
		OR 
		EventType.rbMedicalKind_id IS NULL 
		OR 
		rbService.code LIKE 'А%'
	) 
-- профиль помощи
LEFT JOIN rbMedicalAidProfile ON rbMedicalAidProfile.id = rbService.medicalAidProfile_id  
-- категория помощи
INNER JOIN rbMedicalKind ON rbMedicalKind.id = rbService.rbMedicalKind_id  
-- Наличие в обращении нескольких движений 
LEFT JOIN Action anotherMovingAction ON (
	anotherMovingAction.event_id = Event.id 
	AND 
	anotherMovingAction.deleted = 0 
	AND 
	anotherMovingAction.id <> Action.id 
	AND 
	anotherMovingAction.actionType_id = Action.actionType_id
	AND 
	rbMedicalKind.code <> 'G'
)  
-- ВМП --------------------------------------------------------------
-- 'ВМП' из свойств 'движения' http://helpdesk.korusconsulting.ru/browse/WMIS-95
LEFT JOIN ActionProperty_Integer AP_I_VMP ON AP_I_VMP.id = (
	SELECT AP.id 
	FROM ActionProperty AP
	INNER JOIN ActionPropertyType APT ON AP.type_id = APT.id
	WHERE Ap.action_id = Action.id
	AND APT.name = 'Метод ВМП (при наличии)'
	AND AP.deleted = 0
	LIMIT 1
) AND AP_I_VMP.index = 0
-- Метод ВМП
LEFT JOIN rbTreatment ON (
	-- заполнено свойство
	AP_I_VMP.id IS NOT NULL
	AND
	-- только круглосуточный стационар
	rbMedicalKind.code = 'S'
	AND
	-- длительность лечения больше двух дней
	IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))) > 2  
	AND
	-- идентификатор метода rbTreatment.id равнялся бы результату выполнения функции search_Treatment
	rbTreatment.id = search_Treatment(
		::@contractId,
		Action.endDate,
		rbService.id,
		IF(anotherMovingAction.id IS NULL, 
			IF(MKB.diagID IS NOT NULL, 
				MKB.diagID, 
				Diagnosis.MKB
			), 
			IF(MKB.diagID IS NOT NULL, 
				MKB.diagID,
				IF(MKB2.diagID IS NOT NULL, MKB2.diagID,'')
			)
		),
		AP_I_VMP.value
	)		
)
-- Модель пациента
LEFT JOIN rbPacientModel ON rbPacientModel.id = rbTreatment.pacientModel_id
-- вид ВМП
LEFT JOIN QuotaType ON QuotaType.id = rbPacientModel.quotaType_id
-- END OF ВМП -------------------------------------------------------
-- группа КСГ
LEFT JOIN rbCSG ON 
	-- Примечание: метод ВМП пытаться искать до КСГ и поиск КСГ не проводить, если найден метод ВМП (не будут одновременно)
	rbTreatment.id IS NULL
	AND
	rbMedicalKind.code <> 'G'
	AND
	NOT(
		TIMESTAMPDIFF(DAY, Client.birthDate, DATE(Action.begDate)) > 28
		AND
		rbMedicalAidProfile.code = '55'
		AND
		rbMedicalKind.code = 'S'
	)
	AND
	NOT (
		(rbMedicalKind.code = 'D' OR rbMedicalKind.code = 'P') 
		AND 
		IF(DATE(Action.endDate) = DATE(Action.begDate), 1, TIMESTAMPDIFF(DAY, DATE(Action.begDate), DATE(Action.endDate))+1 - num_sunday_days(DATE(Action.begDate), DATE(Action.endDate))) >= 2
	)
	AND
	NOT(
		rbMedicalKind.code = 'S'  
		AND 
		IF(DATE(Action.endDate) = DATE(Action.begDate), 1, TIMESTAMPDIFF(DAY, DATE(Action.begDate), DATE(Action.endDate)) ) <= 2
	) 
	AND 
	rbCSG.id = search_CSG(
		AP_S_CSG.value,
		::@levelMO,
		::@contractId, 
		Action.endDate,
		rbService.id,
		IF(anotherMovingAction.id IS NULL, 
			IF(MKB.diagID IS NOT NULL, 
				MKB.diagID, 
				Diagnosis.MKB
			), 
			IF(MKB.diagID IS NOT NULL, 
				MKB.diagID,
				IF(MKB2.diagID IS NOT NULL, MKB2.diagID,'')
			)
		), 
		rbOperationType.TFOMSCode
	)  
-- Таблица-связка
INNER JOIN MedicalKindUnit MKU	ON 
(
-- Совпадает категория помощи
MKU.rbMedicalKind_id = rbMedicalKind.id 
AND 
(
    -- Совпадает тип обращения
	MKU.eventType_id = EventType.id   
	OR 
	-- ИЛИ с искомым типом обращения нет записей -> NULL
	(
		MKU.eventType_id IS NULL 
		AND 
		NOT EXISTS(
			SELECT * 
			FROM MedicalKindUnit bMKU  
			WHERE 
			bMKU.eventType_id =  EventType.id 
			AND 
			bMKU.rbMedicalKind_id = rbMedicalKind.id
		) -- END OF SUBQUERY
	)
) 
AND 
(   
	-- Круглосуточный стационар 'S'
	(
		-- S_1 Круглосуточный стационар с длительностью лечения менее 2-х дней   (по койко-дням (1))
		rbMedicalKind.code = 'S' 
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))) <= 2  
		AND 
		MKU.rbMedicalAidUnit_id = (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '1' LIMIT 1)
	) -- END OF 'S_1'  
	OR   
	(
		-- S_2 Круглосуточный стационар с длительностью лечения более 2-х дней, но без КСГ-группы, и без ВМП (по законченному случаю (2))
		rbMedicalKind.code = 'S' 
		AND 
		rbCSG.id IS NULL  
		AND
		rbTreatment.id IS NULL
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))) > 2  
		AND
		MKU.rbMedicalAidUnit_id = (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '2' LIMIT 1)
	) -- END OF 'S_2'
	OR   
	(
		-- S_3 Круглосуточный стационар с длительностью лечения более 2-х дней с найденной КСГ-группой (по КСГ(7))
		rbMedicalKind.code = 'S' 
		AND 
		rbCSG.id IS NOT NULL  
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))) > 2 
		AND 
		MKU.rbMedicalAidUnit_id =  (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '7' LIMIT 1)
	) -- END OF 'S_3'
	OR   
	(
		-- S_4 Круглосуточный стационар с длительностью лечения более 2-х дней с найденной ВМП (по ВМП(6))
		rbMedicalKind.code = 'S' 
		AND 
		rbTreatment.id IS NOT NULL  
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))) > 2 
		AND 
		MKU.rbMedicalAidUnit_id =  (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '6' LIMIT 1)
	) -- END OF 'S_4'
	-- END OF 'S'
	
	-- Дневной стационар 'D'
	OR 
	(
		-- D_1 Дневной стационар с длительностью лечения <= 2-х дней, но без КСГ-группы (по койко-дням (1))
		rbMedicalKind.code = 'D' 
		AND 
		rbCSG.id IS NULL  
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))+1 - get_sunday_count(date(Action.begDate), date(Action.endDate))) <= 2  
		AND
		MKU.rbMedicalAidUnit_id = 	(SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '1' LIMIT 1)  
	) -- END OF 'D_1'  
	OR 
	(
		-- D_2 Дневной стационар с длительностью лечения = 1 дню с найденной группой КСГ (по КСГ (7))
		rbMedicalKind.code = 'D' 
		AND 
		rbCSG.id IS NOT NULL  
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))+1 - get_sunday_count(date(Action.begDate), date(Action.endDate))) = 1  
		AND 
		MKU.rbMedicalAidUnit_id = (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '7' LIMIT 1)  
	)  -- END OF 'D_2'
	OR 
	(
		-- D_3 Дневной стационар с длительностью лечения = 2 дня с найденной КСГ-группой (по койко-дням (1))
		rbMedicalKind.code = 'D' 
		AND 
		rbCSG.id IS NOT NULL  
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))+1 - get_sunday_count(date(Action.begDate), date(Action.endDate))) = 2 
		AND 
		MKU.rbMedicalAidUnit_id = (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '1' LIMIT 1)  
	) -- END OF 'D_3'   
	OR 
	(
		-- D_4 Дневной стационар с длительностью лечения более 2-х дней (по законченному случаю (2))
		rbMedicalKind.code = 'D'   
		AND 
		IF(date(Action.endDate) = date(Action.begDate), 1, TIMESTAMPDIFF(DAY, date(Action.begDate), date(Action.endDate))+1 - get_sunday_count(date(Action.begDate), date(Action.endDate))) > 2  
		AND 
		MKU.rbMedicalAidUnit_id = (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '2' LIMIT 1)
	) -- END OF 'D_4'
	OR
	(
		-- P_1 Полилкиника по КСГ (по КСГ(7))
		rbMedicalKind.code = 'P'
		AND
		rbCSG.id IS NOT NULL
		AND
		MKU.rbMedicalAidUnit_id = (SELECT bMAU.id FROM rbMedicalAidUnit bMAU WHERE bMAU.code = '7' LIMIT 1)
		-- END OF 'P_1'
	)
	OR 
	-- Диагностика
	(rbMedicalKind.code = 'I')  
	OR 
	-- Гемодиализ
	(rbMedicalKind.code = 'G')
) 
)   
-- единица измерения помощи
INNER JOIN rbMedicalAidUnit	ON rbMedicalAidUnit.id = MKU.rbMedicalAidUnit_id  
-- категория оплаты
LEFT JOIN rbPayType  ON rbPayType.id = MKU.rbPayType_id  
-- врач, выполнивший услугу
LEFT JOIN Person ON Person.id = Action.person_id  
-- подразделение в котором работает врач, выполнивший услугу
LEFT JOIN OrgStructure ON OrgStructure.id = Person.orgStructure_id  
-- Специальность врача
LEFT JOIN rbSpeciality ON rbSpeciality.id = Person.speciality_id  
-- Тариф
INNER JOIN Contract_Tariff CT ON (
		CT.master_id = ::@contractId
		AND 
		CT.service_id = rbService.id
		AND (
				(
					CT.rbCSG_id IS NULL 
					AND 
					rbCSG.id IS NULL
				) 
				OR 
				(
					CT.rbCSG_id = rbCSG.id
					AND 
					rbCSG.id IS NOT NULL
				)
		) 
		AND (
				(
					CT.rbTreatment_id IS NULL 
					AND 
					rbTreatment.id IS NULL
				)
				OR 
				(
					CT.rbTreatment_id = rbTreatment.id 
					AND 
					rbTreatment.id IS NOT NULL
				)
		)
		AND (
			CT.eventType_id = EventType.id  
			OR 
			CT.eventType_id IS NULL
		)
		AND 
		DATE(Action.endDate) BETWEEN CT.begDate AND CT.endDate
		AND 
		checkAge(CT.age, Client.birthDate, Action.begDate)
		AND 
		CT.unit_id = MKU.rbMedicalAidUnit_id   
) 
-- Источник финансирования 
INNER JOIN rbServiceFinance	ON rbServiceFinance.id = CT.rbServiceFinance_id
-- WHERE PHRASE ------------------------------------------------------
WHERE 
-- Обращение не удалено
Event.deleted = 0
-- Контракт совпадает с указанным
AND   
Event.contract_id = ::@contractId
-- Действие не удалено
AND      
Action.deleted = 0 
AND 
Action.actionType_id = ::@movingActionTypeId 
AND 
NOT EXISTS(SELECT * FROM Account_Item ac_i  WHERE ac_i.action_id =  Action.id AND ac_i.deleted=0) 
-- Обращение попадает в указанный интервал
AND  
Event.execDate BETWEEN TIMESTAMP(::@beginInterval)  AND TIMESTAMP(::@endInterval)   
-- Дата начала движения существует
AND 
Action.begDate IS NOT NULL   
-- Действие завершено
AND 
Action.status = 2  
-- услуга оказана врачом из заданного набора подразделений или по всему ЛПУ
AND
( ::@orgStructureIdList = '' OR FIND_IN_SET(OrgStructure.id, ::@orgStructureIdList) )
-- Сортировка -------------------------------------------------------
ORDER BY Client.id, Event.id, Action.id, rbServiceFinance.id; 
''',
	'SpecialVar_TFOMS_Policlinic_Additional': '''
SELECT 
Action.id as 'ActionId',
Event.id as 'EventId', 
rbService.id as 'rbServiceId',
rbService.infis AS 'rbServiceInfis',
rbServiceFinance.id as 'rbServiceFinanceId', 
rbMedicalKind.code as 'rbMedicalKindCode',
rbMedicalAidUnit.id AS 'rbMedicalAidUnitId',
rbMedicalAidUnit.code as 'rbMedicalAidUnitCode', 
IF(Event.order = 2, 2, 1) AS 'EXTR',  
IF(TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.endDate)) < 18, 1, 0) AS 'DET',  
DATE(Action.endDate) AS 'DATE_1',  
DATE(Action.endDate) AS 'DATE_2',  
IF(rbDiseasePhases.code IS NOT NULL, rbDiseasePhases.code, '0') AS 'DS0',  
Diagnosis.MKB AS 'DS1',  
IF(Diagnosis2.MKB IS NOT NULL, Diagnosis2.MKB, '') AS 'DS2',  
rbResult.code AS 'RSLT',  
rbAcheResult.code AS 'ISHOD',  
rbSpeciality.code AS 'PRVS',  
IF(Person.SNILS <> '', insert(insert(insert(Person.SNILS, 4, 0, '-'), 8, 0, '-'), 12,0, ' ' ), '') AS 'IDDOKT',
0 AS 'OS_SLUCH',  
rbService.departCode  AS 'PODR',        
rbMedicalAidProfile.code   AS 'PROFIL', 
CONCAT(
	rbMedicalAidUnit.code, 
	rbMedicalKind.code, 
	0, 
	rbService.infis,
	IF(TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.endDate)) >= 18, 1, 2),
	rbServiceFinance.code
)  AS 'CODE_USL',
0 AS 'TARIF',
CT.id AS 'tariffId',
1 AS 'ED_COL',
rbResult.regionalCode AS 'RSLTRegionalCode'
FROM Action 
INNER JOIN Event ON Event.id = Action.event_id  
INNER JOIN Client ON Client.id = ::@clientId  
INNER JOIN EventType ON EventType.id = Event.eventType_id  
LEFT JOIN Diagnostic ON (
	Diagnostic.event_id = Event.id 
	AND   
	(Diagnostic.diagnosisType_id = 2 OR Diagnostic.diagnosisType_id = 1)  
	AND   
	Diagnostic.deleted  = 0
)  
LEFT JOIN Diagnosis	ON (
	Diagnosis.id = Diagnostic.diagnosis_id 
	AND 
	Diagnosis.deleted = 0
)  
LEFT JOIN Diagnostic Diagnostic2	ON Diagnostic2.id = (
	SELECT 
	min(Diagnostic3.id)  
	FROM Diagnostic Diagnostic3  
	WHERE 
	Diagnostic3.event_id = Event.id  
	AND 
	Diagnostic3.deleted = 0  
	AND 
	Diagnostic3. diagnosisType_id <> 2  
	AND 
	Diagnostic3. diagnosisType_id <> 1
)
LEFT JOIN Diagnosis Diagnosis2	ON Diagnosis2.id = Diagnostic2.diagnosis_id  AND Diagnosis2.deleted = 0
LEFT JOIN rbResult ON rbResult.id = COALESCE(Diagnostic.result_id, Event.result_id)   
LEFT JOIN rbAcheResult ON rbAcheResult.id = COALESCE(Diagnostic.rbAcheResult_id,Event.rbAcheResult_id)   
LEFT JOIN rbDiseasePhases ON rbDiseasePhases.id = Diagnostic.phase_id  
INNER JOIN ActionType ON ActionType.id = Action.actionType_id AND ActionType.service_id IS NOT NULL  
INNER JOIN rbService ON rbService.id = ActionType.service_id 
LEFT JOIN rbMedicalAidProfile ON rbMedicalAidProfile.id = rbService.medicalAidProfile_id 
INNER JOIN rbMedicalKind ON rbMedicalKind.id = 
	COALESCE(EventType.rbMedicalKind_id, rbService.rbMedicalKind_id) 	
INNER JOIN MedicalKindUnit MKU ON (
	MKU.rbMedicalKind_id = rbMedicalKind.id
	AND (
		MKU.eventType_id = ::@eventTypeId  
		OR 
		(
			MKU.eventType_id IS NULL 
			AND 
			NOT EXISTS(
				SELECT 
				bMKU.id 
				FROM MedicalKindUnit bMKU
				WHERE 
				bMKU.eventType_id = ::@eventTypeId  
				AND 
				bMKU.rbMedicalKind_id = rbMedicalKind.id
			) 
		)  
	) 
) /*ON*/  
INNER JOIN rbMedicalAidUnit ON rbMedicalAidUnit.id = MKU.rbMedicalAidUnit_id  
LEFT JOIN Person ON Person.id = Action.person_id  
LEFT JOIN OrgStructure ON OrgStructure.id = Person.orgStructure_id  
LEFT JOIN rbSpeciality ON rbSpeciality.id = Person.speciality_id  
LEFT JOIN Contract_Tariff CT ON 
	CT.master_id = ::@contractId
	AND 
	CT.service_id = rbService.id  
	AND 
	( 
		(
			(
				CT.eventType_id = ::@eventTypeId   
				AND  
				LOCATE(rbMedicalKind.code, 'HCVZ')
			)  
			OR 
			(
				NOT LOCATE(rbMedicalKind.code, 'HCVZ')
				and 
				CT.eventType_id IS NULL
			)  
		)
	)  
	AND 
	(
		CT.begDate  <= DATE(::@checkDate)  
		OR 
		CT.begDate = '0000-00-00'
	)  
	AND 
	(
		CT.endDate >= DATE(::@checkDate)  
		OR 
		CT.endDate = '0000-00-00'
	)  
	AND 
	checkAge(CT.age, Client.birthDate, DATE(Action.endDate))
	AND 
	CT.unit_id = MKU.rbMedicalAidUnit_id  
	AND 
	NOT 
	(
		(
			SUBSTRING(::@InsurerArea, 1, 2) = ::@SMOArea 
			OR 
			::@InsurerArea IS NULL
		) 
		AND 
		(
			rbMedicalKind.code = 'F' 
			OR 
			rbMedicalKind.code = 'R' 
			OR  
			(
				rbMedicalKind.code = 'P' 
				AND 
				(rbMedicalAidUnit.code = '2' OR rbMedicalAidUnit.code = '1') 
				AND 
				SUBSTRING(rbService.infis, 3, 3) IN('026','076','081') 
			) 
		)  
	)  
INNER JOIN rbServiceFinance	ON (
	(
		NOT 
		(
			(
				SUBSTRING(::@InsurerArea, 1, 2) = ::@SMOArea 
				OR 
				::@InsurerArea IS NULL
			) 
			AND 
			(
				rbMedicalKind.code = 'F'  
				OR 
				rbMedicalKind.code = 'R' 
				OR 
				(
					rbMedicalKind.code = 'P' 
					AND 
					(rbMedicalAidUnit.code = '2' OR rbMedicalAidUnit.code = '1')  
					AND 
					SUBSTRING(rbService.infis, 3, 3) IN('026','076','081')
				) 
			)
		)  
		AND 
		rbServiceFinance.id = CT.rbServiceFinance_id
	)  
	OR 
	(
		(
			(
				SUBSTRING(::@InsurerArea, 1, 2) = ::@SMOArea 
				OR 
				::@InsurerArea IS NULL
			) 
			AND 
			(
				rbMedicalKind.code = 'F'  
				OR 
				rbMedicalKind.code = 'R' 
				OR 
				(
					rbMedicalKind.code = 'P' 
					AND 
					(rbMedicalAidUnit.code = '2' OR rbMedicalAidUnit.code = '1')  
					AND 
					SUBSTRING(rbService.infis, 3, 3) IN('026','076','081')
				) 
			)
		)  
		AND 
		rbServiceFinance.code = '2'
	)
)
WHERE    
Event.client_id = ::@clientId 
AND 
rbMedicalKind.code = 'P'  
AND      
Event.deleted = 0  
AND      
Event.contract_id = ::@contractId  
AND      
Action.deleted = 0  
AND      
SUBSTRING(rbService.infis, 1, 5) = SUBSTRING(::@serviceInfisCode, 1, 5)  
AND      
Action.endDate < ::@checkDate  
-- Услуга оказана в заданном списке подразделений или по всем подразделениям
AND
( ::@orgStructureIdList = '' OR FIND_IN_SET(OrgStructure.id, ::@orgStructureIdList) )  
AND  
Event.eventType_id  = ::@eventTypeId  
ORDER BY Action.endDate DESC, Action.id DESC, rbServiceFinance.id; 
''',
	'SpecialVar_TFOMS_Dispanserization_Additional': '''
SELECT 
Action.id as 'ActionId',
Event.id as 'EventId' ,
rbService.id as 'rbServiceId', 
rbService.infis as 'rbServiceInfis',
rbServiceFinance.id as 'rbServiceFinanceId', 
rbMedicalKind.code as 'rbMedicalKindCode', 
rbMedicalAidUnit.id AS 'rbMedicalAidUnitId',
rbMedicalAidUnit.code as 'rbMedicalAidUnitCode',       
IF(Event.order = 2, 2, 1) AS 'EXTR',        
IF(TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.endDate)) < 18, 1, 0) AS 'DET',        
DATE(Action.endDate) AS 'DATE_1',        
DATE(Action.endDate) AS 'DATE_2',        
IF(rbDiseasePhases.code IS NOT NULL, rbDiseasePhases.code, '0') AS 'DS0',        
Diagnosis.MKB AS 'DS1',         
IF(Diagnosis2.MKB IS NOT NULL, Diagnosis2.MKB, '') AS 'DS2',        
rbResult.code AS 'RSLT',        
rbAcheResult.code AS 'ISHOD',       
rbSpeciality.code AS 'PRVS',        
IF(Person.SNILS <> '', insert(insert(insert(Person.SNILS, 4, 0, '-'), 8, 0, '-'), 12,0, ' ' ), '') AS 'IDDOKT',        
0 AS 'OS_SLUCH',        
rbService.departCode  AS 'PODR',        
rbMedicalAidProfile.code   AS 'PROFIL',        
CONCAT(
	rbMedicalAidUnit.code, 
	rbMedicalKind.code,
	IF(LOCATE(rbMedicalKind.code,'HCVZ') AND rbMedicalAidUnit.code = '2' AND MKU.stageCode <> '2',
			CONCAT(rbDispInfo.code, SUBSTRING(rbService.infis, 3, 5)),
			CONCAT('0', 
				IF(LOCATE(rbMedicalKind.code, 'PHCVZ') AND (rbMedicalAidUnit.code = '3' or MKU.stageCode = '2') AND SUBSTRING(rbService.infis, 1, 2) <> '06', 
					INSERT(rbService.infis, 1, 2, '04'),
					rbService.infis
				)
			)
	),
	IF(TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.endDate)) >= 18, 1, 2), 
	rbServiceFinance.code
)  AS 'CODE_USL',        
CT.price AS 'TARIF',
CT.id AS 'tariffId',        
1 AS 'ED_COL',        
rbResult.regionalCode as 'RSLTRegionalCode' 
FROM Action 
INNER JOIN Event ON Event.id = Action.event_id  
INNER JOIN Client ON Client.id = ::@clientId  
INNER JOIN EventType ON EventType.id = Event.eventType_id  
LEFT JOIN Diagnostic ON (
	Diagnostic.event_id = Event.id 
	AND   
	(Diagnostic.diagnosisType_id = 2 OR Diagnostic.diagnosisType_id = 1)  
	AND   
	Diagnostic.deleted  = 0
)  
LEFT JOIN Diagnosis	ON (
	Diagnosis.id = Diagnostic.diagnosis_id 
	AND 
	Diagnosis.deleted = 0
)  
LEFT JOIN Diagnostic Diagnostic2	ON Diagnostic2.id = (
	SELECT 
	min(Diagnostic3.id)  
	FROM Diagnostic Diagnostic3  
	WHERE 
	Diagnostic3.event_id = Event.id  
	AND 
	Diagnostic3.deleted = 0  
	AND 
	Diagnostic3. diagnosisType_id <> 2  
	AND 
	Diagnostic3. diagnosisType_id <> 1
)  
LEFT JOIN Diagnosis Diagnosis2	ON Diagnosis2.id = Diagnostic2.diagnosis_id AND Diagnosis2.deleted = 0 
LEFT JOIN rbResult ON rbResult.id = COALESCE(Diagnostic.result_id, Event.result_id)   
LEFT JOIN rbAcheResult ON rbAcheResult.id = COALESCE(Diagnostic.rbAcheResult_id,Event.rbAcheResult_id)   
LEFT JOIN rbDiseasePhases ON rbDiseasePhases.id = Diagnostic.phase_id  
INNER JOIN ActionType ON ActionType.id = Action.actionType_id AND ActionType.service_id IS NOT NULL  
INNER JOIN rbService ON rbService.id = ActionType.service_id 
LEFT JOIN rbMedicalAidProfile ON rbMedicalAidProfile.id = rbService.medicalAidProfile_id 
INNER JOIN rbMedicalKind ON rbMedicalKind.id = 
	COALESCE(EventType.rbMedicalKind_id, rbService.rbMedicalKind_id) 
INNER JOIN MedicalKindUnit MKU ON (
	MKU.rbMedicalKind_id = rbMedicalKind.id
	AND (
		MKU.eventType_id = ::@eventTypeId  
		OR 
		(
			MKU.eventType_id IS NULL 
			AND 
			NOT EXISTS(
				SELECT 
				bMKU.id 
				FROM MedicalKindUnit bMKU
				WHERE 
				bMKU.eventType_id = ::@eventTypeId  
				AND 
				bMKU.rbMedicalKind_id = rbMedicalKind.id
			) 
		)  
	) 
) /*ON*/  
INNER JOIN rbMedicalAidUnit ON rbMedicalAidUnit.id = MKU.rbMedicalAidUnit_id  
LEFT JOIN Person ON Person.id = Action.person_id  
LEFT JOIN OrgStructure ON OrgStructure.id = Person.orgStructure_id  
LEFT JOIN rbSpeciality ON rbSpeciality.id = Person.speciality_id  
LEFT JOIN Contract_Tariff CT ON (
	(CT.sex = 0 OR CT.sex = Client.sex) 
	AND 
	(
		CT.master_id = ::@contractId  
		AND 
		CT.service_id = rbService.id  
		AND 
		( 
			(
				CT.eventType_id = ::@eventTypeId
				AND  
				LOCATE(rbMedicalKind.code, 'HCVZ')
			)  
			OR 
			(
				CT.eventType_id IS NULL
				AND  
				NOT LOCATE(rbMedicalKind.code, 'HCVZ')
			)  
		)  
		AND 
		(
			CT.begDate  <= DATE(Action.endDate)  
			OR 
			CT.begDate = '0000-00-00'
		)  
		AND 
		(
			CT.endDate >= DATE(Action.endDate)  
			OR 
			CT.endDate = '0000-00-00'
		)  
		AND 
		checkAge(
			CT.age,
			Client.birthDate,
			IF( LOCATE('М', CT.age),
			-- TRUE
				DATE(::@checkDate),
			-- FALSE
				IF(
					(
						(rbMedicalKind.code = 'H' AND TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(::@checkDate)) >= 3)
						OR 
						rbMedicalKind.code = 'V' 
						OR 
						rbMedicalKind.code = 'Z'
					)
					AND
					rbMedicalAidUnit.code = '2'
					AND 
					TIMESTAMPDIFF(YEAR, Client.birthDate, DATE(Action.endDate)) <> 17,
				-- TRUE 
					CONCAT(YEAR(DATE(Action.endDate)), '-12-31'),
				-- FALSE
					DATE(Action.endDate)
				)
			)
		)
		AND 
		CT.unit_id =  rbMedicalAidUnit.id  
	)  
)  
LEFT JOIN rbDispInfo ON LOCATE(rbMedicalKind.code, 'HCVZ') AND rbDispInfo.sex = CT.sex AND rbDispInfo.age = CT.age AND rbDispInfo.rbMedicalKind_id = rbMedicalKind.id  
INNER JOIN rbServiceFinance  ON  rbServiceFinance.id = CT.rbServiceFinance_id
WHERE    
Event.client_id = ::@clientId 
AND
Event.eventType_id = ::@eventTypeId  
AND
Event.deleted = 0  
AND
Event.contract_id = ::@contractId  
AND 
Action.deleted = 0  
AND
Action.endDate < CONCAT(DATE(::@checkDate), ' 23:59:59')  
AND 
Action.id <> ::@actionId  
-- Услуга оказана в заданном списке подразделений или по всем подразделениям
AND
( ::@orgStructureIdList = '' OR FIND_IN_SET(OrgStructure.id, ::@orgStructureIdList) ) 
AND      
ActionType.service_id IS NOT NULL  

ORDER BY 
	DATE(Action.endDate) DESC,
	IF((SUBSTRING(rbService.infis,3,3) IN ('026','076','081','031') AND rbMedicalKind.code <> 'P') OR (rbResult.regionalCode = '2' AND rbMedicalKind.code = 'P'), 0, 1), 
	Action.id DESC,
	rbServiceFinance.id ASC 
''',
	'SpecialVar_TFOMS_Patient_OKATOG': '''
-- Запрос на определение ОКАТО-кода адреса регистрации

SELECT
KL.OCATD AS 'OKATO'
FROM ClientAddress CA
INNER JOIN Address AD ON AD.id = CA.address_id
INNER JOIN AddressHouse AH ON AH.id = AD.house_id
INNER JOIN kladr.KLADR KL ON KL.code = AH.KLADRCode
WHERE CA.`type` = 1
AND CA.client_id = ::@clientId
''',
	'SpecialVar_TFOMS_Patient_OKATOP' : '''
-- Запрос для определения ОКАТО-кода адреса проживания

SELECT
KL.OCATD AS 'OKATO'
FROM ClientAddress CA
INNER JOIN Address AD ON AD.id = CA.address_id
INNER JOIN AddressHouse AH ON AH.id = AD.house_id
INNER JOIN kladr.KLADR KL ON KL.code = AH.KLADRCode
WHERE CA.`type` = 0
AND CA.client_id = ::@clientId
'''
    }
	
    specialvarInsertSQL = '''INSERT INTO rbSpecialVariablesPreferences(name, query) VALUES("{0}","{1}");'''
    variableInsertSQL = '''INSERT INTO VariablesForSQL(`specialVarName_id`, `name`, `label`, `var_type`) VALUES({0}, '{1}', '{2}', '')'''
    # PreSelect queries
    c.execute(specialvarInsertSQL.format('SpecialVar_getMovingActionTypeId', specialvar['SpecialVar_getMovingActionTypeId']))
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationaryDiagnosisActionPropertyTypeId', specialvar['SpecialVar_getStationaryDiagnosisActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId']))
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationarySecondaryDiagnosisActionPropertyTypeId', specialvar['SpecialVar_getStationarySecondaryDiagnosisActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId']))
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationaryIshodActionPropertyTypeId', specialvar['SpecialVar_getStationaryIshodActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId']))
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationaryResultActionPropertyTypeId', specialvar['SpecialVar_getStationaryResultActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId']))
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationaryCSGActionPropertyTypeId', specialvar['SpecialVar_getStationaryCSGActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId']))
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationaryStageActionPropertyTypeId', specialvar['SpecialVar_getStationaryStageActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId'])) 
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getStationaryHospitalBedProfileActionPropertyTypeId', specialvar['SpecialVar_getStationaryHospitalBedProfileActionPropertyTypeId']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId'])) 
	
    c.execute(specialvarInsertSQL.format('SpecialVar_getMultipleBirthContactTypeId', specialvar['SpecialVar_getMultipleBirthContactTypeId']))
    #--------------- Stationary
    c.execute(specialvarInsertSQL.format('SpecialVar_TFOMS_FlatStationar', specialvar['SpecialVar_TFOMS_FlatStationar']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@beginInterval', variables['@beginInterval'])) 
    c.execute(variableInsertSQL.format(id, '@endInterval', variables['@endInterval']))
    c.execute(variableInsertSQL.format(id, '@orgStructureIdList', variables['@orgStructureIdList'])) 
    c.execute(variableInsertSQL.format(id, '@contractId', variables['@contractId'])) 
    c.execute(variableInsertSQL.format(id, '@levelMO', variables['@levelMO'])) 
    c.execute(variableInsertSQL.format(id, '@obsoleteInfisCode', variables['@obsoleteInfisCode'])) 
    c.execute(variableInsertSQL.format(id, '@stationaryMainDiagnosisActionPropertyTypeId', variables['@stationaryMainDiagnosisActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@stationarySecondaryDiagnosisActionPropertyTypeId', variables['@stationarySecondaryDiagnosisActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@stationaryIshodActionPropertyTypeId', variables['@stationaryIshodActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@stationaryResultActionPropertyTypeId', variables['@stationaryResultActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@stationaryCSGActionPropertyTypeId', variables['@stationaryCSGActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@stationaryStageActionPropertyTypeId', variables['@stationaryStageActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@stationaryHospitalBedProfileActionPropertyTypeId', variables['@stationaryHospitalBedProfileActionPropertyTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@multipleBirthContactTypeId', variables['@multipleBirthContactTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@movingActionTypeId', variables['@movingActionTypeId']))
    #--------------- Policlinic
    c.execute(specialvarInsertSQL.format('SpecialVar_TFOMS_Policlinic', specialvar['SpecialVar_TFOMS_Policlinic']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@contractId', variables['@contractId'])) 
    c.execute(variableInsertSQL.format(id, '@beginInterval', variables['@beginInterval'])) 
    c.execute(variableInsertSQL.format(id, '@endInterval', variables['@endInterval']))
    c.execute(variableInsertSQL.format(id, '@organisationId', variables['@organisationId']))
    c.execute(variableInsertSQL.format(id, '@obsoleteInfisCode', variables['@obsoleteInfisCode'])) 
    c.execute(variableInsertSQL.format(id, '@SMOArea', variables['@SMOArea'])) 
    c.execute(variableInsertSQL.format(id, '@orgStructureIdList', variables['@orgStructureIdList'])) 
    c.execute(variableInsertSQL.format(id, '@multipleBirthContactTypeId', variables['@multipleBirthContactTypeId'])) 
    #--------------- Additional queries
    #2P_Additional
    c.execute(specialvarInsertSQL.format('SpecialVar_TFOMS_Policlinic_Additional', specialvar['SpecialVar_TFOMS_Policlinic_Additional']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@contractId', variables['@contractId'])) 
    c.execute(variableInsertSQL.format(id, '@eventTypeId', variables['@eventTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@checkDate', variables['@checkDate']))
    c.execute(variableInsertSQL.format(id, '@clientId', variables['@clientId']))
    c.execute(variableInsertSQL.format(id, '@InsurerArea', variables['@InsurerArea'])) 
    c.execute(variableInsertSQL.format(id, '@SMOArea', variables['@SMOArea'])) 
    c.execute(variableInsertSQL.format(id, '@orgStructureIdList', variables['@orgStructureIdList'])) 
    c.execute(variableInsertSQL.format(id, '@serviceInfisCode', variables['@serviceInfisCode'])) 
    #HCVZ_Additional
    c.execute(specialvarInsertSQL.format('SpecialVar_TFOMS_Dispanserization_Additional', specialvar['SpecialVar_TFOMS_Dispanserization_Additional']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@contractId', variables['@contractId'])) 
    c.execute(variableInsertSQL.format(id, '@eventTypeId', variables['@eventTypeId'])) 
    c.execute(variableInsertSQL.format(id, '@checkDate', variables['@checkDate']))
    c.execute(variableInsertSQL.format(id, '@clientId', variables['@clientId']))
    c.execute(variableInsertSQL.format(id, '@orgStructureIdList', variables['@orgStructureIdList'])) 
    c.execute(variableInsertSQL.format(id, '@actionId', variables['@actionId'])) 
    #OCATOG\P
    c.execute(specialvarInsertSQL.format('SpecialVar_TFOMS_Patient_OKATOG', specialvar['SpecialVar_TFOMS_Patient_OKATOG']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@clientId', variables['@clientId']))
    c.execute(specialvarInsertSQL.format('SpecialVar_TFOMS_Patient_OKATOP', specialvar['SpecialVar_TFOMS_Patient_OKATOP']))
    id = c.lastrowid
    c.execute(variableInsertSQL.format(id, '@clientId', variables['@clientId']))
    
    c.close

def downgrade(conn):
    c = conn.cursor()
	
    specialvarDeleteSQL = '''DELETE FROM rbSpecialVariablePreferences WHERE rbSpecialVariablePreferences.name = "{0}"'''
    specialvarNames = (
	'SpecialVar_TFOMS_Dispanserization_Additional',
	'SpecialVar_TFOMS_Policlinic_Additional',
	'SpecialVar_TFOMS_Policlinic',
	'SpecialVar_TFOMS_FlatStationar',
	'SpecialVar_getMultipleBirthContactTypeId',
	'SpecialVar_getStationaryHospitalBedProfileActionPropertyTypeId',
	'SpecialVar_getStationaryStageActionPropertyTypeId',
	'SpecialVar_getStationaryCSGActionPropertyTypeId',
	'SpecialVar_getStationaryResultActionPropertyTypeId',
	'SpecialVar_getStationaryIshodActionPropertyTypeId',
	'SpecialVar_getStationarySecondaryDiagnosisActionPropertyTypeId',
	'SpecialVar_getStationaryDiagnosisActionPropertyTypeId',
	'SpecialVar_getMovingActionTypeId',
	'SpecialVar_TFOMS_Patient_OKATOG',
	'SpecialVar_TFOMS_Patient_OKATOP',
    )
    for specialvarName in specialvarNames:
        c.execute(specialvarDeleteSQL.format(specialvarName))
    c.close