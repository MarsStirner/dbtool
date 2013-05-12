#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Заведение шаблонов по умолчанию для фрейма информации о пациенте
'''

templates = \
[
('__normal', u'''<html><body>
<div class="clientInfoFrame">
<p><span class="name">{{ client.fullName }}</span>
{% if event and event.externalId %}<span class="baseInfo">Номер ИБ (№ обращения): <span class="value">{{ event.externalId }}</span></span>{% endif %}</p>
<div class="padder">
{% if deptLabel %}<p class="baseInfo">Госпитализация: <span class="value">{{ deptLabel }}</span> Койка: <span class="value">{{ bedLabel }}</span></p>{% endif %}
<p class="baseInfo">Дата рождения: <span class="value">{{ client.birthDate }} ({{ client.age }})</span>
Пол: <span class="value">{{ client.sex }}</span> Код пациента: <span class="value">{{ client.id }}</span></p>
{% if contractNumber %}<p class="baseInfo">Номер договора: <span class="value">{{ contractNumber }}</span></p> {% endif %}
{% if showDocs %}
<div class="docs">
    {% if client.phones %}<p class="additionalInfo">Контактный телефон: {{ client.phones }}</p>{% endif %}
    {% if client.regAddress %}<p class="additionalInfo">Адрес регистрации: <span>{{ client.regAddress }}</span></p>{% endif %}
    {% if client.locAddress %}<p class="additionalInfo">Адрес проживания: <span>{{ client.locAddress }}</span></p>{% endif %}

    {% if client.document %}<p class="additionalInfo">Документ удост. личность: <span>{{ client.document }}</span></p>{% endif %}
    {% if client.policy %}<p class="additionalInfo">Полис: <span>{{ client.policy }}</span></p>{% endif %}

    {% if disability %}<p class="additionalInfo">Инвалидность: <span>{{ disability }}</span></p>{% endif %}
</div>
{% endif %}
{% if agreeText %}<p class="additionalInfo">Согласие: <span class="value agreementValue">{{ agreeText }}</span></p>{% endif %}
</div>
</body></html>'''),
('__empty', u'''
<html><body><div class="clientInfoFrame">
<p><span class="name">Пациент не выбран</span></p>
</div></body></html>'''),
]


def upgrade(conn):
    global config        
    c = conn.cursor()
    c.execute(ur'''DELETE FROM rbPrintTemplate WHERE `context`='__client_info';''')
    for code, html in templates:
        sql = u'''INSERT INTO rbPrintTemplate (`context`, `code`, `default`, `render`, `name`, `fileName`, `dpdagreement`) VALUES ('__client_info', '{0}', '{1}', 1, '{0}', '', 0)
        '''.format(code, html)
        c.execute(sql)
    c.close()

def downgrade(conn):
    pass
