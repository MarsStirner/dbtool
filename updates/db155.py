#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Добавление триггера на пометку записей в Account_Item удалёнными, если "удаляется" запись в Account
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    c.execute(u'''
CREATE DEFINER=%s TRIGGER `Delete_AccountItem_ON_UPDATE` AFTER UPDATE ON `Account` FOR EACH ROW BEGIN
    IF NEW.deleted IS NOT NULL AND NEW.deleted != OLD.deleted AND NEW.deleted = 1 THEN
        UPDATE Account_Item
        SET deleted = NEW.deleted
        WHERE master_id = NEW.id;
    END IF;
END''' % config['definer'])

    c.close()


def downgrade(conn):
    pass
