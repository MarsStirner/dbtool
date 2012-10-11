#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Коллекция необходимых изменений для ЗНР по ВМП
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
CREATE ALGORITHM = UNDEFINED DEFINER=`%s`@`%s` SQL SECURITY DEFINER VIEW `vClient_Quoting_sub` AS select distinct c1.* 
from Client_Quoting c1 join Client_Quoting c2 
on c1.master_id=c2.master_id and c1.event_id=c2.event_id
 and c1.createDatetime<c2.createDatetime ;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE ALGORITHM = UNDEFINED DEFINER=`%s`@`%s` SQL SECURITY DEFINER VIEW `vClient_Quoting` AS select c0.* from Client_Quoting c0 left join 
vClient_Quoting_sub c00 on c0.id=c00.id
where c00.id is NULL ;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE ALGORITHM = UNDEFINED DEFINER=`%s`@`%s` SQL SECURITY DEFINER VIEW `vClient_Quoting_History` AS
select cq.id, p.login as modifyPerson, cq.createDatetime, cq.master_id as client_id,
cq.identifier, cq.quotaTicket, qt.name as quotaName, cq.stage, cq.directionDate, cq.freeInput,
o.shortName as organ, cq.amount, cq.MKB, qs.name as `status`, cq.request, cq.statment, cq.dateRegistration,
cq.dateEnd, os.name as orgStruct, cq.regionCode, pm.code as patientModelCode, t.code as treatmentCode,
cq.event_id
from Client_Quoting cq left join Person p on cq.createPerson_id=p.id
left join QuotaType qt on cq.quotaType_id=qt.id
left join Organisation o on cq.org_id=o.id
left join rbQuotaStatus qs on cq.`status`=qs.id
left join OrgStructure os on cq.orgStructure_id=os.id
left join rbPacientModel pm on cq.pacientModel_id=pm.id
left join rbTreatment t on cq.treatment_id=t.id 

order by client_id, cq.createDatetime DESC;
''' % (config['username'], config['host'])
    c.execute(sql)
    
    sql = u'''
CREATE TABLE `rbQuotaStatus` (
`id` INT(11) NOT NULL AUTO_INCREMENT,
`code` VARCHAR(8) NOT NULL,
`name` VARCHAR(50) NOT NULL,
PRIMARY KEY (`id`),
INDEX `code` (`code`),
INDEX `name` (`name`)
)
COMMENT='Статусы для квот'
COLLATE='utf8_general_ci'
ENGINE=InnoDB;
'''
    c.execute(sql) 
        

def downgrade(conn):
    pass
