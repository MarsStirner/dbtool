#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Создание типов действий, связанных с родами
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    # Корневой узел родов во вкладке Медицинские документы
    chbirth_id = tools.addNewActionType(c, class_=0,
                                        name="'Роды (документы)'",
                                        title="'Роды (документы)'",
                                        code="'24_02'",
                                        flatCode="'ChBirth'",
                                        sex=2,)
    perform_birthinfo_upgrade(c, chbirth_id)
    perform_childinfo_upgrade(c, chbirth_id)
    perform_abortioninfo_upgrade(c, chbirth_id)

    c.close()

def perform_birthinfo_upgrade(c, parent_at_id):
    # Сведения о родах
    chbirthinfo_id = tools.addNewActionType(c, class_=0,
                                            group_id=parent_at_id,
                                            name="'Сведения о родах'",
                                            title="'Сведения о родах'",
                                            code="'27_01'",
                                            flatCode="'СhildbirthInfo'",
                                            sex=2,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'Date'",
                                   name="'Дата поступления'",
                                   descr="'Дата поступления'",
                                   code="'entrdate'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'Time'",
                                   name="'Время поступления'",
                                   descr="'Время поступления'",
                                   code="'entrtime'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'Organisation'",
                                   name="'Принявшее ЛПУ'",
                                   descr="'Принявшее ЛПУ'",
                                   code="'pci'",
                                   valueDomain="'ЛПУ'",
                                   mandatory=1)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'Date'",
                                   name="'Дата родов'",
                                   descr="'Дата родов'",
                                   code="'cbdate'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'Time'",
                                   name="'Время родов'",
                                   descr="'Время родов'",
                                   code="'cbtime'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'MKB'",
                                   name="'Основной диагноз'",
                                   descr="'Основной диагноз'",
                                   code="'gdiagnosis'", )
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'String'",
                                   name="'Исход родов'",
                                   descr="'Исход родов'",
                                   code="'result'",
                                   valueDomain='''"'Благополучное родоразрешение','Смертельный исход'"''',
                                   defaultValue="'Благополучное родоразрешение'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'String'",
                                   name="'Особенности родов'",
                                   descr="'Особенности родов'",
                                   code="'cbfeatures'",
                                   valueDomain='''"'Самопроизвольные','Индуцированные'"''',
                                   defaultValue="'Самопроизвольные'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'String'",
                                   name="'Вид родов'",
                                   descr="'Вид родов'",
                                   code="'cbtype'",
                                   valueDomain='''"'Одноплодные','Многоплодные'"''',
                                   defaultValue="'Одноплодные'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'String'",
                                   name="'Роды'",
                                   descr="'Роды'",
                                   code="'complication'",
                                   valueDomain='''"'без осложнений','с осложнениями'"''',
                                   defaultValue="'без осложнений'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'String'",
                                   name="'Операции'",
                                   descr="'Операции'",
                                   code="'operations'",
                                   valueDomain='''"'Нет','Были осуществлены'"''',
                                   defaultValue="'Нет'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chbirthinfo_id,
                                   typeName="'String'",
                                   name="'Кесарево сечение'",
                                   descr="'Кесарево сечение'",
                                   code="'cesareanSection'",
                                   valueDomain='''"'в н.м. сегменте','корпоральное'"''',)

def perform_childinfo_upgrade(c, parent_at_id):
    # Сведения о ребёнке
    chinfo_id = tools.addNewActionType(c, class_=0,
                                       group_id=parent_at_id,
                                       name="'Сведения о ребёнке'",
                                       title="'Сведения о ребёнке'",
                                       code="'28_01'",
                                       flatCode="'ChildInfo'",
                                       sex=2,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Date'",
                                   name="'Дата рождения'",
                                   descr="'Дата рождения'",
                                   code="'bdate'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Time'",
                                   name="'Время рождения'",
                                   descr="'Время рождения'",
                                   code="'btime'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Integer'",
                                   name="'На какой неделе родился'",
                                   descr="'На какой неделе родился'",
                                   code="'bweek'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'String'",
                                   name="'Живой'",
                                   descr="'Живой'",
                                   code="'isAlive'",
                                   valueDomain='''"'Да','Нет'"''',
                                   defaultValue="'Да'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'String'",
                                   name="'Степень доношенности'",
                                   descr="'Степень доношенности'",
                                   code="'full-term'",
                                   valueDomain='''"'недоношенный', 'доношенный','переношенный'"''',
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'String'",
                                   name="'Пол'",
                                   descr="'Пол'",
                                   code="'gender'",
                                   valueDomain='''"'Мужской','Женский'"''',
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Integer'",
                                   name="'Длина (см)'",
                                   descr="'Длина (см)'",
                                   code="'length'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Double'",
                                   name="'Масса (г)'",
                                   descr="'Масса (г)'",
                                   code="'weight'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Date'",
                                   name="'Дата смерти'",
                                   descr="'Дата смерти'",
                                   code="'ddate'",) 
    tools.addNewActionPropertyType(c, actionType_id=chinfo_id,
                                   typeName="'Time'",
                                   name="'Время смерти'",
                                   descr="'Время смерти'",
                                   code="'dtime'",)

def perform_abortioninfo_upgrade(c, parent_at_id):
    # Сведения об аборте
    abortion_id = tools.addNewActionType(c, class_=0,
                                         group_id=parent_at_id,
                                         name="'Сведения об аборте'",
                                         title="'Сведения об аборте'",
                                         code="'29_01'",
                                         flatCode="'Abortion'",
                                         sex=2,)
    tools.addNewActionPropertyType(c, actionType_id=abortion_id,
                                   typeName="'MKB'",
                                   name="'Основной диагноз'",
                                   descr="'Основной диагноз'",
                                   code="'gdiagnosis'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=abortion_id,
                                   typeName="'String'",
                                   name="'Беременность закончилась'",
                                   descr="'Беременность закончилась'",
                                   code="'presult'",
                                   valueDomain='''"'Абортом'"''',
                                   defaultValue="'Абортом'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=abortion_id,
                                   typeName="'Date'",
                                   name="'Дата аборта'",
                                   descr="'Дата аборта'",
                                   code="'abdate'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=abortion_id,
                                   typeName="'Time'",
                                   name="'Время аборта'",
                                   descr="'Время аборта'",
                                   code="'abtime'",
                                   mandatory=1,)
    tools.addNewActionPropertyType(c, actionType_id=abortion_id,
                                   typeName="'String'",
                                   name="'Аборт'",
                                   descr="'Аборт'",
                                   code="'abtype'",
                                   valueDomain='''"'самопроизвольный','искусственный - по желанию женщины','искусственный - по мед.показаниям женщины','''
                                               ''''искусственный - по мед.показаниям плода','искусственный - по социальным показаниям','''
                                               ''''другие виды прерывания беременности (криминальные)','неуточненные','аборт медикаментозным методом'''
                                               ''' - по состоянию женщины',' 'аборт медикаментозным методом - по состоянию ребенка'"''',
                                   mandatory=1,)
