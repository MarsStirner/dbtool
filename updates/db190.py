#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Интеграция с ЕПГУ для новых расписаний
'''

def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS `EPGUTickets`;''')
    sql = '''
	CREATE TABLE `EPGUTickets` (
		`id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор',
		`scheduleClientTicket_id` INT(11) NOT NULL COMMENT 'Идентификатор записи на прием',
		`status` VARCHAR(3) NOT NULL DEFAULT 'NEW' COMMENT 'Статус талончика (NEW-новый, CNC-отмена, SND-отправлено)',
		`lastModificationDate` DATETIME NULL DEFAULT NULL COMMENT 'Время последнего изменения',
		PRIMARY KEY (`id`),
		INDEX `ticketId` (`scheduleClientTicket_id`),
		CONSTRAINT `fkEPGU_ScheduleClientTicket` FOREIGN KEY (`scheduleClientTicket_id`) REFERENCES `ScheduleClientTicket` (`id`) ON DELETE CASCADE
	)
	COMMENT='талончики для Гос. Портала'
	COLLATE='utf8_general_ci'
	ENGINE=InnoDB;
'''
    c.execute(sql)
    
    c.execute('''DROP TRIGGER IF EXISTS `ScheduleClientTicket_AFTER_INSERT`;''')
    sql = '''
CREATE DEFINER=%s TRIGGER `ScheduleClientTicket_AFTER_INSERT` AFTER INSERT ON `ScheduleClientTicket` FOR EACH ROW BEGIN
IF(NEW.deleted = 0) THEN
   --  Вставлять в таблицу только созданные неудаленными записи (хотя зачем создавать удаленными?!)
	INSERT INTO `EPGUTickets`(`scheduleClientTicket_id`, `status`,`lastModificationDate`) VALUES ( NEW.id, 'NEW', CURRENT_TIMESTAMP());
END IF;
END
'''%config['definer']
    c.execute(sql)


    c.execute('''DROP TRIGGER IF EXISTS `ScheduleClientTicket_AFTER_UPDATE`;''')
    sql = '''
CREATE DEFINER=%s TRIGGER `ScheduleClientTicket_AFTER_UPDATE` AFTER UPDATE ON `ScheduleClientTicket` FOR EACH ROW BEGIN
IF(NEW.deleted = 1 AND OLD.deleted = 0) THEN
	-- Была нормальная запись, а стала удаленной
	IF( EXISTS(SELECT e.id FROM `EPGUTickets` e WHERE e.`scheduleClientTicket_id` = NEW.id AND e.`status` = 'NEW' LIMIT 1) ) 
	THEN
		-- Есть NEW на удаляемую запись - DELETE IT
		DELETE FROM `EPGUTickets` WHERE `scheduleClientTicket_id` = NEW.id AND `status` <> 'SND';
	ELSE
		-- Нету NEW на удаляемую запись (скорее всего есть SND) - создаем CNC
		INSERT INTO `EPGUTickets`(`scheduleClientTicket_id`, `status`, `lastModificationDate`) VALUES (NEW.id, 'CNC', CURRENT_TIMESTAMP());
	END IF;
ELSEIF (NEW.deleted = 0 AND OLD.deleted = 1) THEN
	-- Была отменена запись, и отмену удалили
	IF( EXISTS(SELECT e.id FROM `EPGUTickets` e WHERE e.`scheduleClientTicket_id` = NEW.id AND e.`status` = 'CNC' LIMIT 1) ) 
	THEN
		-- Есть CNC на возобновляемую запись - DELETE IT
		DELETE FROM `EPGUTickets` WHERE `scheduleClientTicket_id` = NEW.id AND `status` <> 'SND';
	ELSE
		-- Нету CNC на удаляемую запись (скорее всего есть SND) - создаем NEW
		INSERT INTO `EPGUTickets`(`scheduleClientTicket_id`, `status`, `lastModificationDate`) VALUES (NEW.id, 'NEW', CURRENT_TIMESTAMP());
	END IF;
END IF;
END
'''%config['definer']
    c.execute(sql)




def downgrade(conn):
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS `EPGUTickets`;''')
    c.execute('''DROP TRIGGER IF EXISTS `ScheduleClientTicket_AFTER_UPDATE`;''')
    c.execute('''DROP TRIGGER IF EXISTS `ScheduleClientTicket_AFTER_INSERT`;''')