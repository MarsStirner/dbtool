#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import sys


__doc__ = '''\
Миграция расписания (с Event-Action-Properties на Schedule-Ticket)
'''

MIN_SCHEMA_VERSION = 188

def all_in(who, where):
    return all((i in where) for i in who)


def upgrade(conn):
    # import pprint
    # reasons = open('why.txt', 'wt')
    # pp = pprint.PrettyPrinter(indent=4, stream=reasons)

    import datetime

    create_schedule = """
    INSERT INTO Schedule (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, person_id, `date`,
    receptionType_id, begTime, endTime, numTickets, office_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    create_schedule_empty = """
    INSERT INTO Schedule (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, person_id, `date`,
    reasonOfAbsence_id, begTime, endTime)
    VALUES (%s, %s, %s, %s, %s, %s, %s, '00:00', '00:00')
    """

    create_ticket = """
    INSERT INTO ScheduleTicket (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, schedule_id,
    begTime, endTime, attendanceType_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    create_client_ticket = """
    INSERT INTO ScheduleClientTicket (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, client_id,
    ticket_id, appointmentType_id, infisFrom, deleted)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    def get_office_id(office_name):
        if office_name:
            if not office_name in Office:
                oc = conn.cursor()
                oc.execute('INSERT INTO Office (`code`, `name`) VALUES (%s, "")', (office_name,))
                Office[office_name] = oc.lastrowid
            return Office[office_name]



    # Предзагрузка справочников:
    c = conn.cursor()
    c.execute("SELECT code, id FROM rbReceptionType")
    rbReceptionType = dict(result for result in c)
    c.close()
    c = conn.cursor()
    c.execute("SELECT code, id FROM rbAppointmentType")
    rbAppointmentType = dict(result for result in c)
    c.close()
    c = conn.cursor()
    c.execute("SELECT code, id FROM rbAttendanceType")
    rbAttendanceType = dict(result for result in c)
    c.close()
    c = conn.cursor()
    c.execute("SELECT code, id FROM Office")
    Office = dict(result for result in c)
    c.close()

    print(u'Загрузка списка расписаний...')
    ca = conn.cursor()
    rowcount = ca.execute("""SELECT `Action`.id,
        `Action`.createDatetime, `Action`.createPerson_id, `Action`.modifyDateTime, `Action`.modifyPerson_id,
        `Event`.setPerson_id, `Event`.setDate,
        ActionType.code, Person.maxOverQueue, Person.maxCito
    FROM `Action`
    JOIN `Event` ON `Event`.`id` = `Action`.`event_id`
    JOIN `EventType` ON `EventType`.`id` = `Event`.`eventType_id`
    JOIN `ActionType` ON `ActionType`.`id` = `Action`.`actionType_id`

    JOIN Person ON Person.id = Event.setPerson_id

    WHERE `EventType`.`code` = '0' AND `Action`.deleted = 0""")
    print(u'прочитано расписаний: %s' % rowcount)

    # Проход по каждому расписанию
    for processed, (aid, cdt, cpid, mdt, mpid, person_id, setDate, type_code, max_extra, max_cito) in enumerate(ca):
        ap_cursor = conn.cursor()
        ap_cursor.execute("""
        SELECT ActionProperty.id, ActionPropertyType.name
            FROM ActionProperty
            JOIN ActionPropertyType ON ActionProperty.type_id = ActionPropertyType.id
        WHERE ActionProperty.action_id = %s""", (aid,))

        props = {}

        # Проход по свойствам расписания
        for ap_id, ap_name in ap_cursor:
            ap_val_cursor = conn.cursor()
            if ap_name == 'queue':  # Записи на прём
                ap_val_cursor.execute("""
                    SELECT ActionProperty_Action.value, ActionProperty_Action.index,
                    ActionType.code, Action.AppointmentType, Action.pacientInQueueType,
                    Event.client_id, Client.id, TIME(Action.directionDate), Action.deleted,
                    Action.createDatetime, Action.createPerson_id, Action.modifyDatetime, Action.modifyPerson_id,
                    Action.hospitalUidFrom
                    FROM ActionProperty_Action
                    JOIN Action ON Action.id = ActionProperty_Action.value
                    JOIN ActionType ON ActionType.id = Action.actionType_id
                    JOIN Event ON Event.id = Action.event_id
                    LEFT JOIN Client ON Client.id = Event.client_id
                    WHERE ActionProperty_Action.id = %s
                """, (ap_id, ))
                props['queue'] = list(ap_val_cursor)
            elif ap_name == 'times':  # запланированные тикеты
                ap_val_cursor.execute("""
                    SELECT ActionProperty_Time.value
                    FROM ActionProperty_Time
                    WHERE ActionProperty_Time.id = %s
                    ORDER BY ActionProperty_Time.index
                """, (ap_id, ))
                result = list(ap_val_cursor)
                if result:
                    props[ap_name] = [i[0] for i in result]
            elif ap_name[3:7] == 'Time':  # Времена начала, конца периодов
                ap_val_cursor.execute("""
                    SELECT ActionProperty_Time.value
                    FROM ActionProperty_Time
                    WHERE ActionProperty_Time.id = %s
                """, (ap_id, ))
                result = list(ap_val_cursor)
                if result:
                    props[ap_name] = result[0][0]
            elif ap_name.startswith('office'):  # Кабинет
                ap_val_cursor.execute("""
                    SELECT ActionProperty_String.value
                    FROM ActionProperty_String
                    WHERE ActionProperty_String.id = %s
                """, (ap_id, ))
                result = list(ap_val_cursor)
                if result:
                    props[ap_name] = result[0][0]
            elif ap_name == 'reasonOfAbsence':  # Причины отсутствия
                if ap_val_cursor.execute("""
                    SELECT ActionProperty_rbReasonOfAbsence.value
                    FROM ActionProperty_rbReasonOfAbsence
                    WHERE ActionProperty_rbReasonOfAbsence.id = %s
                    """, (ap_id, )):
                    props[ap_name] = list(ap_val_cursor)[0][0]
            ap_val_cursor.close()

        # В одном расписании старого типа может быть 2 расписания нового
        scheds = []

        if 'reasonOfAbsence' in props:
            scheds.append({
                'reasonOfAbsence': props['reasonOfAbsence']
            })
            sys.stdout.write(b'>')
        elif 'times' in props:
            times = props['times']
            queue = props.get('queue', [])
            cito = [p for p in queue if p[4] == 1]
            len_cito = len(cito)
            len_times = len(times)
            extra = [p for p in queue if p[4] != 1 and (not p[7] or p[1] - len_cito >= len_times)]
            normal = [p for p in queue if p[7] and p[4] == 0 and 0 <= p[1] - len_cito < len_times]
            if all_in(('begTime1', 'endTime1', 'begTime2', 'endTime2'), props):
                intervals = [
                    (props['begTime1'], props['endTime1'], props.get('office1')),
                    (props['begTime2'], props['endTime2'], props.get('office2'))
                ]
                intervals.sort(key=lambda (beg, end, office): beg)
                if intervals[0][0] <= intervals[1][0] <= intervals[0][1]:
                    #  Объединение интервалов, ибо пересеклись
                    intervals = [(
                        min(intervals[0][0], intervals[1][0]),
                        max(intervals[0][1], intervals[1][1]),
                        intervals[0][2]
                    )]
                    sys.stdout.write(b'M')
                else:
                    sys.stdout.write(b'*')
            elif all_in(('begTime', 'endTime'), props):
                intervals = [(props['begTime'], props['endTime'], props.get('office'))]
                sys.stdout.write(b'+')
            else:
                # reasons.write(b'Some shit happened\n')
                # pp.pprint(props)
                # reasons.write(b'\n\n')
                # reasons.flush()
                sys.stdout.write(b'?')
                # Какая-то хрень в расписании и хз, что делать
                continue
            counter = len_cito  # Это постоянное смещение за счёт цито-тикетов
            for index, interval in enumerate(intervals):
                l_times = [p for p in times if interval[0] <= p < interval[1]]
                l = len(l_times)
                scheds.append({
                    'begTime': interval[0],
                    'endTime': interval[1],
                    'office': get_office_id(interval[2]),
                    'times': l_times,
                    'queue': [(p, p[1] - counter) for p in normal if counter <= p[1] < counter + l],
                    'cito': cito if not index else [],
                    'extra': extra if not index else [],
                    'max_cito': max_cito if not index else 0,
                    'max_extra': max_extra if not index else 0,
                })
                counter += l
        else:
            # if props:
            #     reasons.write(b'Strange empty Action\n')
            #     pp.pprint(props)
            #     reasons.write(b'\n\n')
            #     reasons.flush()
            sys.stdout.write(b'-')

        if not ((processed+1) % 80):
            sys.stdout.write(b'\n')

        for sched in scheds:
            ticket_ids_normal = []
            ticket_ids_cito = []
            ticket_ids_extra = []

            # Создание расписания на день
            c = conn.cursor()
            if 'reasonOfAbsence' in sched:
                c.execute(create_schedule_empty, (
                    cdt, cpid, mdt, mpid, person_id, setDate,
                    sched['reasonOfAbsence'])
                )
                c.close()
                continue
            else:
                c.execute(create_schedule, (
                    cdt, cpid, mdt, mpid, person_id, setDate,
                    rbReceptionType.get(type_code, 'NULL'),
                    sched['begTime'], sched['endTime'], len(sched['times']), sched['office']
                ))
                schedule_id = c.lastrowid
                c.close()

            c = conn.cursor()
            # Создаём плановые тикеты
            for i, t in enumerate(sched['times']):
                dt = datetime.datetime.combine(setDate, datetime.time())
                begDateTime = dt + t
                endDateTime = dt + (sched['times'][i + 1] if i < len(sched['times']) - 1 else sched['endTime'])
                c.execute(create_ticket, (
                    cdt, cpid, mdt, mpid, schedule_id, begDateTime.time(), endDateTime.time(),
                    rbAttendanceType.get('planned')
                ))
                ticket_ids_normal.append(c.lastrowid)

            # Создаём цито тикеты
            for i in xrange(max(sched['max_cito'], len(sched['cito']))):
                c.execute(create_ticket, (
                    cdt, cpid, mdt, mpid, schedule_id, "NULL", "NULL", rbAttendanceType.get('CITO')
                ))
                ticket_ids_cito.append(c.lastrowid)

            # Создаём сверх-плановые тикеты
            for i in xrange(max(sched['max_extra'], len(sched['extra']))):
                c.execute(create_ticket, (
                    cdt, cpid, mdt, mpid, schedule_id, "NULL", "NULL", rbAttendanceType.get('extra')
                ))
                ticket_ids_extra.append(c.lastrowid)

            # Создаём плановые записи на прём
            for (action, index) in sched['queue']:
                if not action[6]:
                    print(u'Запись на приём (Action.id = %s) ссылается на несуществующего пациента (id=%s)' % (action[0], action[5]))
                else:
                    if index >= len(ticket_ids_normal):
                        print(u'oops... В расписании Action.id=%s создано записей больше, чем тикетов, '
                              u'в т.ч. сверх плана. Action.id=%s проигнорирован' % (aid, action[0]))
                    else:
                        ticket_id = ticket_ids_normal[index]
                        c.execute(create_client_ticket, (
                            action[9], action[10], action[11], action[12],
                            action[6], ticket_id, rbAppointmentType.get(action[3], None),
                            action[13] if action[13] != '0' else None, action[8]
                        ))
            for index, action in enumerate(sched['extra']):
                if not action[6]:
                    print(u'Запись на приём (Action.id = %s) ссылается на несуществующего пациента (id=%s)' % (action[0], action[5]))
                else:
                    ticket_id = ticket_ids_extra[index]
                    c.execute(create_client_ticket, (
                        action[9], action[10], action[11], action[12],
                        action[6], ticket_id, rbAppointmentType.get(action[3], None),
                        action[13] if action[13] != '0' else None, action[8]
                    ))
            for index, action in enumerate(sched['cito']):
                if not action[6]:
                    print(u'Запись на приём (Action.id = %s) ссылается на несуществующего пациента (id=%s)' % (action[0], action[5]))
                else:
                    ticket_id = ticket_ids_cito[index]
                    c.execute(create_client_ticket, (
                        action[9], action[10], action[11], action[12],
                        action[6], ticket_id, rbAppointmentType.get(action[3], None),
                        action[13] if action[13] != '0' else None, action[8]
                    ))
            c.close()

    ca.close()

    # print(u'Загрузка свойств расписаний')
    # c = conn.cursor()
    # rowcount = c.execute("""
    # SELECT ActionProperty.id, ActionPropertyType.name
    #     FROM ActionProperty
    #     JOIN ActionPropertyType ON ActionProperty.type_id = ActionPropertyType.id
    # WHERE ActionProperty.action_id IN (%s)""", (schedule_ids,))
    # print(u'Прочитано свойств: %s' % rowcount)

    # sys.exit(-1)

    conn.commit()

    global tools
