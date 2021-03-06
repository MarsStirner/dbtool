#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Добавление справочника способов приема лекарственных средств
- Корректировка кодов и флеткодов AT, APT, связанных с назначениями
- Корректировка типов действий и типов свойств назначений для работы с новым справочником
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    sql = u'''
CREATE  TABLE `rbMethodOfAdministration` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `code` VARCHAR(16) NOT NULL COMMENT 'Код' ,
  `name` VARCHAR(64) NOT NULL COMMENT 'Наименование' ,
  PRIMARY KEY (`id`) ,
  INDEX `code` (`code` ASC) ,
  INDEX `name` (`name` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Способы ввода лекарственных препаратов';
'''
    c.execute(sql)

    sql = u'''INSERT IGNORE INTO `rbMethodOfAdministration` (`code`,`name`) VALUES (%s, %s);'''
    data = [('IV', u'внутривенно'),
            ('PO', u'внутрь'),
            ('IM', u'внутримышечно'),
            ('SC', u'подкожно'),
            ('AP', u'местное'),
            ('IN', u'интраназально'),
            ('IT', u'интратекальное'),
            ('IO', u'в конъюнктивальный мешок'),
            ('B', u'полоскание'),
            ('ID', u'внутрикожно'),
            ('IH', u'ингаляция'),
            ('IA', u'внутриартериально'),
            ('IP', u'внутрибрюшное'),
            ('IS', u'внутрисуставное'),
            ('NG', u'назогастрально'),
            ('GU', u'оросительный'),
            ('TP', u'наружно'),
            ('PR', u'ректально'),
            ('OTHER', u'Другое'),

            ('DT', u'стоматологический'),
            ('GTT', u'GASTRONOMY TUBE'),
            ('IC', u'внутрисердечно'),
            ('NS', u'назально'),
            ('OP', u'офтальмологическое'),
            ('OT', u'ушное'),
            ('SL', u'подъязычное'),
            ('TD', u'трансдермальное'),
            ('TL', u'межъязыковой'),
            ('UR', u'уретрально'),
            ('VG', u'вагинально'),
            ]
    c.executemany(sql, data)

    # Исправление флеткодов для Анальгезия, Инфузионная терапия, Химиотерапии
    sql = u'''UPDATE ActionType SET flatCode='%s' WHERE flatCode='%s' AND name='%s' ''' % ('analgesia', 'prescription', u'Анальгезия')
    c.execute(sql)
    sql = u'''UPDATE ActionType SET flatCode='%s' WHERE flatCode='%s' AND name='%s' ''' % ('infusion', 'prescription', u'Инфузионная терапия')
    c.execute(sql)
    sql = u'''UPDATE ActionType SET flatCode='%s' WHERE flatCode='%s' AND name='%s' ''' % ('chemotherapy', 'prescription', u'Химиотерапия')
    c.execute(sql)

    moa_code = 'moa'
    voa_code = 'voa'
    moa_name = u"Способ введения"
    voa_name = u"Скорость введения"

    prescription_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'prescription\'')
    if prescription_at_id:
        sql = u'''UPDATE ActionType SET name='%s' WHERE id=%d''' % (u'Терапия', prescription_at_id)
        c.execute(sql)
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (moa_code, prescription_at_id, moa_name)
        c.execute(sql)
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (voa_code, prescription_at_id, voa_name)
        c.execute(sql)

        vd = 'rbMethodOfAdministration; IV, PO, IM, SC, AP, IN, IT, IO, B, ID, IH, IA, IP, IS, NG, GU, TP, PR, OTHER'
        sql = u'''UPDATE ActionPropertyType
SET valueDomain='%s', typeName='%s' WHERE actionType_id=%d AND code='%s'
''' % (vd, 'ReferenceRb', prescription_at_id, moa_code)
        c.execute(sql)

    analgesia_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'analgesia\'')
    if analgesia_at_id:
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (moa_code, analgesia_at_id, moa_name)
        c.execute(sql)
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (voa_code, analgesia_at_id, voa_name)
        c.execute(sql)

        vd = 'rbMethodOfAdministration; IV, PO, IM, SC, AP, IN, IT, IO, B, ID, IH, IA, IP, IS, NG, GU, TP, PR, OTHER'
        sql = u'''UPDATE ActionPropertyType
SET valueDomain='%s', typeName='%s' WHERE actionType_id=%d AND code='%s'
''' % (vd, 'ReferenceRb', analgesia_at_id, moa_code)
        c.execute(sql)

    infusion_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'infusion\'')
    if infusion_at_id:
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (moa_code, infusion_at_id, moa_name)
        c.execute(sql)
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (voa_code, infusion_at_id, voa_name)
        c.execute(sql)

        vd = 'rbMethodOfAdministration; IV, PO, IA, OTHER'
        sql = u'''UPDATE ActionPropertyType
SET valueDomain='%s', typeName='%s' WHERE actionType_id=%d AND code='%s'
''' % (vd, 'ReferenceRb', infusion_at_id, moa_code)
        c.execute(sql)

    chemotherapy_at_id = tools.checkRecordExists(c, 'ActionType', 'flatCode=\'chemotherapy\'')
    if chemotherapy_at_id:
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (moa_code, chemotherapy_at_id, moa_name)
        c.execute(sql)
        sql = u'''UPDATE ActionPropertyType SET code='%s' WHERE actionType_id=%d AND name='%s' ''' % (voa_code, chemotherapy_at_id, voa_name)
        c.execute(sql)

        vd = 'rbMethodOfAdministration; IV, PO, IM, SC, IT, IA, IP, IS, NG, TP, PR, OTHER'
        sql = u'''UPDATE ActionPropertyType
SET valueDomain='%s', typeName='%s' WHERE actionType_id=%d AND code='%s'
''' % (vd, 'ReferenceRb', chemotherapy_at_id, moa_code)
        c.execute(sql)

    c.close()


def downgrade(conn):
    pass
