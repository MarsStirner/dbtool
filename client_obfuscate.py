#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import logging
import random
from itertools import product
from _dbtool import Session, ConfigException
from dbtool import configure_loggers


def _obfuscate_clients(db):
    cursor = db.cursor()

    sql = "SELECT `id`, lastName, firstName, patrName, sex FROM `Client`;"
    result = cursor.execute(sql)

    client_ids = {1: [], 2: []}
    lastnames = {1: list(), 2: list()}
    firstnames = {1: list(), 2: list()}
    patrnames = {1: list(), 2: list()}
    for client in cursor.fetchall():
        client_ids[client[4]].append(client[0])
        lastnames[client[4]].append(client[1])
        firstnames[client[4]].append(client[2])
        patrnames[client[4]].append(client[3])

    for gender, clients in client_ids.iteritems():
        for client_id in clients:
            sql = u"UPDATE `Client` SET `lastName` = '%s', `firstName` = '%s', `patrName` = '%s' WHERE `id` = '%i';" % (
                random.choice(lastnames[gender]),
                random.choice(firstnames[gender]),
                random.choice(patrnames[gender]),
                client_id)
            cursor.execute(sql)

    db.commit()


def _obfuscate_docs(db):
    cursor = db.cursor()

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
        cursor.execute(sql)

    db.commit()


def main():
    try:
        config_filename = os.path.join(os.path.dirname(__file__), 'dbtool.conf')
        Session.setConf(config_filename)
        log_filename = Session.getConf()['log_filename']
        configure_loggers(log_filename)
    except ConfigException, e:
        print(unicode(e))
        return None
    except IOError:
        print(u'укажите корректный путь и имя конфигурационного файла, для которого у вас есть права на запись')
        return None

    try:
        Session.checkConf()
    except ConfigException, e:
        logging.error(unicode(e))
        return None

    db = Session.getConnection()

    _obfuscate_clients(db)
    _obfuscate_docs(db)


if __name__ == '__main__':
    main()
