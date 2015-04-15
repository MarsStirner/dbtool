#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление новых привилегий и их привязка к некоторым профилям. Правки по шп для кассы.
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    # добавление новых привилегий
    sql = '''INSERT INTO rbUserRight (code, name) VALUES (%s, %s);'''
    data = [
        ('evtPaymentInfoUpdate', 'Имеет возможность редактировать платежную информацию в обращении'),
    ]
    c.executemany(sql, data)

    # присвоение новых привилегий роли регистратор поликлиники (clinicRegistrator) и кассир (kassir)
    prof_id = tools.checkRecordExists(c, 'rbUserProfile', 'code = "{0}"'.format('clinicRegistrator'))
    tools.add_right(c, prof_id, 'evtPaymentInfoUpdate')
    prof_id = tools.checkRecordExists(c, 'rbUserProfile', 'code = "{0}"'.format('kassir'))
    tools.add_right(c, prof_id, 'evtPaymentInfoUpdate')
    right_exists = tools.checkRecordExists(c,
        'rbUserProfile_Right up_r JOIN rbUserRight ur ON ur.id = up_r.userRight_id',
        'up_r.master_id = {0} AND ur.code = "{1}"'.format(prof_id, 'clientEventUpdate'),
        'up_r.id'
    )
    if not right_exists:
        tools.add_right(c, prof_id, 'clientEventUpdate')

    # правки по шаблонам печати
    sql = '''UPDATE rbPrintTemplate SET templateText = '{0}', render = {1} WHERE context = '{2}' AND code = '{3}';'''
    c.execute(sql.format(
        '''\
<html>
<head>
</head>

<body style="font-family: Times New Roman; font-size: 11px">
<table cellpadding=0 cellspacing=0 width=100%>
  <tr><td align=center><h3><b>{% if payment.sum >= 0 %}Приходный{% else %}Расходный{% endif %} кассовый ордер</b></h3></td></tr>
  <tr><td>
    Пациент: {{ client.fullName }}<br>
    Дата: {{ payment.date }}<br>
    Предоставленные услуги:
  </td></tr>
  <tr>
    <td>
      <table cellpadding=0 cellspacing=0 width=100% border="1">
        <tr>
          <th width=10% align=center>№ п/п</th>
          <th width=40% align=center>Программа предоставляемых услуг</th>
          <th width=20% align=center>Стоимость</th>
          <th width=10% align=center>Кол-во</th>
          <th width=20% align=center>Сумма</th>
        </tr>
        {% set service_data = event.get_grouped_services_and_sum() %}
        {% for at_id, group_info in service_data.services.items() %}
          {% set action = group_info.services[0] %}
          {% set amount = group_info.amount %}
          {% set sum = group_info.sum %}
        <tr>
         <td align="center">{{ loop.index }}</td>
         <td>{{ action.tariff.name }}</td>
         <td>{{ action.price }}</td>
         <td>{{ amount }}</td>
         <td>{{ sum }}</td>
        </tr>
        {% endfor %}
      </table>
    </td>
  </tr>
<tr><td>Итого: <b>{{ payment.sum }}</b> руб.</td></tr>
</table>
</body>
</html>
''',
        1,
        'cashOrder',
        '1'
    ))

    sql = '''INSERT INTO rbPrintTemplate
(`code`, `name`, `context`, `fileName`, `default`, `dpdAgreement`, `render`, `templateText`)
VALUES
(%s, %s, %s, %s, %s, %s, %s, %s);'''
    c.execute(sql, (
        '2',
        'Журнал кассовых операций',
        'cashOperations',
        '',
        '',
        0,
        1,
        '''\
<html>
<head>
</head>
<body style="font-family: Times New Roman; font-size: 11px">
<h1>Журнал кассовых операций</h1>
<p>Приход: {{ metrics.income }} руб.</p>
<p>Расход: {{ metrics.expense }} руб.</p>
<table cellpadding=0 cellspacing=0 width=100% border="1">
  <tr>
    <th width=1% align=center>№</th>
    <th width=5% align=center>Дата</th>
    <th width=1% align=center>Касса</th>
    <th width=10% align=center>Кассир</th>
    <th width=1% align=center>Операция</th>
    <th width=5% align=center>Сумма</th>
    <th width=18% align=center>ФИО</th>
    <th width=7% align=center>Дата рожд.</th>
    <th width=1% align=center>Пол</th>
    <th width=15% align=center>Обращение</th>
    <th width=9% align=center>Назначено</th>
    <th width=9% align=center>Окончено</th>
    <th width=18% align=center>Врач</th>
  </tr>

  {% for payment in operations %}
  <tr>
    <td>{{ loop.index }}</td>
    <td>{{ payment.date }}</td>
    <td>{{ payment.cashBox }}</td>
    <td>{{ payment.createPerson.shortName }}</td>
    <td>{{ payment.cashOperation }}</td>
    <td>{{ payment.sum }}</td>
    <td>{{ payment.event.client.fullName }}</td>
    <td>{{ payment.event.client.birthDate }}</td>
    <td>{{ payment.event.client.sex }}</td>
    <td>{{ payment.event.eventType }}</td>
    <td>{{ payment.event.setDate.date }}</td>
    <td>{{ payment.event.execDate.date }}</td>
    <td>{{ payment.event.execPerson }}</td>
  </tr>
  {% endfor %}
</table>
</body>
</html>
'''))

    c.close()