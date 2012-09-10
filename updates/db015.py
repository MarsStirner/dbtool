# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Вводит статус анализа. Добавляет справочник статусов анализа. Вводит соответствующий тип свойства действия для типа действия анализ.
'''

sqlCreateRbAnalysisStatusTable = '''\
CREATE  TABLE `rbAnalysisStatus` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `statusName` VARCHAR(80) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `statusName_UNIQUE` (`statusName` ASC) ,
  INDEX `statusNameIndex` (`statusName` ASC) )
ENGINE = MyISAM
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci
'''

sqlInsertIntoRbAnalysisStatus = '''\
INSERT INTO `rbAnalysisStatus` (statusName) VALUES ('%s');
'''

analysisStatuses = [
'Назначен',
'Начат',      # (выполнен забор материала)
'В ожидании', # (материал дошел до лаборатории)
'Отменен',
'Закончен'
]

defaultStatusId = 1

statusActionPropertyName = u'Статус анализа'

sqlSelectAnalysisActionTypes = '''\
SELECT id FROM `ActionType` at
WHERE (at.class = 1) AND
EXISTS (SELECT * FROM ActionPropertyType apt WHERE apt.actionType_id = at.id);
'''

sqlInsertActionPropertyType = u'''\
        INSERT INTO `ActionPropertyType`
            (actionType_id, name, typeName,
             descr, valueDomain, defaultValue, norm, sex, age)
        VALUES
            ({actionTypeId}, '{name}', 'AnalysisStatus', '', '', '{defaultStatus}', '', 0, '')
'''

sqlSelectActionByActionTypes = u'''\
SELECT id, createPerson_id, createDateTime, modifyPerson_id, modifyDateTime, actionType_id
FROM `Action` WHERE actionType_id IN ({idStr})
'''

sqlInsertActionProperty = u'''\
INSERT INTO `ActionProperty`
(action_id, type_id, createDatetime, createPerson_id, modifyDatetime,
modifyPerson_id, norm)
VALUES
({actionId}, {typeId}, '{createDateTime}', {createPersonId}, '{modifyDateTime}',
{modifyPersonId}, '')
'''

sqlInsertAPInteger = u'''\
INSERT INTO `ActionProperty_Integer`
(id, `index`, value)
VALUES
({id}, 0, {statusId})
'''

sqlDropAnalysisStatusTable = '''\
DROP TABLE `rbAnalysisStatus`
'''

sqlDeleteActionPropertyType = u'''\
DELETE FROM `ActionPropertyType`
WHERE name = '{name}'
'''

sqlSelectActionProperty = u'''\
SELECT ap.id FROM `ActionProperty` ap, `ActionPropertyType` apt
WHERE ap.type_id = apt.id AND apt.name = '{name}'
'''

sqlDeleteActionProperty = u'''\
DELETE FROM `ActionProperty`
WHERE id = {id}
'''

sqlDeleteActionPropertyInteger = u'''\
DELETE FROM `ActionProperty_Integer`
WHERE id = {id}
'''

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def execute(conn, sql):
    c = conn.cursor()
    c.execute(sql)

def insert(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    sqlLastInsertedId = "SELECT LAST_INSERT_ID()"
    c.execute(sqlLastInsertedId)
    result = c.fetchone()
    return result[0]

def upgrade(conn):
    execute(conn, sqlCreateRbAnalysisStatusTable);

    for status in analysisStatuses:
        sqlInsertStatus = sqlInsertIntoRbAnalysisStatus % (status);
        execute(conn, sqlInsertStatus)

    # Выбираем типы действий для анализов
    rows = query(conn, sqlSelectAnalysisActionTypes)
    actionTypeIds = map(lambda r: str(r[0]), rows)
    atStr = ",".join(actionTypeIds)
    # Вставляем новые типы свойств действий
    at2apt = {}
    for r in rows:
        atId = r[0]
        aptId = insert(conn,
            sqlInsertActionPropertyType.format(
                actionTypeId = atId,
                name = statusActionPropertyName,
		defaultStatus = defaultStatusId))
        at2apt[atId] = aptId

    # Выбираем действия с типами из списка ранее найденных
    rows = query(conn, sqlSelectActionByActionTypes.format(idStr = atStr))
    # Добавляем новое свойство типа действия - СТАТУС АНАЛИЗА
    apIds = []
    for r in rows:
        aId = r[0]
        createPerson = r[1]
        createDate = r[2]
        modifyPerson = r[3]
        modifyDate = r[4]
        atId = r[5]
        # Получаем id типа свойства по типу действия
        aptId = at2apt[atId] 
        sql = sqlInsertActionProperty.format(
            actionId = aId,
            typeId = aptId,
            createDateTime = createDate,
            createPersonId = createPerson,
            modifyDateTime = modifyDate,
            modifyPersonId = modifyPerson
        )
        apId = insert(conn, sql)
        # Сохраняем ключ в списке ключей, чтобы потом вставлять значение
        apIds.append(apId)

    # Добавляем значения для статуса анализа
    for apId in apIds:
        execute(conn, sqlInsertAPInteger.format(id=apId, statusId=defaultStatusId))

def downgrade(conn):
    sql = sqlSelectActionProperty.format(name=statusActionPropertyName)
    # Находим ActionProperty нужного типа
    rows = query(conn, sql)
    ids = map(lambda r: r[0], rows)
    # Удаляем ActionProperty и ActionProperty_Integer
    for _id in ids:
        execute(conn, sqlDeleteActionProperty.format(id=_id))
        execute(conn, sqlDeleteActionPropertyInteger.format(id=_id))
    # Удаляем ActionPropertyType
    execute(conn, sqlDeleteActionPropertyType.format(name=statusActionPropertyName))
    # Удаляем таблицу rbAnalysisStatus
    execute(conn, sqlDropAnalysisStatusTable)


