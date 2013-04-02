#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Изменение необходимое для отображения кнопки дежурного врача;
Изменение необходимое для работы справочника 'Орагнизации';
'''

templates = \
[
('__normal', u'''<html><body>
<div class="clientInfoFrame">
<p><span class="name">{{ nameText }}</span> {% if external_id %}<span class="baseInfo" style="float: right">Номер ИБ (№ обращения): <span class="value">{{ external_id }}</span></span>{% endif %}</p>
<div class="padder">
{% if hospRecord %}<p class="baseInfo">Госпитализация: <span class="value">{{ deptLabel }}</span> Койка: <span class="value">{{ bedLabel }}</span></p>{% endif %}
<p class="baseInfo">Дата рождения: <span class="value">{{ dateText }}</span> Пол: <span class="value">{{ sex }}</span> Код пациента: <span class="value">{{ clientCode }}</span></p>
{% if contractNumber %}<p class="baseInfo">Номер договора: <span class="value">{{ contractNumber }}</span></p> {% endif %}
{% if showDocs %}
<div class="docs">
    {% if phonesText %}<table><tr><td class="baseInfo">Контактный телефон:</td><td class="additionalInfo">{{ phonesText }}</td></tr></table></p>{% endif %}
    {% if regAddress %}<p class="additionalInfo">Адрес регистрации: <span>{{ regAddress }}</span></p>{% endif %}
    {% if locAddress %}<p class="additionalInfo">Адрес проживания: <span>{{ locAddress }}</span></p>{% endif %}
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

    for code, html in templates:
        sql = u'''INSERT INTO rbPrintTemplate (`context`, `code`, `default`, `render`, `name`, `fileName`, `dpdagreement`) VALUES ('__client_info', '{0}', '{1}', 1, '{0}', '', 0)
        '''.format(code, html)
        c.execute(sql)


def downgrade(conn):
    pass
