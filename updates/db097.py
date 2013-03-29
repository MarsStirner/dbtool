#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import uuid
import sys
from _mysql_exceptions import IntegrityError

__doc__ = '''\
- Изменения для 1С:Аптека - Pharmacy + Organisation.uuid
- Изменен тип поля для хранения данных шаблонов в rbPrintTemplate
- flatCode для назначений
- Добавление кодов дял профилей пользователей
'''
prescript_flatCode = 'prescription'

def upgrade(conn):
    global config        
    c = conn.cursor()
    
    sql = u'''DROP TABLE IF EXISTS Pharmacy;'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `Pharmacy` (
  `actionId` int(11) NOT NULL COMMENT 'Идентификатор события',
  `flatCode` varchar(255) DEFAULT NULL COMMENT 'Код события',
  `attempts` int(11) DEFAULT '0' COMMENT 'Кол-во попыток отправить сообщение',
  `status` enum('ADDED','COMPLETE','ERROR') DEFAULT 'ADDED' COMMENT 'Текущий статус сообщения',
  `uuid` varchar(255) DEFAULT '0' COMMENT 'UUID сообщения отправленого в 1С',
  `result` varchar(255) DEFAULT '' COMMENT 'Результат вернувшийся из 1С',
  `error_string` varchar(255) DEFAULT NULL COMMENT 'Строка с ошибкой вернувшейся из 1С',
  `rev` varchar(255) DEFAULT '' COMMENT 'Резерв',
  `value` int(11) DEFAULT '0' COMMENT 'Резерв',
  PRIMARY KEY (`actionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `rbPrintTemplate` CHANGE COLUMN `default` `default` LONGTEXT NOT NULL COMMENT 'Содержание шаблона (если файла нет)'  ;
'''
    c.execute(sql)
    
    c.execute(u'''SELECT id FROM `ActionType` where `name` like "Назначени%" ;''')
    result = c.fetchone()
    if result:
        prescr_at_id = result[0]
        sql = u'''UPDATE `ActionType` SET `flatCode` = "%s" WHERE `id` = %s;''' % (prescript_flatCode, prescr_at_id)
        c.execute(sql)
    
    # Добавить uuid к таблице Organisation
    updateOrganisationWithUUID(conn)
    
    # Проставить коды для профилей пользователей
    updateRbUserProfileWithCode(conn)
    

def updateOrganisationWithUUID(conn):
    c = conn.cursor()
    sql = u'''
ALTER TABLE `Organisation` ADD COLUMN `uuid_id` INT(11) NOT NULL DEFAULT 0  AFTER `isOrganisation` 
, ADD INDEX `uuid_id` (`uuid_id` ASC) ;
'''
    c.execute(sql)
    
    sql = u'''SELECT id from Organisation order by id'''
    c.execute(sql)
    orgIds = [id_[0] for id_ in c.fetchall()]
    numOrgRecords = len(orgIds)
    
    numRecords = sum([numOrgRecords]) 
    print("TOTAL: " + str(numRecords) + '\n', end='')
    sys.stdout.flush()
    
    tableRanges = {'Organisation': iter(orgIds)}
    
    i = 1
    ii = 0 # индекс в tableRanges
    
    while i <= numRecords:
        try:
            curTable = sorted(tableRanges.keys())[ii]
            dst_id = tableRanges[curTable].next()
        except StopIteration:
            ii += 1
            continue
        
        try:
            sql = '''INSERT INTO `UUID` (`uuid`) VALUES ("%s")''' % uuid.uuid4()
            c.execute(sql)
            last_id = conn.insert_id()
            sql = '''UPDATE `%s` SET uuid_id=%s where id=%s''' % (curTable, last_id, dst_id)
            c.execute(sql)
            i += 1
            if i % 100 == 0:
                print(".", end='')
                sys.stdout.flush()
            if i % 1000 == 0:
                print(str(i), end='')
                sys.stdout.flush()
            
        except IntegrityError:
            print('Opa, uuid dublicate!', end='')
        
    print('\n')
    

def updateRbUserProfileWithCode(conn):
    c = conn.cursor()
    table = 'rbUserProfile'
    profile_data = [
        ('admin',                u'Администратор'),
        ('personal',             u'Отдел кадров'),
        ('clinicRegistrator',    u'Регистратор поликлиники'),
        ('tabl',                 u'Табельщик'),
        ('economist',            u'Экономист'),
        ('counter',              u'Бухгалтер'),
        ('doctor',               u'Врач'),
        ('statist',              u'Статистик'),
        ('operator',             u'Оператор'),
        ('localChief',           u'Заведующий/Начальник'),
        ('supportDoctor',        u'Параклиника (вспомогательная служба)'),
        ('localBoss',            u'Руководитель'),
        ('strRegistrator',       u'Старший регистратор'),
        ('statDoctor',           u'Врач медицинский статистик'),
        ('guest',                u'Гость'),
        ('helper',               u'Помощник'),
        ('income',               u'Приемный покой'),
        ('KER',                  u'Специалист по КЭР'),
        ('nurse',                u'Медицинская сестра'),
        ('lab',                  u'Лаборант'),
        ('rRegistartor',         u'Регистратор'),
        ('strDoctor',            u'Врач отделения'),
        ('strNurse',             u'Медсестра отделения'),
        ('chief',                u'Главный врач'),
        ('strHead',              u'Заведующий отделением'),
        ('strDuty',              u'Дежурный врач отделения'),
        ('admNurse',             u'Медсестра приемного отделения'),
        ('admDoctor',            u'Врач приемного отделения'),
        ('clinicDoctor',         u'Врач поликлиники'),
        ('diagDoctor',           u'Врач диагностики'),
        ('dutyDoctor',           u'Дежурный врач'),
        ('clinicManager',        u'Менеджер платной поликлиники'),
        ('kassir',               u'Кассир'),
        ('economistHelper',      u'Помощник экономиста'),
        ('labDoctor',            u'Врач лаборатории'),
    ]
    
    sql = u'''UPDATE %s SET code = "%s" where name = %s'''
    for profile in profile_data:
        c.execute(sql % (table, profile[0], profile[1]))


def downgrade(conn):
    pass
