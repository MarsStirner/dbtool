# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import MySQLdb as db


def execute(cursor, sql):
    cursor.execute(sql)

def ignore_duplicates(func):
    def wrap(cursor, sql):
        try:
            func(cursor, sql)
        except db.OperationalError as e:
            if 'Duplicate' in unicode(e):
                print(e)
                pass
            else:
                raise
    return wrap

def with_safe_updates_off(func):
    def wrap(cursor, sql):
        cursor.execute('SET SQL_SAFE_UPDATES=0;')
        func(cursor, sql)
        cursor.execute('SET SQL_SAFE_UPDATES=1;')
    return wrap

def disable_foreign_keys(func):
    def wrap(cursor, sql):
        cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
        func(cursor, sql)
        cursor.execute('SET FOREIGN_KEY_CHECKS=1;')
    return wrap

def with_empty_sql_mode(func):
    def wrap(cursor, sql):
        cursor.execute('SELECT @@local.sql_mode;')
        prev_sql_mode = cursor.fetchone()[0]
        cursor.execute("SET sql_mode=''")
        func(cursor, sql)
        cursor.execute("SET sql_mode='%s'" % prev_sql_mode)
    return wrap

def executeEx(*args, **kwargs):
    func = lambda *args: execute(*args)
    modes = kwargs.get('mode')
    if modes:
        if 'ignore_duplicates' in modes:
            func = ignore_duplicates(func)
        if 'safe_updates_off' in modes:
            func = with_safe_updates_off(func)
        if 'disable_fk' in modes:
            func = disable_foreign_keys(func)
        if 'empty_sql_mode' in modes:
            func = with_empty_sql_mode(func)

    func(*args)

def checkRecordExists(cursor, table, cond):
    cursor.execute(u'''SELECT id FROM %s WHERE %s ''' % (table, cond))
    result = cursor.fetchone()
    if result:
        id_ = int(result[0])
    else:
        id_ = None
    return id_

def addNewActionType(cursor, **kwargs):
    name = kwargs.get('name')
    class_ = kwargs.get('class_')
    if name is None or class_ is None:
        raise AttributeError('name and class_ cannot be empty')

    musthave_fields = (('createDatetime', 'CURRENT_TIMESTAMP'),
                       ('modifyDatetime', 'CURRENT_TIMESTAMP'),
                       ('class', class_), # class_ in kwargs
                       ('code', "''"),
                       ('name', name),
                       ('title', "''"),
                       ('flatCode', "''"),
                       ('sex', 0),
                       ('office', "''"),
                       ('showInForm', 0),
                       ('genTimetable', 0),
                       ('context', "''"),
                       ('defaultPlannedEndDate', "'0'"),
                       )
    other_fields = ('createPerson_id', 'modifyPerson_id', 'deleted', 'hidden', 'group_id',
                    'age_bu', 'age_bc', 'age_eu', 'age_ec', 'service_id', 'quotaType_id',
                    'amount', 'amountEvaluation', 'defaultStatus', 'defaultDirectionDate',
                    'defaultEndDate', 'defaultExecPerson_id', 'defaultPersonInEvent', 'defaultPersonInEditor',
                    'maxOccursInEvent', 'showTime', 'isMES', 'nomenclativeService_id',
                    'isPreferable', 'prescribedType_id', 'shedule_id', 'isRequiredCoordination',
                    'jobType_id', 'mnem', 'isRequiredTissue', 'testTubeType_id',)

    fields_to_sql = []
    values_to_sql = []
    for mh_field, default_val in musthave_fields:
        fields_to_sql.append(mh_field)
        if mh_field == 'class':
            mh_field += '_'
        val = kwargs.get(mh_field)
        if val is not None:
            val = val
        else:
            val = default_val
        values_to_sql.append(val)
    for o_field in other_fields:
        val = kwargs.get(o_field)
        if val is not None:
            fields_to_sql.append(o_field)
            values_to_sql.append(val)

    sql = u'''
INSERT INTO `ActionType` (%s) VALUES (%s)
''' % (','.join(map(unicode, fields_to_sql)), ','.join(map(unicode, values_to_sql)))
    cursor.execute(sql)
    return cursor.lastrowid

def addNewActionPropertyType(cursor, **kwargs):
    at_id = kwargs.get('actionType_id')
    typeName = kwargs.get('typeName')
    if at_id is None or typeName is None:
        raise AttributeError('actionTyped and typeName cannot be empty')

    musthave_fields = (('createDatetime', 'CURRENT_TIMESTAMP'),
                       ('modifyDatetime', 'CURRENT_TIMESTAMP'),
                       ('actionType_id', at_id),
                       ('idx', lambda: _countAPT(cursor, at_id)),
                       ('name', "''"),
                       ('descr', "''"),
                       ('typeName', typeName),
                       ('valueDomain', "''"),
                       ('defaultValue', "''"),
                       ('norm', "''"),
                       ('sex', 0),
                       ('age', "''"))
    other_fields = ('createPerson_id', 'modifyPerson_id', 'deleted', 'template_id', 'unit_id', 'code',
        'isVector', 'age_bu', 'age_bc', 'age_eu', 'age_ec', 'penalty', 'visibleInJobTicket', 'isAssignable',
        'test_id', 'defaultEvaluation', 'toEpicrisis', 'mandatory', 'readOnly')

    fields_to_sql = []
    values_to_sql = []
    for mh_field, default_val in musthave_fields:
        fields_to_sql.append(mh_field)
        val = kwargs.get(mh_field)
        if val is not None:
            val = val
        else:
            val = default_val
            if mh_field == 'idx':
                val = val()
        values_to_sql.append(val)
    for o_field in other_fields:
        val = kwargs.get(o_field)
        if val is not None:
            fields_to_sql.append(o_field)
            values_to_sql.append(val)

    sql = u'''
INSERT INTO `ActionPropertyType` (%s) VALUES (%s)
''' % (','.join(map(unicode, fields_to_sql)), ','.join(map(unicode, values_to_sql)))
#     print(sql)
    cursor.execute(sql)
    return cursor.lastrowid

def _countAPT(cursor, at_id):
    cursor.execute('SELECT count(*) FROM ActionPropertyType WHERE actionType_id=%d AND deleted=0' % at_id)
    count = int(cursor.fetchone()[0])
    return count

addNewActionProperty = addNewActionPropertyType # FIXME: заменить в проекте, где раньше использовалось название addNewActionProperty





