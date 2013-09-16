#!/usr/bin/pypy
# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import codecs
from contextlib import closing, contextmanager
import logging
import sys

logging.basicConfig(
    # stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s')
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime
# import yaml
import MySQLdb as db

__author__ = 'mmalkov'

from HTMLParser import HTMLParser

mattersRe = re.compile(ur'(?P<rus>.*) \((?P<lat>.*)\)')
CONFIG_FILENAME = os.path.join(os.path.dirname(__file__), 'dbtool.conf')


def get_config():
    p = ConfigParser(defaults={'port': '3306'})
    p.read([CONFIG_FILENAME])
    return {
        'host': p.get(b'database', b'host'),
        'port': p.get(b'database', b'port'),
        'username': p.get(b'database', b'username'),
        'password': p.get(b'database', b'password'),
        'dbname': p.get(b'database', b'dbname'),
        'definer': p.get(b'database', b'definer'),
        'rlsPath': p.get(b'rlsConvert', 'rlsPath', b'./rlsDisk')
    }


@contextmanager
def open_db_connection():
    params = get_config()
    logging.info(u'Opening database')
    with closing(db.connect(host=params['host'],
                            port=int(params['port']),
                            user=params['username'],
                            passwd=params['password'],
                            db=params['dbname'],
                            charset='utf8',
                            use_unicode=True)) as c:
        c.autocommit(False)
        logging.info(u'Database opened')
        yield c
    logging.info(u'Database closed')


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._data = {}
        self._currentName = ''
        self._currentRLS = None

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            a = dict(attrs)
            self._currentName = a['name']

    def unknown_decl(self, data):
        val = data[6:]
        if self._currentName == 'URL':
            self._currentRLS = int(val[val.index('/') + 1:val.rindex('.html')])
            self._data[self._currentRLS] = {}
            return
        elif self._currentName == 'NDV':
            am = getActMatters(val)
            self._data[self._currentRLS]['ACTMATTERS'] = am or val
            return
        self._data[self._currentRLS][self._currentName] = val


def getActMatters(string):
    match = mattersRe.match(string)
    if not match:
        return string, None
    else:
        gDict = match.groupdict()
        return gDict['rus'], gDict['lat']


def main3():
    """Ппреобразование папки с кучей рлсовских файлов к одному огромному файлу.
    Его быстрее читать, хотя преобразование, да, медленное"""
    pathName = './rlsDisk'
    with open('rlsBloat.html', 'wt', buffering=65536) as fout:
        for fileName in os.listdir(pathName):
            with open(os.path.join(pathName, fileName), 'rt', buffering=16777216) as fin:
                fout.write(fin.read().decode('utf-16').encode('utf-16'))


def main4():
    """Преобразование одного жирного РЛСовского файла к ЯМЛ-представлению. Требует не менее 3 ГБ свободной ОЗУ!!!"""
    config = get_config()
    with open_db_connection() as dbc:
        dbc.autocommit(False)

        d_Packing = {}
        d_Filling = {}
        d_TradeName = {}
        d_AM = {}
        d_Form = {}
        d_Unit = {}
        d_Nomen = {}

        rd_Packing = {}
        rd_Filling = {}
        rd_TradeName = {}
        rd_AM = {}
        rd_Form = {}
        rd_Unit = {}

        fields = (
            'actMatters_id', 'tradeName_id', 'form_id', 'packing_id', 'filling_id', 'unit_id', 'dosageValue',
            'dosageUnit_id', 'drugLifetime', 'regDate'
        )

        logging.info(u'Loading database tables')
        with dbc as cursor:
            logging.info('... `rbUnit`')
            cursor.execute('''SELECT `id`, `code`, `name` FROM `rbUnit`; ''')
            for row in cursor:
                rd_Unit[row[1]] = row[0]
                d_Unit[row[0]] = row[1:]

            logging.info('... `rlsPacking`')
            cursor.execute('''SELECT `id`, `name` FROM `rlsPacking`; ''')
            for row in cursor:
                rd_Packing[row[1]] = row[0]
                d_Packing[row[0]] = row[1]

            logging.info('... `rlsFilling`')
            cursor.execute('''SELECT `id`, `name` FROM `rlsFilling`; ''')
            for row in cursor:
                rd_Filling[row[1]] = row[0]
                d_Filling[row[0]] = row[1]

            logging.info('... `rlsForm`')
            cursor.execute('''SELECT `id`, `name` FROM `rlsForm`; ''')
            for row in cursor:
                rd_Form[row[1]] = row[0]
                d_Form[row[0]] = row[1]

            logging.info('... `rlsTradeName`')
            cursor.execute('''SELECT `id`, `localName`, `name` FROM `rlsTradeName`; ''')
            for row in cursor:
                rd_TradeName[row[1:]] = row[0]
                d_TradeName[row[0]] = row[1:]

            logging.info('... `rlsActMatters`')
            cursor.execute('''SELECT `id`, `localName`, `name` FROM `rlsActMatters`; ''')
            for row in cursor:
                rd_AM[row[1:]] = row[0]
                d_AM[row[0]] = row[1:]

            logging.info('... `rlsNomen`')
            cursor.execute('''SELECT * FROM `rlsNomen`; ''')
            for row in cursor:
                d_Nomen[row[0]] = row[1:]

        logging.info("Parsing BLOAT...")
        p = MyHTMLParser()

        pathName = config['rlsPath']
        for fileName in os.listdir(pathName):
            with open(os.path.join(pathName, fileName), 'rt', buffering=16777216) as fin:
                buf = fin.read()
                p.feed(buf.decode('utf-16'))

        logging.info("Running")
        try:
            cursor = dbc.cursor()
            for rlsId, rlsData in p._data.iteritems():
                dosage = None
                dosageUnit = rlsData.get(
                    'DFMASS_SHORTNAME', rlsData.get(
                        'DFCONC_SHORTNAME', rlsData.get(
                            'DFACT_SHORTNAME', rlsData.get(
                                'DFSIZE_SHORTNAME'))))
                dosageUnitLong = rlsData.get(
                    'DFMASS_FULLNAME', rlsData.get(
                        'DFCONC_FULLNAME', rlsData.get(
                            'DFACT_FULLNAME', rlsData.get(
                                'DFSIZE_FULLNAME'))))
                if not (dosageUnit and dosageUnitLong):
                    dosageUnit = rlsData.get(
                        'PPACKMASS_SHORTNAME', rlsData.get(
                            'PPACKVOLUME_SHORTNAME'))
                    dosageUnitLong = rlsData.get(
                        'PPACKMASS_FULLNAME', rlsData.get(
                            'PPACKVOLUME_FULLNAME'))
                    if dosageUnit and dosageUnitLong:
                        dosage = rlsData.get(
                            'PPACKMASS', rlsData.get(
                                'PPACKVOLUME'))
                    else:
                        dosage = rlsData.get('DRUGDOSE')
                        if dosage is not None:
                            dosageUnit = u'шт'
                            dosageUnitLong = u'штука'
                else:
                    dosage = rlsData.get(
                        'DFMASS', rlsData.get(
                            'DFCONC', rlsData.get(
                                'DFACT', rlsData.get(
                                    'DFSIZE', rlsData.get(
                                        'DRUGDOSE')))))
                if dosage is None:
                    dUnit_id = None
                else:
                    dUnit_id = rd_Unit.get(dosageUnit)
                    if (not dUnit_id) and dosageUnit and dosageUnitLong:
                        cursor.execute('''INSERT INTO `rbUnit` (`code`, `name`) VALUES (%s, %s)''',
                                       (dosageUnit, dosageUnitLong))
                        dUnit_id = cursor.lastrowid
                        d_Unit[dUnit_id] = dosageUnit
                        rd_Unit[dosageUnit] = dUnit_id

                unit = rlsData.get(
                    'PPACKMASS_SHORTNAME', rlsData.get(
                        'PPACKVOLUME_SHORTNAME', rlsData.get(
                            'DFMASS_SHORTNAME', u'шт')))
                unitLong = rlsData.get(
                    'PPACKMASS_FULLNAME', rlsData.get(
                        'PPACKVOLUME_FULLNAME', rlsData.get(
                            'DFMASS_FULLNAME', u'штука')))

                unit_id = rd_Unit.get(unit)
                if (not unit_id) and unit and unitLong:
                    cursor.execute('''INSERT INTO `rbUnit` (`code`, `name`) VALUES (%s, %s)''',
                                   (unit, unitLong))
                    unit_id = cursor.lastrowid
                    d_Unit[unit_id] = unit
                    rd_Unit[unit] = unit_id

                regD = rlsData.get('REGDATE')
                if regD:
                    regDate = datetime.strptime(regD, '%Y%m%d').date()
                else:
                    regDate = None

                name = rlsData.get('TRADENAME'), rlsData.get('LATNAME')
                name_id = rd_TradeName.get(name)
                if not name_id:
                    # print 'TradeName', name[0], name[1], 'not found'
                    cursor.execute('''INSERT INTO `rlsTradeName` (`localName`, `name`) VALUES (%s, %s)''', name)
                    name_id = cursor.lastrowid
                    d_TradeName[name_id] = name
                    rd_TradeName[name] = name_id

                packing = rlsData.get('UPACK_SHORTNAME')
                if packing:
                    packing_id = rd_Packing.get(packing)
                    if not packing_id:
                        # print 'Packing', packing, 'not found'
                        cursor.execute('''INSERT INTO `rlsPacking` (`name`) VALUES (%s)''', packing)
                        packing_id = cursor.lastrowid
                        d_Packing[packing_id] = packing
                        rd_Packing[packing] = packing_id
                else:
                    packing_id = None

                filling = rlsData.get('PPACK_FULLNAME')
                if filling:
                    filling_id = rd_Filling.get(filling)
                    if not filling_id:
                        # print 'Filling', filling, 'not found'
                        cursor.execute('''INSERT INTO `rlsFilling` (`name`) VALUES (%s)''', filling)
                        filling_id = cursor.lastrowid
                        d_Filling[filling_id] = filling
                        rd_Filling[filling] = filling_id
                else:
                    filling_id = None

                form = rlsData.get('DRUGFORM_FULLNAME')
                if form:
                    form_id = rd_Form.get(form)
                    if not form_id:
                        # print 'Form', form, 'not found'
                        cursor.execute('''INSERT INTO `rlsForm` (`name`) VALUES (%s)''', form)
                        form_id = cursor.lastrowid
                        d_Form[form_id] = form
                        rd_Form[form] = form_id
                else:
                    form_id = None

                matter = rlsData.get('ACTMATTERS')
                if matter:
                    matter_id = rd_AM.get(matter)
                    if not matter_id:
                        cursor.execute('''INSERT INTO `rlsActMatters` (`localName`, `name`) VALUES (%s, %s)''',
                                       matter)
                        matter_id = cursor.lastrowid
                        d_AM[matter_id] = matter
                        rd_AM[matter] = matter_id
                else:
                    matter_id = None

                try:
                    lifetime = int(rlsData.get('DRUGLIFETIME'))
                except:
                    lifetime = None

                dbData = d_Nomen.get(rlsId)
                data = {
                    'id': rlsId,
                    'actMatters_id': matter_id,
                    'tradeName_id': name_id,
                    'form_id': form_id,
                    'filling_id': filling_id,
                    'packing_id': packing_id,
                    'unit_id': unit_id,
                    'dosageUnit_id': dUnit_id,
                    'dosageValue': dosage,
                    'regDate': regDate,
                    'drugLifetime': lifetime,
                }
                if dbData:
                    if any([dbData[n] != data[k] for n, k in enumerate(fields)]):
                        reason = '\n    '.join(
                            ['%s: %s != %s' % (k, dbData[n], data[k])
                             for n, k in enumerate(fields)
                             if dbData[n] != data[k]
                            ])
                        logging.info(u'Updating rls:%i because:\n    %s', rlsId, reason)
                        sql = u'UPDATE rlsNomen SET ' \
                              u'`actMatters_id` = %(actMatters_id)s, ' \
                              u'`tradeName_id` = %(tradeName_id)s, ' \
                              u'`form_id` = %(form_id)s, ' \
                              u'`packing_id` = %(packing_id)s, ' \
                              u'`filling_id` = %(filling_id)s, ' \
                              u'`unit_id` = %(unit_id)s, ' \
                              u'`dosageValue` = %(dosageValue)s, ' \
                              u'`dosageUnit_id` = %(dosageUnit_id)s, ' \
                              u'`regDate` = %(regDate)s, ' \
                              u'`drugLifetime` = %(drugLifetime)s ' \
                              u'WHERE `id` = %(id)s'
                        try:
                            cursor.execute(sql, data)
                        except TypeError:
                            logging.critical(u'Achtung!\n%s', repr(data))
                            raise
                else:
                    sql = u'INSERT INTO rlsNomen (`id`, `actMatters_id`, `tradeName_id`, `form_id`, `packing_id`, ' \
                          u'`filling_id`,`unit_id`,`dosageValue`, `dosageUnit_id`, `regDate`, `drugLifetime`) ' \
                          u'VALUES (%(id)s, %(actMatters_id)s, %(tradeName_id)s, %(form_id)s, %(packing_id)s, ' \
                          u'%(filling_id)s, %(unit_id)s, %(dosageValue)s, %(dosageUnit_id)s, %(regDate)s, ' \
                          u'%(drugLifetime)s)'
                    cursor.execute(sql, data)

        finally:
            dbc.commit()
            cursor.close()

            # with open('output.yaml', 'wt') as fout:
            #     yaml.safe_dump(p._data, fout, default_flow_style=False, encoding='utf-8', allow_unicode=True)


def main1():
    """Преобразование папки с кучей РЛСовских файлов к ЯМЛу. Требует не менее 3 ГБ свободного ОЗУ"""
    pathName = './rlsDisk'
    result = {}
    for fileName in os.listdir(pathName):
        code = int(fileName[3:])
        p = MyHTMLParser()
        with open(os.path.join(pathName, fileName), 'rt', buffering=16777216) as fin:
            p.feed(fin.read().decode('utf-16'))
        result[code] = p._data

    with open('output.yaml', 'wt', buffering=16777216) as fout:
        yaml.safe_dump(result, fout, default_flow_style=False, encoding='utf-8', allow_unicode=True)


def main2():
    """Преобразование ответа от 1С Аптеки (getDrugList) к ЯМЛовской форме"""

    def getQualifiers(node):
        qNode = node.find('{urn:hl7-org:v3}qualifier')
        if qNode is not None:
            nameET = qNode.find('{urn:hl7-org:v3}name')
            valueET = qNode.find('{urn:hl7-org:v3}value')
            valueOT = valueET.find('{urn:hl7-org:v3}originalText') if valueET is not None else None
            value = valueOT.text if (valueOT is not None) else None
            name = nameET.attrib['code']
            yield name, {'code': valueET.attrib.get('code'),
                         'displayName': valueET.attrib.get('displayName'),
                         'csName': valueET.attrib.get('codeSystemName'),
                         'value': value}

    with codecs.open('drugList.xml', 'r') as fin:
        root = ET.XML(fin.read())
        startTree = root \
            .find('{http://schemas.xmlsoap.org/soap/envelope/}Body') \
            .find('{MISExchange}GetDrugListResponse') \
            .find('{MISExchange}return')
        result = {}
        for drugET in startTree:
            codeET = drugET.find('{urn:hl7-org:v3}code')
            drugDict = {}
            if codeET.attrib.get('codeSystemName', None) == 'RLS_NOMEN':
                result[int(codeET.attrib['code'])] = drugDict
            else:
                continue
            for translation in codeET:
                tcode = translation.attrib['code']
                tname = translation.attrib.get('displayName', None)
                csn = translation.attrib['codeSystemName']
                if csn == 'RLS_TRADENAMES':
                    drugDict['TRADENAME_RUS'] = tcode.replace('_', ' ')
                    drugDict['TRADENAME_LAT'] = tname

                elif csn == 'RLS_ACTMATTERS':
                    am = getActMatters(tname)
                    if am is None:
                        drugDict['ACTMATTERS_NONE'] = tname
                    else:
                        drugDict['ACTMATTERS'] = am

                elif csn == 'RLS_CLSDRUGFORMS':
                    # drugDict['DRUGFORM_FULLNAME'] = tname
                    # drugDict['DRUGFORM_SHORTNAME'] = tcode

                    for qName, qDict in getQualifiers(translation):
                        if qName in ('DFMASS', 'DFCONC', 'DFSIZE', 'DFFACT'):
                            drugDict[qName] = qDict['value']
                            drugDict[qName + '_SHORTNAME'] = qDict['code']
                            drugDict[qName + '_FULLNAME'] = qDict['displayName']
                        elif qName == 'CLSDRUGFORM':
                            # Тут очень серьёзный вопрос. Ибо здесь данные более общие
                            drugDict['DRUGFORM_FULLNAME'] = tname
                            drugDict['DRUGFORM_SHORTNAME'] = tcode

                elif tcode == 'PPACK':
                    for qName, qDict in getQualifiers(translation):
                        if qName == 'PPACK':
                            drugDict['DRUGSINPPACK'] = qDict['value']
                            drugDict[qName + '_SHORTNAME'] = qDict['code']
                            drugDict[qName + '_FULLNAME'] = qDict['displayName']
                        elif qName in ('PPACKVOLUME', 'PPACKMASS'):
                            drugDict[qName] = qDict['value']
                            drugDict[qName + '_SHORTNAME'] = qDict['code']
                            drugDict[qName + '_FULLNAME'] = qDict['displayName']

                elif tcode in ('UPACK', 'SPACK'):
                    for qName, qDict in getQualifiers(translation):
                        if qName == tcode:
                            drugDict[qName + '_SHORTNAME'] = qDict['code']
                            drugDict[qName + '_FULLNAME'] = qDict['displayName']

    with open('output2.yaml', 'wt') as fout:
        yaml.safe_dump(result, fout, default_flow_style=False, encoding='utf-8', allow_unicode=True)


if __name__ == "__main__":
    if '--help' in sys.argv or '-h' in sys.argv:
        print(u'Скрипт преобразования данных из дампа РЛС в записи в БД.\n'
              u'Используется файл dbtool.conf в качестве конфига.\n'
              u'Файлы должны быть уложены в директорию %s\n'
              u'(определяется в параметре rlsPath секции rlsConvert)\n'
              u'Для работы необходимо не менее 3 ГиБ свободной ОЗУ, \n'
              u'желательно использовать интерпретатор PyPy (быстрее в 4-7 раз)\n'
              u'Преобразование может занять очень много времени (около 10 минут с PyPy)' % get_config()['rlsPath'])
    else:
        main4()
