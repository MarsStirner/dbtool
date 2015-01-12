#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


__doc__ = '''\
Шаблон печати "Маршрутные листы на опеределенную дату"
'''


def upgrade(conn):
    global tools
    c = conn.cursor()
    template_text = ur'''<html>
<head>
<body style="font-family:\'Times New Roman\'; font-size:10pt; font-weight:400; font-style:normal;">

{{ setPageSize(\'A4\') }}
{{ setOrientation(\'P\') }}
{{ setLeftMargin(20) }} {{ setTopMargin(20) }} {{ setBottomMargin(20) }} {{ setRightMargin(10) }}

{% set index = 0 %}
<table border=0 width="100%" cellpadding="0" cellspacing="0" style="font-family: \'Times New Roman\'; font-size: 12pt">
    <tr>
        <td align="center">
            {{ currentOrganisation.fullName }}
            <HR>
        </td>
    </tr>

    <tr>
        <td align="right"><span class="barcode">*{{ client.id }}*</span></td>
    </tr>

    <tr>
        <td>
            № пациента: <B>{{ client.id }}</B>
            Ф.И.О.: <B>{{ client.lastName }} {{ client.firstName }} {{ client.patrName }}</B><BR>
            Документ: <B>{{ client.document }}</B><BR/>
            Адрес: <B>{% if client.regAddress.KLADRCode ==\'\' %}{{ client.regAddress.freeInput }}{% else %}{{
            client.regAddress }}{% endif %}</B><BR/>
            Дата рождения: <B>{{ client.birthDate }}</B><BR/>
            Номер страхового полиса: <B>{{ client.policy.number }}</B><BR/>
            СМО: <B>{{ client.policy.insurer }}</B>
        </td>
    </tr>
    <tr>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            <table style="font-family: \'Times New Roman\'; font-size: 8pt; width:100%;"
                   border="1" cellpadding="0" cellspacing="0">
                <tr>

                    <td align="center" width="5%">№п/п</td>
                    <td align="center" width="15%">Дата<br/>приема/ время</td>
                    <td align="center" width="30%">Специальность</td>
                    <td align="center" width="35%"> ФИО</td>
                    <td align="center" width="15%">Кабинет</td>

                </tr>
                {% for client_ticket in client.appointments %}
                {% if client_ticket.date== routeDate %}
                {% set index = index + 1 %}
                {% set person = client_ticket.ticket.schedule.person %}
                <tr style="font-size: 12pt;">
                    <td>{{index}}</td>
                    <td><b>{{ client_ticket.date }} / {{ client_ticket.time }}</b></td>
                    <td>{{ person.speciality }}</td>
                    <td>{{ person.shortName }}</td>
                    <td>{{ person.office }}</td>
                </tr>
                {% endif %}
                {% endfor %}
            </table>

        </td>
    </tr>
</table>
</body>
</html>
    '''
    sql = '''
            INSERT INTO `rbPrintTemplate` (`code`,`name`, `context`, `templateText`, `fileName`, `default`) VALUES
            ('routeListsDate','Маршрутные листы на дату','token', '{0}', '', '');
            '''.format(template_text)
    c.execute(sql)
    template_id = c.lastrowid
    sql = '''
            INSERT INTO `rbPrintTemplateMeta` (`template_id`, `type`, `name`, `title`, `description`) VALUES
            ({0}, 'Date', 'routeDate', 'Укажите дату', '');
            '''.format(template_id)
    c.execute(sql)
    c.close()