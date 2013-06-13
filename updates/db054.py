# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from MySQLdb import OperationalError

__doc__ = '''\
Полная интеграция НТК и ВебМис
'''

def upgrade(conn):
    global tools
    c = conn.cursor()
    
    sql = u'''
CREATE TABLE `FlatDirectory` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(4096) NOT NULL COMMENT 'Имя справочника',
  `description` VARCHAR(4096) COMMENT 'Описание справочника',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB;
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `FDField` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `fdFieldType_id` INTEGER UNSIGNED NOT NULL COMMENT 'id типа поля из таблицы FDFieldType',
  `flatDirectory_id` INTEGER UNSIGNED NOT NULL COMMENT 'id справочника из таблицы FlatDirectory',
  `name` VARCHAR(4096) NOT NULL COMMENT 'Название поля справочника (отображаемый вид)',
  `description` VARCHAR(4096) COMMENT 'Описание поля справочника',
  `mask` VARCHAR(4096) COMMENT 'Маска формата значения',
  `mandatory` BOOLEAN COMMENT 'Обязательность заполнения (влияет на заполнение справочников когда будет приложение для этого)',
  `order` INTEGER UNSIGNED COMMENT 'Очередность поля в рамках записи в справочнике',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE `FDFieldType` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(4096) NOT NULL COMMENT 'Наименование типа поля',
  `description` VARCHAR(4096) COMMENT 'Описание типа поля',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE `FDRecord` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `flatDictionary_id` INTEGER UNSIGNED NOT NULL COMMENT 'id справочника из таблицы FlatDictionaryID',
  `order` INTEGER COMMENT 'Порядковый номер в справочнике (необязательно)',
  `name` VARCHAR(4096) COMMENT 'Имя записи в справочнике (необязательно)',
  `description` VARCHAR(4096) COMMENT 'Описание записи в справочнике (необязательно)',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
COMMENT = 'Запись в справочнике';
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `FDRecord` ADD COLUMN `dateStart` DATETIME COMMENT 'Дата начала действительности данной записи в справочнике (необязательно)' AFTER `description`,
ADD COLUMN `dateEnd` DATETIME COMMENT 'Дата окончания действия данной записи в справочнике (необязательно)' AFTER `dateStart`;
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE `FDFieldValue` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `fdRecord_id` INTEGER UNSIGNED NOT NULL COMMENT 'id записи из таблицы FDRecord',
  `fdField_id` INTEGER UNSIGNED NOT NULL COMMENT 'id поля из таблицы АВАшудв',
  `value` LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'Значение поля',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
COMMENT = 'Значение таблиц';
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `ActionProperty_FlatDirectory` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '{ActionProperty}',
  `index` INTEGER UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Индекс очередности 0 - id записи в справочнике (таблица FDRecord) ',
  `value` INTEGER UNSIGNED NOT NULL COMMENT 'Значение - id записи в справочнике (таблица FDRecord)',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
COMMENT = 'Значение из справочника FlatDirectory';
'''
    c.execute(sql)

    sql = u'''
CREATE TABLE `ClientFDProperty` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `flatDirectory_id` INTEGER UNSIGNED NOT NULL COMMENT 'id справочника, из которого выбираются значения для этого свойства',
  `name` LONGTEXT NOT NULL COMMENT 'Имя свойства',
  `description` LONGTEXT COMMENT 'Описание',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
COMMENT = 'Справочник свойств пациента из FlatDirectory';
'''
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `ClientFlatDirectory` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `clientFDProperty_id` INTEGER UNSIGNED NOT NULL COMMENT 'id свойства пациента из таблицы ClientFDProperty',
  `fdRecord_id` INTEGER UNSIGNED NOT NULL COMMENT 'id записи в справочнике, по сути - значение свойства',
  `dateStart` DATETIME COMMENT 'Дата начала действия данного значения',
  `dateEnd` DATETIME COMMENT 'Дата окончания действия данного значения',
  `createDateTime` DATETIME NOT NULL COMMENT 'Дата создания значения свойства',
  `createPerson_id` INTEGER UNSIGNED NOT NULL COMMENT 'Пользователь, создавший значение этого свойства',
  `modifyDateTime` DATETIME NOT NULL COMMENT 'Время последнего изменения значения свойства',
  `modifyPerson_id` INTEGER UNSIGNED COMMENT 'Пользователь, последний раз изменивший значение свойства',
  `deleted` TINYINT(1) UNSIGNED NOT NULL COMMENT 'Признак удаления',
  `client_id` INTEGER NOT NULL COMMENT 'id пациента из таблицы Client',
  `comment` LONGTEXT COMMENT 'Комментарий к значению',
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
COMMENT = 'Таблица со свойствами пациента из справочников';
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `FDField` ADD CONSTRAINT `FK_FDField_FlatDirectory` FOREIGN KEY `FK_FDField_FlatDirectory` (`flatDirectory_id`)
    REFERENCES `FlatDirectory` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FDField` ADD CONSTRAINT `FK_FDField_FDFieldType` FOREIGN KEY `FK_FDField_FDFieldType` (`fdFieldType_id`)
    REFERENCES `FDFieldType` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `ClientFlatDirectory` ADD CONSTRAINT `FK_ClientFlatDirectory_Client` FOREIGN KEY `FK_ClientFlatDirectory_Client` (`client_id`)
    REFERENCES `Client` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `ClientFlatDirectory` ADD CONSTRAINT `FK_ClientFlatDirectory_ClientFDProperty` FOREIGN KEY `FK_ClientFlatDirectory_ClientFDProperty` (`clientFDProperty_id`)
    REFERENCES `ClientFDProperty` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `ClientFlatDirectory` ADD CONSTRAINT `FK_ClientFlatDirectory_FDRecord` FOREIGN KEY `FK_ClientFlatDirectory_FDRecord` (`fdRecord_id`)
    REFERENCES `FDRecord` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `FDRecord` ADD CONSTRAINT `FK_FDRecord_FlatDictionary` FOREIGN KEY `FK_FDRecord_FlatDictionary` (`flatDictionary_id`)
    REFERENCES `FlatDirectory` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FDFieldValue` ADD CONSTRAINT `FK_FDFieldValue_FDRecord` FOREIGN KEY `FK_FDFieldValue_FDRecord` (`fdRecord_id`)
    REFERENCES `FDRecord` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `FDFieldValue` ADD CONSTRAINT `FK_FDFieldValue_FDField` FOREIGN KEY `FK_FDFieldValue_FDField` (`fdField_id`)
    REFERENCES `FDField` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `ActionProperty_FlatDirectory` ADD CONSTRAINT `FK_ActionProperty_FlatDirectory_FDRecord` FOREIGN KEY `FK_ActionProperty_FlatDirectory_FDRecord` (`value`)
    REFERENCES `FDRecord` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)

    sql = u'''
ALTER TABLE `ClientFDProperty` ADD CONSTRAINT `FK_ClientFDProperty_FlatDirectory` FOREIGN KEY `FK_ClientFDProperty_FlatDirectory` (`flatDirectory_id`)
    REFERENCES `FlatDirectory` (`id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Client` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientAddress` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientAllergy` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientContact` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientDocument` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientFDProperty` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientFlatDirectory` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientIdentification` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientIntoleranceMedicament` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientPolicy` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientRelation` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientSocStatus` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';    
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientWork` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';   
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `Diagnostic` ADD COLUMN `version` INTEGER UNSIGNED NOT NULL COMMENT 'Версия данных';   
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
CREATE TABLE `rbCoreActionProperty` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `actionType_id` int(10) unsigned NOT NULL,
  `name` varchar(128) NOT NULL,
  `actionPropertyType_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Client` ADD COLUMN `birthPlace` VARCHAR(128) CHARACTER SET utf8 COLLATE utf8_general_ci
NOT NULL DEFAULT '' COMMENT 'Место рождения';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientDocument` ADD COLUMN `endDate` DATE NOT NULL COMMENT 'Срок окончания действия документа';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientSocStatus` ADD COLUMN `note` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci
NOT NULL DEFAULT '' COMMENT 'Примечание';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientSocStatus` ADD COLUMN `benefitCategory_id` INTEGER UNSIGNED COMMENT 'Заполняется только для инвалидности (socStatusClass_id=2) Категория льгот, берется из справочников FDirectory с id 10 и 11';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientAddress` ADD COLUMN `localityType` INTEGER UNSIGNED NOT NULL COMMENT 'Тип населенного пункута 0 - село, 1 - город';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientWork` ADD COLUMN `rank_id` INTEGER UNSIGNED NOT NULL COMMENT 'Звание военнослужащего. FlatDirectory№7';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
ALTER TABLE `ClientWork` ADD COLUMN `arm_id` INTEGER UNSIGNED NOT NULL COMMENT 'Род войск. FlatDirectory №6';
'''
    tools.executeEx(c, sql, mode=['ignore_dublicates'])
    
    sql = u'''
INSERT INTO `FlatDirectory` VALUES
(1,'Cправочник социальных статусов','string'),(2,'Справочник групп крови','string'),(3,'Справочник типов жителей','string'),(4,'Справочник типов инвалидности','string'),(5,'Справочник документов, подтверждающих инвалидность','string'),(6,'Справочник Род войск (военнослужащий)','string'),(7,'Справочник званий (военнослужащий)','string'),(8,'Cправочник участков','string'),(9,'Справочник степени аллергии','string'),(10,'Справочник категорий федеральных льготников','string'),(11,'Справочник категорий региональных льгот','string'),(12,'Справочник 7 нозологий','string'),(13,'Справочник аллергий','string'),(14,'Справочник мест работы','string'),(15,'Справочник типов документов, удостоверяющих личность','string'),(16,'Справочник типов обращений','string'),(17,'Справочник типов согласований','string'),(18,'Справочник госпитализации','string'),(19,'Справочник \"Цель госпитализации\"','string'),(20,'Справочник \"Канал госпитализации\"','string'),(21,'Справочник \"Кем доставлен\"','string'),(22,'Справочник \"Доставлен от начала заболевания\"','string'),(23,'Справочник \"В состоянии при поступлении\" (опьянение)','string'),(24,'Справочник \"Травма\"','string'),(25,'Справочник \"Типы обращений\"','string'),(26,'Справочник \"Тип согласования\"','string'),(27,'Справочник \"Отказ в госпитализации\"','string'),
(28, 'Справочник \"Источник запасов\"', 'string'),
(29, 'Справочник \"Схема назначения\"', 'string'),
(30, 'Справочник \"Способ приема\"', 'string') ;
'''
    c.execute(sql)
    
    sql = u'''
INSERT INTO `FDFieldType` VALUES (1,'string','string');
'''
    c.execute(sql)
    
    sql = u'''
INSERT INTO `FDField` VALUES (1,1,1,'Код','string',NULL,0,1),(2,1,1,'Наименование','string',NULL,0,2),(3,1,2,'Код','string',NULL,0,1),(4,1,2,'Шифр','string',NULL,0,2),(5,1,2,'Наименование','string',NULL,NULL,3),(6,1,3,'Код','string',NULL,NULL,1),(7,1,3,'Шифр','string',NULL,NULL,2),(8,1,3,'Наименование','string',NULL,NULL,3),(9,1,4,'Код','string',NULL,NULL,1),(10,1,4,'Шифр','string',NULL,NULL,2),(11,1,4,'Наименование','string',NULL,NULL,3),(12,1,5,'Код','string',NULL,NULL,1),(13,1,5,'Шифр','string',NULL,NULL,2),(14,1,5,'Наименование','string',NULL,NULL,3),(15,1,6,'Код','string',NULL,NULL,1),(16,1,6,'Шифр','string',NULL,NULL,2),(17,1,6,'Название','string',NULL,NULL,3),(18,1,7,'Код','string',NULL,NULL,1),(19,1,7,'Шифр','string',NULL,NULL,2),(20,1,7,'Наименование','string',NULL,NULL,3),(21,1,7,'Сокращенное наименование','string',NULL,NULL,4),(22,1,9,'Код','string',NULL,NULL,1),(23,1,9,'Шифр','string',NULL,NULL,2),(24,1,9,'Наименование','string',NULL,NULL,3),(25,1,10,'Код','string',NULL,NULL,1),(26,1,10,'Шифр','string',NULL,NULL,2),(27,1,10,'Наименование','string',NULL,NULL,3),(28,1,11,'Код','string',NULL,NULL,1),(29,1,11,'Шифр','string',NULL,NULL,2),(30,1,11,'Наименование','string',NULL,NULL,3),(31,1,12,'Код','string',NULL,NULL,1),(32,1,12,'Шифр','string',NULL,NULL,2),(33,1,12,'Наименование','string',NULL,NULL,3),(34,1,14,'Код','string',NULL,NULL,1),(35,1,14,'Название','string',NULL,NULL,2),(36,1,14,'Код для реестра','string',NULL,NULL,3),(37,1,14,'Тип организации','string',NULL,NULL,4),(38,1,14,'Адрес регистрации','string',NULL,NULL,5),(39,1,14,'Адрес фактический','string',NULL,NULL,6),(40,1,15,'Код','string',NULL,NULL,1),(41,1,15,'Наименование документа','string',NULL,NULL,2),(42,1,16,'Код','string',NULL,NULL,1),(43,1,16,'Наименование','string',NULL,NULL,2),(44,1,17,'Код','string',NULL,NULL,1),(45,1,17,'Наименование','string',NULL,NULL,2),(46,1,18,'Код','string',NULL,NULL,1),(47,1,18,'Наименование','string',NULL,NULL,2),(48,1,19,'Код','string',NULL,NULL,1),(49,1,19,'Наименование','string',NULL,NULL,2),(50,1,20,'Код','string',NULL,NULL,1),(51,1,20,'Наименование','string',NULL,NULL,2),(52,1,21,'Код','string',NULL,NULL,1),(53,1,21,'Наименование','string',NULL,NULL,2),(54,1,22,'Код','string',NULL,NULL,1),(55,1,22,'Наименование','string',NULL,NULL,2),(56,1,23,'Код','string',NULL,NULL,1),(57,1,23,'Наименование','string',NULL,NULL,2),(58,1,24,'Код','string',NULL,NULL,1),(59,1,24,'Наименование','string',NULL,NULL,2),(60,1,25,'Код','string',NULL,NULL,1),(61,1,25,'Наименование','string',NULL,NULL,2),(62,1,26,'rbPost.code','string',NULL,NULL,1),(63,1,26,'Наименование','string',NULL,NULL,2),(64,1,27,'Код',NULL,NULL,NULL,NULL),(65,1,27,'Наименование',NULL,NULL,NULL,NULL);
'''
    c.execute(sql)
    
    sql = u'''
INSERT INTO `FDRecord` VALUES (1,1,1,NULL,NULL,NULL,NULL),(2,1,2,NULL,NULL,NULL,NULL),(3,1,3,NULL,NULL,NULL,NULL),(4,1,4,NULL,NULL,NULL,NULL),(5,1,5,NULL,NULL,NULL,NULL),(6,1,6,NULL,NULL,NULL,NULL),(7,1,7,NULL,NULL,NULL,NULL),(8,1,8,NULL,NULL,NULL,NULL),(9,2,1,NULL,NULL,NULL,NULL),(10,2,2,NULL,NULL,NULL,NULL),(11,2,3,NULL,NULL,NULL,NULL),(12,2,4,NULL,NULL,NULL,NULL),(13,2,5,NULL,NULL,NULL,NULL),(14,2,6,NULL,NULL,NULL,NULL),(15,2,7,NULL,NULL,NULL,NULL),(16,2,8,NULL,NULL,NULL,NULL),(17,3,1,NULL,NULL,NULL,NULL),(18,3,2,NULL,NULL,NULL,NULL),(19,4,1,NULL,NULL,NULL,NULL),(20,4,2,NULL,NULL,NULL,NULL),(21,4,3,NULL,NULL,NULL,NULL),(22,4,4,NULL,NULL,NULL,NULL),(23,4,5,NULL,NULL,NULL,NULL),(24,5,1,NULL,NULL,NULL,NULL),(25,5,2,NULL,NULL,NULL,NULL),(26,6,1,NULL,NULL,NULL,NULL),(27,6,2,NULL,NULL,NULL,NULL),(28,6,3,NULL,NULL,NULL,NULL),(29,6,4,NULL,NULL,NULL,NULL),(30,6,5,NULL,NULL,NULL,NULL),(31,6,6,NULL,NULL,NULL,NULL),(32,7,1,NULL,NULL,NULL,NULL),(33,7,2,NULL,NULL,NULL,NULL),(34,7,3,NULL,NULL,NULL,NULL),(35,7,4,NULL,NULL,NULL,NULL),(36,7,5,NULL,NULL,NULL,NULL),(37,7,6,NULL,NULL,NULL,NULL),(38,7,7,NULL,NULL,NULL,NULL),(39,7,8,NULL,NULL,NULL,NULL),(40,7,9,NULL,NULL,NULL,NULL),(41,7,10,NULL,NULL,NULL,NULL),(42,7,11,NULL,NULL,NULL,NULL),(43,7,12,NULL,NULL,NULL,NULL),(44,7,13,NULL,NULL,NULL,NULL),(45,7,14,NULL,NULL,NULL,NULL),(46,7,15,NULL,NULL,NULL,NULL),(47,7,16,NULL,NULL,NULL,NULL),(48,7,17,NULL,NULL,NULL,NULL),(49,7,18,NULL,NULL,NULL,NULL),(50,7,19,NULL,NULL,NULL,NULL),(51,7,20,NULL,NULL,NULL,NULL),(52,7,21,NULL,NULL,NULL,NULL),(53,7,22,NULL,NULL,NULL,NULL),(54,7,23,NULL,NULL,NULL,NULL),(55,7,24,NULL,NULL,NULL,NULL),(56,7,25,NULL,NULL,NULL,NULL),(57,7,26,NULL,NULL,NULL,NULL),(58,7,27,NULL,NULL,NULL,NULL),(59,7,28,NULL,NULL,NULL,NULL),(60,7,29,NULL,NULL,NULL,NULL),(61,7,30,NULL,NULL,NULL,NULL),(62,7,31,NULL,NULL,NULL,NULL),(63,7,32,NULL,NULL,NULL,NULL),(64,7,33,NULL,NULL,NULL,NULL),(65,7,34,NULL,NULL,NULL,NULL),(66,7,35,NULL,NULL,NULL,NULL),(67,7,36,NULL,NULL,NULL,NULL),(68,7,37,NULL,NULL,NULL,NULL),(69,7,38,NULL,NULL,NULL,NULL),(70,7,39,NULL,NULL,NULL,NULL),(71,7,40,NULL,NULL,NULL,NULL),(72,7,41,NULL,NULL,NULL,NULL),(73,7,42,NULL,NULL,NULL,NULL),(74,7,43,NULL,NULL,NULL,NULL),(75,7,44,NULL,NULL,NULL,NULL),(76,7,45,NULL,NULL,NULL,NULL),(77,7,46,NULL,NULL,NULL,NULL),(78,7,47,NULL,NULL,NULL,NULL),(79,9,1,NULL,NULL,NULL,NULL),(80,9,2,NULL,NULL,NULL,NULL),(81,9,3,NULL,NULL,NULL,NULL),(82,10,1,NULL,NULL,NULL,NULL),(83,10,2,NULL,NULL,NULL,NULL),(84,10,3,NULL,NULL,NULL,NULL),(85,10,4,NULL,NULL,NULL,NULL),(86,10,5,NULL,NULL,NULL,NULL),(87,10,6,NULL,NULL,NULL,NULL),(88,10,7,NULL,NULL,NULL,NULL),(89,10,8,NULL,NULL,NULL,NULL),(90,10,9,NULL,NULL,NULL,NULL),(91,10,10,NULL,NULL,NULL,NULL),(92,10,11,NULL,NULL,NULL,NULL),(93,10,12,NULL,NULL,NULL,NULL),(94,10,13,NULL,NULL,NULL,NULL),(95,10,14,NULL,NULL,NULL,NULL),(96,10,15,NULL,NULL,NULL,NULL),(97,11,1,NULL,NULL,NULL,NULL),(98,11,2,NULL,NULL,NULL,NULL),(99,11,3,NULL,NULL,NULL,NULL),(100,11,4,NULL,NULL,NULL,NULL),(101,12,1,NULL,NULL,NULL,NULL),(102,12,2,NULL,NULL,NULL,NULL),(103,12,3,NULL,NULL,NULL,NULL),(104,12,4,NULL,NULL,NULL,NULL),(105,12,5,NULL,NULL,NULL,NULL),(106,12,6,NULL,NULL,NULL,NULL),(107,12,7,NULL,NULL,NULL,NULL),(108,15,1,NULL,NULL,NULL,NULL),(109,15,2,NULL,NULL,NULL,NULL),(110,15,3,NULL,NULL,NULL,NULL),(111,15,4,NULL,NULL,NULL,NULL),(112,15,5,NULL,NULL,NULL,NULL),(113,15,6,NULL,NULL,NULL,NULL),(114,15,7,NULL,NULL,NULL,NULL),(115,15,8,NULL,NULL,NULL,NULL),(116,15,9,NULL,NULL,NULL,NULL),(117,15,10,NULL,NULL,NULL,NULL),(118,15,11,NULL,NULL,NULL,NULL),(119,15,12,NULL,NULL,NULL,NULL),(120,15,13,NULL,NULL,NULL,NULL),(121,15,14,NULL,NULL,NULL,NULL),(122,15,15,NULL,NULL,NULL,NULL),(123,15,16,NULL,NULL,NULL,NULL),(124,15,17,NULL,NULL,NULL,NULL),(125,16,1,NULL,NULL,NULL,NULL),(126,16,2,NULL,NULL,NULL,NULL),(127,17,1,NULL,NULL,NULL,NULL),(128,17,2,NULL,NULL,NULL,NULL),(129,17,3,NULL,NULL,NULL,NULL),(130,17,4,NULL,NULL,NULL,NULL),(131,17,5,NULL,NULL,NULL,NULL),(132,18,1,NULL,NULL,NULL,NULL),(133,18,2,NULL,NULL,NULL,NULL),(134,19,1,NULL,NULL,NULL,NULL),(135,19,2,NULL,NULL,NULL,NULL),(136,19,3,NULL,NULL,NULL,NULL),(137,19,4,NULL,NULL,NULL,NULL),(138,19,5,NULL,NULL,NULL,NULL),(139,19,6,NULL,NULL,NULL,NULL),(140,20,1,NULL,NULL,NULL,NULL),(141,20,2,NULL,NULL,NULL,NULL),(142,20,3,NULL,NULL,NULL,NULL),(143,20,4,NULL,NULL,NULL,NULL),(144,20,5,NULL,NULL,NULL,NULL),(145,20,6,NULL,NULL,NULL,NULL),(146,21,1,NULL,NULL,NULL,NULL),(147,21,2,NULL,NULL,NULL,NULL),(148,21,3,NULL,NULL,NULL,NULL),(149,22,1,NULL,NULL,NULL,NULL),(150,22,2,NULL,NULL,NULL,NULL),(151,22,3,NULL,NULL,NULL,NULL),(152,22,4,NULL,NULL,NULL,NULL),(153,23,1,NULL,NULL,NULL,NULL),(154,23,2,NULL,NULL,NULL,NULL),(155,23,3,NULL,NULL,NULL,NULL),(156,24,1,NULL,NULL,NULL,NULL),(157,24,2,NULL,NULL,NULL,NULL),(158,24,3,NULL,NULL,NULL,NULL),(159,24,4,NULL,NULL,NULL,NULL),(160,24,5,NULL,NULL,NULL,NULL),(161,24,6,NULL,NULL,NULL,NULL),(162,24,7,NULL,NULL,NULL,NULL),(163,24,8,NULL,NULL,NULL,NULL),(164,24,9,NULL,NULL,NULL,NULL),(165,25,1,NULL,NULL,NULL,NULL),(166,25,2,NULL,NULL,NULL,NULL),(167,25,3,NULL,NULL,NULL,NULL),(168,25,4,NULL,NULL,NULL,NULL),(169,25,5,NULL,NULL,NULL,NULL),(170,25,6,NULL,NULL,NULL,NULL),(171,25,7,NULL,NULL,NULL,NULL),(172,26,1,NULL,NULL,NULL,NULL),(173,26,2,NULL,NULL,NULL,NULL),(174,26,3,NULL,NULL,NULL,NULL),(175,26,4,NULL,NULL,NULL,NULL),(176,27,1,NULL,NULL,NULL,NULL),(177,27,2,NULL,NULL,NULL,NULL),(178,27,3,NULL,NULL,NULL,NULL),(179,27,4,NULL,NULL,NULL,NULL),(180,27,5,NULL,NULL,NULL,NULL);
'''
    c.execute(sql)
    
    sql = u'''
INSERT INTO `FDFieldValue` VALUES (1,1,1,'0'),(2,1,2,'Неработающий'),(3,2,1,'1'),(4,2,2,'Работающий'),(5,3,1,'2'),(6,3,2,'Неработающий пенсионер'),(7,4,1,'3'),(8,4,2,'Дошкольник'),(9,5,1,'4'),(10,5,2,'Учащийся'),(11,6,1,'5'),(12,6,2,'Военнослужащий'),(13,7,1,'6'),(14,7,2,'Член семьи военнослужащего'),(15,8,1,'7'),(16,8,2,'БОМЖ'),(17,9,3,'1'),(18,9,4,'1+'),(19,9,5,'O(1)Rh+'),(20,10,3,'2'),(21,10,4,'1-'),(22,10,5,'O(1)Rh-'),(23,11,3,'3'),(24,11,4,'2+'),(25,11,5,'A(II)Rh+'),(26,12,3,'4'),(27,12,4,'2-'),(28,12,5,'A(II)Rh-'),(29,13,3,'5'),(30,13,4,'3+'),(31,13,5,'B(III)Rh-'),(32,14,3,'6'),(33,14,4,'3-'),(34,14,5,'B(III)Rh+'),(35,15,3,'7'),(36,15,4,'4+'),(37,15,5,'AB(IV)Rh+'),(38,16,3,'8'),(39,16,4,'4-'),(40,16,5,'AB(IV)Rh+'),(41,17,6,'1'),(42,17,7,'1'),(43,17,8,'Город'),(44,18,6,'2'),(45,18,7,'2'),(46,18,8,'Село'),(47,19,9,'1'),(48,19,10,'0'),(49,19,11,'Инвалидность снята'),(50,20,9,'2'),(51,20,10,'1'),(52,20,11,'1 группа'),(53,21,9,'3'),(54,21,10,'2'),(55,21,11,'2 группа'),(56,22,9,'4'),(57,22,10,'3'),(58,22,11,'3 группа'),(59,23,9,'5'),(60,23,10,'4'),(61,23,11,'Инвалид детства'),(62,24,12,'1'),(63,24,13,'1'),(64,24,14,'Справка МСЭ'),(65,25,12,'2'),(66,25,13,'2'),(67,25,14,'Выписка из акта освидетельствования'),(68,26,15,'1'),(69,26,16,'1'),(70,26,17,'Черноморский флот'),(71,27,15,'2'),(72,27,16,'2'),(73,27,17,'Балтийский флот'),(74,28,15,'3'),(75,28,16,'3'),(76,28,17,'Тихоокеанский флот'),(77,29,15,'4'),(78,29,16,'4'),(79,29,17,'Северный флот'),(80,30,15,'5'),(81,30,16,'5'),(82,30,17,'Каспийский флот'),(83,31,15,'6'),(84,31,16,'6'),(85,31,17,'Части центрального подчинения'),(86,32,18,'1'),(87,32,19,'1'),(88,32,20,'Курсант'),(89,32,21,'Курсант'),(90,33,18,'2'),(91,33,19,'2'),(92,33,20,'Рядовой'),(93,33,21,'Рядовой'),(94,34,18,'3'),(95,34,19,'3'),(96,34,20,'Матрос'),(97,34,21,'Матрос'),(98,35,18,'4'),(99,35,19,'4'),(100,35,20,'Сержант'),(101,35,21,'Сержант'),(102,36,18,'5'),(103,36,19,'5'),(104,36,20,'Старшина 2 статьи'),(105,36,21,'Ст. 2 стат.'),(106,37,18,'6'),(107,37,19,'6'),(108,37,20,'Старшина 1 статьи'),(109,37,21,'Ст. 1 стат.'),(110,38,18,'7'),(111,38,19,'7'),(112,38,20,'Старшина'),(113,38,21,'Старшина'),(114,39,18,'8'),(115,39,19,'8'),(116,39,20,'Главный корабельный старшина'),(117,39,21,'ГКС'),(118,40,18,'9'),(119,40,19,'9'),(120,40,20,'Прапорщик'),(121,40,21,'Прапорщик'),(122,41,18,'10'),(123,41,19,'10'),(124,41,20,'Мичман'),(125,41,21,'Мичман'),(126,42,18,'11'),(127,42,19,'11'),(128,42,20,'Старший прапорщик'),(129,42,21,'Ст.Пр-к'),(130,43,18,'12'),(131,43,19,'12'),(132,43,20,'Старший мичман'),(133,43,21,'Ст. Мичман'),(134,44,18,'13'),(135,44,19,'13'),(136,44,20,'Лейтенант'),(137,44,21,'Лейтенант'),(138,45,18,'14'),(139,45,19,'14'),(140,45,20,'Старший лейтенант'),(141,45,21,'Ст. Лейтенант'),(142,46,18,'15'),(143,46,19,'15'),(144,46,20,'Капитан'),(145,46,21,'Капитан'),(146,47,18,'16'),(147,47,19,'16'),(148,47,20,'Капитан-лейтенант'),(149,47,21,'Кап.Лей-т.'),(150,48,18,'17'),(151,48,19,'17'),(152,48,20,'Майор'),(153,48,21,'Майор'),(154,49,18,'18'),(155,49,19,'18'),(156,49,20,'Капитан 3 ранга'),(157,49,21,'Кап. 3 ран.'),(158,50,18,'19'),(159,50,19,'19'),(160,50,20,'Подполковник'),(161,50,21,'П/полк.'),(162,51,18,'20'),(163,51,19,'20'),(164,51,20,'Капитан 2 ранга'),(165,51,21,'Кап. 2 ран.'),(166,52,18,'21'),(167,52,19,'21'),(168,52,20,'Полковник'),(169,52,21,'Полковник'),(170,53,18,'22'),(171,53,19,'22'),(172,53,20,'Капитан 1 ранга'),(173,53,21,'Кап. 1 ран.'),(174,54,18,'23'),(175,54,19,'23'),(176,54,20,'Генерал-майор'),(177,54,21,'Генерал-майор'),(178,55,18,'24'),(179,55,19,'24'),(180,55,20,'Контр-адмирал'),(181,55,21,'Контр-адмирал'),(182,56,18,'25'),(183,56,19,'25'),(184,56,20,'Генерал-лейтенант'),(185,56,21,'Генерал-лейтенант'),(186,57,18,'26'),(187,57,19,'26'),(188,57,20,'Вице-адмирал'),(189,57,21,'Вице-адмирал'),(190,58,18,'27'),(191,58,19,'27'),(192,58,20,'Генерал-полковник'),(193,58,21,'Генерал-полковник'),(194,59,18,'28'),(195,59,19,'28'),(196,59,20,'Адмирал'),(197,59,21,'Адмирал'),(198,60,18,'29'),(199,60,19,'29'),(200,60,20,'Старший лейтенант в отставке'),(201,60,21,'Ст. Лей-т. Отст.'),(202,61,18,'30'),(203,61,19,'30'),(204,61,20,'Капитан в отставке'),(205,61,21,'Кап. Отст.'),(206,62,18,'31'),(207,62,19,'31'),(208,62,20,'Майор в отставке'),(209,62,21,'Майор в отставке'),(210,63,18,'32'),(211,63,19,'32'),(212,63,20,'Подполковник в отставке'),(213,63,21,'П/п-к. Отст.'),(214,64,18,'33'),(215,64,19,'33'),(216,64,20,'Полковник в отставке'),(217,64,21,'П-к отст.'),(218,65,18,'34'),(219,65,19,'34'),(220,65,20,'Адмирал в отставке'),(221,65,21,'Адм. Отст.'),(222,66,18,'35'),(223,66,19,'35'),(224,66,20,'Капитан 1 ранга в отставке'),(225,66,21,'Кап. 1 ран. Отст.'),(226,67,18,'36'),(227,67,19,'36'),(228,67,20,'Старший матрос'),(229,67,21,'Ст.Матрос'),(230,68,18,'37'),(231,68,19,'37'),(232,68,20,'Ефрейтор'),(233,68,21,'Ефр.'),(234,69,18,'38'),(235,69,19,'38'),(236,69,20,'Старший прапорщик в отставке'),(237,69,21,'Ст. Пр-к. Отст.'),(238,70,18,'39'),(239,70,19,'39'),(240,70,20,'Вице-адмирал в отставке'),(241,70,21,'Вице-адм. Отст.'),(242,71,18,'40'),(243,71,19,'40'),(244,71,20,'Подполковник медицинской службы'),(245,71,21,'П/п-к. М.С.'),(246,72,18,'41'),(247,72,19,'41'),(248,72,20,'Служащий'),(249,72,21,'Служ.'),(250,73,18,'42'),(251,73,19,'42'),(252,73,20,'Адмирал флота'),(253,73,21,'Адм. Флота'),(254,74,18,'43'),(255,74,19,'43'),(256,74,20,'Генерал армии'),(257,74,21,'Ген.Арм.'),(258,75,18,'44'),(259,75,19,'44'),(260,75,20,'Главный старшина'),(261,75,21,'Гл.Ст-на.'),(262,76,18,'45'),(263,76,19,'45'),(264,76,20,'Младший лейтенант'),(265,76,21,'Мл. Лей-т.'),(266,77,18,'46'),(267,77,19,'46'),(268,77,20,'Младший сержант'),(269,77,21,'Мл. Серж.'),(270,78,18,'47'),(271,78,19,'47'),(273,78,20,'Полковник медицинской службы'),(274,78,21,'П-к М.С.'),(275,79,22,'1'),(276,79,23,'1'),(277,79,24,'Легкая'),(278,80,22,'2'),(279,80,23,'2'),(280,80,24,'Средняя'),(281,81,22,'3'),(282,81,23,'3'),(283,81,24,'Тяжелая'),(284,82,25,'1'),(285,82,26,'1'),(286,82,27,'Инвалид войны'),(287,83,25,'2'),(288,83,26,'2'),(289,83,27,'Участники ВОВ'),(290,84,25,'3'),(291,84,26,'3'),(292,84,27,'Ветераны боевых действий'),(293,85,25,'4'),(294,85,26,'4'),(295,85,27,'Военнослужащие, проходившие военную службу...'),(296,86,25,'5'),(297,86,26,'5'),(298,86,27,'Граждане, награжденные знаком \"Жителю блокадного Ленинграда\"'),(299,87,25,'6'),(300,87,26,'6'),(301,87,27,'Лица, работавшие в период ВОВ'),(302,88,25,'7'),(303,88,26,'7'),(304,88,27,'Члены семей погибших (умерших) инвалидов войны'),(305,89,25,'8'),(306,89,26,'8'),(307,89,27,'Инвалид III группы'),(308,90,25,'9'),(309,90,26,'9'),(310,90,27,'Инвалид II группы'),(311,91,25,'10'),(312,91,26,'10'),(313,91,27,'Инвалид I группы'),(314,92,25,'11'),(315,92,26,'11'),(316,92,27,'Дети-инвалиды'),(317,93,25,'12'),(318,93,26,'12'),(319,93,27,'Граждане, пострадавшие в результате радиационных техногенных катасроф'),(320,94,25,'13'),(321,94,26,'13'),(322,94,27,'Граждане РФ, удостоенные званий Героя Советского Союза, Героя РФ или являющиеся полными кавалерами'),(323,95,25,'14'),(324,95,26,'14'),(325,95,27,'Члены семей (вдова, вдовец), родители дети до 18 лет, дети старше 18 лет, ставшие инвалидами до достижения ими 18 лет'),(326,96,25,'15'),(327,96,26,'15'),(328,96,27,'Граждане РФ, удостоенные звания Героя Социалистического труда либо награжденные'),(329,97,28,'1'),(330,97,29,'1'),(331,97,30,'Ветераны труда, а также граждане, приравненные к ним'),(332,98,28,'2'),(333,98,29,'2'),(334,98,30,'Труженики тыла'),(335,99,28,'3'),(336,99,29,'3'),(337,99,30,'Реабилитированные лица и лица, пострадавшие от политических репрессий'),(338,100,28,'4'),(339,100,29,'4'),(340,100,30,'Нерабаотающие пенсионеры'),(341,101,31,'1'),(342,101,32,'1'),(343,101,33,'Гемофилия'),(344,102,31,'2'),(345,102,32,'2'),(346,102,33,'Муковисцидоз'),(347,103,31,'3'),(348,103,32,'3'),(349,103,33,'Гипофизарный нанизм'),(350,104,31,'4'),(351,104,32,'4'),(352,104,33,'Болезнь Гоше'),(353,105,31,'5'),(354,105,32,'5'),(355,105,33,'Миелолейкоз'),(356,106,31,'6'),(357,106,32,'6'),(358,106,33,'Рассеянный склероз'),(359,107,31,'7'),(360,107,32,'7'),(361,107,33,'Трансплантация органов'),(362,108,40,'1'),(363,108,41,'ПАСПОРТ РФ'),(364,109,40,'2'),(365,109,41,'ЗАГРАНПАСПОРТ'),(366,110,40,'3'),(367,110,41,'СВИД О РОЖД'),(368,111,40,'4'),(369,111,41,'УДОСТ ОФИЦЕРА'),(370,112,40,'5'),(371,112,41,'СПРАВКА ОБ ОСВ'),(372,113,40,'6'),(373,113,41,'ПАСПОРТ МОРФЛТ'),(374,114,40,'7'),(375,114,41,'ВОЕННЫЙ БИЛЕТ'),(376,115,40,'8'),(377,115,41,'ДИППАСПОРТ РФ'),(378,116,40,'9'),(379,116,41,'ИНПАСПОРТ'),(380,117,40,'10'),(381,117,41,'СВИД БЕЖЕНЦА'),(382,118,40,'11'),(383,118,41,'ВИД НА ЖИТЕЛЬ'),(384,119,40,'12'),(385,119,41,'УДОСТ БЕЖЕНЦА'),(386,120,40,'13'),(387,120,41,'ВРЕМ УДОСТ'),(388,121,40,'14'),(389,121,41,'ПАСПОРТ СССР'),(390,122,40,'16'),(391,122,41,'ПАСПОРТ МОРЯКА'),(392,123,40,'17'),(393,123,41,'ВОЕН БИЛЕТ ОЗ'),(394,124,42,'11'),(395,124,43,'Стационарное лечение'),(396,125,42,'12'),(397,125,43,'Дневной стационар'),(398,127,44,'2001'),(399,127,45,'Заведующий отделением'),(400,128,44,'2002'),(401,128,45,'Зав. приемным отделением'),(402,129,44,'1004'),(403,129,45,'Зам. главного врача'),(404,130,44,'1001'),(405,130,45,'Главный врач'),(406,131,44,'1'),(407,131,45,'Директор'),(408,132,46,'1'),(409,132,47,'по экстренным показаниям'),(410,133,46,'1'),(411,133,47,'в плановом порядке'),(412,134,48,'1'),(413,134,49,'лечение'),(414,135,48,'2'),(415,135,49,'дообследование'),(416,136,48,'3'),(417,136,49,'уточнение диагноза'),(418,137,48,'4'),(419,137,49,'экспертный случай'),(420,138,48,'5'),(421,138,49,'медикосоциальный уход'),(422,139,48,'6'),(423,139,49,'прочее'),(424,140,50,'1'),(425,140,51,'Бюджет'),(426,141,50,'2'),(427,141,51,'ОМС'),(428,142,50,'3'),(429,142,51,'ДМС'),(430,143,50,'4'),(431,143,51,'ВМП'),(432,144,50,'5'),(433,144,51,'СМП'),(434,145,50,'6'),(435,145,51,'платные услуги'),(436,146,52,'1'),(437,146,53,'СМП'),(438,147,52,'2'),(439,147,53,'Самостоятельно'),(440,148,52,'3'),(441,148,53,'Другое'),(442,149,54,'1'),(443,149,55,'в первые 6 часов'),(444,150,54,'2'),(445,150,55,'в течение 7-24 часов'),(446,151,54,'3'),(447,151,55,'позднее 24-х часов'),(448,152,54,'4'),(449,152,55,'другое'),(450,153,56,'1'),(451,153,57,'Алкогольного'),(452,154,56,'2'),(453,154,57,'Наркотического'),(454,155,56,'3'),(455,155,57,'Другое'),(456,156,58,'1'),(457,156,59,'промышленная'),(458,157,58,'2'),(459,157,59,'транспортная'),(460,158,58,'3'),(461,158,59,'ДТП'),(462,159,58,'4'),(463,159,59,'с\\хоз'),(464,160,58,'5'),(465,160,59,'бытовая'),(466,161,58,'6'),(467,161,59,'уличная'),(468,162,58,'7'),(469,162,59,'спортивная'),(470,163,58,'8'),(471,163,59,'школьная'),(472,164,58,'9'),(473,164,59,'другое'),(474,165,60,'11'),(475,165,61,'Стационарное лечение'),(476,166,60,'06'),(477,166,61,'Стационарное лечение (ВМП)'),(478,167,60,'15'),(479,167,61,'Стационарное лечение (фонд)'),(480,168,60,'12'),(481,168,61,'Дневной стационар'),(482,169,60,'01'),(483,169,61,'Дневной стационар (ВМП)'),(484,170,60,'16'),(485,170,61,'Дневной стационар (фонд)'),(486,171,60,'14'),(487,171,61,'Реанимация'),(488,172,62,'2001'),(489,172,63,'Заведующий отделением'),(490,173,62,'2002'),(491,173,63,'Зав. приемным отделением'),(492,174,62,'1004'),(493,174,63,'Зам. главного врача'),(494,175,62,'1001'),(495,175,63,'Главный врач'),(496,176,64,'1'),(497,176,65,'Госпитализация не показана'),(498,177,64,'2'),(499,177,65,'Нет показаний к экстренной госпитализации'),(500,178,64,'3'),(501,178,65,'Не по профилю стационара'),(502,179,64,'4'),(503,179,65,'Отсутствие мест'),(504,180,64,'5'),(505,180,65,'Отказ со стороны больного');
'''    
    c.execute(sql)

def downgrade(conn):
    pass