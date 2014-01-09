#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

import sys
import os
from getopt import getopt, GetoptError
from _dbtool import DBTool, DBToolException

if os.name == 'nt' and sys.stdout.isatty():
    ENCODING = 'CP866'
else:
    try:
        import locale
        ENCODING = locale.getpreferredencoding()
        if not ENCODING or 'ascii' in ENCODING.lower():
            ENCODING = 'UTF-8'
    except locale.Error:
        ENCODING = 'UTF-8'

def error(msg):
    print('error: {0}'.format(msg).encode(ENCODING, 'replace'),
          file=sys.stderr)

def info(msg, file=sys.stdout):
    print(msg.encode(ENCODING, 'replace'), file=file)


def main(argv):
    CONFIG_FILENAME = os.path.join(os.path.dirname(__file__), 'dbtool.conf')
    dbtool = DBTool()
    try:
        dbtool.load(CONFIG_FILENAME)
        opts, args = getopt(argv, b'hlcu:',
                            [b'help', b'list', b'change-definers', b'update=', b'update-content='])
        if args:
            error('bad command line arguments: "{0}"'.format(' '.join(args)))
            sys.exit(1)

        if not opts:
            msg = dbtool.usage()
            info(msg, file=sys.stderr)
            sys.exit(1)

        for opt, arg in opts:
            if opt in [b'-h', b'--help']:
                msg = dbtool.usage()
                info(msg, file=sys.stderr)
                sys.exit(0)
            elif opt in [b'-l', b'--list']:
                msg = dbtool.list_db_updates()
                info(msg)
            elif opt in [b'-c', b'--change-definers']:
                dbtool.change_definers()
            elif opt in [b'-u', b'--update']:
                try:
                    version = int(arg)
                except ValueError:
                    error('argument must be a number: "{0}"'.format(arg))
                    sys.exit(1)
                if version < 0:
                    error('argument must be a '
                          'positive number: {0}'.format(version))
                    sys.exit(1)
                dbtool.update_schema(version)
            elif opt in (b'--update-content'):
                try:
                    version = int(arg)
                except ValueError:
                    error('argument must be a number: "{0}"'.format(arg))
                    sys.exit(1)
                if version < 0:
                    error('argument must be a '
                          'positive number: {0}'.format(version))
                    sys.exit(1)
                dbtool.update_content(version)
            else:
                msg = dbtool.usage()
                info(msg, file=sys.stderr)
                sys.exit(1)
    except (GetoptError, DBToolException), e:
        error(e)
        sys.exit(1)
    except:
        raise
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
#     main(sys.argv[1:])
    
    main(['--update-content=2'])
#     main(['-l'])
