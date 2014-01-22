# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import traceback

__doc__ = '''\
Создание таблицы EPGUTickets для хранения данных о записях пациентов на приемы к врачам и статуса их отправки на ИС
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    try:
        c.execute(u"""CREATE TABLE IF NOT EXISTS`EPGUTickets` (
						`id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор',
						`personId` INT(11) NOT NULL COMMENT 'Идентфикатор врача к которому назначен прием',
						`clientId` INT(11) NOT NULL COMMENT 'Идентификатор пациента, записанного  на прием',
						`queueId` INT(11) NOT NULL COMMENT 'Идентификатор Действия (Action) записи на прием',
						`begDateTime` DATETIME NOT NULL COMMENT 'Дата и время начала талончика',
						`endDateTime` DATETIME NOT NULL COMMENT 'Дата и время окончания талончика',
						`office` VARCHAR(15) NULL DEFAULT NULL COMMENT 'Офис в котором бдует проходить прием врача',
						`status` VARCHAR(3) NULL DEFAULT NULL COMMENT 'Статус талончика (NEW-новый, CNC - отмена, DEL - удалено, SND-отправлено)',
						`lastModificationDate` DATETIME NULL DEFAULT NULL COMMENT 'Время последнего изменения',
						PRIMARY KEY (`id`),
						INDEX `personId` (`personId`),
						INDEX `clientId` (`clientId`),
						INDEX `queueId` (`queueId`)
					)
					COMMENT='талончики для Гос. Портала'
					COLLATE='utf8_general_ci'
					ENGINE=InnoDB;""")
    except:
         traceback.print_exc()

    c.close()

def downgrade(conn):
    pass