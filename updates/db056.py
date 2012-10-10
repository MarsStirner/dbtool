#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    c = conn.cursor()

    sql = u'''
ALTER TABLE Account CHANGE COLUMN payer_id payer_id INTEGER COMMENT 'Плательщик {Organisation}' NOT NULL;

ALTER TABLE Account CHANGE COLUMN settleDate settleDate DATE COMMENT 'Расчетная дата' NOT NULL;

ALTER TABLE Account CHANGE COLUMN number number VARCHAR(20) COMMENT 'Номер счета' NOT NULL;

ALTER TABLE Account CHANGE COLUMN date date DATE COMMENT 'Дата счета' NOT NULL;

ALTER TABLE Account CHANGE COLUMN exposeDate exposeDate DATE COMMENT 'Дата выставления' NULL;

ALTER TABLE Account CHANGE COLUMN payedAmount payedAmount DOUBLE COMMENT 'Количество оплаченных услуг' NOT NULL;

ALTER TABLE Account CHANGE COLUMN payedSum payedSum DOUBLE COMMENT 'Сумма оплаченных услуг' NOT NULL;

ALTER TABLE Account CHANGE COLUMN refusedAmount refusedAmount DOUBLE COMMENT 'Количество отказанных услуг' NOT NULL;

ALTER TABLE Account CHANGE COLUMN refusedSum refusedSum DOUBLE COMMENT 'Сумма отказанных услуг' NOT NULL;

ALTER TABLE Account CHANGE COLUMN format_id format_id INTEGER COMMENT 'Формат счета {rbAccountExportFormat' NULL;

ALTER TABLE Action CHANGE COLUMN finance_id finance_id INTEGER COMMENT 'тип финансирования {rbFinance}' NULL;

ALTER TABLE Action CHANGE COLUMN prescription_id prescription_id INTEGER COMMENT 'Ссылка на назначение {Action}' NULL;

ALTER TABLE Action CHANGE COLUMN contract_id contract_id INTEGER COMMENT 'договор {Contract}' NULL;

ALTER TABLE Action CHANGE COLUMN coordDate coordDate DATETIME COMMENT 'Дата и время согласования' NULL;

ALTER TABLE Action CHANGE COLUMN coordAgent coordAgent VARCHAR(128) COMMENT 'Сотрудник ЛПУ, согласовавший действие' NOT NULL;

ALTER TABLE Action CHANGE COLUMN coordInspector coordInspector VARCHAR(128) COMMENT 'Представитель плательщика (сотрудник СМО), согласовавший действие' NOT NULL;

ALTER TABLE Action CHANGE COLUMN coordText coordText TINYTEXT COMMENT 'Текст согласования' NOT NULL;

ALTER TABLE ActionPropertyType CHANGE COLUMN defaultEvaluation defaultEvaluation TINYINT(1) DEFAULT 0 COMMENT '0-не определять, 1-автомат, 2-полуавтомат, 3-ручное' NOT NULL;

ALTER TABLE ActionProperty_ImageMap CHANGE COLUMN value value MEDIUMTEXT COMMENT 'код картинки и отметки в xml' NULL;

ALTER TABLE ActionProperty_ImageMap COMMENT = 'Маркировка изображения';

ALTER TABLE ActionProperty_Person COMMENT = 'Значение свойства действия типа';

ALTER TABLE ActionProperty_rbFinance CHANGE COLUMN value value INTEGER COMMENT 'собственно значение {rbFinance}' NULL;

ALTER TABLE ActionProperty_rbFinance COMMENT = 'Значение свойства действия';

ALTER TABLE ActionType CHANGE COLUMN age_bu age_bu TINYINT(1) UNSIGNED COMMENT 'Единица измерения нижней границы дипазона возраста (0 - не задано, 1 - день, 2 - неделя,3 - месяц,4 - год)' NULL;

ALTER TABLE ActionType CHANGE COLUMN age_eu age_eu TINYINT(1) UNSIGNED COMMENT 'Единица измерения верхней границы дипазона возраста (0 - не задано, 1 - день, 2 - неделя, 3 - месяц,4 - год)' NULL;

ALTER TABLE ActionType CHANGE COLUMN defaultDirectionDate defaultDirectionDate TINYINT DEFAULT 0 COMMENT 'Код значение по умолчанию для даты назначения действияия: 0-Не задано, 1-По дате начала события, 2-Текущая дата, 3-Синхронизация по дате выполн' NOT NULL;

ALTER TABLE ActionType CHANGE COLUMN defaultPlannedEndDate defaultPlannedEndDate TINYINT(1) COMMENT 'Планируемя дата выполнения (0=не определено, 1=След. день, 2=След. рабочий день)' NOT NULL;

ALTER TABLE ActionType CHANGE COLUMN defaultPersonInEvent defaultPersonInEvent TINYINT DEFAULT 0 COMMENT 'исполнитель в редакторе события: 0-Не определено, 1-Не заполняется, 2-Назначивший действие, 3-Ответственный за событие, 4-Пользователь' NOT NULL;

ALTER TABLE ActionType CHANGE COLUMN defaultPersonInEditor defaultPersonInEditor TINYINT DEFAULT 0 COMMENT 'исполнитель в отдельном редакторе: 0-Не определено, 1-Не заполняется, 2-Назначивший действие, 3-Ответственный за событие, 4-Пользователь' NOT NULL;

ALTER TABLE ActionType CHANGE COLUMN prescribedType_id prescribedType_id INTEGER COMMENT 'Предписываемое действие {ActionType}' NULL;

ALTER TABLE ActionType CHANGE COLUMN shedule_id shedule_id INTEGER COMMENT 'График по умолчанию {rbActionShedule}' NULL;

ALTER TABLE ActionType CHANGE COLUMN isRequiredCoordination isRequiredCoordination TINYINT(1) DEFAULT 0 COMMENT 'Требуется обязательное согласование' NOT NULL;

ALTER TABLE ActionType_QuotaType CHANGE COLUMN master_id master_id INTEGER COMMENT 'тип действия {ActionType}' NOT NULL;

ALTER TABLE ActionType_QuotaType CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'индекс для сортировки при показе таблицы' NOT NULL;

ALTER TABLE ActionType_QuotaType CHANGE COLUMN quotaClass quotaClass TINYINT(1) COMMENT 'класс вида квоты' NULL;

ALTER TABLE ActionType_QuotaType CHANGE COLUMN finance_id finance_id INTEGER COMMENT 'фип финансирования {rbFinance}' NULL;

ALTER TABLE ActionType_QuotaType CHANGE COLUMN quotaType_id quotaType_id INTEGER COMMENT 'вид квоты {QuotaType}' NULL;

ALTER TABLE ActionType_QuotaType COMMENT = 'Вид квотирования';

ALTER TABLE ActionType_TissueType CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'индекс для сортировки при показе таблицы' NOT NULL;

ALTER TABLE ActionType_TissueType CHANGE COLUMN amount amount INTEGER DEFAULT 0 COMMENT 'количество' NOT NULL;

ALTER TABLE ActionType_TissueType COMMENT = 'Заборы ткани применяемые в типах';

ALTER TABLE AppLock CHANGE COLUMN lockTime lockTime TIMESTAMP DEFAULT '0000-00-00 00:00:00' COMMENT 'время блокировки' NOT NULL;

ALTER TABLE AppLock CHANGE COLUMN retTime retTime TIMESTAMP DEFAULT '0000-00-00 00:00:00' COMMENT 'время последнего продления блокировки' NOT NULL;

ALTER TABLE AppLock CHANGE COLUMN addr addr VARCHAR(255) COMMENT 'имя, ip и пр. описание заблокировавшего' NOT NULL;

ALTER TABLE AppLock COMMENT = 'Прикладные блокировки';

ALTER TABLE AppLock_Detail CHANGE COLUMN tableName tableName VARCHAR(64) COMMENT 'Имя таблицы' NOT NULL;

ALTER TABLE AppLock_Detail CHANGE COLUMN recordId recordId INTEGER COMMENT 'id блокируемой записи' NOT NULL;

ALTER TABLE AppLock_Detail CHANGE COLUMN recordIndex recordIndex INTEGER DEFAULT 0 COMMENT 'Индекс для свойства' NOT NULL;

ALTER TABLE AppLock_Detail COMMENT = 'Подробности блокировки';

ALTER TABLE BlankActions CHANGE COLUMN code code VARCHAR(16) COMMENT 'Код' NOT NULL;

ALTER TABLE BlankActions CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE BlankActions CHANGE COLUMN checkingSerial checkingSerial TINYINT COMMENT 'Контроль серии 0-нет, 1-мягко, 2-жестко' NOT NULL;

ALTER TABLE BlankActions CHANGE COLUMN checkingNumber checkingNumber TINYINT COMMENT 'Контроль номера 0-нет, 1-мягко, 2-жестко' NOT NULL;

ALTER TABLE BlankActions CHANGE COLUMN checkingAmount checkingAmount TINYINT COMMENT 'Контроль количества 0-нет, 1-списание' NOT NULL;

ALTER TABLE BlankActions COMMENT = 'Бланки на основе Action';

ALTER TABLE BlankTempInvalids CHANGE COLUMN code code VARCHAR(16) COMMENT 'Код' NOT NULL;

ALTER TABLE BlankTempInvalids CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE BlankTempInvalids CHANGE COLUMN checkingSerial checkingSerial TINYINT COMMENT 'Контроль серии 0-нет, 1-мягко, 2-жестко' NOT NULL;

ALTER TABLE BlankTempInvalids CHANGE COLUMN checkingNumber checkingNumber TINYINT COMMENT 'Контроль номера 0-нет, 1-мягко, 2-жестко' NOT NULL;

ALTER TABLE BlankTempInvalids CHANGE COLUMN checkingAmount checkingAmount TINYINT COMMENT 'Контроль количества 0-нет, 1-списание' NOT NULL;

ALTER TABLE BlankTempInvalids COMMENT = 'Бланки для ВУТ';

ALTER TABLE Client CHANGE COLUMN growth growth VARCHAR(16) COMMENT 'Рост при рождении' NOT NULL;

ALTER TABLE Client CHANGE COLUMN weight weight VARCHAR(16) COMMENT 'Вес при рождении' NOT NULL;

ALTER TABLE ClientPolicy CHANGE COLUMN name name VARCHAR(64) COMMENT 'Название' NOT NULL;

ALTER TABLE ClientPolicy CHANGE COLUMN note note VARCHAR(200) COMMENT 'Примечание' NOT NULL;

ALTER TABLE Client_Quoting CHANGE COLUMN statment statment VARCHAR(255) COMMENT 'Показания' NULL;

ALTER TABLE Client_Quoting COMMENT = 'Квоты клиентов';

ALTER TABLE Client_QuotingDiscussion CHANGE COLUMN responsiblePerson_id responsiblePerson_id INTEGER COMMENT 'Ответственный ЛПУ {Person}' NULL;

ALTER TABLE Client_QuotingDiscussion CHANGE COLUMN cosignatory cosignatory VARCHAR(25) COMMENT 'Название контрагента' NULL;

ALTER TABLE Client_QuotingDiscussion CHANGE COLUMN cosignatoryPost cosignatoryPost VARCHAR(20) COMMENT 'Должность' NULL;

ALTER TABLE Client_QuotingDiscussion CHANGE COLUMN cosignatoryName cosignatoryName VARCHAR(50) COMMENT 'Имя' NULL;

ALTER TABLE Client_QuotingDiscussion CHANGE COLUMN remark remark VARCHAR(128) COMMENT 'Примечание' NULL;

ALTER TABLE Client_QuotingDiscussion COMMENT = 'Переговоры по квоте';

ALTER TABLE Contract CHANGE COLUMN exposeDiscipline exposeDiscipline TINYINT(1) DEFAULT 0 COMMENT 'Дисциплина формирования счёта (0-Один по всем оказанным услугам, 1-На каждый месяц отдельно, 2-На каждое событие отдельно)' NOT NULL;

ALTER TABLE Contract CHANGE COLUMN priceList_id priceList_id INTEGER COMMENT 'Прайс-лист {Contract}' NULL;

ALTER TABLE Contract CHANGE COLUMN coefficient coefficient DOUBLE DEFAULT 0 COMMENT 'Коэффициент для расчета тарифов' NOT NULL;

ALTER TABLE Contract CHANGE COLUMN coefficientEx coefficientEx DOUBLE DEFAULT 0 COMMENT 'Коэффициент расчета тарифа для превышенного количества' NOT NULL;

ALTER TABLE Contract_Tariff CHANGE COLUMN tariffCategory_id tariffCategory_id INTEGER COMMENT 'Тарифная категория сотрудника {rbTariffCategory}' NULL;

ALTER TABLE EventType CHANGE COLUMN scene_id scene_id INTEGER COMMENT 'Место визита по умолчанию {rbScene}' NULL;

ALTER TABLE EventType CHANGE COLUMN visitServiceModifier visitServiceModifier VARCHAR(128) COMMENT 'Модификатор сервиса; пусто - нет изменения, "-" - удаляет сервис, "+XXX"-меняет сервис на XXХ, "~/s/r/"-замена по рег.выражению, x - меняет первую букву в' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN visitFinance visitFinance TINYINT(1) DEFAULT 0 COMMENT '0-по событию, 1-финансирование визита определяется по врачу визита' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN actionFinance actionFinance TINYINT(1) DEFAULT 0 COMMENT '0-по событию, 1-по назначившему, 2-по исполнителю' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN canHavePayableActions canHavePayableActions TINYINT(1) DEFAULT 0 COMMENT 'Признак: может иметь платные услуги' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN isRequiredCoordination isRequiredCoordination TINYINT(1) DEFAULT 0 COMMENT 'Требуется обязательное согласование' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN isOrgStructurePriority isOrgStructurePriority TINYINT(1) DEFAULT 0 COMMENT 'Приоритет подразделения для функции "Добавить ..." в событии' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN isTakenTissue isTakenTissue TINYINT(1) DEFAULT 0 COMMENT '0-не использует забор тканей, 1-использует забор тканей' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN sex sex TINYINT DEFAULT 0 COMMENT 'Применимо для указанного пола (0-любой, 1-М, 2-Ж)' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN age age VARCHAR(9) COMMENT 'Применимо для указанного интервала возрастов пусто-нет ограничения, "{NNN{д|н|м|г}-{MMM{д|н|м|г}}" - с NNN дней/недель/месяцев/лет по MMM дней/недель/месяцев/лет' NOT NULL;

ALTER TABLE EventType CHANGE COLUMN age_bu age_bu TINYINT UNSIGNED COMMENT 'Единица измерения нижней границы дипазона возраста (0 - не задано,1 - день, 2 - неделя, 3 - месяц, 4 - год)' NULL;

ALTER TABLE EventType CHANGE COLUMN age_eu age_eu TINYINT UNSIGNED COMMENT 'Единица измерения верхней границы дипазона возраста (0 - не задано, 1 - день, 2 - неделя, 3 - месяц, 4 - год)' NULL;

ALTER TABLE EventType_Action CHANGE COLUMN age_bu age_bu TINYINT(1) UNSIGNED COMMENT 'Единица измерения нижней границы дипазона возраста (0 - не задано, 1 - день, 2 - неделя, 3 - месяц, 4 - год)' NULL;

ALTER TABLE EventType_Action CHANGE COLUMN age_eu age_eu TINYINT(1) UNSIGNED COMMENT 'Единица измерения верхней границы дипазона возраста (0 - не задано, 1 - день, 2 - неделя, 3 - месяц, 4 - год)' NULL;

ALTER TABLE EventType_Action CHANGE COLUMN payable payable TINYINT(1) DEFAULT 0 COMMENT '0-финансирование по событию, 1-финансирование по событию или за нал.расчёт, 2-только нал.расчёт' NOT NULL;

ALTER TABLE Event_Feed CHANGE COLUMN createDatetime createDatetime DATETIME COMMENT 'Дата создания записи' NOT NULL;

ALTER TABLE Event_Feed CHANGE COLUMN createPerson_id createPerson_id INTEGER COMMENT 'Автор записи {Person}' NULL;

ALTER TABLE Event_Feed CHANGE COLUMN modifyDatetime modifyDatetime DATETIME COMMENT 'Дата изменения записи' NOT NULL;

ALTER TABLE Event_Feed CHANGE COLUMN modifyPerson_id modifyPerson_id INTEGER COMMENT 'Автор изменения записи {Person}' NULL;

ALTER TABLE Event_Feed CHANGE COLUMN deleted deleted TINYINT(1) DEFAULT 0 COMMENT 'Отметка удаления записи' NOT NULL;

ALTER TABLE Event_Feed CHANGE COLUMN date date DATETIME COMMENT 'дата питания' NOT NULL;

ALTER TABLE Event_Feed COMMENT = 'Питание';

ALTER TABLE Event_LocalContract CHANGE COLUMN coordDate coordDate DATETIME COMMENT 'Дата и время согласования' NULL;

ALTER TABLE Event_LocalContract CHANGE COLUMN coordAgent coordAgent VARCHAR(128) COMMENT 'Сотрудник ЛПУ, согласовавший действие' NOT NULL;

ALTER TABLE Event_LocalContract CHANGE COLUMN coordInspector coordInspector VARCHAR(128) COMMENT 'Представитель плательщика (сотрудник СМО), согласовавший действие' NOT NULL;

ALTER TABLE Event_LocalContract CHANGE COLUMN coordText coordText TINYTEXT COMMENT 'Текст согласования' NOT NULL;

ALTER TABLE Event_LocalContract CHANGE COLUMN org_id org_id INTEGER COMMENT 'Контрагент-организация {Organisation}' NULL;

ALTER TABLE Event_Payment CHANGE COLUMN cashBox cashBox VARCHAR(32) COMMENT 'идентификатор кассового аппарата' NOT NULL;

ALTER TABLE OrgStructure CHANGE COLUMN hasStocks hasStocks TINYINT(1) DEFAULT 0 COMMENT 'Подразделение имеет склад' NOT NULL;

ALTER TABLE OrgStructure CHANGE COLUMN inheritEventTypes inheritEventTypes TINYINT(1) DEFAULT 0 COMMENT 'Наследует типы события' NOT NULL;

ALTER TABLE OrgStructure CHANGE COLUMN inheritActionTypes inheritActionTypes TINYINT(1) DEFAULT 0 COMMENT 'Наследует типы действий' NOT NULL;

ALTER TABLE OrgStructure CHANGE COLUMN inheritGaps inheritGaps TINYINT(1) DEFAULT 0 COMMENT 'Наследует перерывы' NOT NULL;

ALTER TABLE OrgStructure_ActionType CHANGE COLUMN master_id master_id INTEGER COMMENT 'Подразделение {OrgStructure}' NOT NULL;

ALTER TABLE OrgStructure_ActionType CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'Индекс в списке событий (для сортировки в списке)' NOT NULL;

ALTER TABLE OrgStructure_ActionType CHANGE COLUMN actionType_id actionType_id INTEGER COMMENT 'Тип действия {ActionType}' NULL;

ALTER TABLE OrgStructure_ActionType COMMENT = 'Привязка типов действий к подразделению';

ALTER TABLE OrgStructure_DisabledAttendance CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'Индекс в списке событий (для сортировки в списке)' NOT NULL;

ALTER TABLE OrgStructure_DisabledAttendance CHANGE COLUMN disabledType disabledType TINYINT(1) DEFAULT 0 COMMENT 'Способ ограничения:0-мягко,1-строго,2-запрет' NOT NULL;

ALTER TABLE OrgStructure_DisabledAttendance COMMENT = 'Запрет обслуживания';

ALTER TABLE OrgStructure_EventType CHANGE COLUMN master_id master_id INTEGER COMMENT 'Подразделение {OrgStructure}' NOT NULL;

ALTER TABLE OrgStructure_EventType CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'Индекс в списке событий (для сортировки в списке)' NOT NULL;

ALTER TABLE OrgStructure_EventType CHANGE COLUMN eventType_id eventType_id INTEGER COMMENT 'Тип события {EventType}' NULL;

ALTER TABLE OrgStructure_EventType COMMENT = 'Привязка типов событий к подразделению';

ALTER TABLE OrgStructure_Stock CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE OrgStructure_Stock CHANGE COLUMN constrainedQnt constrainedQnt DOUBLE DEFAULT 0 COMMENT 'Гантированный запас - количество, ниже которого запас не должен снижаться' NOT NULL;

ALTER TABLE OrgStructure_Stock CHANGE COLUMN orderQnt orderQnt DOUBLE DEFAULT 0 COMMENT 'Точка заказа - количество, которое желательно поддерживать' NOT NULL;

ALTER TABLE OrgStructure_Stock COMMENT = 'Планируемые запасы ЛСиИМН на складе';

ALTER TABLE Organisation CHANGE COLUMN infisCode infisCode VARCHAR(12) COMMENT 'код по ИНФИС (тер.фонд)' NOT NULL;

ALTER TABLE Organisation CHANGE COLUMN compulsoryServiceStop compulsoryServiceStop TINYINT(1) DEFAULT 0 COMMENT 'ОМС: 0-обслуживается, 1-приостановлено обслуживание' NOT NULL;

ALTER TABLE Organisation CHANGE COLUMN voluntaryServiceStop voluntaryServiceStop TINYINT(1) DEFAULT 0 COMMENT 'ДМС: 0-обслуживается, 1-приостановлено обслуживание' NOT NULL;

ALTER TABLE Person CHANGE COLUMN office2 office2 VARCHAR(8) COMMENT 'Кабинет2' NOT NULL;

ALTER TABLE Person CHANGE COLUMN tariffCategory_id tariffCategory_id INTEGER COMMENT 'Тарифная категория {rbTariffCategory}' NULL;

ALTER TABLE Person CHANGE COLUMN ambPlan2 ambPlan2 SMALLINT COMMENT 'Количество человек на весь амбулаторный приём' NOT NULL;

ALTER TABLE Person CHANGE COLUMN homPlan2 homPlan2 SMALLINT COMMENT 'Количество человек на вызов' NOT NULL;

ALTER TABLE Person CHANGE COLUMN lastAccessibleTimelineDate lastAccessibleTimelineDate DATE COMMENT 'Последняя доступная дата в расписании врача' NULL;

ALTER TABLE Person CHANGE COLUMN timelineAccessibleDays timelineAccessibleDays INTEGER DEFAULT 0 COMMENT 'Количество дней, на которые доступно расписание врача' NOT NULL;

ALTER TABLE Person CHANGE COLUMN typeTimeLinePerson typeTimeLinePerson INTEGER COMMENT 'Тип персонального графика' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN createDatetime createDatetime DATETIME COMMENT 'Дата создания записи' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN modifyDatetime modifyDatetime DATETIME COMMENT 'Дата изменения записи' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN deleted deleted TINYINT(1) DEFAULT 0 COMMENT 'Отметка удаления записи' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN ambBegTime ambBegTime TIME COMMENT 'начало амбулаторного приёма' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN ambEndTime ambEndTime TIME COMMENT 'конец амбулаторного приёма' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN ambPlan ambPlan SMALLINT COMMENT 'Количество человек на амбулаторный приём' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN office office VARCHAR(8) COMMENT 'Кабинет' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN ambBegTime2 ambBegTime2 TIME COMMENT 'начало второго амбулаторного приёма' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN ambEndTime2 ambEndTime2 TIME COMMENT 'конец второго амбулаторного приёма' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN ambPlan2 ambPlan2 SMALLINT COMMENT 'Количество человек на второй амбулаторный приём' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN office2 office2 VARCHAR(8) COMMENT 'Кабинет2' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN homBegTime homBegTime TIME COMMENT 'начало вызова' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN homEndTime homEndTime TIME COMMENT 'конец вызова' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN homPlan homPlan SMALLINT COMMENT 'Количество человек на вызов' NOT NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN homBegTime2 homBegTime2 TIME COMMENT 'начало второго вызова' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN homEndTime2 homEndTime2 TIME COMMENT 'конец второго вызова' NULL;

ALTER TABLE PersonTimeTemplate CHANGE COLUMN homPlan2 homPlan2 SMALLINT COMMENT 'Количество человек на повторный вызов' NOT NULL;

ALTER TABLE PersonTimeTemplate COMMENT = 'Персональный график';

ALTER TABLE Person_Activity CHANGE COLUMN master_id master_id INTEGER COMMENT 'сотрудник{Person}' NOT NULL;

ALTER TABLE Person_Activity CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'индекс для сортировки при показе таблицы' NOT NULL;

ALTER TABLE Person_Activity CHANGE COLUMN activity_id activity_id INTEGER COMMENT 'вид деятельности{rbActivity}' NULL;

ALTER TABLE Person_Activity COMMENT = 'Обзор: Виды деятельности сотрудника';

ALTER TABLE Person_TimeTemplate CHANGE COLUMN createDatetime createDatetime DATETIME COMMENT 'Дата создания записи' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN modifyDatetime modifyDatetime DATETIME COMMENT 'Дата изменения записи' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN deleted deleted TINYINT(1) DEFAULT 0 COMMENT 'Отметка удаления записи' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN ambBegTime ambBegTime TIME COMMENT 'начало амбулаторного приёма' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN ambEndTime ambEndTime TIME COMMENT 'конец амбулаторного приёма' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN ambPlan ambPlan SMALLINT COMMENT 'Количество человек на амбулаторный приём' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN office office VARCHAR(8) COMMENT 'Кабинет' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN ambBegTime2 ambBegTime2 TIME COMMENT 'начало второго амбулаторного приёма' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN ambEndTime2 ambEndTime2 TIME COMMENT 'конец второго амбулаторного приёма' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN ambPlan2 ambPlan2 SMALLINT COMMENT 'Количество человек на второй амбулаторный приём' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN office2 office2 VARCHAR(8) COMMENT 'Кабинет2' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN homBegTime homBegTime TIME COMMENT 'начало вызова' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN homEndTime homEndTime TIME COMMENT 'конец вызова' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN homPlan homPlan SMALLINT COMMENT 'Количество человек на вызов' NOT NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN homBegTime2 homBegTime2 TIME COMMENT 'начало второго вызова' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN homEndTime2 homEndTime2 TIME COMMENT 'конец второго вызова' NULL;

ALTER TABLE Person_TimeTemplate CHANGE COLUMN homPlan2 homPlan2 SMALLINT COMMENT 'Количество человек на повторный вызов' NOT NULL;

ALTER TABLE Person_TimeTemplate COMMENT = 'Персональный график';

ALTER TABLE Quoting COMMENT = 'Квотирование';

ALTER TABLE Quoting_Region CHANGE COLUMN master_id master_id INTEGER COMMENT 'Идентификатор квотирования {Quoting}' NULL;

ALTER TABLE Quoting_Region CHANGE COLUMN confirmed confirmed INTEGER DEFAULT 0 COMMENT 'Подтверждено' NOT NULL;

ALTER TABLE Quoting_Region COMMENT = 'Ограничение квотирования';

ALTER TABLE StockMotion CHANGE COLUMN createDatetime createDatetime DATETIME COMMENT 'Дата создания записи' NOT NULL;

ALTER TABLE StockMotion CHANGE COLUMN modifyDatetime modifyDatetime DATETIME COMMENT 'Дата изменения записи' NOT NULL;

ALTER TABLE StockMotion CHANGE COLUMN deleted deleted TINYINT(1) COMMENT 'Отметка удаления записи' NOT NULL;

ALTER TABLE StockMotion CHANGE COLUMN type type INTEGER DEFAULT 0 COMMENT '0-Накладная, 1-Инвентаризация, 2-финансовая переброска, 3-Производство' NULL;

ALTER TABLE StockMotion CHANGE COLUMN date date DATETIME DEFAULT '0000-00-00 00:00:00' COMMENT 'Дата и время перемещения' NOT NULL;

ALTER TABLE StockMotion CHANGE COLUMN note note TINYTEXT COMMENT 'Примечания' NOT NULL;

ALTER TABLE StockMotion COMMENT = 'Движение ЛСиИМН';

ALTER TABLE StockMotion_Item CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE StockMotion_Item CHANGE COLUMN qnt qnt DOUBLE DEFAULT 0 COMMENT 'Количество' NOT NULL;

ALTER TABLE StockMotion_Item CHANGE COLUMN sum sum DOUBLE DEFAULT 0 COMMENT 'Сумма' NOT NULL;

ALTER TABLE StockMotion_Item CHANGE COLUMN oldQnt oldQnt DOUBLE DEFAULT 0 COMMENT 'Старое количество (в инвентаризации)' NOT NULL;

ALTER TABLE StockMotion_Item CHANGE COLUMN oldSum oldSum DOUBLE DEFAULT 0 COMMENT 'Старая сумма (в инвентаризации)' NOT NULL;

ALTER TABLE StockMotion_Item CHANGE COLUMN isOut isOut INTEGER DEFAULT 0 COMMENT '0: затрата, 1:получение (в производстве)' NOT NULL;

ALTER TABLE StockMotion_Item CHANGE COLUMN note note TINYTEXT COMMENT 'Примечания' NOT NULL;

ALTER TABLE StockMotion_Item COMMENT = 'Э­лемент движения ЛСиИМН';

ALTER TABLE StockRecipe CHANGE COLUMN createDatetime createDatetime DATETIME COMMENT 'Дата создания записи' NOT NULL;

ALTER TABLE StockRecipe CHANGE COLUMN modifyDatetime modifyDatetime DATETIME COMMENT 'Дата изменения записи' NOT NULL;

ALTER TABLE StockRecipe CHANGE COLUMN deleted deleted TINYINT(1) COMMENT 'Отметка удаления записи' NOT NULL;

ALTER TABLE StockRecipe CHANGE COLUMN code code VARCHAR(32) COMMENT 'Код' NOT NULL;

ALTER TABLE StockRecipe CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE StockRecipe COMMENT = 'Рецепт для производства ЛСиИМН';

ALTER TABLE StockRecipe_Item CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE StockRecipe_Item CHANGE COLUMN qnt qnt DOUBLE DEFAULT 0 COMMENT 'Количество' NOT NULL;

ALTER TABLE StockRecipe_Item CHANGE COLUMN isOut isOut INTEGER DEFAULT 0 COMMENT '0: затрата, 1: производство' NOT NULL;

ALTER TABLE StockRecipe_Item COMMENT = 'Элемент рецепта для производства';

ALTER TABLE StockRequisition CHANGE COLUMN createDatetime createDatetime DATETIME DEFAULT '0000-00-00 00:00:00' COMMENT 'Дата создания записи' NOT NULL;

ALTER TABLE StockRequisition CHANGE COLUMN modifyDatetime modifyDatetime DATETIME DEFAULT '0000-00-00 00:00:00' COMMENT 'Дата изменения записи' NOT NULL;

ALTER TABLE StockRequisition CHANGE COLUMN deleted deleted TINYINT(1) DEFAULT 0 COMMENT 'Отметка удаления записи' NOT NULL;

ALTER TABLE StockRequisition CHANGE COLUMN date date DATE DEFAULT '0000-00-00' COMMENT 'дата требования' NOT NULL;

ALTER TABLE StockRequisition CHANGE COLUMN deadline deadline DATETIME COMMENT 'срок требования' NULL;

ALTER TABLE StockRequisition CHANGE COLUMN revoked revoked TINYINT(1) DEFAULT 0 COMMENT 'признак отказа от требования' NOT NULL;

ALTER TABLE StockRequisition CHANGE COLUMN note note TINYTEXT COMMENT 'примечание' NOT NULL;

ALTER TABLE StockRequisition COMMENT = 'Требование на поставку ЛСиИМН';

ALTER TABLE StockRequisition_Item CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'Последовательный номер для сортировки' NOT NULL;

ALTER TABLE StockRequisition_Item CHANGE COLUMN qnt qnt DOUBLE DEFAULT 0 COMMENT 'Запрашиваемое количество' NOT NULL;

ALTER TABLE StockRequisition_Item CHANGE COLUMN satisfiedQnt satisfiedQnt DOUBLE DEFAULT 0 COMMENT 'Удовлетворённое количество' NOT NULL;

ALTER TABLE StockRequisition_Item COMMENT = 'Позиция требования на поставку';

ALTER TABLE StockTrans CHANGE COLUMN date date DATETIME DEFAULT '0000-00-00 00:00:00' COMMENT 'Дата и время проводки' NOT NULL;

ALTER TABLE StockTrans CHANGE COLUMN qnt qnt DOUBLE DEFAULT 0 COMMENT 'Количество' NOT NULL;

ALTER TABLE StockTrans CHANGE COLUMN sum sum DOUBLE DEFAULT 0 COMMENT 'Сумма' NOT NULL;

ALTER TABLE StockTrans COMMENT = 'Фантазия на тему бух. проводки';

ALTER TABLE TakenTissueJournal CHANGE COLUMN externalId externalId VARCHAR(30) COMMENT 'Внешний идентификатор' NOT NULL;

ALTER TABLE TakenTissueJournal CHANGE COLUMN amount amount INTEGER DEFAULT 0 COMMENT 'Количество' NOT NULL;

ALTER TABLE TakenTissueJournal CHANGE COLUMN datetimeTaken datetimeTaken DATETIME COMMENT 'Дата и время забора' NOT NULL;

ALTER TABLE TakenTissueJournal CHANGE COLUMN note note VARCHAR(128) COMMENT 'Примечания' NOT NULL;

ALTER TABLE TakenTissueJournal COMMENT = 'Журнал забора тканей';

ALTER TABLE TempInvalid CHANGE COLUMN duration duration INTEGER COMMENT 'Продолжительность в днях' NOT NULL;

ALTER TABLE rbActionShedule CHANGE COLUMN code code VARCHAR(16) COMMENT 'Код' NOT NULL;

ALTER TABLE rbActionShedule CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbActionShedule CHANGE COLUMN period period TINYINT DEFAULT 1 COMMENT 'Период; ежедневно = 1' NOT NULL;

ALTER TABLE rbActionShedule COMMENT = 'График выполнения действия';

ALTER TABLE rbActionShedule_Item CHANGE COLUMN master_id master_id INTEGER COMMENT 'Ссылка на график {rbActionShedule}' NOT NULL;

ALTER TABLE rbActionShedule_Item CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE rbActionShedule_Item CHANGE COLUMN offset offset TINYINT DEFAULT 0 COMMENT 'Смещение в сутках от начала выполнения; 0-первый день, 1-второй и т.п.' NOT NULL;

ALTER TABLE rbActionShedule_Item CHANGE COLUMN time time TIME DEFAULT '00:00:00' COMMENT 'Время выполнения' NOT NULL;

ALTER TABLE rbActionShedule_Item COMMENT = 'Э­лемент графика выполнения действия';

ALTER TABLE rbActivity CHANGE COLUMN code code VARCHAR(8) COMMENT 'код' NOT NULL;

ALTER TABLE rbActivity CHANGE COLUMN name name VARCHAR(64) COMMENT 'название' NOT NULL;

ALTER TABLE rbActivity CHANGE COLUMN regionalCode regionalCode VARCHAR(8) COMMENT 'региональный код' NOT NULL;

ALTER TABLE rbActivity COMMENT = 'Виды(типы) деятельности врача';

ALTER TABLE rbAgreementType CHANGE COLUMN code code VARCHAR(32) COMMENT 'Код типа согласования' NOT NULL;

ALTER TABLE rbAgreementType CHANGE COLUMN name name VARCHAR(64) COMMENT 'Название типа согласования' NOT NULL;

ALTER TABLE rbAgreementType CHANGE COLUMN quotaStatusModifier quotaStatusModifier INTEGER DEFAULT 0 COMMENT 'Модификатор статуса квоты 0-Не меняет, 1-Отменено, 2-Ожидание, 3-Активный талон, 4-Талон для заполнения, 5-Заблокированный талон, 6-Отказано,7-Не' NULL;

ALTER TABLE rbAgreementType COMMENT = 'Типы согласования';

ALTER TABLE rbCounter CHANGE COLUMN code code VARCHAR(8) COMMENT 'Код' NOT NULL;

ALTER TABLE rbCounter CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbCounter CHANGE COLUMN value value INTEGER DEFAULT 0 COMMENT 'Текущее значение счетчика' NOT NULL;

ALTER TABLE rbCounter CHANGE COLUMN prefix prefix VARCHAR(32) COMMENT 'Префикс' NULL;

ALTER TABLE rbCounter CHANGE COLUMN reset reset INTEGER DEFAULT 0 COMMENT '0-Не сбрасывается, 1-Через сутки,2-Через неделю,3-через месяц,4-через квартал, 5-через полугодие, 6-через год' NOT NULL;

ALTER TABLE rbCounter CHANGE COLUMN startDate startDate DATETIME COMMENT 'Дата начала работы счетчика' NOT NULL;

ALTER TABLE rbCounter CHANGE COLUMN resetDate resetDate DATETIME COMMENT 'Дата последнего сброса' NULL;

ALTER TABLE rbCounter CHANGE COLUMN sequenceFlag sequenceFlag TINYINT(1) DEFAULT 0 COMMENT 'Флаг последовательности' NOT NULL;

ALTER TABLE rbCounter COMMENT = 'Счетчики';

ALTER TABLE rbDiet CHANGE COLUMN code code VARCHAR(8) COMMENT 'Код' NOT NULL;

ALTER TABLE rbDiet CHANGE COLUMN name name VARCHAR(64) COMMENT 'название' NOT NULL;

ALTER TABLE rbDiet COMMENT = 'Справочник Столы питания';

ALTER TABLE rbImageMap CHANGE COLUMN code code VARCHAR(8) COMMENT 'код картинки' NOT NULL;

ALTER TABLE rbImageMap CHANGE COLUMN image image MEDIUMBLOB COMMENT 'Картинка в QByteArray' NOT NULL;

ALTER TABLE rbImageMap CHANGE COLUMN markSize markSize INTEGER COMMENT 'Размер наносимого маркера' NULL;

ALTER TABLE rbImageMap COMMENT = 'Библиотека изображений';

ALTER TABLE rbMealTime CHANGE COLUMN code code VARCHAR(8) COMMENT 'Код' NOT NULL;

ALTER TABLE rbMealTime CHANGE COLUMN name name VARCHAR(64) COMMENT 'название' NOT NULL;

ALTER TABLE rbMealTime CHANGE COLUMN begTime begTime TIME COMMENT 'начало периода' NOT NULL;

ALTER TABLE rbMealTime CHANGE COLUMN endTime endTime TIME COMMENT 'конец периода' NOT NULL;

ALTER TABLE rbMealTime COMMENT = 'Справочник Периоды питания';

ALTER TABLE rbMedicalAidProfile CHANGE COLUMN code code VARCHAR(16) COMMENT 'Код' NOT NULL;

ALTER TABLE rbMedicalAidProfile CHANGE COLUMN regionalCode regionalCode VARCHAR(16) COMMENT 'Региональный код' NOT NULL;

ALTER TABLE rbMedicalAidProfile CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbMedicalAidProfile COMMENT = 'Профили мед.помощи';

ALTER TABLE rbMenu CHANGE COLUMN code code VARCHAR(8) COMMENT 'Код' NOT NULL;

ALTER TABLE rbMenu CHANGE COLUMN name name VARCHAR(64) COMMENT 'Название' NOT NULL;

ALTER TABLE rbMenu COMMENT = 'Справочник Шаблон питания';

ALTER TABLE rbMesSpecification CHANGE COLUMN code code VARCHAR(16) COMMENT 'Код' NOT NULL;

ALTER TABLE rbMesSpecification CHANGE COLUMN regionalCode regionalCode VARCHAR(16) COMMENT 'Региональный код' NOT NULL;

ALTER TABLE rbMesSpecification CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbMesSpecification COMMENT = 'Особенность выполнения МИС';

ALTER TABLE rbNomenclature CHANGE COLUMN code code VARCHAR(64) COMMENT 'Код' NOT NULL;

ALTER TABLE rbNomenclature CHANGE COLUMN regionalCode regionalCode VARCHAR(64) COMMENT 'Региональный код' NOT NULL;

ALTER TABLE rbNomenclature CHANGE COLUMN name name VARCHAR(128) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbNomenclature COMMENT = 'Номенклатура лекарственных сред';

ALTER TABLE rbPrintTemplate CHANGE COLUMN dpdAgreement dpdAgreement TINYINT(1) DEFAULT 0 COMMENT 'Меняет ли ДПД клиента при печати: 0-Не меняет, 1-Меняет на "Да", 2-Меняет на "Нет"' NOT NULL;

ALTER TABLE rbScene CHANGE COLUMN serviceModifier serviceModifier VARCHAR(128) COMMENT 'Модификатор сервиса; пусто - нет изменения, "-" - удаляет сервис, "+XXX"-меняет сервис на XXХ, "~/s/r/"-замена по рег.выражению, x - меняет первую букву в' NOT NULL;

ALTER TABLE rbService CHANGE COLUMN adultUetDoctor adultUetDoctor DOUBLE DEFAULT 0 COMMENT 'взрослый УЕТ (Условные Единицы Трудозатрат) для врача' NULL;

ALTER TABLE rbService CHANGE COLUMN adultUetAverageMedWorker adultUetAverageMedWorker DOUBLE DEFAULT 0 COMMENT 'взрослый УЕТ (Условные Единицы Трудозатрат) для среднего медицинского персонала' NULL;

ALTER TABLE rbService CHANGE COLUMN childUetDoctor childUetDoctor DOUBLE DEFAULT 0 COMMENT 'детский УЕТ (Условные Единицы Трудозатрат) для врача' NULL;

ALTER TABLE rbService CHANGE COLUMN childUetAverageMedWorker childUetAverageMedWorker DOUBLE DEFAULT 0 COMMENT 'детский УЕТ (Условные Единицы Трудозатрат) для среднего медицинского персонала' NULL;

ALTER TABLE rbServiceClass CHANGE COLUMN section section CHAR(1) COMMENT 'Раздел' NOT NULL;

ALTER TABLE rbServiceClass CHANGE COLUMN code code VARCHAR(3) COMMENT 'Код класса услуги' NOT NULL;

ALTER TABLE rbServiceClass CHANGE COLUMN name name VARCHAR(200) COMMENT 'Класс услуги' NOT NULL;

ALTER TABLE rbServiceClass COMMENT = 'Класс услуг';

ALTER TABLE rbServiceGroup CHANGE COLUMN group_id group_id INTEGER COMMENT 'комплексная услуга {rbService}' NOT NULL;

ALTER TABLE rbServiceGroup CHANGE COLUMN service_id service_id INTEGER COMMENT 'услуга, входящая в состав комплексной {rbService}' NOT NULL;

ALTER TABLE rbServiceGroup CHANGE COLUMN required required TINYINT(1) DEFAULT 0 COMMENT 'присутствует обязательно' NOT NULL;

ALTER TABLE rbServiceGroup COMMENT = 'Группы услуг, подчинённые сложны';

ALTER TABLE rbServiceSection COMMENT = 'Раздел услуг';

ALTER TABLE rbServiceType CHANGE COLUMN section section CHAR(1) COMMENT 'Раздел' NOT NULL;

ALTER TABLE rbServiceType CHANGE COLUMN code code VARCHAR(3) COMMENT 'Код типа услуги' NOT NULL;

ALTER TABLE rbServiceType CHANGE COLUMN name name VARCHAR(200) COMMENT 'Тип услуги' NOT NULL;

ALTER TABLE rbServiceType CHANGE COLUMN description description TEXT COMMENT 'Описание типа услуги' NOT NULL;

ALTER TABLE rbServiceType COMMENT = 'Тип услуг';

ALTER TABLE rbService_Profile CHANGE COLUMN idx idx INTEGER DEFAULT 0 COMMENT 'относительный индекс (для сортировки в списке)' NOT NULL;

ALTER TABLE rbService_Profile CHANGE COLUMN sex sex TINYINT DEFAULT 0 COMMENT 'Применимо для указанного пола (0-любой, 1-М, 2-Ж)' NOT NULL;

ALTER TABLE rbService_Profile CHANGE COLUMN age age VARCHAR(9) COMMENT 'рименимо для указанного интервала возрастов пусто-нет ограничения, "{NNN{д|н|м|г}-{MMM{д|н|м|г}}" - с NNN дней/недель/месяцев/лет по MMM дней/недель/мес' NOT NULL;

ALTER TABLE rbService_Profile CHANGE COLUMN age_bu age_bu TINYINT UNSIGNED COMMENT 'Единица измерения нижней границы дипазона возраста (0 - не задано, 1 - день, 2 - неделя, 3 - месяц, 4 - год)' NULL;

ALTER TABLE rbService_Profile CHANGE COLUMN age_eu age_eu TINYINT UNSIGNED COMMENT 'Единица измерения верхней границы дипазона возраста (0 - не задано,1 - день, 2 - неделя, 3 - месяц, 4 - год)' NULL;

ALTER TABLE rbService_Profile CHANGE COLUMN mkbRegExp mkbRegExp VARCHAR(64) COMMENT 'Регулярное выражение для сопоставления с кодом МКБ' NOT NULL;

ALTER TABLE rbService_Profile COMMENT = 'Профили мед.помощи';

ALTER TABLE rbSocStatusType CHANGE COLUMN regionalCode regionalCode VARCHAR(8) COMMENT 'Региональный код' NOT NULL;

ALTER TABLE rbTariffCategory CHANGE COLUMN code code VARCHAR(16) COMMENT 'Код' NOT NULL;

ALTER TABLE rbTariffCategory CHANGE COLUMN name name VARCHAR(64) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbTariffCategory COMMENT = 'Тарифная категория';

ALTER TABLE rbTempInvalidReason CHANGE COLUMN regionalCode regionalCode VARCHAR(3) COMMENT 'Региональный код' NOT NULL;

ALTER TABLE rbTissueType CHANGE COLUMN code code VARCHAR(64) COMMENT 'Код' NOT NULL;

ALTER TABLE rbTissueType CHANGE COLUMN name name VARCHAR(128) COMMENT 'Наименование' NOT NULL;

ALTER TABLE rbTissueType CHANGE COLUMN sex sex TINYINT DEFAULT 0 COMMENT '0-Любой пол, 1-М, 2-Ж' NOT NULL;

ALTER TABLE rbTissueType COMMENT = 'Типы тканей';

ALTER TABLE rbVisitType CHANGE COLUMN serviceModifier serviceModifier VARCHAR(128) COMMENT 'Модификатор сервиса; пусто - нет изменения, "-" - удаляет сервис, "+XXX"-меняет сервис на XXХ, "~/s/r/"-замена по рег.выражению, x - меняет первую букву в' NOT NULL;
'''
    c.execute(sql)


def downgrade(conn):
    pass
