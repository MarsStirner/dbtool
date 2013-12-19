#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Форма 007
'''

def upgrade(conn):
    global config
    c = conn.cursor()

    queries = ( 
u'''select 
	rbhbp.name,
	total.count_koikas,
	total.countDisable,
	total.countStartDate,
	total.countInput,
	total.countFromStac12,
	total.countVillages,
	total.countInput017,
	total.countInput60,
	total.countFromOtherUnit,
	total.countToOtherUnit,
	total.countTotalOut,
	total.countToOtherStac,
	total.countOut247,
	total.countOut12,
	total.countDeaht,
	total.countPatOnEnd,
	total.countMothers,
	total.countMaleBed,
	total.countFemaleBed
from (
select 
	IFNULL(p13.value,IFNULL(p14.input_value,IFNULL(p15.input_value,IFNULL(p16.input_value,IFNULL(p17.input_value,IFNULL(p18.input_value,IFNULL(p19.input_value,IFNULL(p20.input_value,IFNULL(p21.out_value,IFNULL(p22.out_value,IFNULL(p23.out_value,IFNULL(p24.out_value,IFNULL(p26.out_value,IFNULL(p27.value,IFNULL(p28.value,IFNULL(p29.prof_id,IFNULL(p30.prof_id,koikas.prof_id))))))))))))))))) profile,
	count(distinct koikas.koika_id) as count_koikas,
	count(p12.svern_id) countDisable,
	count(p13.action_id) countStartDate,
	count(distinct p14.input_action_id) countInput,
	count(distinct p15.input_day_stac_action_id) countFromStac12,
	count(distinct p16.input_village_action_id) countVillages,
	count(distinct p17.input017_action_id) countInput017,
	count(distinct p18.input60_action_id) countInput60,
	count(distinct p19.fromother_action_id) countFromOtherUnit,
	count(distinct p20.toother_action_id) countToOtherUnit,
	count(distinct p21.out_action_id) countTotalOut,
	count(distinct p22.outother_action_id) countToOtherStac,
	count(distinct p23.out247_action_id) countOut247,
	count(distinct p24.out12_action_id) countOut12,
	count(distinct p26.death_action_id) countDeaht,
	count(distinct p27.totalendday_action_id) countPatOnEnd,
	count(distinct p28.mother_action_id) countMothers,
	count(distinct p29.male_koika_id) countMaleBed,
	count(distinct p30.female_koika_id) countFemaleBed
from
#---- койки отделения
	(	Select ohb.id koika_id ,hbp.id prof_id
		from 
			OrgStructure_HospitalBed  ohb
		LEFT JOIN rbHospitalBedProfile  hbp
  			ON ohb.`profile_id`=hbp.`id` 
		where 
			master_id =::@org_str
		  ) as p11
#--- 11. Количество коек
	left join
	(	Select ohb.id koika_id ,hbp.id prof_id
		from 
			OrgStructure_HospitalBed  ohb
		LEFT JOIN rbHospitalBedProfile  hbp
  			ON ohb.`profile_id`=hbp.`id` 
		where 
			master_id =::@org_str
			and ohb.isPermanent = 1 #штатные койки
			and hbp.id in (::@profiles) #Тут указать переменную свободы
		  ) as koikas
	ON p11.koika_id = koikas.koika_id
left join
		 #---  12. Количество свернутых коек
	(	 Select ohb.id svern_id , hbp.id drop_pr_id
		from 
			OrgStructure_HospitalBed ohb
		LEFT JOIN rbHospitalBedProfile hbp
			ON ohb.`profile_id`=hbp.`id`  
		where 
			master_id =::@org_str
			and ohb.isPermanent = 1 #штатные койки
			and ohb.involution != 0 #свернутые
			and hbp.id in (::@profiles)
			) as p12
	on
		p11.koika_id = p12.svern_id
		#---13. состояло больных на начало суток
left join
	(
		SELECT Action.id action_id,OrgStructure_HospitalBed.id koika_id , sz.value
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
										AND ((Action.`begDate`<=::@end_date - INTERVAL 1 DAY)
										AND (((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) OR (Action.`endDate` IS NULL))))
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`begDate`<=::@end_date - INTERVAL 1 DAY) AND ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) OR (Action.`endDate` IS NULL))) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0) 
	) as p13
