#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import logging
import sys
import os
import traceback
from getopt import getopt, GetoptError
from _dbtool import (DBTool, Session, get_config, DBToolException,
    ConfigException, DBToolUpdateException)


def main(argv):
    try:
        config_filename = os.path.join(os.path.dirname(__file__), 'dbtool.conf')
        conf = get_config(config_filename)
        Session.setConf(conf)
        log_filename = Session.getConf()['log_filename']
        configure_loggers(log_filename)
    except ConfigException, e:
        print(unicode(e))
        return
    except IOError:
        print('укажите корректный путь и имя конфигурационного файла, для которого у вас есть права на запись')
        return
    logger = logging.getLogger('dbtool')
    logger.debug('========== Новый запуск ==========')
    try:
        Session.checkConf()
    except ConfigException, e:
        logger.error(unicode(e))
        return

    dbtool = DBTool()
    try:
        dbtool.load(Session)
        opts, args = getopt(argv, 'hlcu:',
                            ['help', 'list', 'change-definers', 'update=', 'update-content='])
        if args:
            logger.error('неизвестные аргументы, смотрите --help: "{0}"'.format(' '.join(args)))
            sys.exit(1)

        if not opts:
            msg = dbtool.usage()
            logger.info(msg)
            sys.exit(1)

        for opt, arg in opts:
            if opt in ['-h', '--help']:
                msg = dbtool.usage()
                logger.info(msg)
                sys.exit(0)
            elif opt in ['-l', '--list']:
                msg = dbtool.list_db_updates()
                logger.info(msg)
            elif opt in ['-c', '--change-definers']:
                dbtool.change_definers()
            elif opt in ['-u', '--update']:
                try:
                    version = int(arg)
                except ValueError:
                    logger.error('номер версии должен быть числом: "{0}"'.format(arg))
                    sys.exit(1)
                if version < 0:
                    logger.error('номер версии не может быть отрицательным числом')
                    sys.exit(1)
                dbtool.update_schema(version)
                logger.info('Результат работы смотрите в логе ({0})'.format(log_filename))
            elif opt in (b'--update-content'):
                try:
                    version = int(arg)
                except ValueError:
                    logger.error('номер версии должен быть числом: "{0}"'.format(arg))
                    sys.exit(1)
                if version < 0:
                    logger.error('номер версии не может быть отрицательным числом')
                    sys.exit(1)
                dbtool.update_content(version)
                logger.info('Результат работы смотрите в логе ({0})'.format(log_filename))
            else:
                msg = dbtool.usage()
                logger.info(msg)
                sys.exit(1)
    except (GetoptError, DBToolException, ConfigException), e:
        logger.error(unicode(e))
        logger.info('Результат работы смотрите в логе ({0})'.format(log_filename))
        sys.exit(1)
    except DBToolUpdateException, e:
        logger.error(unicode(e))
        logger.error(unicode(''.join(traceback.format_tb(e.tb))))
        logger.info('Результат работы смотрите в логе ({0})'.format(log_filename))
        sys.exit(1)
    except Exception, e:
        logger.error(unicode(e))
        logger.error(unicode(traceback.format_exc(), encoding='utf-8'))
        logger.info('Результат работы смотрите в логе ({0})'.format(log_filename))
        sys.exit(1)
    finally:
        Session.closeConnection()
    sys.exit(0)


def configure_loggers(log_filename):
    logger = logging.getLogger('dbtool')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    f_hdl = logging.FileHandler(log_filename, 'a')
    f_hdl.setLevel(logging.DEBUG)
    f_hdl.setFormatter(formatter)
    logger.addHandler(f_hdl)

#     logging.basicConfig(
#         filename=log_filename,
#         filemode='a',
#         level=logging.DEBUG,
#         format='%(asctime)s [%(levelname)s] %(message)s')
    s_hdl = logging.StreamHandler()
    s_hdl.setLevel(logging.INFO)
    s_hdl.setFormatter(formatter)
    logger.addHandler(s_hdl)


if __name__ == '__main__':
    main(sys.argv[1:])
