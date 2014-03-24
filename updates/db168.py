#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

__doc__ = '''\
Фукнция для работы с ограничениями на возраст
'''


def upgrade(conn):
    global config
    c = conn.cursor()

    sql = '''
DROP function IF EXISTS `checkAgeLimitFits`;
'''
    c.execute(sql)

    sql = '''
CREATE DEFINER=%s FUNCTION `checkAgeLimitFits`(
    age_limit VARCHAR(9),
    interval_from INT(11),
    interval_to INT(11),
    unit CHAR(1),
    reverse TINYINT(1)) RETURNS int(11)
    DETERMINISTIC
    COMMENT 'Check that age limit from `age` fields falls within the interval'
BEGIN
    /*
    age_limit - age limit like "{NNN{д|н|м|г}-{MMM{д|н|м|г}}"
    interval_from - lower border
    interval_to - upper border
    unit - character in age limit {д|н|м|г} defines in which units all limits must be defined
    reverse - check age limit falls within interval if reverse = 0 and interval falls within age limit otherwise
    */
    DECLARE limit_from VARCHAR(16);
    DECLARE limit_from_val INT(11);
    DECLARE limit_to VARCHAR(16);
    DECLARE limit_to_val INT(11);

    IF age_limit = '' THEN
        RETURN  1;
    END IF;

    SET limit_from = substring_index(age_limit, '-', 1);
    IF limit_from = '' THEN
        SET limit_from_val = 0;
    ELSEIF RIGHT(limit_from, 1) = unit THEN
        SET limit_from = LEFT(limit_from, LENGTH(limit_from) - 1);
        IF limit_from REGEXP '^[0-9]+$' THEN -- check is integer
            SET limit_from_val = CAST(limit_from AS SIGNED);
        ELSE
            RETURN 0;
        END IF;
    ELSE
        RETURN 0;
    END IF;

    SET limit_to = substring_index(age_limit, '-', -1);
    IF limit_to = '' THEN
        SET limit_to_val = NULL;
    ELSEIF RIGHT(limit_to, 1) = unit THEN
        SET limit_to = LEFT(limit_to, LENGTH(limit_to) - 1);
        IF limit_to REGEXP '^[0-9]+$' THEN -- check is integer
            SET limit_to_val = CAST(limit_to AS SIGNED);
        ELSE
            RETURN 0;
        END IF;
    ELSE
        RETURN 0;
    END IF;

    IF reverse = 0 THEN
        IF interval_from <= limit_from_val AND
            (limit_to_val is NOT NULL AND limit_to_val <= interval_to
            OR limit_to_val is NULL) THEN
            RETURN 1;
        END IF;
    ELSE
        IF limit_from_val <= interval_from AND
            (limit_to_val is NOT NULL AND interval_to < limit_to_val
            OR limit_to_val is NULL) THEN
            RETURN 1;
        END IF;
    END IF;

    RETURN 0;
END''' % config['definer']
    c.execute(sql)
    c.close()


def downgrade(conn):
    pass