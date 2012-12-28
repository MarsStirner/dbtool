#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Скрипт помагает деперсонализировать БД.
'''

import MySQLdb
from itertools import product

# Настройки
HOST = 'localhost'
DBUSER = 'root'
DBPASSWORD = 'root'
DBNAME = 'hosp'

db = MySQLdb.connect(host=HOST, user=DBUSER, passwd=DBPASSWORD, db=DBNAME)
cursor = db.cursor()

sql = "SELECT `id` FROM `Client`;"
result = cursor.execute(sql)

client_ids = []
for id in cursor.fetchall():
    client_ids.append(id[0])

new_data_list = []
for dataline in product(u'абвгде', repeat=8):
    new_data_list.append(''.join(dataline))

for id in client_ids:
    sql = u"UPDATE `Client` SET `lastName` = '%s', `firstName` = '%s', `patrName` = '%s' WHERE `id` = '%i';" % (new_data_list[id], new_data_list[id], new_data_list[id], id)
    cursor = db.cursor()
    cursor.execute(sql)

db.commit()

# ===

sql = "SELECT `id` FROM `Person`;"
result = cursor.execute(sql)

person_ids = []
for id in cursor.fetchall():
    person_ids.append(id[0])

new_data_list = []
for dataline in product(u'едгвба', repeat=8):
    new_data_list.append(''.join(dataline))

for id in person_ids:
    sql = u"UPDATE `Person` SET `lastName` = '%s', `firstName` = '%s', `patrName` = '%s' WHERE `id` = '%i';" % (new_data_list[id], new_data_list[id], new_data_list[id], id)
    cursor = db.cursor()
    cursor.execute(sql)

db.commit()

# ===

#/* 3:44:32 PM  lolalhost */ UPDATE `ClientDocument` SET `number` = '1' WHERE `id` = '635';
sql = "SELECT `id` FROM `ClientDocument`;"
result = cursor.execute(sql)

clientdocument_ids = []
for id in cursor.fetchall():
    clientdocument_ids.append(id[0])

new_data_list = []
for dataline in product(u'123456789', repeat=6):
    new_data_list.append(''.join(dataline))

for id in clientdocument_ids:
    sql = u"UPDATE `ClientDocument` SET `number` = '%s' WHERE `id` = '%i';" % (new_data_list[id], id)
    cursor = db.cursor()
    cursor.execute(sql)

db.commit()
