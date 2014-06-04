#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Новые таблицы для работы с записью пациентов на прием в амбулатории
'''


def upgrade(conn):
    c = conn.cursor()

    sql = '''
CREATE TABLE `rbReceptionType` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(32) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `rbAttendanceType` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(32) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `rbAppointmentType` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(32) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `Office` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(32) NOT NULL,
  `name` varchar(64) NOT NULL,
  `orgStructure_id` int(11) NULL COMMENT 'Отделение с кабинетом',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `Schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор записи',
  `person_id` int(11) NULL COMMENT 'Идентификатор сотрудника, которому назначен график',
  `date` date NOT NULL COMMENT 'Дата графика',
  `begTime` time NOT NULL COMMENT 'Время начала работы',
  `endTime` time NOT NULL COMMENT 'Время окончания работы',
  `numTickets` int(11) DEFAULT NULL,
  `office_id` int(64) DEFAULT NULL COMMENT 'кабинет',
  `reasonOfAbsence_id` int(11) DEFAULT NULL,
  `receptionType_id` int(11) DEFAULT NULL COMMENT 'тип приема. Например, "На дому", "Амбулаторно"',
  `createDatetime` datetime NOT NULL COMMENT 'Время создания записи',
  `createPerson_id` int(11) DEFAULT NULL COMMENT 'ИД сотрудника, создавшего запись',
  `modifyDatetime` datetime NOT NULL COMMENT 'Время изменения записи',
  `modifyPerson_id` int(11) DEFAULT NULL COMMENT 'ИД сотрудника, изменившего запись',
  `deleted` tinyint(4) NOT NULL DEFAULT '0' COMMENT 'Признак удаления графика',
  PRIMARY KEY (`id`),
  KEY `person_id` (`person_id`),
  KEY `reasonOfAbsence_id` (`reasonOfAbsence_id`),
  KEY `receptionType_id` (`receptionType_id`),
  KEY `fk_Schedule_1_idx` (`createPerson_id`),
  KEY `fk_Schedule_2_idx` (`modifyPerson_id`),
  INDEX `FK_Schedule_Office` (`office_id`),
  CONSTRAINT `fk_Schedule_1` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Schedule_2` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Schedule_Office` FOREIGN KEY (`office_id`) REFERENCES `Office` (`id`),
  CONSTRAINT `schedule_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`),
  CONSTRAINT `schedule_ibfk_2` FOREIGN KEY (`reasonOfAbsence_id`) REFERENCES `rbReasonOfAbsence` (`id`),
  CONSTRAINT `schedule_ibfk_3` FOREIGN KEY (`receptionType_id`) REFERENCES `rbReceptionType` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
COMMENT='Таблица графиков врачей на каждый день. Если в рамках одного типа приема (например, "Амбулаторно") есть перерыв, то в БД за данное число лежит 2 записи. ';
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `ScheduleTicket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `schedule_id` int(11) NOT NULL,
  `begDateTime` datetime DEFAULT NULL,
  `endDateTime` datetime DEFAULT NULL,
  `attendanceType_id` int(11) NOT NULL,
  `createDatetime` datetime NOT NULL,
  `createPerson_id` int(11) DEFAULT NULL,
  `modifyDatetime` datetime NOT NULL,
  `modifyPerson_id` int(11) DEFAULT NULL,
  `deleted` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_ScheduleTicket_1_idx` (`createPerson_id`),
  KEY `fk_ScheduleTicket_2_idx` (`modifyPerson_id`),
  KEY `scheduleticket_ibfk_1` (`schedule_id`),
  KEY `scheduleticket_ibfk_2` (`attendanceType_id`),
  CONSTRAINT `scheduleticket_ibfk_1` FOREIGN KEY (`schedule_id`) REFERENCES `Schedule` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `scheduleticket_ibfk_2` FOREIGN KEY (`attendanceType_id`) REFERENCES `rbAttendanceType` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_ScheduleTicket_1` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ScheduleTicket_2` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Таблица талонов врача. Талоны формируются в рамках графика врача.';
'''
    c.execute(sql)

    sql = '''
CREATE TABLE `ScheduleClientTicket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `ticket_id` int(11) NOT NULL,
  `isUrgent` tinyint(1) DEFAULT NULL,
  `note` varchar(256) DEFAULT NULL,
  `appointmentType_id` int(11) DEFAULT NULL,
  `infisFrom` varchar(15) DEFAULT NULL,
  `createDatetime` datetime NOT NULL,
  `createPerson_id` int(11) DEFAULT NULL,
  `modifyDatetime` datetime NOT NULL,
  `modifyPerson_id` int(11) DEFAULT NULL,
  `deleted` smallint(6) NOT NULL DEFAULT '0',
  `event_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_id` (`client_id`),
  KEY `ticket_id` (`ticket_id`),
  KEY `appointmentType_id` (`appointmentType_id`),
  KEY `FK_SCT_Event` (`event_id`),
  KEY `ix_ScheduleClientTicket_createPerson_id` (`createPerson_id`),
  KEY `ix_ScheduleClientTicket_modifyPerson_id` (`modifyPerson_id`),
  CONSTRAINT `fk_ScheduleClientTicket_1` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_ScheduleClientTicket_2` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_SCT_Event` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `scheduleclientticket_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `Client` (`id`),
  CONSTRAINT `scheduleclientticket_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ScheduleTicket` (`id`),
  CONSTRAINT `scheduleclientticket_ibfk_3` FOREIGN KEY (`appointmentType_id`) REFERENCES `rbAppointmentType` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Таблица занятых пациентами талонов на прием.';
'''
    c.execute(sql)

    c.close()


def downgrade(conn):
    pass