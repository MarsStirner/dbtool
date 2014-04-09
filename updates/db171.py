#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Создание связей между таблицами, хранящими информацию об адресах
'''

def upgrade(conn):
    c = conn.cursor()

    sql = '''
        UPDATE `Address` SET `createPerson_id`=1 WHERE `createPerson_id` NOT IN (SELECT `id` FROM `Person`);
        ALTER TABLE `Address` ADD CONSTRAINT `address_to_person_by_create_person` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

        UPDATE `Address` SET `modifyPerson_id`=1 WHERE `modifyPerson_id` NOT IN (SELECT id FROM `Person`);
        ALTER TABLE `Address` ADD CONSTRAINT `address_to_person_by_modify_person` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

        UPDATE `AddressHouse` SET `createPerson_id`=1 WHERE `createPerson_id` NOT IN (SELECT `id` FROM `Person`);
        ALTER TABLE `AddressHouse` ADD CONSTRAINT `address_house_to_person_by_create_person` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

        UPDATE `AddressHouse` SET `modifyPerson_id`=1 WHERE `modifyPerson_id` NOT IN (SELECT `id` FROM `Person`);
        ALTER TABLE `AddressHouse` ADD CONSTRAINT `address_house_to_person_by_modify_person` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

        UPDATE `ClientAddress` SET `createPerson_id`=1 WHERE `createPerson_id` NOT IN (SELECT `id` FROM `Person`);
        ALTER TABLE `ClientAddress` ADD CONSTRAINT `client_address_to_person_by_create_person` FOREIGN KEY (`createPerson_id`) REFERENCES `Person` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

        UPDATE `ClientAddress` SET `modifyPerson_id`=1 WHERE `modifyPerson_id` NOT IN (SELECT `id` FROM `Person`);
        ALTER TABLE `ClientAddress` ADD CONSTRAINT `client_address_to_person_by_modify_person` FOREIGN KEY (`modifyPerson_id`) REFERENCES `Person` (`id`) ON DELETE SET NULL ON UPDATE CASCADE;

        # Address -> AddressHouse
        UPDATE `Address` SET `house_id` = 1 WHERE `house_id` NOT IN (SELECT `id` FROM `AddressHouse`); # Тут должен быть какой-то стандартный id, который есть на всех БД.
        ALTER TABLE `Address` ADD CONSTRAINT `address_to_address_house_by_house_id` FOREIGN KEY (`house_id`) REFERENCES `AddressHouse` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE; # Каскадное удаление, т.к. поле house_id NOT NULL

        # Удаляем избыточные элементы на которые никто не ссылается
        DELETE FROM `Address` WHERE `id` NOT IN (SELECT `address_id` FROM `ClientAddress`);

        # ClientAddress -> Address
        UPDATE `ClientAddress` SET `address_id` = NULL WHERE `address_id` NOT IN (SELECT `id` FROM `Address`);
        ALTER TABLE `ClientAddress` ADD CONSTRAINT `client_address_to_address_by_address_id` FOREIGN KEY (`address_id`) REFERENCES `Address` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

        # ClientAddress -> Client
        DELETE FROM `ClientAddress` WHERE `client_id` NOT IN (SELECT `id` FROM Client);
        ALTER TABLE `ClientAddress` ADD CONSTRAINT `client_address_to_client_by_client_id` FOREIGN KEY (`client_id`) REFERENCES Client (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
'''
    c.execute(sql)


def downgrade(conn):
    c = conn.cursor()
    sql = '''
        ALTER TABLE `Address` DROP FOREIGN KEY `address_to_person_by_create_person`;
        ALTER TABLE `Address` DROP FOREIGN KEY `address_to_person_by_modify_person`;
        ALTER TABLE `AddressHouse` DROP FOREIGN KEY `address_house_to_person_by_create_person`;
        ALTER TABLE `AddressHouse` DROP FOREIGN KEY `address_house_to_person_by_modify_person`;
        ALTER TABLE `ClientAddress` DROP FOREIGN KEY `client_address_to_person_by_create_person`;
        ALTER TABLE `ClientAddress` DROP FOREIGN KEY `client_address_to_person_by_modify_person`;

        ALTER TABLE `Address` DROP FOREIGN KEY `address_to_address_house_by_house_id`;
        ALTER TABLE `ClientAddress` DROP FOREIGN KEY `client_address_to_address_by_address_id`;
        ALTER TABLE `ClientAddress` DROP FOREIGN KEY `client_address_to_client_by_client_id`;
    '''
    c.execute(sql)