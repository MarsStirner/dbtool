# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = u'''\
Добавляет таблицу биоматериалов и таблицу привязки биоматериалов к действиям.
'''

sqlCreateTissueTable = '''\
CREATE  TABLE IF NOT EXISTS `Tissue` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type_id` INT NOT NULL ,
  `date` DATETIME NOT NULL ,
  `barcode` VARCHAR(255) NOT NULL ,
  `event_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `idxBarCode` (`barcode` ASC) ,
  INDEX `fk_rbTissueType` (`type_id` ASC) ,
  INDEX `fk_Event` (`event_id` ASC) ,
  CONSTRAINT `fk_rbTissueType`
    FOREIGN KEY (`type_id` )
    REFERENCES `rbTissueType` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Event`
    FOREIGN KEY (`event_id` )
    REFERENCES `Event` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;
'''

sqlCreateActionTissueTable = '''\
CREATE  TABLE IF NOT EXISTS `ActionTissue` (
  `action_id` INT NOT NULL ,
  `tissue_id` INT NOT NULL ,
  PRIMARY KEY (`action_id`, `tissue_id`) ,
  INDEX `fk_Action` (`action_id` ASC) ,
  INDEX `fk_Tissue` (`tissue_id` ASC) ,
  CONSTRAINT `fk_Action`
    FOREIGN KEY (`action_id` )
    REFERENCES `Action` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tissue`
    FOREIGN KEY (`tissue_id` )
    REFERENCES `Tissue` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
COMMENT = 'Связывает Action и Tissue' ;
'''

sqlDropTissueTable = '''\
DROP TABLE `Tissue`
'''

sqlDropActionTissueTable = '''\
DROP TABLE `ActionTissue`
'''

def execute(conn, sql):
    c = conn.cursor()
    c.execute(sql)

def upgrade(conn):
    for sql in [sqlCreateTissueTable, sqlCreateActionTissueTable]:
        execute(conn, sql);

def downgrade(conn):
    for sql in [sqlDropActionTissueTable, sqlDropTissueTable]:
        execute(conn, sql);


