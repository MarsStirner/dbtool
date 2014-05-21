#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Миграция расписания (с Event-Action-Properties на Schedule-Ticket)
'''

MIN_SCHEMA_VERSION = 175


def upgrade(conn):
    import datetime

    print(u'Этап 1')
    first_step_sql = """
    SELECT
        `Action`.id, `Action`.createDatetime, `Action`.createPerson_id, `Action`.modifyDateTime, `Action`.modifyPerson_id,
        `Event`.setPerson_id, `Event`.setDate,
        ActionType.code,
        ap_begTime.value, ap_endTime.value, ap_plan.value, ap_office.value,
        Person.maxOverQueue, Person.maxCito
    FROM `Action`
    JOIN `Event` ON `Event`.`id` = `Action`.`id`
    JOIN `EventType` ON `EventType`.`id` = `Event`.`eventType_id`
    JOIN `ActionType` ON `ActionType`.`id` = `Action`.`actionType_id`

    JOIN Person ON Person.id = Event.setPerson_id

    JOIN ActionProperty ap_1 ON ap_1.action_id = `Action`.id
    JOIN ActionPropertyType apt_1 ON (apt_1.id = ap_1.type_id AND apt_1.name = 'begTime')
    JOIN ActionProperty_Time ap_begTime ON ap_begTime.id = ap_1.id

    JOIN ActionProperty ap_2 ON ap_2.action_id = `Action`.id
    JOIN ActionPropertyType apt_2 ON (apt_2.id = ap_2.type_id AND apt_2.name = 'endTime')
    JOIN ActionProperty_Time ap_endTime ON ap_endTime.id = ap_2.id

    JOIN ActionProperty ap_3 ON ap_3.action_id = `Action`.id
    JOIN ActionPropertyType apt_3 ON (apt_3.id = ap_3.type_id AND apt_3.name = 'plan')
    JOIN ActionProperty_Integer ap_plan ON ap_plan.id = ap_3.id

    JOIN ActionProperty ap_4 ON ap_4.action_id = `Action`.id
    JOIN ActionPropertyType apt_4 ON (apt_4.id = ap_4.type_id AND apt_4.name = 'office')
    JOIN ActionProperty_String ap_office ON ap_office.id = ap_4.id

    WHERE `EventType`.`code` = '0' AND `Action`.deleted = 0
    """
    c = conn.cursor()
    c.execute(first_step_sql)
    schedules = dict(
        (result[0], result[1:] + ([],) + ([],))
        for result in c
    )
    c.close()

    print(u'Этап 2')
    second_step_sql = """
    SELECT
        ActionProperty.action_id,
        ActionProperty_Action.value,
        ActionProperty_Action.`index`,
        Action.AppointmentType,
        Action.pacientInQueueType,
        Event.client_id,
        Event.setDate,
        `Action`.createDatetime, `Action`.createPerson_id, `Action`.modifyDateTime, `Action`.modifyPerson_id,
        `Action`.deleted
    FROM ActionProperty
    JOIN ActionPropertyType ON (ActionPropertyType.id = ActionProperty.type_id AND ActionPropertyType.name = 'queue')
    JOIN ActionProperty_Action ON ActionProperty_Action.id = ActionProperty.id
    JOIN `Action` ON ActionProperty_Action.value = `Action`.id
    JOIN `Event` ON `Action`.event_id = `Event`.id
    WHERE ActionProperty.action_id in (
        SELECT `Action`.`id`
        FROM `Action`
        JOIN `Event` ON `Event`.`id` = `Action`.`id`
        JOIN `EventType` ON `EventType`.`id` = `Event`.`eventType_id`
        WHERE `EventType`.`code` = '0'
    )
    ORDER BY `ActionProperty`.`action_id`, ActionProperty_Action.`id`, ActionProperty_Action.`index`
    """
    c = conn.cursor()
    c.execute(second_step_sql)
    for result in c:
        aid = result[0]
        if not aid in schedules:
            continue
        schedules[aid][-1].append(result[1:])
    c.close()


    print(u'Этап 3')
    third_step_sql = """
    SELECT
        ActionProperty.action_id,
        ActionProperty_Time.`value`
    FROM ActionProperty
    JOIN ActionPropertyType ON (ActionPropertyType.id = ActionProperty.type_id AND ActionPropertyType.name = 'times')
    JOIN ActionProperty_Time ON ActionProperty_Time.id = ActionProperty.id
    WHERE ActionProperty.action_id in (
        SELECT `Action`.`id`
        FROM `Action`
        JOIN `Event` ON `Event`.`id` = `Action`.`id`
        JOIN `EventType` ON `EventType`.`id` = `Event`.`eventType_id`
        WHERE `EventType`.`code` = '0'
    )
    ORDER BY `ActionProperty`.`action_id`, ActionProperty_Time.`id`, ActionProperty_Time.`index`
    """
    c = conn.cursor()
    c.execute(third_step_sql)
    for result in c:
        aid = result[0]
        if not aid in schedules:
            continue
        schedules[aid][-2].append(result[1])
    c.close()

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

    # Action.id -> [  Action.createDatetime, Action.createPerson_id, Action.modifyDateTime, Action.modifyPerson_id,
    # Event.setPerson_id, Event.setDate,
    # ActionType.code,
    # begTime, endTime, numTickets, office,
    # [], [] ]

    create_schedule = """
    INSERT INTO Schedule (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, person_id, `date`,
    receptionType_id, begTime, endTime, numTickets, office)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    create_ticket = """
    INSERT INTO ScheduleTicket (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, schedule_id,
    begDateTime, endDatetime, attendanceType_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    create_client_ticket = """
        INSERT INTO ScheduleClientTicket (createDatetime, createPerson_id, modifyDatetime, modifyPerson_id, client_id,
        ticket_id, appointmentType_id, orgFrom_id, deleted)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

    for aid, result in schedules.iteritems():
        maxOverQueue = result[11]
        maxCito = result[12]

        cito = [action for action in result[-1] if action[3] == 1]
        cito_count = len(cito)
        extra = [action for action in result[-1] if action[3] == 2]

        c = conn.cursor()
        c.execute(create_schedule, (
            result[0], result[1], result[2], result[3], result[4], result[5],
            rbReceptionType.get(result[6], 'NULL'),
            result[7], result[8], result[9], result[10]
        ))
        schedule_id = c.lastrowid
        c.close()
        c = conn.cursor()
        ticket_ids_normal = []
        ticket_ids_cito = []
        ticket_ids_extra = []

        used_cito_tickets = 0
        used_extra_tickets = 0

        for i, t in enumerate(result[-2]):
            dt = datetime.datetime.combine(result[5], datetime.time())
            begDateTime = dt + t
            endDateTime = dt + (result[-2][i + 1] if i < len(result[-2]) - 1 else result[8])
            c.execute(create_ticket, (
                result[0], result[1], result[2], result[3], schedule_id, begDateTime, endDateTime,
                rbAttendanceType.get('planned')
            ))
            ticket_ids_normal.append(c.lastrowid)

        for i in xrange(max(maxCito, len(cito))):
            c.execute(create_ticket, (
                result[0], result[1], result[2], result[3], schedule_id, "NULL", "NULL", rbAttendanceType.get('CITO')
            ))
            ticket_ids_cito.append(c.lastrowid)

        for i in xrange(max(maxOverQueue, len(extra))):
            c.execute(create_ticket, (
                result[0], result[1], result[2], result[3], schedule_id, "NULL", "NULL", rbAttendanceType.get('extra')
            ))
            ticket_ids_extra.append(c.lastrowid)

        for action in result[-1]:
            if action[3] == 1:
                ticket_id = ticket_ids_cito[used_cito_tickets]
                if not action[10]:
                    used_cito_tickets += 1
            elif action[3] == 2:
                ticket_id = ticket_ids_extra[used_extra_tickets]
                if not action[10]:
                    used_extra_tickets += 1
            else:
                ticket_id = ticket_ids_normal[action[1] - cito_count]
            c.execute(create_client_ticket, (
                action[6], action[7], action[8], action[9],
                action[4], ticket_id, rbAppointmentType.get(action[2], 'NULL'),
                action[3] if action[3] != '0' else 'NULL', action[10]
            ))
        c.close()

    conn.commit()

    global tools