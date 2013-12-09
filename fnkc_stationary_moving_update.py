#!/usr/bin/python
# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
from contextlib import closing, contextmanager
import logging
import sys
import os
import MySQLdb as db
from utils.tools import checkRecordExists

u"""Перенос данных об отделениях в бизнесс-процессе движений пациента в ФНКЦ."""

logging.basicConfig(
#     stream=sys.stdout,
    filename='conv_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s')

CONFIG_FILENAME = os.path.join(os.path.dirname(__file__), 'dbtool.conf')


def get_config():
    p = ConfigParser(defaults={'port': '3306'})
    p.read([CONFIG_FILENAME])
    return {
        'host': p.get(b'database', b'host'),
        'port': p.get(b'database', b'port'),
        'username': p.get(b'database', b'username'),
        'password': p.get(b'database', b'password'),
        'dbname': p.get(b'database', b'dbname'),
        'definer': p.get(b'database', b'definer'),
        'rlsPath': p.get(b'rlsConvert', 'rlsPath', b'./rlsDisk')
    }


@contextmanager
def open_db_connection():
    params = get_config()
    logging.info(u'Opening database')
    with closing(db.connect(host=params['host'],
                            port=int(params['port']),
                            user=params['username'],
                            passwd=params['password'],
                            db=params['dbname'],
                            charset='utf8',
                            use_unicode=True)) as c:
        c.autocommit(False)
        logging.info(u'Database opened')
        yield c
    logging.info(u'Database closed')

DAMAGED_EVENTS_LIST = [
    7783, 8161, 9561, 10065, 11393, 11429, 12008, 16403, 16652, 16867, 18388,
    20591, 20743, 21563, 22920, 22944, 23598, 23732, 24792, 25485, 25835, 26016,
    26066, 26465, 27341, 27703, 27802, 30497, 31308, 32237, 32345, 32444, 36598,
    36889, 44161, 48621, 59707, 63387, 63844, 65121, 66261, 66790, 67220, 67398,
    68937, 70780, 72209, 72745, 76905, 163113, 169896, 172270, 172380, 173097,
    182762, 193262, 196722, 197476, 201700, 206414, 209444, 216733, 222219, 229772,
    230550, 230775, 232456, 233409, 234389, 235059, 236180, 237422, 237491, 238926,
    241426, 241986, 242163, 245243, 249188, 249275, 14190, 18010, 20012, 20191,
    21554, 21611, 22604, 25314, 26017, 27059]

def main():
    with open_db_connection() as conn:
        conn.autocommit(False)

        try:
            with conn as cursor:
                # const:
                # Поступление
                rec_id = checkRecordExists(cursor, 'ActionType', 'flatCode = "received" AND deleted = 0')
                # Движение
                mov_id = checkRecordExists(cursor, 'ActionType', 'flatCode = "moving" AND deleted = 0')
                # Поступление, Направлен из
                rec_received_id = checkRecordExists(cursor, 'ActionPropertyType',
                    'code = "orgStructDirectedFrom" AND actionType_id=%d AND deleted = 0' % rec_id)
                # Поступление, Отделение поступления
                rec_stay_id = checkRecordExists(cursor, 'ActionPropertyType',
                    'code = "orgStructStay" AND actionType_id=%d AND deleted = 0' % rec_id)
                # Движение, Переведен из отделения
                mov_received_id = checkRecordExists(cursor, 'ActionPropertyType',
                    'code = "orgStructReceived" AND actionType_id=%d AND deleted = 0' % mov_id)
                # Приемное отделение
                admissions_os = checkRecordExists(cursor, 'OrgStructure',
                    u'name = "Приемное отделение"')
                # Дневной стационар
                dpf_os = checkRecordExists(cursor, 'OrgStructure',
                    u'name = "Дневной стационар"')
    
                logging.info('... selecting action_ids')
                sql = u"""
SELECT a1.event_id,
a1.id as rec_id,
(SELECT a2.id FROM Action a2
WHERE a2.actionType_id = (SELECT id FROM ActionType WHERE flatCode = 'moving' and deleted = 0)
AND a2.deleted = 0 AND a2.event_id = a1.event_id
ORDER BY a2.begDate LIMIT 1) as mov_id

FROM Action a1

WHERE a1.actionType_id = (SELECT id FROM ActionType WHERE flatCode = 'received' and deleted = 0)
AND a1.deleted = 0
"""
                cursor.execute(sql)
                actions = cursor.fetchall()
                total = len(actions)
                for num, (event_id, action_rec, action_mov) in enumerate(actions):
                    logging.info('')
                    logging.info('%s/%s: %s-%s-%s' % (num + 1, total, event_id, action_rec, action_mov))
                    if event_id in DAMAGED_EVENTS_LIST:
                        logging.info('PASSING BAD EVENT')
                        continue
                    if action_mov is None:
                        logging.info('No movings, passed')
                        continue
                    action_rec = int(action_rec); action_mov = int(action_mov)
                    res = getReceivedValue(cursor, action_mov, mov_received_id)
                    logging.info("result in first moving: %s" % str(res))
                    if res:
                        res = res[0]
                        # как минимум есть AP
                        if res[3] is not None and res[5] is not None:
                            # занесено какое-то value
                            os_value = res[5]
                            if os_value == admissions_os:
                                # поступление из Приемного отделения
                                insertOrUpdateProperty(cursor, action_rec, rec_stay_id, os_value)
                            else:
                                # поступление из отделения Дневной стационар
                                if os_value != dpf_os:
                                    logging.critical('bad event %s %s %s' % (event_id, action_rec, action_mov))
                                    continue
                                insertOrUpdateProperty(cursor, action_rec, rec_received_id, os_value)
                        else:
                            # есть AP, но нет value; Добавление данных в поступление, также добавление V в движение
                            os_value = admissions_os
                            insertOrUpdateProperty(cursor, action_rec, rec_stay_id, os_value)
                            ap_id = res[1]
                            insertPropertyValue(cursor, ap_id, os_value)
                            
                    else:
                        # нет вообще ничего; Добавление данных в поступление, также добавление AP, V в движение
                        os_value = admissions_os
                        insertOrUpdateProperty(cursor, action_rec, rec_stay_id, os_value)
                        insertOrUpdateProperty(cursor, action_mov, mov_received_id, os_value)

