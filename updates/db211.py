#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''Квоты ВМП'''


def upgrade(conn):
    c = conn.cursor()

    print(u'Создаём таблицу QuotaCatalog')
    sql = '''
CREATE TABLE IF NOT EXISTS `QuotaCatalog` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `finance_id` INT(11) NOT NULL COMMENT 'источник финансирования',
  `begDate` DATE NOT NULL COMMENT 'дата начала действия справочника',
  `endDate` DATE NOT NULL COMMENT 'дата окончания действия справочника',
  `catalogNumber` VARCHAR(45) NULL DEFAULT '' COMMENT 'номер (версия) справочника',
  `documentDate` DATE NULL COMMENT 'дата выхода приказа, на основе которого сформирован справочник',
  `documentNumber` VARCHAR(45) NULL COMMENT 'номер приказа',
  `documentCorresp` VARCHAR(256) NULL COMMENT 'корреспондент (автор) приказа',
  `comment` TEXT NULL,
  `createDatetime` DATETIME NOT NULL COMMENT 'Дата создания записи',
  `createPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор записи {Person}',
  `modifyDatetime` DATETIME NULL COMMENT 'Дата изменения записи',
  `modifyPerson_id` INT(11) NULL DEFAULT NULL COMMENT 'Автор изменения записи {Person}',
  PRIMARY KEY (`id`),
  INDEX `fk_finance_id_idx` (`finance_id` ASC),
  INDEX `fk_create_person_id_idx` (`createPerson_id` ASC),
  INDEX `fk_modify_person_id_idx` (`modifyPerson_id` ASC),
  CONSTRAINT `fk_finance_id`
    FOREIGN KEY (`finance_id`)
    REFERENCES `rbFinance` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_create_person_id`
    FOREIGN KEY (`createPerson_id`)
    REFERENCES `Person` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_modify_person_id`
    FOREIGN KEY (`modifyPerson_id`)
    REFERENCES `Person` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Добавляем колонки в QuotaType')
    sql = '''
ALTER TABLE `QuotaType` 
CHANGE COLUMN `group_code` `group_code` VARCHAR(16) NULL DEFAULT NULL COMMENT 'Код группы{QuotaType}\nДля профиля будет пустое' ,
CHANGE COLUMN `class` `class` TINYINT(1) NOT NULL DEFAULT '0' COMMENT '0 - ВМП',
CHANGE COLUMN `teenOlder` `teenOlder` TINYINT(1) NOT NULL DEFAULT '0' COMMENT 'Для пациентов старше 18 лет',
ADD COLUMN `catalog_id` INT(11) NULL DEFAULT NULL COMMENT 'ссылка на справочник квот' AFTER `id`,
ADD COLUMN `profile_code` VARCHAR(16) NULL DEFAULT NULL COMMENT 'код профиля. Для профиля будет пустое' AFTER `class`,
ADD COLUMN `type_code` VARCHAR(16) NULL COMMENT 'код вида ВМП. Для профиля будет являться его кодом и = коду профиля для его видов ВМП' AFTER `group_code`,
ADD COLUMN `price` DECIMAL(11,2) NOT NULL DEFAULT '0' COMMENT 'норматив фин.затрат' AFTER `teenOlder`,
ADD INDEX `fk_catalog_id_idx` (`catalog_id` ASC);
ALTER TABLE `QuotaType`
ADD CONSTRAINT `fk_catalog_id`
  FOREIGN KEY (`catalog_id`)
  REFERENCES `QuotaCatalog` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
    '''

    c.execute(sql)
    c.close()
    
    c = conn.cursor()
    print(u'Переносим значения из QuotaType.group_code в QuotaType.profile_code')
    sql = '''UPDATE `QuotaType` SET profile_code=group_code, group_code=NULL WHERE group_code IS NOT NULL;'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Создаём VMPQuotaDetails')
    sql = '''
CREATE TABLE IF NOT EXISTS `VMPQuotaDetails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pacientModel_id` INT(11) NULL DEFAULT NULL,
  `treatment_id` INT(11) NULL DEFAULT NULL COMMENT 'Ссылка на данные по методу и виду лечения (rbTreatment)',
  `quotaType_id` INT(11) NOT NULL,
  `price` DECIMAL(11,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pacientModel_id_idx` (`pacientModel_id` ASC),
  INDEX `fk_treatment_id_idx` (`treatment_id` ASC),
  INDEX `fk_quotaType_id_idx` (`quotaType_id` ASC),
  CONSTRAINT `fk_pacientModel_id`
    FOREIGN KEY (`pacientModel_id`)
    REFERENCES `rbPacientModel` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_treatment_id`
    FOREIGN KEY (`treatment_id`)
    REFERENCES `rbTreatment` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_quotaType_id`
    FOREIGN KEY (`quotaType_id`)
    REFERENCES `QuotaType` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Создаём MKB_VMPQuotaFilter')
    sql = '''
