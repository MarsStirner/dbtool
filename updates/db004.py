# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

# from nis import cat
import re
from PyQt4.QtCore import *

__doc__ = '''\
Конвертирование значений АД из строкового представления в два значения АД верхн. и АД. нижн. типа Double.
Для каждого типа свойства действия с именем АД создается два свойства типа действия АД верх. и АД нижн.
Для каждого значения АД из ActionProperty_String
Если преобразование возможно, создаются два значения ActionProperty_Double
Если преобразование невозможно, удаляется свойство и значение,
выводится сообщение в лог.
'''

def forceString(val):
    if type(val) == QVariant:
        if  val.type() == QVariant.Date :
            val = val.toDate()
        elif val.type() == QVariant.DateTime :
            val = val.toDateTime()
        else :
            val = val.toString()
    if type(val) == QDate:
        return unicode(val.toString('dd.MM.yyyy'))
    elif type(val) == QDateTime:
        return unicode(val.toString('dd.MM.yyyy hh:mm:ss'))
    elif val == None:
        return u''
    else :
        return unicode(val)

def forceDouble(val):
    if type(val) == QVariant:
        return val.toDouble()[0]
    else:
        return float(val)

def safeToDouble(v):
    try:
        return forceDouble(v)
    except:
        return None

def toPair(v):
    lst = re.split('\W+', forceString(v))
    if len(lst) < 2:
	return None
    ret0 = safeToDouble(lst[0])
    ret1 = safeToDouble(lst[1])
    if ret0 and ret1:
	return (ret0, ret1)
    else:
        return None

sqlInsertActionProperty = '''\
    INSERT INTO `ActionProperty`
    (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, action_id, type_id, unit_id, norm)
    VALUES (NOW(), %d, NOW(), %d, %d, %d, 17, '')
'''

sqlInsertActionPropertyDouble = '''\
        INSERT INTO `ActionProperty_Double`
        (id, `index`, value)
        VALUES (%d, 0, %lf)
'''

sqlUpdateActionPropertyTypeIndex = '''\
	UPDATE `ActionPropertyType` apt
	SET idx = {index}
	WHERE apt.id = {id}
'''

sqlDeleteActionProperty = '''\
    DELETE FROM `ActionProperty`
    WHERE id = %d
'''

sqlDeleteActionPropertyString = '''\
    DELETE FROM `ActionProperty_String`
    WHERE id = %d
'''

sqlDeleteActionProperty_Person = '''\
    DELETE FROM `ActionProperty_Person`
    WHERE id = %d
'''

sqlDeleteActionPropertyType = '''\
    DELETE FROM `ActionPropertyType`
    WHERE id = %d
'''

sqlSelectActionTypes = '''\
    SELECT DISTINCT at.id FROM
        `ActionPropertyType` apt,
        `ActionType` at
    WHERE
        apt.actionType_id = at.id AND
        apt.name like 'АД%' AND
        apt.name not like 'АД верхн.%' AND
        apt.name not like 'АД нижн.%'
'''

sqlSelectStringArterialPressureValues = '''\
    SELECT a.id, apd.id, apd.value, at.id as "type_id", ap.createPerson_id, apt.id, apt.idx FROM
        `ActionPropertyType` apt,
        `ActionProperty` ap,
        `Action` a,
        `ActionProperty_String` apd,
        `ActionType` at
    WHERE
        ap.type_id = apt.id AND
        apd.id = ap.id AND
        ap.action_id = a.id AND
        a.event_id IS NOT NULL AND
        a.actionType_id = at.id AND
        apt.name like 'АД%'
'''

sqlInsertActionPropertyType = '''\
        INSERT INTO `ActionPropertyType`
            (actionType_id, name, unit_id, typeName,
             descr, valueDomain, defaultValue, norm, sex, age)
        VALUES
            (%d, '%s', 17, 'Double', '', '', '', '', 0, '')
'''

sqlSelectActionPropertiesWithNullEventId = '''\
    SELECT ap.id FROM
    `ActionProperty` ap,
    `Action` a
    WHERE
    ap.action_id = a.id AND
    a.event_id IS NULL
'''

sqlSelectActionsWithNullEventId = '''\
    SELECT a.id FROM
    `Action` a
    WHERE
    a.event_id IS NULL
'''

sqlSelectActionPropertiesWithoutAction = '''\
    SELECT ap.id FROM
    `ActionProperty` ap
    WHERE NOT EXISTS (select * from `Action` where id = ap.action_id)
'''

sqlDeleteAction = '''\
    DELETE FROM `Action`
    WHERE id = %d
'''

def deleteActionPropertiesWithNullEvent(conn):
    rows = query(conn, sqlSelectActionPropertiesWithNullEventId)
    for row in rows:
        apId = row[0]
        execute(conn, sqlDeleteActionProperty_Person % apId)
        execute(conn, sqlDeleteActionPropertyString % apId)
        execute(conn, sqlDeleteActionProperty % apId)
    rows = query(conn, sqlSelectActionsWithNullEventId)
    for row in rows:
        aId = row[0]
        execute(conn, sqlDeleteAction % aId)

