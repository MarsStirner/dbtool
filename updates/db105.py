#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = u'''\
Добавление двух новых типов свойств действия для типов действия amb и home
Необходимо для корректного отображение отмененных записей на прием на вкладках 'Амбулаторно' и 'На дому'
'''


def upgrade(conn):
    global config        
    c = conn.cursor()
    
    def checkRecordExists(c, table, cond):
        c.execute(u'''SELECT id FROM %s where %s ''' % (table, cond))
        result = c.fetchone()
        if result:
            id_ = int(result[0])
        else:
            id_ = None
        return id_
    
    AT_id = checkRecordExists(c, u'ActionType', u"code='amb' and group_id IS NULL")
    
    if AT_id:
        APT_id = checkRecordExists(c, u'ActionPropertyType', u"name='queueDeleted' and actionType_id=%s"%AT_id)
        if not APT_id:
            sql = u'''
            INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `name`, `descr`, `typeName`, `valueDomain`, `defaultValue`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`) 
            VALUES (0, %s, 0, 'queueDeleted', '', 'Reference', 'Action', '', 1, '', 0, '', 0, 000, 0, 000, 0, 0, 0, 0, 0, 0, 0);
        '''%AT_id
            
            c.execute(sql)
    
    AT_id = checkRecordExists(c, u'ActionType', u"code='home' and group_id IS NULL")
    if AT_id:
        APT_id = checkRecordExists(c, u'ActionPropertyType', u"name='queueDeleted' and actionType_id=%s"%AT_id)
        if not APT_id:
            sql = u'''
            INSERT INTO `ActionPropertyType` (`deleted`, `actionType_id`, `idx`, `name`, `descr`, `typeName`, `valueDomain`, `defaultValue`, `isVector`, `norm`, `sex`, `age`, `age_bu`, `age_bc`, `age_eu`, `age_ec`, `penalty`, `visibleInJobTicket`, `isAssignable`, `defaultEvaluation`, `toEpicrisis`, `mandatory`, `readOnly`) 
            VALUES (0, %s, 0, 'queueDeleted', '', 'Reference', 'Action', '', 1, '', 0, '', 0, 000, 0, 000, 0, 0, 0, 0, 0, 0, 0);
            '''%AT_id
            
            c.execute(sql)
        else: 
            print('exists')
    
    c.close()
    
def downgrade(conn):
    pass
