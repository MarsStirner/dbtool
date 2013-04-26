# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Вводим таблицу ActionProperty_MKB - тип свойства действия МКБ
'''


def upgrade(conn):
    sql = [
# Создаём таблицу
'''\
CREATE TABLE IF NOT EXISTS `ActionProperty_MKB` (
  `id` INT(11) NOT NULL COMMENT '{ActionProperty}' ,
  `index` INT(11) NOT NULL DEFAULT '0' COMMENT 'Индекс элемента векторного значения или 0' ,
  `value` INT(11) NULL DEFAULT NULL COMMENT 'собственно значение {MKB}' ,
  PRIMARY KEY (`id`, `index`) ,
  INDEX `ActionProperty_MKB_value` (`value` ASC) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = 'Значение свойства действия типа МКБ' ;
'''
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    sql = [
# Удаляем таблицу
'''\
DROP TABLE `ActionProperty_MKB`;
''',
    ]
    c = conn.cursor()
    for s in sql:
        c.execute(s)