def deleteActionPropertiesWithoutAction(conn):
    rows = query(conn, sqlSelectActionPropertiesWithoutAction)
    for row in rows:
        apId = row[0]
        execute(conn, sqlDeleteActionProperty_Person % apId)
        execute(conn, sqlDeleteActionPropertyString % apId)
        execute(conn, sqlDeleteActionProperty % apId)


def convertStringToDouble(conn, actionId, actionPropertyId, value, actionTypeId, personId, aptId, idx):
    try:
        pair = toPair(value)
    except:
        print("Error: actionPropertyId = %d" % actionPropertyId)
        raise
    
    if pair is None:
        print(u"Can't convert ap_id=%d at_id=%d" % (actionPropertyId, actionTypeId))
        # Удаляем старое свойство и значение
        execute(conn, sqlDeleteActionPropertyString % actionPropertyId)
        execute(conn, sqlDeleteActionProperty % actionPropertyId)
        execute(conn, sqlDeleteActionPropertyType % aptId)
	return False # Оставляем старую запись, если не смогли сконвертировать

    actionProperyTypeIdHigh = highMap[actionTypeId]
    actionProperyTypeIdLow = lowMap[actionTypeId]

    # Вставляем два новых ActionProperty
    qHigh = sqlInsertActionProperty % (personId, personId, actionId, actionProperyTypeIdHigh)
    propIdHigh = insert(conn, qHigh)
    qLow = sqlInsertActionProperty % (personId, personId, actionId, actionProperyTypeIdLow)
    propIdLow = insert(conn, qLow)

    # Вставляем значения для новых свойств
    (highPressure, lowPressure) = pair
    insert(conn, sqlInsertActionPropertyDouble % (propIdHigh, highPressure))
    insert(conn, sqlInsertActionPropertyDouble % (propIdLow, lowPressure))

    # Обновляем индекс у свойств типа АД верхн. и АД нижн.
    execute(conn, sqlUpdateActionPropertyTypeIndex.format(index=idx, id=actionProperyTypeIdHigh))
    execute(conn, sqlUpdateActionPropertyTypeIndex.format(index=idx, id=actionProperyTypeIdLow))

    # Удаляем старое свойство, значение и тип свойства
    execute(conn, sqlDeleteActionPropertyString % actionPropertyId)
    execute(conn, sqlDeleteActionProperty % actionPropertyId)
    execute(conn, sqlDeleteActionPropertyType % aptId)
    return True

pressureHigh = "АД верхн."
pressureLow = "АД нижн."

lowMap = {}
highMap = {}

def query(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows

def insert(conn, sql):
    c = conn.cursor()
    c.execute(sql)
    sqlLastInsertedId = "SELECT LAST_INSERT_ID()"
    c.execute(sqlLastInsertedId)
    result = c.fetchone()
    return result[0]

def execute(conn, sql):
    c = conn.cursor()
    c.execute(sql)

def insertActionPropertyType(conn, actionTypeId, pressureName):
    q = sqlInsertActionPropertyType % (actionTypeId, pressureName)
    return insert(conn, q)

def downgrade(conn):
    print("Object model consistency update: no downgrading supported")
    print("Skipping...")

def upgrade(conn):
    # Удаляем все action и actionProperty с event_id = NULL
    # Нет, этого делать нельзя, потому что есть ActionTemplates, у которых event_id is NULL
    # deleteActionPropertiesWithNullEvent(conn)
    # Удаляем все actionProperties без action
    # А вот это - можно удалять, ибо реальные висюки
    deleteActionPropertiesWithoutAction(conn)

    # Выбираем все actionTypeId, для которых было свойство АД
    # и создаем новые типы свойств, связанные с данным actionType
    ids = query(conn, sqlSelectActionTypes)
    for row in ids:
        actionTypeId = row[0]
        #print("actionTypeId = %d" % actionTypeId)
        idHigh = insertActionPropertyType(conn, actionTypeId, pressureHigh)
        idLow = insertActionPropertyType(conn, actionTypeId, pressureLow)
        highMap[actionTypeId] = idHigh
        lowMap[actionTypeId] = idLow

    # Выбираем строковые значения для свойства АД
    res = query(conn, sqlSelectStringArterialPressureValues)
    for row in res:
        actionId = row[0]
        actionPropertyId = row[1]
        val = row[2]
        actionTypeId = row[3]
        personId = row[4]
        aptId = row[5]
	idx = row[6]
        #print("converting actionPropertyId=%d" % actionPropertyId)
        #print(str(row))
        convertStringToDouble(conn, actionId, actionPropertyId, val, actionTypeId, personId, aptId, idx)