#                 raise RuntimeError('Stopped commit intentionally')
        except:
            raise
        else:
            pass
        finally:
            cursor.close()


def getReceivedValue(cursor, action_id, apt_id):
    sql = u"""
SELECT a.id, ap.id, apt.id, ap_os.id, ap_os.index, ap_os.value
FROM
Action a
LEFT JOIN ActionProperty ap ON ap.action_id = a.id
LEFT JOIN ActionPropertyType apt ON ap.type_id = apt.id
LEFT JOIN ActionProperty_OrgStructure ap_os ON ap.id = ap_os.id
WHERE
a.id = %d AND apt.id = %d
""" % (action_id, apt_id)

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def insertOrUpdateProperty(cursor, action_rec, apt_id, os_value):
    sql = u"""
SELECT ap.id, apt.id, ap_os.id, ap_os.index, ap_os.value
FROM
ActionProperty ap 
LEFT JOIN ActionPropertyType apt ON ap.type_id = apt.id
LEFT JOIN ActionProperty_OrgStructure ap_os ON ap.id = ap_os.id
WHERE
ap.action_id = %d AND apt.id = %d
""" % (action_rec, apt_id)
    cursor.execute(sql)
    existing_ap = cursor.fetchall()
    if existing_ap:
        existing_ap = existing_ap[0]
        if existing_ap[0] is not None:
            logging.critical("AP already exists, skipping")
        if existing_ap[2] is not None and existing_ap[4] is not None:
            logging.critical("APV already exists, skipping")
        elif existing_ap[2] is None and existing_ap[4] is None:
            insertPropertyValue(cursor, existing_ap[0], os_value)
        else:
            logging.critical('WARNING, BAD APV')
        
    else:
        logging.info('... inserting new Property and Value')
        insertProperty(cursor, action_rec, apt_id)
        ap_id = int(cursor.lastrowid)
        insertPropertyValue(cursor, ap_id, os_value)


def insertProperty(cursor, action_rec, apt_id):
    insert_ap_sql = u"""INSERT INTO ActionProperty (createDatetime, modifyDatetime, deleted, action_id, type_id, norm)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0, %d, %d, '')"""

    logging.info('... inserting: %s' % insert_ap_sql % (action_rec, apt_id))
    cursor.execute(insert_ap_sql % (action_rec, apt_id))

def insertPropertyValue(cursor, ap_id, os_value):
    insert_apv_sql = u"""INSERT INTO ActionProperty_OrgStructure (id, `index`, value) VALUES (%d, 0, %d)"""

    logging.info('... inserting: %s' % insert_apv_sql % (ap_id, os_value))
    cursor.execute(insert_apv_sql % (ap_id, os_value))


if __name__ == "__main__":
    main()
