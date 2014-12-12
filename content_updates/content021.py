#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Данные для противоинфекционной терапии
'''

def upgrade(conn):
    global config
    c = conn.cursor()
    c.execute('SET SQL_SAFE_UPDATES=0;')
    sql = '''
UPDATE ActionPropertyType SET valueDomain = ',Профилактика,Эмпирическая,Целенаправленная' WHERE code = 'infectTherapyType';
'''
    c.execute(sql)

    sql = '''
UPDATE ActionPropertyType SET valueDomain = ',Амбизом, Амикацин, Амоксиклав, Амоксициллина клавуланат, Амфолип, Аугментин, Ацикловир, Бисептол, Ванкомицин, Вифенд, Дифлюкан, Дориппрекс, Зивокс, Зиннат, Зовиракс, Изониазид, Кансидас, Кларитро/Азитромицин, Клиндамицин, Колистин, Максипим, Метроджил, Меронем, Метронидазол, Микамин, Микосист, Ноксафил, Панцеф, Роцефин, Сульперазон, Тазоцин, Тиенам, Флюконазол, Флагил, Фортум, Фторхинолоны, Цимевен, Эраксис, Эдицин' WHERE code = 'infectDrugName';
'''
    c.execute(sql)    

    c.execute('SET SQL_SAFE_UPDATES=1;')

    c.close()
