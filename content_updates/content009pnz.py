#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
- Пенза
- Добавление справочника способов приема лекарственных средств
- Создание *новых* типов действий для назначений
'''

MIN_SCHEMA_VERSION = 130

def upgrade(conn):
    global tools
    c = conn.cursor()

#     c.execute('TRUNCATE `rbMethodOfAdministration`')
# 
#     sql = u'''INSERT IGNORE INTO `rbMethodOfAdministration` (`code`,`name`) VALUES (%s, %s);'''
#     data = [('IV', u'внутривенно'),
#             ('PO', u'внутрь'),
#             ('IM', u'внутримышечно'),
#             ('SC', u'подкожно'),
#             ('AP', u'местное'),
#             ('IN', u'интраназально'),
#             ('IT', u'интратекальное'),
#             ('IO', u'в конъюнктивальный мешок'),
#             ('B', u'полоскание'),
#             ('ID', u'внутрикожно'),
#             ('IH', u'ингаляция'),
#             ('IA', u'внутриартериально'),
#             ('IP', u'внутрибрюшное'),
#             ('IS', u'внутрисуставное'),
#             ('NG', u'назогастрально'),
#             ('GU', u'оросительный'),
#             ('TP', u'наружно'),
#             ('PR', u'ректально'),
#             ('OTHER', u'Другое'),
# 
#             ('DT', u'стоматологический'),
#             ('GTT', u'GASTRONOMY TUBE'),
#             ('IC', u'внутрисердечно'),
#             ('NS', u'назально'),
#             ('OP', u'офтальмологическое'),
#             ('OT', u'ушное'),
#             ('SL', u'подъязычное'),
#             ('TD', u'трансдермальное'),
#             ('TL', u'межъязыковой'),
#             ('UR', u'уретрально'),
#             ('VG', u'вагинально'),
#             ]
#     c.executemany(sql, data)

    'SELECT id FROM ActionType WHERE code="3_01" '

    # Терапия (Назначение)
    prescription_at_id = tools.addNewActionType(c, name="'Терапия Новая'",
                                                class_=2,
                                                title="'Назначения'",
                                                flatCode="'prescription'",
                                                mnem="'THER'",
                                                context='med_ter',)
    tools.addNewActionProperty(c, actionType_id=prescription_at_id,
                               typeName="'ReferenceRb'",
                               name="'Способ введения'",
                               descr="'Способ введения",
                               code="'moa'",
                               valueDomain="'rbMethodOfAdministration; IV, PO, IM, SC, AP, IN, IT, IO, B, ID, IH, IA, IP, IS, NG, GU, TP, PR, OTHER'",)
    tools.addNewActionProperty(c, actionType_id=prescription_at_id,
                               typeName="'String'",
                               name="'Скорость введения'",
                               descr="'Скорость введения",
                               code="'voa'",)
    # Анальгезия
    analgesia_at_id = tools.addNewActionType(c, name="'Анальгезия Новая'",
                                             class_=2,
                                             title="'Анальгезия'",
                                             flatCode="'analgesia'",
                                             mnem="'THER'",
                                             context='med_ter',)
    tools.addNewActionProperty(c, actionType_id=analgesia_at_id,
                               typeName="'ReferenceRb'",
                               name="'Способ введения'",
                               descr="'Способ введения",
                               code="'moa'",
                               valueDomain="'rbMethodOfAdministration; IV, PO, IM, SC, AP, IN, IT, IO, B, ID, IH, IA, IP, IS, NG, GU, TP, PR, OTHER'",)
    tools.addNewActionProperty(c, actionType_id=analgesia_at_id,
                               typeName="'String'",
                               name="'Скорость введения'",
                               descr="'Скорость введения",
                               code="'voa'",)
    # Инфузионная терапия
    infusion_at_id = tools.addNewActionType(c, name="'Инфузионная терапия Новая'",
                                            class_=2,
                                            title="'Инфузионная терапия'",
                                            flatCode="'infusion'",
                                            mnem="'THER'",
                                            context='med_ter',)
    tools.addNewActionProperty(c, actionType_id=infusion_at_id,
                               typeName="'ReferenceRb'",
                               name="'Способ введения'",
                               descr="'Способ введения",
                               code="'moa'",
                               valueDomain="'rbMethodOfAdministration; IV, PO, IA, OTHER'",)
    tools.addNewActionProperty(c, actionType_id=infusion_at_id,
                               typeName="'String'",
                               name="'Скорость введения'",
                               descr="'Скорость введения",
                               code="'voa'",)
    # Химиотерапия
    chemotherapy_at_id = tools.addNewActionType(c, name="'Химиотерапия Новая'",
                                                class_=2,
                                                title="'Химиотерапия'",
                                                flatCode="'chemotherapy'",
                                                mnem="'THER'",
                                                context='ximio',)
    tools.addNewActionProperty(c, actionType_id=chemotherapy_at_id,
                               typeName="'ReferenceRb'",
                               name="'Способ введения'",
                               descr="'Способ введения",
                               code="'moa'",
                               valueDomain="'rbMethodOfAdministration; IV, PO, IM, SC, IT, IA, IP, IS, NG, TP, PR, OTHER'",)
    tools.addNewActionProperty(c, actionType_id=chemotherapy_at_id,
                               typeName="'String'",
                               name="'Скорость введения'",
                               descr="'Скорость введения",
                               code="'voa'",)


    c.close()