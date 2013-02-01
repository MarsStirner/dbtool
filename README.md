База данных ТМИС
================

TODO


Утилита dbtool
--------------

Утилита предназначена для апгрейдов и даунгрейдов версий схемы базы.


### Зависимости

* Python 2.6.6
* setuptools-0.6c11
* mysql-python
* libmysqlclient
* pyqt4
* sip-4.3

### Конфигурация

Файл `dbtool.conf` в каталоге с `dbtool` содержит настройки соединения к БД:

    [database]
    host = example.com
    username = user1
    password = password1
    dbname = s11r64


### Использование

Справка:

    $ dbtool -h
    Usage: dbtool [ -u <version> | -l | -h ]

    Options:
      -u, --update <version>   upgrade database to <version>
      -l, --list               list database versions
      -h, --help               show help message

Список обновлений базы с указанием текущего:

    $ dbtool -l
         0 БД без версионирования схемы
     *   1 Системная таблица Meta для хранения версий схемы БД
         2 В таблицу foo_bar добавлено поле количества baz в клинике

Обновиться на указанную версию:

    $ dbtool -u 2
    warning: database: table 'Meta' not found, assuming schema version 0
    upgrading to 1...
    upgrading to 2...
    updated to 2

