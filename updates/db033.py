# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавляем шаблон печати для журнала 001
'''
def upgrade(conn):
    sql0 = [
'''\
Insert into `rbPrintTemplate` (`code`, `name`, `context`, `fileName`, `default`, `dpdAgreement`) 
values ('001', 'Журнал 001', '-', '', 
'<HTML><BODY>{setPageSize("A4")}{setOrientation("P")}{setLeftMargin(5)}{setTopMargin(5)}{setBottomMargin(5)}{setRightMargin(5)}<TABLE BORDER=1 WIDTH="100%" cellpadding="0" cellspacing="0" STYLE="font-family: Arial; font-size: 13pt"><TR><TH align="center" rowspan=2>№ п/п</TH><TH align="center" colspan=2>Поступление</TH><TH align="center" rowspan=2>Фамилия, имя, отчество</TH><TH align="center" rowspan=2>Дата рождения</TH><TH align="center" rowspan=2>Постоянное место жительства или адрес родственников, близких и № телефона</TH><TH align="center" rowspan=2>Каким учреждением был направлен или доставлен</TH><TH align="center" rowspan=2>Отделение, в которое помещен больной</TH></TR><TR><TH align="center">Дата</TH><TH align="center">Час</TH></TR><TR><TH align="center">1</TH><TH align="center">2</TH><TH align="center">3</TH><TH align="center">4</TH><TH align="center">5</TH><TH align="center">6</TH><TH align="center">7</TH><TH align="center">8</TH></TR>{for: client in clientList}<TR><TD>{client.id}</TD><TD>{client.inDate}</TD><TD>{client.inTime}</TD><TD>{client.names}</TD><TD>{client.birthDate}</TD><TD>{client.addressPhone}</TD><TD>{client.directedBy}</TD><TD>{client.org}</TD></TR>{end:}</TABLE></BODY></HTML>', 0)
'''
    ] 
    c = conn.cursor()
    for s in sql0:
        c.execute(s)
        
def downgrade(conn):
    sql0 = [
'''\
Delete from `rbPrintTemplate` where `code` = "001"
'''
    ]
    c = conn.cursor()
    for s in sql0:
        c.execute(s)