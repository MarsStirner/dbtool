#!/usr/bin/python
# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
from contextlib import closing, contextmanager
import os
import MySQLdb as db
from utils.tools import checkRecordExists

__doc__ = '''\
Изменения для формы 007. Создание протоколов установления смерти человека.
'''

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
    with closing(db.connect(host=params['host'],
                            port=int(params['port']),
                            user=params['username'],
                            passwd=params['password'],
                            db=params['dbname'],
                            charset='utf8',
                            use_unicode=True)) as c:
        c.autocommit(False)
        yield c


def main():
    with open_db_connection() as conn:
        conn.autocommit(False)

        try:
            with conn as cursor:
                deathProtocol_at_id = checkRecordExists(cursor, 'ActionType', 'flatCode=\'deadMan\'')
                deathProtocol_aptDate_id = checkRecordExists(cursor, 'ActionPropertyType', 'code=\'deathDate\'')
                deathProtocol_aptTime_id = checkRecordExists(cursor, 'ActionPropertyType', 'code=\'deathTime\'')

                if deathProtocol_at_id and deathProtocol_aptDate_id and deathProtocol_aptTime_id:
                    # через выписку
                    query = u'''SELECT Action.event_id, Action.directionDate, Action.begDate, Action.endDate
                        from Action
                        join ActionType on Action.actionType_id = ActionType.id
                        join ActionProperty on ActionProperty.action_id = Action.id
                        join ActionPropertyType on ActionProperty.type_id = ActionPropertyType.id
                        join ActionProperty_String on ActionProperty_String.id = ActionProperty.id
                        where ActionType.flatCode = 'leaved'
                        and ActionPropertyType.code = 'hospOutcome'
                        and ActionProperty_String.value like '%умер%'
                        and Action.deleted = 0;'''
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    # через закрытые обращения
                    query = u'''SELECT Event.id, setDate, setDate, execDate from Event
                                    join rbResult on Event.result_id = rbResult.id
                                    and Event.deleted = 0
                                    where rbResult.name like '%умер%'
                                    and Event.id not in (SELECT Action.event_id from Action
                                    join ActionType on Action.actionType_id = ActionType.id
                                    join ActionProperty on ActionProperty.action_id = Action.id
                                    join ActionPropertyType on ActionProperty.type_id = ActionPropertyType.id
                                    join ActionProperty_String on ActionProperty_String.id = ActionProperty.id
                                    where ActionType.flatCode = 'leaved'
                                    and ActionPropertyType.code = 'hospOutcome'
                                    and ActionProperty_String.value like '%умер%'
                                    and Action.deleted = 0);'''

                    cursor.execute(query)
                    rows += cursor.fetchall()
                    for row in rows:
                        # протокол
                        if row[0] and row[1] and row[2] and row[3]:
                            death_protocol = checkRecordExists(cursor, 'Action',
                                                               'actionType_id={0} and event_id = {1}'.format(deathProtocol_at_id, row[0]))
                            if death_protocol:
                                print("Для обращения {0} 'Протокол установления смерти уже создан'".format(row[0]))
                            else:
                                query = u'''
                                INSERT INTO Action
                                    (createDatetime, modifyDatetime, deleted, actionType_id, event_id,
                                    directionDate, status, isUrgent, begDate, endDate, note, coordText)
                                VALUES
                                    (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0, {0}, {1}, "{2}", 2, 0, "{3}", "{4}", "",
                                    "")
                                '''.format(deathProtocol_at_id, row[0], row[1], row[2], row[3])
                                cursor.execute(query)
                                new_a_id = cursor.lastrowid

                                # дата смерти
                                sql = u'''INSERT INTO `ActionProperty`
                                            (`createDatetime`, `modifyDatetime`, `deleted`, `action_id`, `type_id`,
                                            `norm`)
                                            VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0, {0}, {1}, '');
                                            '''.format(new_a_id, deathProtocol_aptDate_id)
                                cursor.execute(sql)
                                new_ap_id = cursor.lastrowid
                                sql = u'''INSERT INTO `ActionProperty_Date`
                                            (`id`, `index`, `value`)
                                            VALUES ({0}, '0', "{1}");
                                            '''.format(new_ap_id, row[3].strftime("%Y-%m-%d"))
                                cursor.execute(sql)

                                # время смерти
                                sql = u'''INSERT INTO `ActionProperty`
                                            (`createDatetime`, `modifyDatetime`, `deleted`, `action_id`, `type_id`,
                                            `norm`)
                                            VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0, {0}, {1}, '');
                                            '''.format(new_a_id, deathProtocol_aptTime_id)
                                cursor.execute(sql)
                                new_ap_id = cursor.lastrowid
                                sql = u'''INSERT INTO `ActionProperty_Time`
                                            (`id`, `index`, `value`)
                                            VALUES ({0}, '0', "{1}");
                                            '''.format(new_ap_id, row[3].strftime("%H:%M:%S"))
                                cursor.execute(sql)
                        else:
                            if row[0]:
                                print(u'''Необходимо проверить обращение {0} и, при необходимости, создать
                                      "протокол установления смерти" вручную'''.format(row[0]))
                else:
                    print(u'Тип действия "Протокол установления смерти" не создан или создан некорректно')
#                 raise RuntimeError('Stopped commit intentionally')
        except:
            raise
        else:
            pass
        finally:
            cursor.close()

if __name__ == "__main__":
    main()