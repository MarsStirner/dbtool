#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Форма 007
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    sqls = ( 
#----------------------------------------------------------------------------------------------------------------------------------
        u'''CREATE DEFINER=%s PROCEDURE `FIOinput007`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
              BEGIN
#Специальная переменная выводит ФИО поступивших
SET @tpl = "SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
		FROM Action 
			INNER JOIN ActionType 
			  ON Action.`actionType_id`=ActionType.`id`  
			INNER JOIN ActionProperty 
			  ON Action.`id`=ActionProperty.`action_id`  
			INNER JOIN ActionProperty_HospitalBed 
			  ON ActionProperty.`id`=ActionProperty_HospitalBed.`id`  
			INNER JOIN OrgStructure_HospitalBed 
			  ON ActionProperty_HospitalBed.`value`=OrgStructure_HospitalBed.`id`   
			INNER JOIN Event ON Action.`event_id`=Event.`id` 
			INNER JOIN EventType ON EventType.id = Event.eventType_id
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id
			INNER JOIN
				(SELECT Action.id , ActionProperty_HospitalBedProfile.value
								FROM Action
										INNER JOIN ActionType 
								  ON Action.`actionType_id`=ActionType.`id`
										INNER JOIN ActionProperty 
								  ON Action.`id`=ActionProperty.`action_id`
										INNER JOIN ActionPropertyType 
								  ON ActionPropertyType.`id`=ActionProperty.`type_id`
										INNER JOIN ActionProperty_HospitalBedProfile 
								  ON ActionProperty.`id`=ActionProperty_HospitalBedProfile.`id`
										INNER JOIN rbHospitalBedProfile 
								  ON ActionProperty_HospitalBedProfile.`value`=rbHospitalBedProfile.`id`
										WHERE (ActionType.`flatCode`='moving')
										AND (ActionPropertyType.`code`='hospitalBedProfile')
										AND ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
										AND (rbHospitalBedProfile.id IN (::@profile)) ) sz
			ON Action.id = sz.id
			INNER JOIN
				Client c
			ON c.id = Event.client_id
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` = ::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0) 
			AND (Action.id in (select id from
								(select Action.id, min(Action.id) from Action
								join ActionType
								  on Action.actionType_id = ActionType.id
								where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
								group by event_id) A))";
SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@profile",profiles);
PREPARE sqlQuery FROM  @sqlPrepare;
EXECUTE sqlQuery;
              END''' %config['definer'],

#----------------------------------------------------------------------------------------------------------------------------------
    u'''CREATE DEFINER=%s PROCEDURE `FIOinpuFrom12`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
BEGIN 
#Специальная переменная выводит ФИО поступивших из круглосуточного стационара
SET @tpl = "SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
				FROM Action 
			INNER JOIN ActionType 
			  ON Action.`actionType_id`=ActionType.`id`  
			INNER JOIN ActionProperty 
			  ON Action.`id`=ActionProperty.`action_id`  
			INNER JOIN ActionProperty_HospitalBed 
			  ON ActionProperty.`id`=ActionProperty_HospitalBed.`id`  
			INNER JOIN OrgStructure_HospitalBed 
			  ON ActionProperty_HospitalBed.`value`=OrgStructure_HospitalBed.`id`   
			INNER JOIN Event ON Action.`event_id`=Event.`id`  
			INNER JOIN EventType ON EventType.id = Event.eventType_id #только для ФНКЦ
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #только для ФНКЦ			
			INNER JOIN
				(SELECT Action.id , ActionProperty_HospitalBedProfile.value
								FROM Action
										INNER JOIN ActionType 
								  ON Action.`actionType_id`=ActionType.`id`
										INNER JOIN ActionProperty 
								  ON Action.`id`=ActionProperty.`action_id`
										INNER JOIN ActionPropertyType 
								  ON ActionPropertyType.`id`=ActionProperty.`type_id`
										INNER JOIN ActionProperty_HospitalBedProfile 
								  ON ActionProperty.`id`=ActionProperty_HospitalBedProfile.`id`
										INNER JOIN rbHospitalBedProfile 
								  ON ActionProperty_HospitalBedProfile.`value`=rbHospitalBedProfile.`id`
										WHERE (ActionType.`flatCode`='moving')
										AND (ActionPropertyType.`code`='hospitalBedProfile')
										AND ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
										AND (rbHospitalBedProfile.id IN (::@profile)) ) sz
			ON Action.id = sz.id
			INNER JOIN
				Client c
			ON c.id = Event.client_id
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` = ::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0) 
			AND (Event.id in (select Event.id
                                    from Action
                                    inner join ActionType
                                      ON Action.actionType_id = ActionType.id
                                    INNER JOIN ActionProperty
                                      ON ActionProperty.action_id = Action.id
                                    INNER JOIN ActionPropertyType
                                      ON ActionProperty.type_id = ActionPropertyType.id
                                    INNER JOIN ActionProperty_OrgStructure
                                      ON ActionProperty.id = ActionProperty_OrgStructure.id
                                    INNER JOIN OrgStructure
                                      ON ActionProperty_OrgStructure.value = OrgStructure.id
                                    inner Join Event
                                    on Action.event_id = Event.id
                                    where ActionType.flatCode = 'received'
                                      and Action.begDate is not Null
                                      and Action.deleted=0
                                      and ActionPropertyType.code = 'orgStructDirectedFrom'
                                      and OrgStructure.type = 5
                                    group by event_id))
			AND (Action.id in (select id from
                    (select Action.id, min(Action.id) from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A))";
SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@profile",profiles);
PREPARE sqlQuery FROM  @sqlPrepare;
EXECUTE sqlQuery;
              END''' %config['definer'],

#----------------------------------------------------------------------------------------------------------------------------------
    u'''CREATE DEFINER=%s PROCEDURE `FIOoutTotal`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
BEGIN
#Специальная переменная выводит ФИО выписанных
SET @tpl = "SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
				FROM Action 
			INNER JOIN ActionType 
			  ON Action.`actionType_id`=ActionType.`id`  
			INNER JOIN ActionProperty 
			  ON Action.`id`=ActionProperty.`action_id`  
			INNER JOIN ActionProperty_HospitalBed 
			  ON ActionProperty.`id`=ActionProperty_HospitalBed.`id`  
			INNER JOIN OrgStructure_HospitalBed 
			  ON ActionProperty_HospitalBed.`value`=OrgStructure_HospitalBed.`id`   
			INNER JOIN Event ON Action.`event_id`=Event.`id`  
			INNER JOIN EventType ON EventType.id = Event.eventType_id #только для ФНКЦ
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #только для ФНКЦ			
			INNER JOIN
				(SELECT Action.id , ActionProperty_HospitalBedProfile.value
								FROM Action
										INNER JOIN ActionType 
								  ON Action.`actionType_id`=ActionType.`id`
										INNER JOIN ActionProperty 
								  ON Action.`id`=ActionProperty.`action_id`
										INNER JOIN ActionPropertyType 
								  ON ActionPropertyType.`id`=ActionProperty.`type_id`
										INNER JOIN ActionProperty_HospitalBedProfile 
								  ON ActionProperty.`id`=ActionProperty_HospitalBedProfile.`id`
										INNER JOIN rbHospitalBedProfile 
								  ON ActionProperty_HospitalBedProfile.`value`=rbHospitalBedProfile.`id`
										WHERE (ActionType.`flatCode`='moving')
										AND (ActionPropertyType.`code`='hospitalBedProfile')
										AND ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
										AND (rbHospitalBedProfile.id IN (::@profile) )) sz
			ON Action.id = sz.id
			INNER JOIN
				Client c
			ON c.id = Event.client_id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` = ::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (Action.id in (select id from
                    (select max(Action.id) id from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A) ) 
			AND (Action.event_id in (select distinct Event.id
                                         from Action
                                         INNER JOIN ActionType
                                         ON Action.actionType_id = ActionType.id
                                         INNER JOIN ActionProperty
                                         ON ActionProperty.action_id = Action.id
                                         INNER JOIN Event
                                         ON Event.id = Action.event_id
                                         inner join ActionProperty_String aps
                                         on ActionProperty.id = aps.id
                                         where ActionType.flatCode = 'leaved'))
         and Action.event_id not in (
											select e.id
												from
												Event e
												inner join
													Action a
												on a.event_id = e.id
												inner join
													ActionProperty ap
												on a.id=ap.action_id
												inner join
													ActionProperty_Date apd
												on ap.id = apd.id
												inner join
													ActionProperty ap1
												on a.id=ap1.action_id	
												inner join
													ActionProperty_Time apt
												on ap1.id = apt.id
												where
													DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) <= ::@end_date
													and DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) >= ::@end_date - INTERVAL 1 DAY
													)
";
SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@profile",profiles);
PREPARE sqlQuery FROM  @sqlPrepare;
EXECUTE sqlQuery;
              END''' %config['definer'],

#----------------------------------------------------------------------------------------------------------------------------------
    u'''CREATE DEFINER=%s PROCEDURE `FIOoutToOtherUnit`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
BEGIN
#Специальная переменная выводит ФИО переведенных в другие отделения
SET @tpl = "SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
				FROM Action 
			INNER JOIN ActionType 
			  ON Action.`actionType_id`=ActionType.`id`  
			INNER JOIN ActionProperty 
			  ON Action.`id`=ActionProperty.`action_id`  
			INNER JOIN ActionProperty_HospitalBed 
			  ON ActionProperty.`id`=ActionProperty_HospitalBed.`id`  
			INNER JOIN OrgStructure_HospitalBed 
			  ON ActionProperty_HospitalBed.`value`=OrgStructure_HospitalBed.`id`   
			INNER JOIN Event ON Action.`event_id`=Event.`id`
			INNER JOIN EventType ON EventType.id = Event.eventType_id #только для ФНКЦ
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #только для ФНКЦ			
			INNER JOIN
				(SELECT Action.id , ActionProperty_HospitalBedProfile.value
								FROM Action
										INNER JOIN ActionType 
								  ON Action.`actionType_id`=ActionType.`id`
										INNER JOIN ActionProperty 
								  ON Action.`id`=ActionProperty.`action_id`
										INNER JOIN ActionPropertyType 
								  ON ActionPropertyType.`id`=ActionProperty.`type_id`
										INNER JOIN ActionProperty_HospitalBedProfile 
								  ON ActionProperty.`id`=ActionProperty_HospitalBedProfile.`id`
										INNER JOIN rbHospitalBedProfile 
								  ON ActionProperty_HospitalBedProfile.`value`=rbHospitalBedProfile.`id`
										WHERE (ActionType.`flatCode`='moving')
										AND (ActionPropertyType.`code`='hospitalBedProfile')
										AND ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
										AND (rbHospitalBedProfile.id IN (::@profile)) ) sz
			ON Action.id = sz.id
			INNER JOIN
				Client c
			ON c.id = Event.client_id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` = ::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (Action.id not in (select id from
                    (select max(Action.id) id from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A) )
";
SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@profile",profiles);
PREPARE sqlQuery FROM  @sqlPrepare;
EXECUTE sqlQuery;
              END''' %config['definer'],

#----------------------------------------------------------------------------------------------------------------------------------
    u'''CREATE DEFINER=%s PROCEDURE `FIOoutToOtherHospital`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
BEGIN
#Специальная переменная выводит ФИО переведенных в другие стационары
SET @tpl = "SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
				FROM Action 
			INNER JOIN ActionType 
			  ON Action.`actionType_id`=ActionType.`id`  
			INNER JOIN ActionProperty 
			  ON Action.`id`=ActionProperty.`action_id`  
			INNER JOIN ActionProperty_HospitalBed 
			  ON ActionProperty.`id`=ActionProperty_HospitalBed.`id`  
			INNER JOIN OrgStructure_HospitalBed 
			  ON ActionProperty_HospitalBed.`value`=OrgStructure_HospitalBed.`id`   
			INNER JOIN Event ON Action.`event_id`=Event.`id`  
			INNER JOIN EventType ON EventType.id = Event.eventType_id #только для ФНКЦ
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #только для ФНКЦ			
			INNER JOIN
				(SELECT Action.id , ActionProperty_HospitalBedProfile.value
								FROM Action
										INNER JOIN ActionType 
								  ON Action.`actionType_id`=ActionType.`id`
										INNER JOIN ActionProperty 
								  ON Action.`id`=ActionProperty.`action_id`
										INNER JOIN ActionPropertyType 
								  ON ActionPropertyType.`id`=ActionProperty.`type_id`
										INNER JOIN ActionProperty_HospitalBedProfile 
								  ON ActionProperty.`id`=ActionProperty_HospitalBedProfile.`id`
										INNER JOIN rbHospitalBedProfile 
								  ON ActionProperty_HospitalBedProfile.`value`=rbHospitalBedProfile.`id`
										WHERE (ActionType.`flatCode`='moving')
										AND (ActionPropertyType.`code`='hospitalBedProfile')
										AND ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
										AND (rbHospitalBedProfile.id IN (::@profile)) ) sz
			ON Action.id = sz.id
			INNER JOIN
				Client c
			ON c.id = Event.client_id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` = ::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (Action.id in (select id from
                    (select max(Action.id) id from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A) ) 
			AND (Action.event_id in (select distinct Event.id
                                         from Action
                                         INNER JOIN ActionType
                                         ON Action.actionType_id = ActionType.id
                                         INNER JOIN ActionProperty
                                         ON ActionProperty.action_id = Action.id
                                         INNER JOIN Event
                                         ON Event.id = Action.event_id
                                         inner join ActionProperty_String aps
                                         on ActionProperty.id = aps.id
                                         where ActionType.flatCode = 'leaved' and aps.value = 'переведен в другой стационар'))
         and Action.event_id not in (
											select e.id
												from
												Event e
												inner join
													Action a
												on a.event_id = e.id
												inner join
													ActionProperty ap
												on a.id=ap.action_id
												inner join
													ActionProperty_Date apd
												on ap.id = apd.id
												inner join
													ActionProperty ap1
												on a.id=ap1.action_id	
												inner join
													ActionProperty_Time apt
												on ap1.id = apt.id
												where
													DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) <= ::@end_date
													and DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) >= ::@end_date - INTERVAL 1 DAY
													)
";
SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@profile",profiles);
PREPARE sqlQuery FROM  @sqlPrepare;
EXECUTE sqlQuery;
              END''' %config['definer'],

#----------------------------------------------------------------------------------------------------------------------------------
    u'''CREATE DEFINER=%s PROCEDURE `FIOtotalDeath`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
BEGIN
#Специальная переменная выводит ФИО умерших
SET @tpl = "SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
				FROM Action 
			INNER JOIN ActionType 
			  ON Action.`actionType_id`=ActionType.`id`  
			INNER JOIN ActionProperty 
			  ON Action.`id`=ActionProperty.`action_id`  
			INNER JOIN ActionProperty_HospitalBed 
			  ON ActionProperty.`id`=ActionProperty_HospitalBed.`id`  
			INNER JOIN OrgStructure_HospitalBed 
			  ON ActionProperty_HospitalBed.`value`=OrgStructure_HospitalBed.`id`   
			INNER JOIN Event ON Action.`event_id`=Event.`id`   
			INNER JOIN EventType ON EventType.id = Event.eventType_id #только для ФНКЦ
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #только для ФНКЦ
			INNER JOIN
				(SELECT Action.id , ActionProperty_HospitalBedProfile.value
								FROM Action
										INNER JOIN ActionType 
								  ON Action.`actionType_id`=ActionType.`id`
										INNER JOIN ActionProperty 
								  ON Action.`id`=ActionProperty.`action_id`
										INNER JOIN ActionPropertyType 
								  ON ActionPropertyType.`id`=ActionProperty.`type_id`
										INNER JOIN ActionProperty_HospitalBedProfile 
								  ON ActionProperty.`id`=ActionProperty_HospitalBedProfile.`id`
										INNER JOIN rbHospitalBedProfile 
								  ON ActionProperty_HospitalBedProfile.`value`=rbHospitalBedProfile.`id`
										WHERE (ActionType.`flatCode`='moving')
										AND (ActionPropertyType.`code`='hospitalBedProfile')
										AND ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
										AND (rbHospitalBedProfile.id IN (::@profile)) ) sz
			ON Action.id = sz.id
			INNER JOIN
					(select e.id,DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) deathdate
							from
							Event e
							inner join
								Action a
							on a.event_id = e.id
							inner join
								ActionProperty ap
							on a.id=ap.action_id												
							inner join
								ActionProperty_Date apd
							on ap.id = apd.id
							inner join
								ActionProperty ap1
							on a.id=ap1.action_id	
							inner join
								ActionProperty_Time apt
							on ap1.id = apt.id) dead
			ON Action.event_id = dead.id
			INNER JOIN
				Client c
			ON c.id = Event.client_id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` = ::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (Action.id in (select id from
                    (select max(Action.id) id from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A) ) 
			AND (Action.event_id in (select distinct Event.id
                                         from Action
                                         INNER JOIN ActionType
                                         ON Action.actionType_id = ActionType.id
                                         INNER JOIN ActionProperty
                                         ON ActionProperty.action_id = Action.id
                                         INNER JOIN Event
                                         ON Event.id = Action.event_id
                                         inner join ActionProperty_String aps
                                         on ActionProperty.id = aps.id
                                         where ActionType.flatCode = 'leaved'))
			AND dead.deathdate BETWEEN ::@end_date - INTERVAL 1 DAY AND ::@end_date
";
SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@profile",profiles);
PREPARE sqlQuery FROM  @sqlPrepare;
EXECUTE sqlQuery;
              END''' %config['definer'],

 )

    for sql in sqls:	
       c.execute(sql)
    c.close()

def downgrade(conn):
    pass