CREATE TABLE IF NOT EXISTS `MKB_VMPQuotaFilter` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `MKB_id` INT(11) NOT NULL,
  `quotaDetails_id` INT(11) NOT NULL COMMENT 'Ссылка на детали квоты, для которой применяется диагноз',
  PRIMARY KEY (`id`),
  INDEX `fk_MKB_id_idx` (`MKB_id` ASC),
  INDEX `fk_quotaDetails_id_idx` (`quotaDetails_id` ASC),
  CONSTRAINT `fk_MKB_id`
    FOREIGN KEY (`MKB_id`)
    REFERENCES `MKB` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_quotaDetails_id`
    FOREIGN KEY (`quotaDetails_id`)
    REFERENCES `VMPQuotaDetails` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Добавляем колонки в Client_Quoting')
    sql = '''
ALTER TABLE `Client_Quoting`
ADD COLUMN `quotaDetails_id` INT(11) NULL DEFAULT NULL COMMENT 'Ссылка на детали квоты, для которой применяется диагноз' AFTER `quotaType_id`,
ADD INDEX `fk_details_id_idx` (`quotaDetails_id` ASC);
ALTER TABLE `Client_Quoting`
ADD CONSTRAINT `fk_details_id`
    FOREIGN KEY (`quotaDetails_id`)
    REFERENCES `VMPQuotaDetails` (`id`)
    ON DELETE RESTRICT 
    ON UPDATE RESTRICT;
    '''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Создаём таблицу rbTreatmentType')
    sql = '''
CREATE TABLE IF NOT EXISTS `rbTreatmentType` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(32) NOT NULL,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `code_idx` (`code` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Добавляем в rbTreatment связь с rbTreatmentType')
    sql = '''
ALTER TABLE `rbTreatment`
ADD COLUMN `treatmentType_id` INT(11) NULL DEFAULT NULL,
ADD INDEX `fk_treatmentType_id_idx` (`treatmentType_id` ASC);
ALTER TABLE `rbTreatment`
ADD CONSTRAINT `fk_treatmentType_id`
    FOREIGN KEY (`treatmentType_id`)
    REFERENCES `rbTreatmentType` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
    '''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Мигрируем Client_Quoting в VMPQuotaDetails')
    __migrate_client_quoting(c)
    c.close()

    c = conn.cursor()

    print(u'Изменяем Client_Quoting')
    sql = '''
ALTER TABLE `Client_Quoting` 
DROP FOREIGN KEY `fk_details_id`;
ALTER TABLE `Client_Quoting` 
CHANGE COLUMN `quotaDetails_id` `quotaDetails_id` INT(11) NOT NULL COMMENT 'Ссылка на детали квоты, для которой применяется диагноз' ;
ALTER TABLE `Client_Quoting` 
ADD CONSTRAINT `fk_details_id`
  FOREIGN KEY (`quotaDetails_id`)
  REFERENCES `VMPQuotaDetails` (`id`);
'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    # print(u'Изменяем VMPQuotaDetails')
    # Не можем выполнить этот запрос, т.к. при миграции перетянулись NULL-значения в pacientModel_id, treatment_id
    sql = '''
ALTER TABLE `VMPQuotaDetails` 
DROP FOREIGN KEY `fk_pacientModel_id`,
DROP FOREIGN KEY `fk_treatment_id`;
ALTER TABLE `VMPQuotaDetails` 
CHANGE COLUMN `pacientModel_id` `pacientModel_id` INT(11) NOT NULL ,
CHANGE COLUMN `treatment_id` `treatment_id` INT(11) NOT NULL COMMENT 'Ссылка на данные по методу и виду лечения (rbTreatment)' ,
ALTER TABLE `VMPQuotaDetails`
ADD CONSTRAINT `fk_pacientModel_id`
  FOREIGN KEY (`pacientModel_id`)
  REFERENCES `rbPacientModel` (`id`),
ADD CONSTRAINT `fk_treatment_id`
  FOREIGN KEY (`treatment_id`)
  REFERENCES `rbTreatment` (`id`);'''
    # c.execute(sql)
    # c.close()

    c = conn.cursor()

    print(u'Удаляем колонки в rbTreatment')
    sql = '''
ALTER TABLE `rbPacientModel` 
DROP FOREIGN KEY `rbPacientModel_ibfk_1`;
ALTER TABLE `rbPacientModel` 
DROP COLUMN `quotaType_id`,
DROP INDEX `quotaType_id` ;
'''
    c.execute(sql)
    c.close()

    c = conn.cursor()

    print(u'Удаляем колонки в rbPacientModel')
    sql = '''
ALTER TABLE `rbPacientModel`
DROP FOREIGN KEY `rbPacientModel_ibfk_1`;'''
    try:
        c.execute(sql)
    except Exception as e:
        print(e)

    sql = '''
ALTER TABLE `rbPacientModel`
DROP COLUMN `quotaType_id`,
DROP INDEX `quotaType_id` ;
'''
    try:
        c.execute(sql)
    except Exception as e:
        print(e)

    c.close()

    c = conn.cursor()
    
    print(u'Удаляем колонки в Client_Quoting')
    sql = '''
ALTER TABLE `Client_Quoting` 
DROP COLUMN `treatment_id`,
DROP COLUMN `pacientModel_id`,
DROP COLUMN `quotaType_id`;
'''
    try:
        c.execute(sql)
    except Exception as e:
        print(e)

    c.close()

    c = conn.cursor()
    print(u'Мигрируем вьюхи')
    __migrate_views(c)
    c.close()


def __migrate_client_quoting(cursor):
    cursor.execute('''SELECT `id`, `quotaType_id`, `pacientModel_id`, `treatment_id` FROM `Client_Quoting`''')
    data = cursor.fetchall()

    for row in data:
        id, quotaType_id, pacientModel_id, treatment_id = row
        sql = ('''SELECT id FROM `VMPQuotaDetails` WHERE `quotaType_id`=%s AND `pacientModel_id`=%s AND `treatment_id`= %s'''
               % (quotaType_id if quotaType_id else 'NULL',
                  pacientModel_id if pacientModel_id else 'NULL',
                  treatment_id if treatment_id else 'NULL'))
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            last_id = row[0]
        else:
            sql = ('''INSERT INTO `VMPQuotaDetails` (`quotaType_id`, `pacientModel_id`, `treatment_id`) VALUES (%s, %s, %s)'''
                   % (quotaType_id if quotaType_id else 'NULL',
                      pacientModel_id if pacientModel_id else 'NULL',
                      treatment_id if treatment_id else 'NULL'))
            cursor.execute(sql)
            last_id = cursor.lastrowid

        sql = '''UPDATE `Client_Quoting` SET `quotaDetails_id`=%s WHERE id=%s''' % (last_id, id)
        cursor.execute(sql)


def __migrate_views(cursor):
    print(u'Изменяем vClient_Quoting_sub')

    sql = '''
    CREATE
     OR REPLACE ALGORITHM = UNDEFINED
    DEFINER = `root`@`localhost`
    SQL SECURITY DEFINER
VIEW `vClient_Quoting_sub` AS
    select distinct
        `c1`.`id` AS `id`,
        `c1`.`createDatetime` AS `createDatetime`,
        `c1`.`createPerson_id` AS `createPerson_id`,
        `c1`.`modifyDatetime` AS `modifyDatetime`,
        `c1`.`modifyPerson_id` AS `modifyPerson_id`,
        `c1`.`deleted` AS `deleted`,
        `c1`.`master_id` AS `master_id`,
        `c1`.`identifier` AS `identifier`,
        `c1`.`quotaTicket` AS `quotaTicket`,
        `qd`.`quotaType_id` AS `quotaType_id`,
        `c1`.`stage` AS `stage`,
        `c1`.`directionDate` AS `directionDate`,
        `c1`.`freeInput` AS `freeInput`,
        `c1`.`org_id` AS `org_id`,
        `c1`.`amount` AS `amount`,
        `c1`.`MKB` AS `MKB`,
        `c1`.`status` AS `status`,
        `c1`.`request` AS `request`,
        `c1`.`statment` AS `statment`,
        `c1`.`dateRegistration` AS `dateRegistration`,
        `c1`.`dateEnd` AS `dateEnd`,
        `c1`.`orgStructure_id` AS `orgStructure_id`,
        `c1`.`regionCode` AS `regionCode`,
        `qd`.`pacientModel_id` AS `pacientModel_id`,
        `qd`.`treatment_id` AS `treatment_id`,
        `c1`.`event_id` AS `event_id`,
        `c1`.`prevTalon_event_id` AS `prevTalon_event_id`
    from
        (`Client_Quoting` `c1`
		join `VMPQuotaDetails` `qd` ON `c1`.`quotaDetails_id`=`qd`.`id`
        join `Client_Quoting` `c2` ON (((`c1`.`master_id` = `c2`.`master_id`)
            and (`c1`.`event_id` = `c2`.`event_id`)
            and (`c1`.`createDatetime` < `c2`.`createDatetime`))));
    '''
    cursor.execute(sql)

    print(u'Изменяем vClient_Quoting')

    sql = '''
    CREATE
     OR REPLACE ALGORITHM = UNDEFINED
    DEFINER = `root`@`localhost`
    SQL SECURITY DEFINER
VIEW `vClient_Quoting` AS
    select
        `c0`.`id` AS `id`,
        `c0`.`createDatetime` AS `createDatetime`,
        `c0`.`createPerson_id` AS `createPerson_id`,
        `c0`.`modifyDatetime` AS `modifyDatetime`,
        `c0`.`modifyPerson_id` AS `modifyPerson_id`,
        `c0`.`deleted` AS `deleted`,
        `c0`.`master_id` AS `master_id`,
        `c0`.`identifier` AS `identifier`,
        `c0`.`quotaTicket` AS `quotaTicket`,
        `qd`.`quotaType_id` AS `quotaType_id`,
        `c0`.`stage` AS `stage`,
        `c0`.`directionDate` AS `directionDate`,
        `c0`.`freeInput` AS `freeInput`,
        `c0`.`org_id` AS `org_id`,
        `c0`.`amount` AS `amount`,
        `c0`.`MKB` AS `MKB`,
        `c0`.`status` AS `status`,
        `c0`.`request` AS `request`,
        `c0`.`statment` AS `statment`,
        `c0`.`dateRegistration` AS `dateRegistration`,
        `c0`.`dateEnd` AS `dateEnd`,
        `c0`.`orgStructure_id` AS `orgStructure_id`,
        `c0`.`regionCode` AS `regionCode`,
        `qd`.`pacientModel_id` AS `pacientModel_id`,
        `qd`.`treatment_id` AS `treatment_id`,
        `c0`.`event_id` AS `event_id`,
        `c0`.`prevTalon_event_id` AS `prevTalon_event_id`
    from
        (`Client_Quoting` `c0`
		left join `VMPQuotaDetails` `qd` ON `c0`.`quotaDetails_id`=`qd`.`id`
        left join `vClient_Quoting_sub` `c00` ON ((`c0`.`id` = `c00`.`id`)))
    where
        (isnull(`c00`.`id`)
            and ((not (`c0`.`event_id` in (select
                `c3`.`prevTalon_event_id`
            from
                `Client_Quoting` `c3`
            where
                ((`c3`.`prevTalon_event_id` is not null)
                    and (`c3`.`deleted` = 0)))))
            or isnull(`c0`.`event_id`)));
    '''
    cursor.execute(sql)

    print(u'Изменяем vClient_Quoting_History')

    sql = '''
    CREATE
     OR REPLACE ALGORITHM = UNDEFINED
    DEFINER = `root`@`localhost`
    SQL SECURITY DEFINER
VIEW `vClient_Quoting_History` AS
    select
        `cq`.`id` AS `id`,
        `p`.`login` AS `modifyPerson`,
        `cq`.`createDatetime` AS `createDatetime`,
        `cq`.`master_id` AS `client_id`,
        `cq`.`identifier` AS `identifier`,
        `cq`.`quotaTicket` AS `quotaTicket`,
        `qt`.`code` AS `quotaCode`,
        `cq`.`stage` AS `stage`,
        `cq`.`directionDate` AS `directionDate`,
        `cq`.`freeInput` AS `freeInput`,
        `o`.`shortName` AS `organ`,
        `cq`.`amount` AS `amount`,
        `cq`.`MKB` AS `MKB`,
        `qs`.`name` AS `status`,
        `cq`.`request` AS `request`,
        `cq`.`statment` AS `statment`,
        `cq`.`dateRegistration` AS `dateRegistration`,
        `cq`.`dateEnd` AS `dateEnd`,
        `os`.`name` AS `orgStruct`,
        `cq`.`regionCode` AS `regionCode`,
        `pm`.`code` AS `patientModelCode`,
        `t`.`code` AS `treatmentCode`,
        `cq`.`event_id` AS `event_id`,
        `cq`.`prevTalon_event_id` AS `prevTalon_event_id`
    from
        (((((((`Client_Quoting` `cq`
		left join `VMPQuotaDetails` `qd` ON `cq`.`quotaDetails_id`=`qd`.`id`
        left join `Person` `p` ON ((`cq`.`createPerson_id` = `p`.`id`)))
        left join `QuotaType` `qt` ON ((`qd`.`quotaType_id` = `qt`.`id`)))
        left join `Organisation` `o` ON ((`cq`.`org_id` = `o`.`id`)))
        left join `rbQuotaStatus` `qs` ON ((`cq`.`status` = `qs`.`id`)))
        left join `OrgStructure` `os` ON ((`cq`.`orgStructure_id` = `os`.`id`)))
        left join `rbPacientModel` `pm` ON ((`qd`.`pacientModel_id` = `pm`.`id`)))
        left join `rbTreatment` `t` ON ((`qd`.`treatment_id` = `t`.`id`)))
    order by `cq`.`master_id` , `cq`.`createDatetime` desc;
    '''
    cursor.execute(sql)


def downgrade(conn):
    pass
