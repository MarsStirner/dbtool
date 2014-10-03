#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
мета-информация для шаблонов печати с использованием специальных переменных
'''


def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute('''SELECT id FROM rbPrintTemplate
    where name = "Лист учета дозовых нагрузок (для текущей истории болезни)"''')
    result = c.fetchone()

    if result:
        sql = u'''
    INSERT INTO `rbPrintTemplateMeta` (`template_id`, `type`, `name`, `title`, `description`, `arguments`)
    VALUES
        ({0}, 'SpecialVariable', 'SpecialVar_rentgenind', '', '', '["id"]');'''.format(result[0])
        c.execute(sql)

    c.execute('''SELECT id FROM rbPrintTemplate
    where name = "Отчет о расходовании предмета пожертвования"''')
    result = c.fetchone()

    if result:
        sql = u'''
    INSERT INTO `rbPrintTemplateMeta` (`template_id`, `type`, `name`, `title`, `description`, `arguments`)
    VALUES
        ({0}, 'SpecialVariable', 'SpecialVar_fundreport2', '', '', '["id"]');'''.format(result[0])
        c.execute(sql)
    c.close()