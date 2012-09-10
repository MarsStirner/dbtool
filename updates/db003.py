# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавлена хранимая функция isOccupiedTransportable, определяющая, занята ли койка транспортабельным больным.
Изменено представление vHospitalBed с использованием этой функции.
'''


def upgrade(conn):
    sql0 = [
# Создаём хранимую функцию
'''\
DROP function IF EXISTS `isOccupiedTransportable`;
''',
'''\
CREATE FUNCTION `isOccupiedTransportable`(aHospitalBed_id INT, aDate DATETIME) RETURNS int(11)
    READS SQL DATA
    DETERMINISTIC
    COMMENT 'Returns 1 if bed is busy with transportable client, 0 otherwise'
BEGIN
    DECLARE vMaxStatus TEXT;
    SELECT APS.value INTO vMaxStatus
        FROM ActionProperty_HospitalBed
        INNER JOIN ActionProperty ON ActionProperty.id = ActionProperty_HospitalBed.id
        INNER JOIN Action ON Action.id = ActionProperty.action_id
        INNER JOIN Event  ON Event.id = Action.event_id
        INNER JOIN ActionProperty AS AP ON AP.action_id = Action.id
        INNER JOIN ActionPropertyType AS APT ON AP.type_id = APT.id
        INNER JOIN ActionProperty_String AS APS ON APS.id = AP.id
        WHERE ActionProperty_HospitalBed.value = aHospitalBed_id
          AND (Action.begDate IS NULL OR Action.begDate<=aDate)
          AND (Action.endDate IS NULL OR Action.endDate>=aDate)
          AND (Action.status IN (0, 1))
          AND Action.deleted = 0
          AND Event.deleted = 0
		 AND APT.name LIKE 'Транспортабельность%'
		 AND APS.value LIKE 'Да% '
        LIMIT 1;
    IF vMaxStatus IS NOT NULL THEN
        RETURN 1;
    END IF;
    RETURN 0;
END;
'''
    ]
    sql1 = [
# Изменяем представление для использования функции
'''\
CREATE OR REPLACE VIEW `vHospitalBed` AS
select
`OrgStructure_HospitalBed`.`id` AS `id`,
`OrgStructure_HospitalBed`.`master_id` AS `master_id`,
`OrgStructure_HospitalBed`.`idx` AS `idx`,
`OrgStructure_HospitalBed`.`code` AS `code`,
`OrgStructure_HospitalBed`.`name` AS `name`,
`OrgStructure_HospitalBed`.`isPermanent` AS `isPermanent`,
`OrgStructure_HospitalBed`.`type_id` AS `type_id`,
`OrgStructure_HospitalBed`.`profile_id` AS `profile_id`,
`OrgStructure_HospitalBed`.`relief` AS `relief`,
`OrgStructure_HospitalBed`.`schedule_id` AS `schedule_id`,
`OrgStructure_HospitalBed`.`begDate` AS `begDate`,
`OrgStructure_HospitalBed`.`endDate` AS `endDate`,
`OrgStructure_HospitalBed`.`sex` AS `sex`,
`isOccupiedTransportable`(`OrgStructure_HospitalBed`.`id`,now()) AS `isTransportable`,
`OrgStructure_HospitalBed`.`age` AS `age`,
`OrgStructure_HospitalBed`.`involution` AS `involution`,
`OrgStructure_HospitalBed`.`begDateInvolute` AS `begDateInvolute`,
`OrgStructure_HospitalBed`.`endDateInvolute` AS `endDateInvolute`,
`isHospitalBedBusy`(`OrgStructure_HospitalBed`.`id`,now()) AS `isBusy` from `OrgStructure_HospitalBed`;
''',
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)
    conn.commit()
    c = conn.cursor()
    for s in sql1:
        c.execute(s)


def downgrade(conn):
    sql = [
# Изменяем представление обратно
'''\
DROP function IF EXISTS `isOccupiedTransportable`;
''',
'''\
CREATE OR REPLACE VIEW `vHospitalBed` AS
select
`OrgStructure_HospitalBed`.`id` AS `id`,
`OrgStructure_HospitalBed`.`master_id` AS `master_id`,
`OrgStructure_HospitalBed`.`idx` AS `idx`,
`OrgStructure_HospitalBed`.`code` AS `code`,
`OrgStructure_HospitalBed`.`name` AS `name`,
`OrgStructure_HospitalBed`.`isPermanent` AS `isPermanent`,
`OrgStructure_HospitalBed`.`type_id` AS `type_id`,
`OrgStructure_HospitalBed`.`profile_id` AS `profile_id`,
`OrgStructure_HospitalBed`.`relief` AS `relief`,
`OrgStructure_HospitalBed`.`schedule_id` AS `schedule_id`,
`OrgStructure_HospitalBed`.`begDate` AS `begDate`,
`OrgStructure_HospitalBed`.`endDate` AS `endDate`,
`OrgStructure_HospitalBed`.`sex` AS `sex`,
`OrgStructure_HospitalBed`.`age` AS `age`,
`OrgStructure_HospitalBed`.`involution` AS `involution`,
`OrgStructure_HospitalBed`.`begDateInvolute` AS `begDateInvolute`,
`OrgStructure_HospitalBed`.`endDateInvolute` AS `endDateInvolute`,
`isHospitalBedBusy`(`OrgStructure_HospitalBed`.`id`,now()) AS `isBusy` from `OrgStructure_HospitalBed`;
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

