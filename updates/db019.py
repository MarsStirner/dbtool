# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавление в таблицу ActionPropertyType поля для учета необходимости помещения \
данных свойства действия в эпикриз. \
Добавление двух таблиц ActionProperty_DiagnosticEpicrisis и \
ActionProperty_CureEpicrisis для хранения данных о диагностике и лечении \
в эпикризах соответственно.
'''


def upgrade(conn):
    # Новое поле таблицы - необходимость переноса содержимого свойства
    #  действия в эпикриз
    sqlAddEpicrisisColumn = u'''\
ALTER TABLE ActionPropertyType
    ADD COLUMN `toEpicrisis` tinyint(1) NOT NULL DEFAULT '0'
'''

    sqlCommentEpicrisisColumn = u'''\
ALTER TABLE ActionPropertyType
    CHANGE `toEpicrisis` `toEpicrisis` tinyint(1) NOT NULL DEFAULT '0'
            COMMENT 'Помещать значение свойства действия в эпикриз'
'''

    sqlCreateDiagnosticActionProperty_Type = '''\
CREATE TABLE IF NOT EXISTS `ActionProperty_DiagnosticEpicrisis` (
  `id` int(11) NOT NULL COMMENT '{ActionProperty}',
  `index` int(11) NOT NULL DEFAULT '0' COMMENT 'Индекс элемента векторного значения или 0',
  `value` text NOT NULL COMMENT 'собственно значение',
  PRIMARY KEY (`id`,`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Данные о диагостике для эпикриза'
'''

    sqlCreateCureActionProperty_Type = '''\
CREATE TABLE IF NOT EXISTS `ActionProperty_CureEpicrisis` (
  `id` int(11) NOT NULL COMMENT '{ActionProperty}',
  `index` int(11) NOT NULL DEFAULT '0' COMMENT 'Индекс элемента векторного значения или 0',
  `value` text NOT NULL COMMENT 'собственно значение',
  PRIMARY KEY (`id`,`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Данные о лечении для эпикриза'
'''

    c = conn.cursor()
    global tools
    
    tools.executeEx(c, sqlAddEpicrisisColumn, mode=['ignore_duplicates'])
    c.execute(sqlCommentEpicrisisColumn)
    c.execute(sqlCreateDiagnosticActionProperty_Type)
    c.execute(sqlCreateCureActionProperty_Type)


def downgrade(conn):
    sqlDropEpicrisisColumn = '''\
ALTER TABLE ActionPropertyType
    DROP COLUMN `toEpicrisis`
'''

    sqlDropDiagnosticActionProperty_Type = '''\
DROP TABLE `ActionProperty_DiagnosticEpicrisis`
'''


    sqlDropCureActionProperty_Type = '''\
DROP TABLE `ActionProperty_CureEpicrisis`
'''

    c = conn.cursor()

    c.execute(sqlDropEpicrisisColumn)
    c.execute(sqlDropDiagnosticActionProperty_Type)
    c.execute(sqlDropCureActionProperty_Type)
