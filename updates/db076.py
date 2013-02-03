#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Изменения, необходимые для работы закрытия обращения
- Изменены коды записей в справочнике типов обращений, на них опирается
правильное функционионирование ТМИС
'''

simple_queries = \
(
u'''
ALTER TABLE `Diagnostic` ADD COLUMN `action_id` INT(11) NULL DEFAULT NULL  AFTER `version` 
, ADD INDEX `action_id` (`action_id` ASC) ;
''',
u'''
ALTER TABLE `rbRequestType` CHANGE COLUMN `code` `code` VARCHAR(16) NOT NULL COMMENT 'Код'  ;
''',
'''
UPDATE `rbRequestType` SET `code`='clinic' WHERE `id`='1';
''',
'''
UPDATE `rbRequestType` SET `code`='hospital' WHERE `id`='2';
''',
'''
UPDATE `rbRequestType` SET `code`='policlinic' WHERE `id`='3';
''',
#'''
#ALTER TABLE `ActionPropertyType` ADD COLUMN `code` VARCHAR(25) NULL  AFTER `toEpicrisis` ;
#''',
'''
UPDATE `ActionPropertyType` SET `code`='resort' WHERE `id`='20170';
''',
'''
UPDATE `ActionPropertyType` SET `code`='hospLength' WHERE `id`='7877';
''',
'''
UPDATE `ActionPropertyType` SET `code`='diagReceived' WHERE `id`='1604';
''',
'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE id in (1870,26657,9331,14171,13937,10277,10481,14602,10536,11002,11030,11877,11444,14551,15083,15101,32237)
''',
'''
UPDATE `ActionPropertyType` SET `code`='assocDiag' WHERE id in (9333,14173,14014,13939,10278,10479,10514,10537,11004,11032,11973,11446,12392,12434,14553,15112,32239)
''',
'''
UPDATE `ActionPropertyType` SET `code`='diagCompl' WHERE id in (9334,14174,14015,13940,10279,10478,10515,10538,11005,11033,11975,11447,12393,12435,14554,15104,32240)
''',
'''
UPDATE `ActionPropertyType` SET `code`='mainDiag' WHERE id in (6806,6841,1825,26749,14266,7878,9708,14603,14626,14649)
''',
'''
UPDATE `ActionPropertyType` SET `code`='mainDiagMkb' WHERE id in (26403,26408,26413,26750,26397,26418,26423,26428,26433,26438,26443)
''',
'''
UPDATE `ActionPropertyType` SET `code`='diagCompl' WHERE id in (6809,6842,26752,6831,7879,13967,9709,14605,14628,14651)
''',
'''
UPDATE `ActionPropertyType` SET `code`='diagComplMkb' WHERE id in (26405,26410,26415,26753,26399,26420,26425,26430,26448,26435,26440,26445)
''',
'''
UPDATE `ActionPropertyType` SET `code`='assocDiag' WHERE id in (6808,6843,26754,6832,7880,13968,14606,14629,14652)
''',
'''
UPDATE `ActionPropertyType` SET `code`='assocDiagMkb' WHERE id in (26406,26411,26416,26400,26421,26426,26431,26436,26441,26446)
''',
'''
UPDATE `ActionPropertyType` SET `code`='nextHospDate' WHERE `id`='20174';
''',
'''
UPDATE `ActionPropertyType` SET `code`='hospOrgStruct' WHERE `id`='36081';
''',
'''
UPDATE `ActionPropertyType` SET `code`='nextHospFinance' WHERE `id`='36082';
''',
'''
UPDATE `ActionPropertyType` SET `code`='preHospDefect' WHERE id in (36064, 36065, 36066, 36067, 36068, 36069, 36070, 36071, 36072, 36073, 36074, 36075, 36076, 36077, 36078, 36079, 36080)
''',
'''
UPDATE `ActionPropertyType` SET `code`='hospOutcome' WHERE `id`='1663';
''',
'''
UPDATE `ActionPropertyType` SET `code`='timeLeaved' WHERE `id`='1617';
''',
)
user_queries = \
()

def upgrade(conn):
    global config    
    
    for query in simple_queries:
        c = conn.cursor()
        c.execute(query)
        c.close()

    for query in user_queries:
        c = conn.cursor()
        c.execute(query % (config['username'], config['host']))
        c.close()

def downgrade(conn):
    pass
