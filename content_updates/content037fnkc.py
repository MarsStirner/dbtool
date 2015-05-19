#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление шаблона печати списка записанных пациентов
'''


def upgrade(conn):
    global tools
    c = conn.cursor()

    sql = '''INSERT INTO rbPrintTemplate
(`code`, `name`, `context`, `fileName`, `default`, `dpdAgreement`, `render`, `templateText`)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s);'''
    c.execute(sql, (
        '1',
        'Список записанных пациентов',
        'scheduleQueue',
        '',
        '',
        0,
        1,
        '''\
<html>
<body>
<h3>запись на амбулаторный приём</h3>
<h2>{{ person.name }}</h2>
<h3>{{ person.speciality.name }}</h3>
<h3>c {{ start_date }} по {{ end_date }}; к. {{ person.office }}</h3>
{% set tickets = schedule.getQueuedPatientsTickets(person.id, start_date, end_date) %}
<table border="1" width="100%" style="border-collapse:collapse;" cellpadding="10">
    <thead>
    <tr>
        <th width="1%">№</th>
        <th width="20%">время</th>
        <th width="39%">пациент</th>
        <th width="40%">жалобы/примечания</th>
    </tr>
    </thead>
    <tbody>
    {% for day in tickets | sort %}
    <tr>
        <td colspan="4">{{ day }}</td>
    </tr>
      {% for ticket in tickets[day] %}
    <tr>
        <td>{{ loop.index }}</td>
        <td>{% if ticket.attendance_type.code == 'planned' and ticket.begDateTime %} {{ ticket.begDateTime.time() }} {% else %} {{ ticket.attendance_type.name }} {% endif %}</td>
        <td>{{ ticket.client.full_name }}, {{ ticket.client.birth_date }}</td>
        <td>{{ ticket.record.note }}</td>
    </tr>
      {% endfor %}
    </tbody>
    {% endfor %}
</table>
</body>
</html>
'''))

    template_id = c.lastrowid

    sql = '''INSERT INTO rbPrintTemplateMeta
(`template_id`, `type`, `name`, `title`)
VALUES
(%s, %s, %s, %s);'''
    c.execute(sql, (
        template_id,
        'Date',
        'start_date',
        'Введите дату начала периода'
    ))
    c.execute(sql, (
        template_id,
        'Date',
        'end_date',
        'Введите дату конца периода'
    ))

    c.close()
