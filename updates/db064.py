#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
- Неоходимые изменения для работы ВМП
- Забытые изменения таблиц для работы функционала 6098
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
ALTER TABLE `Client_Quoting` ADD COLUMN `prevTalon_event_id` INT(11) NULL DEFAULT NULL COMMENT 'Ссылка на предыдущее обращение для использования данных ранее выданного талона'  AFTER `event_id`  ;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Client_Quoting` CHANGE COLUMN `quotaTicket` `quotaTicket` VARCHAR(20) NULL DEFAULT NULL COMMENT 'Номер талона ВМП'  ;
'''
    c.execute(sql)
    
    sql = u'''
CREATE OR REPLACE ALGORITHM=UNDEFINED DEFINER=%s SQL SECURITY DEFINER VIEW `vClient_Quoting_sub` AS select distinct `c1`.`id` AS `id`,`c1`.`createDatetime` AS `createDatetime`,`c1`.`createPerson_id` AS `createPerson_id`,`c1`.`modifyDatetime` AS `modifyDatetime`,`c1`.`modifyPerson_id` AS `modifyPerson_id`,`c1`.`deleted` AS `deleted`,`c1`.`master_id` AS `master_id`,`c1`.`identifier` AS `identifier`,`c1`.`quotaTicket` AS `quotaTicket`,`c1`.`quotaType_id` AS `quotaType_id`,`c1`.`stage` AS `stage`,`c1`.`directionDate` AS `directionDate`,`c1`.`freeInput` AS `freeInput`,`c1`.`org_id` AS `org_id`,`c1`.`amount` AS `amount`,`c1`.`MKB` AS `MKB`,`c1`.`status` AS `status`,`c1`.`request` AS `request`,`c1`.`statment` AS `statment`,`c1`.`dateRegistration` AS `dateRegistration`,`c1`.`dateEnd` AS `dateEnd`,`c1`.`orgStructure_id` AS `orgStructure_id`,`c1`.`regionCode` AS `regionCode`,`c1`.`pacientModel_id` AS `pacientModel_id`,`c1`.`treatment_id` AS `treatment_id`,`c1`.`event_id` AS `event_id`,`c1`.`prevTalon_event_id` AS `prevTalon_event_id` from (`Client_Quoting` `c1` join `Client_Quoting` `c2` on(((`c1`.`master_id` = `c2`.`master_id`) and (`c1`.`event_id` = `c2`.`event_id`) and (`c1`.`createDatetime` < `c2`.`createDatetime`))))
''' % config['definer']
    c.execute(sql)
    
    sql = u'''
CREATE OR REPLACE ALGORITHM=UNDEFINED DEFINER=%s SQL SECURITY DEFINER VIEW `vClient_Quoting` AS select `c0`.`id` AS `id`,`c0`.`createDatetime` AS `createDatetime`,`c0`.`createPerson_id` AS `createPerson_id`,`c0`.`modifyDatetime` AS `modifyDatetime`,`c0`.`modifyPerson_id` AS `modifyPerson_id`,`c0`.`deleted` AS `deleted`,`c0`.`master_id` AS `master_id`,`c0`.`identifier` AS `identifier`,`c0`.`quotaTicket` AS `quotaTicket`,`c0`.`quotaType_id` AS `quotaType_id`,`c0`.`stage` AS `stage`,`c0`.`directionDate` AS `directionDate`,`c0`.`freeInput` AS `freeInput`,`c0`.`org_id` AS `org_id`,`c0`.`amount` AS `amount`,`c0`.`MKB` AS `MKB`,`c0`.`status` AS `status`,`c0`.`request` AS `request`,`c0`.`statment` AS `statment`,`c0`.`dateRegistration` AS `dateRegistration`,`c0`.`dateEnd` AS `dateEnd`,`c0`.`orgStructure_id` AS `orgStructure_id`,`c0`.`regionCode` AS `regionCode`,`c0`.`pacientModel_id` AS `pacientModel_id`,`c0`.`treatment_id` AS `treatment_id`,`c0`.`event_id` AS `event_id`,`c0`.`prevTalon_event_id` AS `prevTalon_event_id` from (`Client_Quoting` `c0` left join `vClient_Quoting_sub` `c00` on((`c0`.`id` = `c00`.`id`))) where (isnull(`c00`.`id`) and (not(`c0`.`event_id` in (select `c3`.`prevTalon_event_id` from `Client_Quoting` `c3` where ((`c3`.`prevTalon_event_id` is not null) and (`c3`.`deleted` = 0))))))
''' % config['definer']
    c.execute(sql)
    
    sql = u'''
CREATE OR REPLACE ALGORITHM=UNDEFINED DEFINER=%s SQL SECURITY DEFINER VIEW `vClient_Quoting_History` AS select `cq`.`id` AS `id`,`p`.`login` AS `modifyPerson`,`cq`.`createDatetime` AS `createDatetime`,`cq`.`master_id` AS `client_id`,`cq`.`identifier` AS `identifier`,`cq`.`quotaTicket` AS `quotaTicket`,`qt`.`code` AS `quotaCode`,`cq`.`stage` AS `stage`,`cq`.`directionDate` AS `directionDate`,`cq`.`freeInput` AS `freeInput`,`o`.`shortName` AS `organ`,`cq`.`amount` AS `amount`,`cq`.`MKB` AS `MKB`,`qs`.`name` AS `status`,`cq`.`request` AS `request`,`cq`.`statment` AS `statment`,`cq`.`dateRegistration` AS `dateRegistration`,`cq`.`dateEnd` AS `dateEnd`,`os`.`name` AS `orgStruct`,`cq`.`regionCode` AS `regionCode`,`pm`.`code` AS `patientModelCode`,`t`.`code` AS `treatmentCode`,`cq`.`event_id` AS `event_id`,`cq`.`prevTalon_event_id` AS `prevTalon_event_id` from (((((((`Client_Quoting` `cq` left join `Person` `p` on((`cq`.`createPerson_id` = `p`.`id`))) left join `QuotaType` `qt` on((`cq`.`quotaType_id` = `qt`.`id`))) left join `Organisation` `o` on((`cq`.`org_id` = `o`.`id`))) left join `rbQuotaStatus` `qs` on((`cq`.`status` = `qs`.`id`))) left join `OrgStructure` `os` on((`cq`.`orgStructure_id` = `os`.`id`))) left join `rbPacientModel` `pm` on((`cq`.`pacientModel_id` = `pm`.`id`))) left join `rbTreatment` `t` on((`cq`.`treatment_id` = `t`.`id`))) order by `cq`.`master_id`,`cq`.`createDatetime` desc
''' % config['definer']
    c.execute(sql)
    
    
    sql = u'''
ALTER TABLE `Person` ADD `maxCito` TINYINT DEFAULT 0 AFTER `maxOverQueue`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise
    
    sql = u'''
CREATE TABLE IF NOT EXISTS QuotingByTime (
    `id`                INT(11) NOT NULL    AUTO_INCREMENT,
    `doctor_id`         INT(11)             COMMENT "Идентификатор доктора",
    `quoting_date`      DATE    NOT NULL    COMMENT "Дата, к которой применяется данное квотирование",
    `QuotingTimeStart`  TIME    NOT NULL    COMMENT "Начало перидона, доступного для записи",
    `QuotingTimeEnd`    TIME    NOT NULL    COMMENT "Конец перидона, доступного для записи",
    `QuotingType`       INT                 COMMENT "Тип записи, ссылается на rbTimeQuotingType.code",
    PRIMARY KEY (`id`)
);
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `rbTimeQuotingType` (
    `id`    INT(11) NOT NULL AUTO_INCREMENT,
    `code`  INT(11) NOT NULL UNIQUE,
    `name`  TEXT NOT NULL,
    PRIMARY KEY (`id`)
)
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
INSERT IGNORE INTO `rbTimeQuotingType` (
    `code`, `name` )
values
    (1, "Запись из регистратуры"),
    (2, "Запись врачём на повторный приём"),
    (3, "Межкабинетная запись"),
    (4, "Запись из других ЛПУ"),
    (5, "Запись через Портал");
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `rbTransferDateType` (
    `id`    INT(11) NOT NULL AUTO_INCREMENT,
    `code`  INT(11) NOT NULL UNIQUE,
    `name`  TEXT     NOT NULL,
    PRIMARY KEY (`id`)
)COLLATE='utf8_unicode_ci' ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
INSERT IGNORE INTO `rbTransferDateType` (
    `code`, `name` )
values
    (1, "В день приема"),
    (2, "За день до приема");
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `CouponsTransferQuotes` (
    `id`                INT(11)     NOT NULL AUTO_INCREMENT,
    `srcQuotingType_id` INT(11)     NOT NULL,
    `dstQuotingType_id` INT(11)     NOT NULL,
    `transferDayType`   INT(11)     NOT NULL,
    `transferTime`      TIME        NOT NULL,
    `couponsEnabled`    TINYINT(1)  NULL  DEFAULT '0',
    PRIMARY KEY (`id`),
    FOREIGN KEY (`srcQuotingType_id`) REFERENCES rbTimeQuotingType(`code`),
    FOREIGN KEY (`dstQuotingType_id`) REFERENCES rbTimeQuotingType(`code`),
    FOREIGN KEY (`transferDayType`)   REFERENCES rbTransferDateType(`code`)
)COLLATE='utf8_unicode_ci' ENGINE=InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Person` ADD `quotUnit` TINYINT DEFAULT 0 AFTER `maxCito`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise
    
    sql = u'''
ALTER TABLE `rbSpeciality` ADD COLUMN `quotingEnabled` TINYINT(1) UNSIGNED ZEROFILL NULL DEFAULT '0' COMMENT 'Если флажок установлен – при записи к врачам выбранной специальности из других ЛПУ учитываются квоты, определенные для этих ЛПУ на данной форме.' AFTER `regionalCode`;
'''
    try:
        c.execute(sql)
    except OperationalError as e:
        if 'Duplicate column name' in unicode(e):
            pass
        else:
            raise
    
    sql = u'''
CREATE TABLE IF NOT EXISTS `QuotingBySpeciality` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `speciality_id` INT(11) NOT NULL,
    `organisation_id` INT(11) NOT NULL,
    `coupons_quote` INT(11) NULL DEFAULT NULL,
    `coupons_remaining` INT(11) NULL DEFAULT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (speciality_id)   REFERENCES rbSpeciality(`id`),
    FOREIGN KEY (organisation_id) REFERENCES Organisation(`id`)
)
COLLATE='utf8_unicode_ci'
ENGINE=InnoDB;
'''
    c.execute(sql)
    

def downgrade(conn):
    pass
