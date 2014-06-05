#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import json
import os
import re
import sys
import gzip


__doc__ = '''\
Трансляция шаблонов печали
'''

content_filename = 'content_updates/content013fnkc.json.gz'

def translate(s):
    stack = []
    stack_1 = []

    s = re.sub(r"u(\\?(\"|')[^'\]\"]*\\?(\"|'))", r"\1", s)  # '' and u" "
    s = re.sub(r":h\}", r" }", s)  # :h}
    s = re.sub(r"\{end\s+:\}", r"{end:}", s)  # {end     :} to {end:}
    j = 0
    while j < len(s) - 6:  # end to endif or endfor
        m = re.match(r"\{\s*(for|if):", s[j:j + 6])
        if m:
            stack.append(m.group(1))
        n = re.match(r"\{end:\}", s[j:j + 6])
        if n and stack:
            l = len(s)
            s = s[0:j] + "{% end" + stack.pop() + " %}" + s[j + 6:l]
        j += 1

    s = re.sub(r"\{\s*(for|if):([^}]*)\}", r"{% \1 \2 %}", s)  # if for
    s = re.sub(r"\{else:\}", "{% else %}", s)
    s = re.sub(r"\{elif:([^}{]+)\}", r"{% elif \1 %}", s)
    s = re.sub(r"\{else:([^}{]+)\}", r"{% elif \1 %}", s)

    #    s = re.sub(r"^{([^%{][^{}=]*)}", r"{{ \1 }}", s)#variables
    #    s = re.sub(r"([^{]){([^%{][^{}=]*)}", r"\1{{ \2 }}", s)#variables
    s = re.sub(r"{{1,2}\s*(\w)\s*}{1,2}", r"{{ \1 }}", s)  # variables {n}
    s = re.sub(r"{{1,2}\s*([^%{\s][^{}=]*[^\s}{])\s*}{1,2}", r"{{ \1 }}", s)  # variables

    s = re.sub(r"{{([^{}]*)if([^{}]*)else([^{}]*)}}",
               r"{%if \2%}{{ \1 }}{% else %}\3{% endif %}", s)
    s = re.sub(r"{([^{}]*)if([^{}]*)else([^{}]*)}",
               r"{%if \2%}{{ \1 }}{% else %}\3{% endif %}", s)
    s = re.sub(r"\{:([^%}]*=[^%}]*)\}", r"{% set \1 %}", s)  # assignments
    s = re.sub(r"len\(([^\)]*)\)", r"\1|length", s)  # len to length

    s = re.sub(r"str(\()", r"\1", s)  # str()
    s = re.sub(r"\+([\s]*\\?(\"|')[^'\"]*\\?(\"|'))", r" ~ \1", s)  # concatenation
    s = re.sub(r"(\\?(\"|')[^\"']*\\?(\"|')[\s]*)\+", r"\1 ~ ", s)  # concatenation
    s = re.sub(r"(\\?(\"|')[^\"']*\\?(\"|')\*[^'\"]*[\s]*)\+", r"\1 ~ ", s)  # concatenation

    pattern = re.search(r"\.toString\((\\?(\'|\")[yM\.d-]*\\?(\'|\"))\)", s, flags=re.U)  #date

    while pattern:
        end = pattern.end()
        middle = pattern.start()
        start = middle - 1
        while re.match("\w|\.", s[start]) or stack_1 or s[start] == ']':
            if s[start] == ']':
                stack_1.append(']')
            if s[start] == '[':
                stack_1.pop()
            start -= 1
        start += 1
        s = s[:start] + "date_toString(" + s[start:middle] + "," + pattern.group(1) + ")" + s[end:]
        pattern = re.search(r"\.toString\((\\?(\'|\")[yM\.d-]*\\?(\'|\"))\)", s, flags=re.U)

        stack_1 = []

    pattern_1 = re.search(r"\.toString\((\\?(\'|\")[hms\.:-H]*\\?(\'|\"))\)", s, flags=re.U)  # time
    while pattern_1:
        end = pattern_1.end()
        middle = pattern_1.start()
        start = middle - 1
        while re.match("\w|\.", s[start]) or stack_1 or s[start] == ']':
            if s[start] == ']':
                stack_1.append(']')
            if s[start] == '[':
                stack_1.pop()
            start -= 1
        start += 1
        s = s[:start] + "time_toString(" + s[start:middle] + "," + pattern_1.group(1) + ")" + s[end:]
        pattern_1 = re.search(r"\.toString\((\\?(\'|\")[hms\.:-H]*\\?(\'|\"))\)", s, flags=re.U)

    return s


def upgrade(conn):
    global tools
    c = conn.cursor()

    # Этот код создаёт json.gz-файл
    # c.execute('''SELECT id, context, code, templateText FROM rbPrintTemplate WHERE valid = 1;''')
    # result = dict((_id, (context, code, template_text)) for (_id, context, code, template_text) in c)
    # with gzip.open(content_filename, 'w') as fout:
    #     fout.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))

    with gzip.open(content_filename, 'r') as fin:
        s = json.load(fin, encoding='utf-8')
        concode = dict(((context, code), _id) for (_id, (context, code, text)) in s.iteritems())
        source = dict((int(key), value) for (key, value) in s.iteritems())
    c.execute('''SELECT id, context, code, templateText, render, `default` FROM rbPrintTemplate''')
    c2 = conn.cursor()
    loaded_from_json = set()
    for _id, context, code, templateText, render, text in c:
        if _id in source:
            src = source[_id]
            if context == src[0] and code == src[1]:
                c2.execute('''UPDATE rbPrintTemplate SET templateText = "%s" WHERE id = %s''', (source[_id][2], _id))
                print('%s loaded from json' % _id)
            else:
                c2.execute('''INSERT INTO rbPrintTemplate (context, code, templateText, render) VALUES ("%s", "%s", "%s", %s)''', src + [0, ])
                print('%s inserted from json' % _id)
            loaded_from_json.add(_id)
        elif (context, code) in concode:
            print("(%s, %s) found..." % (context, code))
        else:
            if render == 0:
                new_text = translate(text)
                c2.execute('''UPDATE rbPrintTemplate SET templateText="%s" WHERE id = %s''', (new_text, _id))
                print('%s translated from standard' % _id)
            else:
                c2.execute('''UPDATE rbPrintTemplate SET templateText="%s" WHERE id = %s''', (text, _id))
                print('%s copied' % _id)
    for _id in set(source.iterkeys()) - loaded_from_json:
        src = source[_id]
        c2.execute('''INSERT INTO rbPrintTemplate (context, code, templateText, render) VALUES ("%s", "%s", "%s", %s)''', src + [0, ])
        new_id = c2.lastrowid
        print('>> %s inserted from json as %s' % (_id, new_id))