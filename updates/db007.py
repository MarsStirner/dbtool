# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

# from nis import cat
import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__doc__ = '''\
Конвертирование значений ЧCC из строкового представления в тип Double.
Для каждого типа свойства действия с именем t создается свойство типа действия t
Для каждого значения ЧCC из ActionProperty_String
Если преобразование возможно, создаётся значение ActionProperty_Double
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

    val = unicode(val)

    if type(val) == QVariant:
        val = unicode(val.toString())

    td = QTextDocument()
    td.setHtml(val)
    val = unicode(td.toPlainText())

    val = val.replace(u',', u'.').strip()

    val = float(val)

    return val

def safeToDouble(v):
    try:
        return forceDouble(v)
    except:
        return None

sqlInsertActionProperty = '''\
    INSERT INTO `ActionProperty`
    (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, action_id, type_id, unit_id, norm)
    VALUES (NOW(), %d, NOW(), %d, %d, %d, 18, '')
'''

sqlInsertActionPropertyDouble = '''\
        INSERT INTO `ActionProperty_Double`
        (id, `index`, value)
        VALUES (%d, 0, %lf)
'''

sqlDeleteActionProperty = '''\
    DELETE FROM `ActionProperty`
    WHERE id = %d
'''

sqlDeleteActionPropertyString = '''\
    DELETE FROM `ActionProperty_String`
    WHERE id = %d
'''

sqlDeleteActionPropertyInteger = '''\
    DELETE FROM `ActionProperty_Integer`
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
        apt.name like 'ЧС%' AND
        apt.typeName not like 'Double'
'''

sqlSelectStringRespRateValues = '''\
    SELECT a.id, apd.id, apd.value, at.id as "type_id", ap.createPerson_id, apt.id FROM
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
        apt.name like 'ЧС%'
'''

sqlSelectIntegerRespRateValues = '''\
    SELECT a.id, apd.id, apd.value, at.id as "type_id", ap.createPerson_id, apt.id FROM
        `ActionPropertyType` apt,
        `ActionProperty` ap,
        `Action` a,
        `ActionProperty_Integer` apd,
        `ActionType` at
    WHERE
        ap.type_id = apt.id AND
        apd.id = ap.id AND
        ap.action_id = a.id AND
        a.event_id IS NOT NULL AND
        a.actionType_id = at.id AND
        apt.name like 'ЧС%'
'''


sqlInsertActionPropertyType = '''\
        INSERT INTO `ActionPropertyType`
            (actionType_id, name, unit_id, typeName,
             descr, valueDomain, defaultValue, norm, sex, age)
        VALUES
            (%d, '%s', 18, 'Double', '', '', '', '', 0, '')
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
        execute(conn, sqlDeleteActionProperty % apId)
        execute(conn, sqlDeleteActionPropertyString % apId)
    rows = query(conn, sqlSelectActionsWithNullEventId)
    for row in rows:
        aId = row[0]
        execute(conn, sqlDeleteAction % aId)

def deleteActionPropertiesWithoutAction(conn):
    rows = query(conn, sqlSelectActionPropertiesWithoutAction)
    for row in rows:
        apId = row[0]
        execute(conn, sqlDeleteActionProperty % apId)
        execute(conn, sqlDeleteActionPropertyString % apId)

def convertStringToDouble(conn, actionId, actionPropertyId, value, actionTypeId, personId, aptId):
    try:
        dbl = safeToDouble(value)
    except:
        print("Error: actionPropertyId = %d" % actionPropertyId)
        raise

    if dbl is None:
        print(u"Can't convert ap_id=%d at_id=%d" % (actionPropertyId, actionTypeId))
        # Удаляем старое свойство и значение
        execute(conn, sqlDeleteActionPropertyString % actionPropertyId)
        execute(conn, sqlDeleteActionProperty % actionPropertyId)
        execute(conn, sqlDeleteActionPropertyType % aptId)
	return False # Оставляем старую запись, если не смогли сконвертировать

    newActionPropertyTypeId = tMap[actionTypeId]

    # Вставляем новый ActionProperty
    qHigh = sqlInsertActionProperty % (personId, personId, actionId, newActionPropertyTypeId)
    propIdnew = insert(conn, qHigh)


    # Вставляем значения для новых свойств
    newT = dbl
    insert(conn, sqlInsertActionPropertyDouble % (propIdnew, newT))

    # Удаляем старое свойство, значение и тип свойства
    execute(conn, sqlDeleteActionPropertyString % actionPropertyId)
    execute(conn, sqlDeleteActionProperty % actionPropertyId)
    execute(conn, sqlDeleteActionPropertyType % aptId)

    return True

def convertIntegerToDouble(conn, actionId, actionPropertyId, value, actionTypeId, personId, aptId):
    try:
        dbl = safeToDouble(value)
    except:
        print("Error: actionPropertyId = %d" % actionPropertyId)
        raise

    if dbl is None:
        print(u"Can't convert ap_id=%d at_id=%d" % (actionPropertyId, actionTypeId))
        # Удаляем старое свойство и значение
        execute(conn, sqlDeleteActionPropertyInteger % actionPropertyId)
        execute(conn, sqlDeleteActionProperty % actionPropertyId)
        execute(conn, sqlDeleteActionPropertyType % aptId)
	return False # Оставляем старую запись, если не смогли сконвертировать

    newActionPropertyTypeId = tMap[actionTypeId]

    # Вставляем новый ActionProperty
    qHigh = sqlInsertActionProperty % (personId, personId, actionId, newActionPropertyTypeId)
    propIdnew = insert(conn, qHigh)


    # Вставляем значения для новых свойств
    newT = dbl
    insert(conn, sqlInsertActionPropertyDouble % (propIdnew, newT))

    # Удаляем старое свойство, значение и тип свойства
    execute(conn, sqlDeleteActionPropertyInteger % actionPropertyId)
    execute(conn, sqlDeleteActionProperty % actionPropertyId)
    execute(conn, sqlDeleteActionPropertyType % aptId)

    return True

temperature = "ЧСС"

tMap = {}

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
    deleteActionPropertiesWithNullEvent(conn)
    # Удаляем все actionProperties без action
    deleteActionPropertiesWithoutAction(conn)

    # Выбираем все actionTypeId, для которых было свойство ЧСС
    # и создаем новые типы свойств, связанные с данным actionType
    ids = query(conn, sqlSelectActionTypes)
    for row in ids:
        actionTypeId = row[0]
        #print("actionTypeId = %d" % actionTypeId)
        idT = insertActionPropertyType(conn, actionTypeId, temperature)
        tMap[actionTypeId] = idT

    # Выбираем строковые значения для свойства ЧСС
    res = query(conn, sqlSelectStringRespRateValues)
    for row in res:
        actionId = row[0]
        actionPropertyId = row[1]
        val = row[2]
        actionTypeId = row[3]
        personId = row[4]
        aptId = row[5]
        #print("converting actionPropertyId=%d" % actionPropertyId)
        #print(str(row))
        convertStringToDouble(conn, actionId, actionPropertyId, val, actionTypeId, personId, aptId)
    res = query(conn, sqlSelectIntegerRespRateValues)
    for row in res:
        actionId = row[0]
        actionPropertyId = row[1]
        val = row[2]
        actionTypeId = row[3]
        personId = row[4]
        aptId = row[5]
        #print("converting actionPropertyId=%d" % actionPropertyId)
        #print(str(row))
        convertIntegerToDouble(conn, actionId, actionPropertyId, val, actionTypeId, personId, aptId)
