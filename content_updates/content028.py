#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import re

__doc__ = '''\
Обновление метаданных для шаблонов печати и аналитических отчётов, обновление запросов (специальных переменных)
'''

MIN_SCHEMA_VERSION = 202


def upgrade(conn):
    with conn as cursor:
        cursor.execute('SET SQL_SAFE_UPDATES=0')
        # Убираем из выборки те шаблоны печати, что не связаны со свободными отчётами
        print(u'Шаблоны печати, имеющие контекст free, но не участвующие в аналитических отчётах получают контекст free_')
        cursor.execute('''
UPDATE rbPrintTemplate SET context = 'free_'
WHERE context = 'free' AND id NOT IN (SELECT PrintTemplate_id FROM rbAnalyticalReports)''')

        # Изменяем имена шаблонам печати согласно именам отчётов
        print(u'Шаблоны, участвующие в аналитических отчётах получают имена аналитических отчётов')
        cursor.execute('''
UPDATE rbPrintTemplate, rbAnalyticalReports SET
  rbPrintTemplate.name = rbAnalyticalReports.name
WHERE rbPrintTemplate.id = rbAnalyticalReports.PrintTemplate_id''')
        print(u'Поздравляю! таблица rbAnalyticReports больше не нужна')

        # Убираем  str_to_date и собаки в именах переменных
        print(u'Удаляются собаки и преобразования дат из текстов специальных запросов...')
        dog_replacer = re.compile(ur'::?@?(\w+)', flags=re.U | re.I)
        std_replacer = re.compile(ur'str_to_date\(:(\w+),.*?\)', flags=re.U | re.I)

        print(u'...чтение...')
        cursor.execute('''SELECT `id`, `query` FROM `rbSpecialVariablesPreferences`''')
        updated = [
            (row[0], std_replacer.sub(ur':\1', dog_replacer.sub(ur':\1', row[1])))
            for row in cursor
        ]
        print(u'...запись...')
        for i, q in updated:
            # print i, 'str_to_date' in q, q
            cursor.execute('''UPDATE `rbSpecialVariablesPreferences` SET `query` = %s WHERE id = %s''', (q, i))
        cursor.execute('SET SQL_SAFE_UPDATES=1')
