#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавление ON DELETE CASCADE ON UPDATE CASCADE к foreignkey bbtResult_Text -> Action
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = u'''
    ALTER TABLE bbtResult_Text DROP FOREIGN KEY `FK_bbtResult_Text_Action`;
    ALTER TABLE bbtResult_Text
    ADD CONSTRAINT `FK_bbtResult_Text_Action`
    FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`)
    ON DELETE CASCADE ON UPDATE CASCADE;
    '''
    c.execute(sql)

def downgrade(conn):
    c = conn.cursor()

    sql = u'''
    ALTER TABLE bbtResult_Text DROP FOREIGN KEY `FK_bbtResult_Text_Action`;
    ALTER TABLE bbtResult_Text
    ADD CONSTRAINT `FK_bbtResult_Text_Action`
    FOREIGN KEY (`action_id`) REFERENCES `Action` (`id`);
    '''
    c.execute(sql)
