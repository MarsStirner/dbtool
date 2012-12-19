#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Перенос шаблона заполнения полей эпикриза из файла в БД
'''


def upgrade(conn):
    global config    
    c = conn.cursor()
    
    sql = ur'''
INSERT IGNORE INTO `rbPrintTemplate` SET
	`code` = '1',
	`name` = 'action_epicrisis',
	`context` = '__fill_epicrisis',
	`fileName` = 'action_epicrisis',
	`render` = '1',
	`dpdAgreement` = '0',
	`default` = '<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  </head>
  <body style=" font-family:\'Times New Roman\'; font-size:14pt; font-style:normal;">
    {% for (action, propList) in actList %}
        <b>{{action[0]}}</b>
        <b style=" font-family:\'Times New Roman\'; font-size:12pt; font-style:normal;">
            ({{action[2]}})</b>
        <br/>
        <table border="1" cellpadding="0" cellspacing="0" width="100%">
                <thead>
                  <tr  style="font-family: \'Times New Roman\'; font-size: 13pt; font-weight:bold;">
                    <th>Показатель</th>
                    <th>Значение</th>
                    {% if action[4] == 1 %}
                        <th>Ед. изм.</th>
                        <th>Норма</th>
                    {% endif %}
                  </tr>
                </thead>
                <tbody>
                    {% for prop in propList %}
						<tr style="font-family: \'Times New Roman\'; font-size: 12pt; font-style:normal;" border="1" cellpadding="0" cellspacing="0" width="100%">
							<td align="left">{{prop[0]}}</td>
							<td align="center">{{prop[2]}}</td>
							{% if action[4] == 1 %}
								<td align="center">{{prop[1]}}</td>
								<td align="center">{{prop[3]}}</td>
							{% endif %}
						</tr>
                    {% endfor %}
                </tbody>
         </table>
         <br/>
         <br/>
    {% endfor %}
    <div>
     <br/><br/><br/>
     </div>
  </body>
</html>
'
'''
    c.execute(sql)
    
    sql = u'''
ALTER TABLE `Action` ADD COLUMN `parentAction_id` INT(11) NULL DEFAULT NULL COMMENT 'Родительский action' AFTER `version` 
, ADD INDEX `parentAction_id` (`parentAction_id` ASC) ;
'''
    c.execute(sql)
    
    sql = u'''
INSERT INTO `ActionType` (`class`, `code`, `name`, `title`, `flatCode`,
`createDatetime`, `modifyDatetime`, `sex`, `age`, `office`, `showInForm`, `genTimetable`, `context`, `defaultPlannedEndDate`)
VALUES (-1, 'PRPA_IN402006UV02', 'Отмена сообщения о госпитализации (поступлении)', 'Отмена сообщения о госпитализации', 'del_received', 
CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0, '0-969', '', 0, 0, '', '0000-00-00');
'''
    c.execute(sql)
    
    sql = u'''
INSERT INTO `ActionType` (`class`, `code`, `name`, `title`, `flatCode`,
`createDatetime`, `modifyDatetime`, `sex`, `age`, `office`, `showInForm`, `genTimetable`, `context`, `defaultPlannedEndDate`)
VALUES (-1, 'PRPA_IN402006UV02', 'Отмена сообщения о переводе между отделениями внутри стационара', 'Отмена сообщения переводе', 'del_moving',
CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 0, '0-969', '', 0, 0, '', '2');
'''
    c.execute(sql)
    

def downgrade(conn):
    pass
