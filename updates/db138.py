#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
from collections import defaultdict
from datetime import datetime
import traceback


__doc__ = '''
Изменения для обновления остатков
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    # First get all affected ActionTypes
    c.execute(u"""SELECT `ActionType`.`id`,
    `ActionType`.`testTubeType_id`, `ActionType_TissueType`.`tissueType_id`, `ActionType_TissueType`.`amount`, `ActionType_TissueType`.`unit_id`
    FROM `ActionType`
    JOIN `ActionType_TissueType` on `ActionType_TissueType`.`master_id` = `ActionType`.`id`
    WHERE `ActionType`.`isRequiredTissue` = '1';""")
    TakenTissueType = dict([
        (row[0], (row[1], row[2], row[3], row[4]))
        for row in c
        if row[1] and row[2]
    ])
    print(TakenTissueType)
    c.execute(u"""CREATE TABLE IF NOT EXISTS `TakenTissueType` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `code` VARCHAR(128) NOT NULL COMMENT 'Код',
    `tissueType_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип ткани {rbTissueType}',
    `testTubeType_id` INT(11) NULL DEFAULT NULL COMMENT 'Тип пробирки {rbTestTubeType}',
    `laboratory_id` INT(11) NULL DEFAULT NULL COMMENT 'Лаборатория {rbLaboratory}',
    `orgStructure_id` INT(11) NULL DEFAULT NULL COMMENT 'Отделение {OrgStructure}',
    `amount` INT(11) NOT NULL COMMENT 'количество',
    `unit_id` INT(11) NOT NULL COMMENT 'Единица измерения {rbUnit}',
    PRIMARY KEY (`id`),
    CONSTRAINT `FK_TakenTissueType_rbTissueType` FOREIGN KEY (`tissueType_id`) REFERENCES `rbTissueType` (`id`),
    CONSTRAINT `FK_TakenTissueType_rbTestTubeType` FOREIGN KEY (`testTubeType_id`) REFERENCES `rbTestTubeType` (`id`),
    CONSTRAINT `FK_TakenTissueType_rbLaboratory` FOREIGN KEY (`laboratory_id`) REFERENCES `rbLaboratory` (`id`),
    CONSTRAINT `FK_TakenTissueType_OrgStructure` FOREIGN KEY (`orgStructure_id`) REFERENCES `OrgStructure` (`id`),
    CONSTRAINT `FK_TakenTissueType_rbUnit` FOREIGN KEY (`unit_id`) REFERENCES `rbUnit` (`id`)
)
COMMENT='Заборы ткани применяемые в типах'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
""")
    TTT_Tuples = set(TakenTissueType.itervalues())
    ActionType_TakenTissueType_id = {}
    TTT_Records = {}
    for TTT in TTT_Tuples:
        value = {
            'testTubeType_id': TTT[0],
            'tissueType_id': TTT[1],
            'amount': TTT[2],
            'unit_id': TTT[3],
            'code': u'%s_%s_%s_%s' % TTT,
        }
        print(value)
        c.execute(u"""INSERT INTO `TakenTissueType`
        (`code`, `tissueType_id`, `testTubeType_id`, `amount`, `unit_id`)
        VALUES
        (%(code)s, %(tissueType_id)s, %(testTubeType_id)s, %(amount)s, %(unit_id)s) """, value)
        for k, v in TakenTissueType.iteritems():
            if v == TTT:
                ActionType_TakenTissueType_id[k] = c.lastrowid
        TTT_Records[c.lastrowid] = TTT

    for actionType_id, TTT_id in ActionType_TakenTissueType_id.iteritems():
        data = {
            'actionType_id': actionType_id,
            'datetime': datetime.now(),
            'code': u'%s_%s_%s_%s' % tuple(TTT_Records[TTT_id])
        }
        c.execute(u"""INSERT INTO `ActionPropertyType`
        (`actionType_id`, `name`, `descr`, `typeName`, `valueDomain`, `defaultValue`, `code`, `norm`, `sex`, `age`, `readOnly`, `createDateTime`, `modifyDatetime`)
        VALUES
        (%(actionType_id)s, 'Биоматериал', 'Биоматериал', 'Tissue', %(code)s, '', 'tissue', '', 0, '', 1, %(datetime)s, %(datetime)s)""",
                  data)
        propertyType_id = c.lastrowid
        c.execute(
            u"""SELECT `id`, `takenTissueJournal_id` FROM `Action` WHERE `actionType_id` = %(actionType_id)s""", data)
        for action_id, ttj_id in c:
            subData = {
                'action_id': action_id,
                'type_id': propertyType_id,
                'datetime': datetime.now(),
                'value': ttj_id,
            }
            c.execute(u"""INSERT INTO `ActionProperty`
            (`createDatetime`, `modifyDatetime`, `action_id`, `type_id`, `norm`)
            VALUES
            (%(datetime)s, %(datetime)s, %(action_id)s, %(type_id)s, '')
            """, subData)
            subData['id'] = c.lastrowid
            c.execute(u"""INSERT INTO `ActionProperty_Integer`
            (`id`, `index`, `value`)
            VALUES
            (%(id)s, 0, %(value)s)
            """, subData)
    # Вытаскиваем какие-нибудь данные из Tissue
    c.execute(u"""INSERT INTO `TakenTissueJournal`
    (`client_id`, `tissueType_id`, `externalId`, `datetimeTaken`, `note`, `barcode`, `period`)
    (SELECT `Event`.`client_id`, `Tissue`.`type_id`, '', `Tissue`.`date`, '', `Tissue`.`barcode`, 0
        FROM `Tissue`
        JOIN `Event` on `Event`.`id` = `Tissue`.`event_id`)""")

    # И тут начинается деструкция
    c.execute(u"""ALTER TABLE `ActionType`
    DROP FOREIGN KEY `rbTestTubeType_id_fk`,
    DROP COLUMN `isRequiredTissue`,
    DROP COLUMN `testTubeType_id`;""")
    c.execute(u"""ALTER TABLE `Action`
    DROP COLUMN `takenTissueJournal_id`,
    DROP FOREIGN KEY `Action_takenTissueJournal_id`;""")
    c.execute(u"""DROP TABLE `ActionType_TissueType`;""")
    c.execute(u"""DROP TABLE `ActionTissue`;""")
    c.execute(u"""DROP TABLE `Tissue`;""")
    c.close()


def downgrade(conn):
    pass