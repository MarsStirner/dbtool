# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Добавление таблицу ActionProperty_Image хранения изображений \
в совйствах действия. \
'''


def upgrade(conn):
    sqlCreateActionProperty_Image = '''\
CREATE TABLE IF NOT EXISTS `ActionProperty_Image` (
    `id` int(11) NOT NULL COMMENT '{ActionProperty}',
    `index` int(11) NOT NULL default '0' COMMENT 'Индекс элемента векторного значения или 0',
    `value` MEDIUMBLOB default NULL COMMENT 'собственно значение',
    PRIMARY KEY  (`id`,`index`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Значение свойства действия типа "Image"';
'''

    c = conn.cursor()

    c.execute(sqlCreateActionProperty_Image)


def downgrade(conn):
    sqlDropActionProperty_Image = '''\
DROP TABLE `ActionProperty_Image`
'''

    c = conn.cursor()

    c.execute(sqlDropActionProperty_Image)
