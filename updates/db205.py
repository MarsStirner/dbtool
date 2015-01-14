#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение структуры данных запросов (специальных переменных)
ОБЯЗАТЕЛЬНО выполните апдейт контента до 33 версии!!!
'''


def upgrade(conn):

    with conn as cursor:
        # Добавляем столбец с аргументами в таблицу специальных запросов
        print(u'В таблицу rbSpecialVariablesPreferences добавляется столбец arguments, в котором хранится сигнатура специального запроса')
        cursor.execute('''
ALTER TABLE `rbSpecialVariablesPreferences` ADD COLUMN `arguments` TEXT NOT NULL COMMENT 'аргументы' AFTER `name`;''')

        print(u'Добавляем тип переменной шаблона MKB')
        cursor.execute('''ALTER TABLE `rbPrintTemplateMeta` ALTER `type` DROP DEFAULT;''')
        cursor.execute('''ALTER TABLE `rbPrintTemplateMeta` CHANGE COLUMN `type` `type`
ENUM('Integer','Float','String','Boolean','Date','Time','List','Multilist','RefBook','Organisation','OrgStructure','Person','Service','SpecialVariable','MKB') NOT NULL AFTER `template_id`;
''')

        # Убираем собаку из имён аргументов специальных запросов
        print(u'Переменные в специальных запросах, имеющие собаку в начале имени теряют оную')
        cursor.execute('''UPDATE VariablesforSQL SET `name` = SUBSTRING(`name`, 2) WHERE `name` LIKE '@%';''')

        # Собираем имена аргментов специальных запросов в столбец в таблице специальных запросов
        print(u'Создаётся временная таблица sql_arguments, собирающая имена агрументов специальных запросов')
        cursor.execute('''
CREATE TEMPORARY TABLE sql_arguments
(`id` INTEGER, `args` TEXT)
    SELECT
      rbSpecialVariablesPreferences.id,
      CONCAT('[',GROUP_CONCAT(CONCAT('"', VariablesforSQL.name, '"') ORDER BY VariablesforSQL.id), ']') as args
    FROM rbSpecialVariablesPreferences
      JOIN VariablesforSQL ON VariablesforSQL.specialVarName_id = rbSpecialVariablesPreferences.id
    GROUP BY rbSpecialVariablesPreferences.id;''')
        print(u'Заполняем rbSpecialVariablesPreferences.arguments...')

        cursor.execute('''
UPDATE rbSpecialVariablesPreferences, sql_arguments SET rbSpecialVariablesPreferences.arguments = sql_arguments.args
WHERE sql_arguments.id = rbSpecialVariablesPreferences.id;''')

        print(u'Поздравляем! Таблица VariablesforSQL больше не нужна')
        print(u'Удаляется временная таблица')
        cursor.execute('DROP TABLE sql_arguments;')

def downgrade(conn):
    pass