on p11.koika_id=p13.koika_id
left join
#14. поступило всего ---------------
		(
			SELECT Action.id input_action_id,OrgStructure_HospitalBed.id input_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0) 
			AND (Action.id in (select id from
								(select Action.id, min(Action.id) from Action
								join ActionType
								  on Action.actionType_id = ActionType.id
								where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
								group by event_id) A))			
 ) as p14
	on
		p11.koika_id=p14.input_koika_id
left join	
#p15 Поступило из дневного стац.
(		
SELECT Action.id input_day_stac_action_id,OrgStructure_HospitalBed.id input_day_stac_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
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
                                      and OrgStructure.type = 1
                                    group by event_id))
			AND (Action.id in (select id from
                    (select Action.id, min(Action.id) from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A))
 ) as p15
on
	p11.koika_id = p15.input_day_stac_koika_id
	
# p16. Количество поступивших из села
left join
(		
SELECT Action.id input_village_action_id,OrgStructure_HospitalBed.id input_village_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			INNER JOIN Client
				ON Event.client_id = Client.id
			INNER JOIN ClientAddress AS Adr
				ON (Adr.client_id = Client.id AND Adr.id IN (SELECT max(Tmp.id)
										  FROM
										ClientAddress AS Tmp
										  WHERE
										Tmp.deleted = 0
										AND type = '0'
										  GROUP BY
										client_id))
				LEFT JOIN Address
					ON Address.id = Adr.address_id
				LEFT JOIN AddressHouse
					ON AddressHouse.id = Address.house_id
				LEFT JOIN kladr.KLADR
					ON kladr.KLADR.Code = AddressHouse.KLADRCode
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (((substring(kladr. KLADR.OCATD, 3, 1) IN (1, 2, 4))
					    AND substring(kladr.KLADR.OCATD, 6, 1) IN (0, 8)
					    AND substring(kladr.KLADR.OCATD, 11, 1) > 0)
					    OR ((substring(kladr.KLADR.OCATD, 3, 1) NOT IN (1, 2, 4))
					    AND substring(kladr.KLADR.OCATD, 6, 1) = 9)
					    OR Adr.localityType = IF(ISNULL(kladr. KLADR.OCATD)=1,2,0))  
			AND (Action.id in (select id from
                    (select Action.id, min(Action.id) from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A))

) as p16
on	p11.koika_id = p16.input_village_koika_id	
# p 17  поступило от 0 до 17лет
left join (
			SELECT Action.id input017_action_id,OrgStructure_HospitalBed.id input017_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			INNER JOIN Client 
				ON Event.`client_id`=Client.`id`
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND ((year(Action.begDate) - year(birthDate)) <= 17)
			AND (Action.id in (select id from
                    (select Action.id, min(Action.id) from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A))
			  ) as p17
on
	p11.koika_id = p17.input017_koika_id			
	
# p18 Поступило старше 60
left join (
SELECT Action.id input60_action_id,OrgStructure_HospitalBed.id input60_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			INNER JOIN Client 
				ON Event.`client_id`=Client.`id`
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND ((year(Action.begDate) - year(birthDate)) > 60)
			AND (Action.id in (select id from
                    (select Action.id, min(Action.id) from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A))
			  ) as p18
on
	p11.koika_id = p18.input60_koika_id	
	#p19 Переведено из других отделений
left join (

SELECT Action.id fromother_action_id,OrgStructure_HospitalBed.id fromother_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`begDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`begDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (Action.id not in (select id from
                    (select Action.id, min(Action.id) from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A) ) 
) as p19
on p11.koika_id=p19.fromother_koika_id	
# p20 Переведено в другие отделения
left join (

SELECT Action.id toother_action_id,OrgStructure_HospitalBed.id toother_koika_id , sz.value input_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0)
			AND (Action.id not in (select id from
                    (select max(Action.id) id from Action
                    join ActionType
                      on Action.actionType_id = ActionType.id
                    where ActionType.flatCode = 'moving' and Action.begDate is not Null and Action.deleted=0
                    group by event_id) A) ) 
) as p20
on p11.koika_id = p20.toother_koika_id
# 21 Выписано всего
left join (

SELECT Action.id out_action_id,OrgStructure_HospitalBed.id out_koika_id , sz.value out_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
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
													DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) <=::@end_date
													and DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) >= ::@end_date - INTERVAL 1 DAY
													)
) as p21
on p11.koika_id = p21.out_koika_id
# 22 Переведено в другие стационары
left join (
		SELECT Action.id outother_action_id,OrgStructure_HospitalBed.id outother_koika_id , sz.value out_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
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
													DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) <=::@end_date
													and DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) >= ::@end_date - INTERVAL 1 DAY
													)										 
) as p22 
on p11.koika_id = p22.outother_koika_id
# 23 переведено в круглосуточный стационар
left join (
	SELECT Action.id out247_action_id,OrgStructure_HospitalBed.id out247_koika_id , sz.value out_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
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
                                         where ActionType.flatCode = 'leaved' and aps.value = 'выписан в круглосуточный стационар'))
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
													DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) <=::@end_date
													and DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) >= ::@end_date - INTERVAL 1 DAY
													)										 
) as p23 
on p11.koika_id = p23.out247_koika_id
# 24 переведено в дневной стационар
left join (
	SELECT Action.id out12_action_id,OrgStructure_HospitalBed.id out12_koika_id , sz.value out_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
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
                                         where ActionType.flatCode = 'leaved' and aps.value = 'выписан в дневной стационар'))
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
													DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) <=::@end_date
													and DATE_ADD(apd.value,INTERVAL apt.value HOUR_SECOND) >= ::@end_date - INTERVAL 1 DAY
													)										 
) as p24 
on p11.koika_id = p24.out12_koika_id
# 26 умерло
left join (							
SELECT Action.id death_action_id,OrgStructure_HospitalBed.id death_koika_id , sz.value out_value
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
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
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
			WHERE ((Action.`endDate`>=::@end_date - INTERVAL 1 DAY) AND (Action.`endDate`<=::@end_date) ) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
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
) as p26
on p11.koika_id = p26.death_koika_id
#---27. Состоит больных всего
left join (
		SELECT Action.id totalendday_action_id,OrgStructure_HospitalBed.id totalendday_koika_id , sz.value
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
										AND ((Action.`begDate`<=::@end_date)
										AND (((Action.`endDate`>=::@end_date) OR (Action.`endDate` IS NULL))))
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			WHERE ((Action.`begDate`<=::@end_date) AND ((Action.`endDate`>=::@end_date) OR (Action.`endDate` IS NULL))) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0) 
) as p27
on p11.koika_id = p27.totalendday_koika_id
# 28 Состоит матерей
left join (
SELECT Action.id mother_action_id,OrgStructure_HospitalBed.id mother_koika_id , sz.value
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
										AND ((Action.`begDate`<=::@end_date)
										AND (((Action.`endDate`>=::@end_date) OR (Action.`endDate` IS NULL))))
										AND (rbHospitalBedProfile.id IN (::@profiles)) ) sz
			ON Action.id = sz.id
			INNER JOIN (select distinct Event.id
					from `Action`
					INNER JOIN ActionType
					    ON Action.actionType_id = ActionType.id
					INNER JOIN ActionProperty
					    ON ActionProperty.action_id = Action.id
					INNER JOIN ActionPropertyType
					    on ActionPropertyType.id = ActionProperty.type_id
					INNER JOIN Event
					    ON Event.id = Action.event_id
					INNER JOIN ActionProperty_String aps
					    on ActionProperty.id = aps.id
					where ActionPropertyType.code = 'patronage'
					    and aps.value = 'да')ev
			ON Event.`id` = ev.id
			WHERE ((Action.`begDate`<=::@end_date) AND ((Action.`endDate`>=::@end_date) OR (Action.`endDate` IS NULL))) 
			AND (ActionType.`flatCode`='moving') 
			AND (OrgStructure_HospitalBed.`master_id` =::@org_str) 
			AND (Action.`deleted`=0) AND (Event.`deleted`=0) 
			AND (ActionProperty.`deleted`=0) 
) as p28 
on p11.koika_id = p28.mother_koika_id
# 29 Свободных мужских мест
left join (
	Select ohb.id male_koika_id ,hbp.id prof_id
			from 
				OrgStructure_HospitalBed  ohb
			LEFT JOIN rbHospitalBedProfile  hbp
	  			ON ohb.`profile_id`=hbp.`id` 
			where 
				master_id =::@org_str
				and ohb.isPermanent = 1 #штатные койки
				and hbp.id in (::@profiles)
				and ohb.sex=1
				AND ohb.id not in
	                                 (SELECT OrgStructure_HospitalBed.id
	                                        FROM Action
	                                        INNER JOIN ActionType
	                                            ON Action.actionType_id = ActionType.id
	                                        INNER JOIN ActionProperty
	                                            ON ActionProperty.action_id = Action.id
	                                        INNER JOIN ActionProperty_HospitalBed
	                                            ON ActionProperty.id = ActionProperty_HospitalBed.id
	                                        INNER JOIN OrgStructure_HospitalBed
	                                            ON ActionProperty_HospitalBed.value = OrgStructure_HospitalBed.id
	                                        INNER JOIN Event
	                                            ON Event.id = Action.event_id
	                                        WHERE
	                                          ((Action.begDate <=::@end_date)
	                                          AND (Action.endDate >=::@end_date OR Action.endDate IS NULL))
	                                          AND ActionType.flatCode = 'moving'
	                                          AND OrgStructure_HospitalBed.master_id =::@org_str
	                                          AND `Action`.deleted = 0
	                                          AND ActionProperty.deleted = 0
	                                          AND Event.deleted = 0) 

) as p29 
on p11.koika_id = p29.male_koika_id
# 30 Свободных женских мест
left join (
Select ohb.id female_koika_id ,hbp.id prof_id
			from 
				OrgStructure_HospitalBed  ohb
			LEFT JOIN rbHospitalBedProfile  hbp
	  			ON ohb.`profile_id`=hbp.`id` 
			where 
				master_id =::@org_str
				and ohb.isPermanent = 1 #штатные койки
				and hbp.id in (::@profiles)
				and ohb.sex=2
				AND ohb.id not in
	                                 (SELECT OrgStructure_HospitalBed.id
	                                        FROM Action
	                                        INNER JOIN ActionType
	                                            ON Action.actionType_id = ActionType.id
	                                        INNER JOIN ActionProperty
	                                            ON ActionProperty.action_id = Action.id
	                                        INNER JOIN ActionProperty_HospitalBed
	                                            ON ActionProperty.id = ActionProperty_HospitalBed.id
	                                        INNER JOIN OrgStructure_HospitalBed
	                                            ON ActionProperty_HospitalBed.value = OrgStructure_HospitalBed.id
	                                        INNER JOIN Event
	                                            ON Event.id = Action.event_id
	                                        WHERE
	                                          ((Action.begDate <=::@end_date)
	                                          AND (Action.endDate >=::@end_date OR Action.endDate IS NULL))
	                                          AND ActionType.flatCode = 'moving'
	                                          AND OrgStructure_HospitalBed.master_id =::@org_str
	                                          AND `Action`.deleted = 0
	                                          AND ActionProperty.deleted = 0
	                                          AND Event.deleted = 0) 
) as p30
on p11.koika_id = p30.female_koika_id
group by
	IFNULL(p13.value,IFNULL(p14.input_value,IFNULL(p15.input_value,IFNULL(p16.input_value,IFNULL(p17.input_value,IFNULL(p18.input_value,IFNULL(p19.input_value,IFNULL(p20.input_value,IFNULL(p21.out_value,IFNULL(p22.out_value,IFNULL(p23.out_value,IFNULL(p24.out_value,IFNULL(p26.out_value,IFNULL(p27.value,IFNULL(p28.value,IFNULL(p29.prof_id,IFNULL(p30.prof_id,p11.prof_id)))))))))))))))))
) total
inner join 
		rbHospitalBedProfile rbhbp
	on rbhbp.id = total.profile''',
#----------------------------------------------------------------------------------------------------------------------------------
    u'''SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
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
			INNER JOIN EventType ON EventType.id = Event.eventType_id #������ ��� ����
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #������ ��� ����			
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
                    group by event_id) A))''',
#----------------------------------------------------------------------------------------------------------------------------------
    u'''SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
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
			INNER JOIN EventType ON EventType.id = Event.eventType_id #������ ��� ����
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #������ ��� ����			
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
													)''',
#----------------------------------------------------------------------------------------------------------------------------------
    u'''SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
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
			INNER JOIN EventType ON EventType.id = Event.eventType_id #������ ��� ����
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #������ ��� ����			
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
                    group by event_id) A) )''',
#----------------------------------------------------------------------------------------------------------------------------------
    u'''SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
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
			INNER JOIN EventType ON EventType.id = Event.eventType_id #������ ��� ����
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #������ ��� ����			
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
                                         where ActionType.flatCode = 'leaved' and aps.value = '��������� � ������ ���������'))
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
													)''',
#----------------------------------------------------------------------------------------------------------------------------------
    u'''SELECT CONCAT_WS(' ',c.lastName,c.firstName,c.patrName,Event.externalId,rbFinance.name) FIO_input
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
			INNER JOIN EventType ON EventType.id = Event.eventType_id #������ ��� ����
			INNER JOIN rbFinance ON rbFinance.id = EventType.finance_id #������ ��� ����
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
			AND dead.deathdate BETWEEN ::@end_date - INTERVAL 1 DAY AND ::@end_date''' )

    proc = u'''CREATE DEFINER=%s PROCEDURE `%s`(IN end_date VARCHAR(128), IN org_str VARCHAR(128) , IN profiles VARCHAR(128))
             BEGIN
                SELECT rbSpecialVariablesPreferences.`query` INTO @tpl FROM rbSpecialVariablesPreferences WHERE rbSpecialVariablesPreferences.name = 'SpecialVar_%s';
		SET @sqlPrepare = REPLACE(REPLACE(REPLACE(@tpl, "::@end_date", end_date),"::@org_str",org_str),"::@%s",profiles);
		PREPARE sqlQuery FROM  @sqlPrepare;
		EXECUTE sqlQuery;
             END'''

    names =    ( u'''form007front''', u'''FIOinput007''', u'''FIOinpuFrom12''', u'''FIOoutTotal''', u'''FIOoutToOtherUnit''', u'''FIOoutToOtherHospital''')
    profiles = (     u'''profiles''',     u'''profile''',       u'''profile''',     u'''profile''',           u'''profile''',               u'''profile''')

    c.execute(u'''ALTER TABLE `rbSpecialVariablesPreferences` ADD UNIQUE INDEX `name` (`name`)''')
    for name in names:	
       c.execute(u'''DROP PROCEDURE IF EXISTS %s'''%name) 
       index = names.index(name)
       c.execute(proc%(config['definer'],name,name,profiles[index])) 
       c.execute(u'''INSERT IGNORE INTO `rbSpecialVariablesPreferences` (`name`,`query`) VALUES ("SpecialVar_%s", "%s")'''%(name, queries[index]) )
                     
    c.close()


def downgrade(conn):
    pass