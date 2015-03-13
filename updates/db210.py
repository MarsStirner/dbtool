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

    print(u'Добавляем колонки в QuotaCatalog')
    sql = '''
ALTER TABLE `QuotaType` 
CHANGE COLUMN `group_code` `group_code` VARCHAR(16) NULL DEFAULT NULL COMMENT 'Код группы{QuotaType}\nДля профиля будет пустое' ,
ADD COLUMN `catalog_id` INT(11) NOT NULL COMMENT 'ссылка на справочник квот' AFTER `id`,
ADD COLUMN `profile_code` VARCHAR(45) NULL DEFAULT NULL COMMENT 'код профиля. Для профиля будет пустое' AFTER `class`,
ADD COLUMN `type_code` VARCHAR(45) NULL COMMENT 'код вида ВМП. Для профиля будет являться его кодом и = коду профиля для его видов ВМП' AFTER `group_code`,
ADD COLUMN `price` DOUBLE NOT NULL DEFAULT '0' COMMENT 'норматив фин.затрат' AFTER `teenOlder`
ADD INDEX `fk_catalog_id_idx` (`catalog_id` ASC);
ALTER TABLE `QuotaType` 
ADD CONSTRAINT `fk_catalog_id`
  FOREIGN KEY (`catalog_id`)
  REFERENCES `QuotaCatalog` (`id`)
  ON DELETE RESTRICT
  ON UPDATE RESTRICT;
    '''

    c.execute(sql)

    print(u'Создаём VMPQuotaDetails')
    sql = '''
CREATE TABLE IF NOT EXISTS `VMPQuotaDetails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pacientModel_id` INT(11) NOT NULL,
  `treatment_id` INT(11) NOT NULL COMMENT 'Ссылка на данные по методу и виду лечения (rbTreatment)',
  `quotaType_id` INT(11) NOT NULL,
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
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)

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
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)

    print(u'Добавляем колонки в Client_Quoting')
    sql = '''
ALTER TABLE `Client_Quoting`
ADD COLUMN `quotaDetails_id` INT(11) NOT NULL COMMENT 'Ссылка на детали квоты, для которой применяется диагноз' AFTER `quotaType_id`,
INDEX `fk_quotaDetails_id_idx` (`quotaDetails_id` ASC);
ALTER TABLE `Client_Quoting`
CONSTRAINT `fk_quotaDetails_id`
    FOREIGN KEY (`quotaDetails_id`)
    REFERENCES `VMPQuotaDetails` (`id`)
    ON DELETE RESTRICT 
    ON UPDATE RESTRICT;
    '''
    c.execute(sql)

    print(u'Создаём таблицу rbTreatmentType')
    sql = '''
CREATE TABLE IF NOT EXISTS `rbTreatmentType` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `code` VARCHAR(32) NOT NULL,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `code_idx` (`code` ASC)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''
    c.execute(sql)

    print(u'Добавляем в rbTreatment связь с rbTreatmentType')
    sql = '''
ALTER TABLE `rbTreatment`
ADD COLUMN `treatmentType_id` INT(11) NULL DEFAULT NULL,
INDEX `fk_treatmentType_id_idx` (`treatmentType_id` ASC);
ALTER TABLE `rbTreatmentType`
CONSTRAINT `fk_treatmentType_id`
    FOREIGN KEY (`treatmentType_id`)
    REFERENCES `rbTreatmentType` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
    '''
    c.execute(sql)

    print(u'Мигрируем Client_Quoting в VMPQuotaDetails')
    __migrate_client_quoting(c)

    print(u'Удаляем колонки в rbTreatment')
    sql = '''
ALTER TABLE `rbPacientModel` 
DROP FOREIGN KEY `rbPacientModel_ibfk_1`;
ALTER TABLE `rbPacientModel` 
DROP COLUMN `quotaType_id`,
DROP INDEX `quotaType_id` ;
'''
    c.execute(sql)

    print(u'Удаляем колонки в rbPacientModel')
    sql = '''
ALTER TABLE `rbPacientModel`
DROP FOREIGN KEY `rbPacientModel_ibfk_1`;
ALTER TABLE `rbPacientModel`
DROP COLUMN `quotaType_id`,
DROP INDEX `quotaType_id` ;
'''
    c.execute(sql)
    
    print(u'Удаляем колонки в Client_Quoting')
    sql = '''
ALTER TABLE `Client_Quoting` 
DROP COLUMN `treatment_id`,
DROP COLUMN `pacientModel_id`,
DROP COLUMN `quotaType_id`;
'''
    c.execute(sql)

    c.close()


def __migrate_client_quoting(cursor):
    cursor.execute('''SELECT `id`, `quotaType_id`, `pacientModel_id`, `treatment_id` FROM `Client_Quoting`''')
    data = cursor.fetchall()

    for row in data:
        id, quotaType_id, pacientModel_id, treatment_id = row
        sql = ('''INSERT INTO `VMPQuotaDetails` (`quotaType_id`, `pacientModel_id`, `treatment_id`) VALUES (%s, %s, %s)'''
               % (quotaType_id, pacientModel_id, treatment_id))
        cursor.execute(sql)
        last_id = cursor.lastrowid
        sql = '''UPDATE `Client_Quoting` SET `quotaDetails_id`=%s WHERE id=%s''' % (last_id, id)
        cursor.execute(sql)


def downgrade(conn):
    pass