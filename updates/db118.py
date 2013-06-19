#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление таблицы для интеграции с HealthShare
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = u'''
        CREATE TABLE IF NOT EXISTS `HSIntegration` (
	    `event_id` INT(11) NOT NULL COMMENT 'Идентификатор события',
	    `status` ENUM('NEW', 'SENDED', 'ERROR') NOT NULL DEFAULT 'NEW' COMMENT 'Статус отправки в  HS (NEW - для отправки,  SENDED - успешно передан, ERROR - ошибка при передаче)',
	    `info` VARCHAR(1024) NULL DEFAULT NULL COMMENT 'Текстовое описание статуса передачи события (сообщение об ошибке)',
	    PRIMARY KEY (`event_id`),
	    CONSTRAINT `FK__Event` FOREIGN KEY (`event_id`) REFERENCES `Event` (`id`)
        )
        COMMENT='Информация об отправке событий в HealthShare'
        COLLATE='utf8_general_ci'
       ENGINE=InnoDB;
    '''
    c.execute(sql)
           
def downgrade(conn):
    pass
