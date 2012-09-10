# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function



__doc__ = '''\
Обновляет шаблоны печати "Лист назначений" и "Лист назначений_реанимация"
'''


def upgrade(conn):
    templates = [
# новый лист назначений
'''\
<html>
<body STYLE=\\"font-family: Times New Roman; font-size: 12pt\\">
{setPageSize('A4')} {setOrientation('L')}
{setLeftMargin(30)} {setTopMargin(10)} {setBottomMargin(5)} {setRightMargin(10)}

{:tmpPerson = action.person.shortName}

{action.begDate.date.toString(\\"dd.MM.yyyy\\")} г.
<h2 align=\\"center\\"><b>ГУЗ \\"САРАТОВСКАЯ ОБЛАСТНАЯ ДЕТСКАЯ КЛИНИЧЕСКАЯ БОЛЬНИЦА\\"</b></h1>
<h3 align=\\"center\\"><b>ЛИСТ НАЗНАЧЕНИЙ
<br/>История болезни № 
{: currentAction = None}
{for: action in event.actions}
    {if: action.name == u\\"Поступление\\"}{: currentAction = action}{end:}
{end:}<b>{currentAction[u\\"Номер ИБ\\"].value if currentAction else ''}</b></h2>

<hr> 
1. Ф.И.О.: <b>{client.fullName}</b><br/>
2. Дата рождения: <b>{client.birthDate} г. (возраст: {client.age})</b><br/>
3. Рост: <b>{currentAction[u\\"Рост\\"].value if currentAction else ''} см.</b>, Вес: <b>{currentAction[u\\"Вес\\"].value if currentAction else ''} кг.</b><br/>
{: currentAction = None}
{for: action in event.actions}
{if: (action.code >= \\"1_1_01\\") and (action.code <= \\"1_1_17\\")}{: currentAction = action}{end:}
{end:}
{for: prop in currentAction}
{if: prop.name == u\\"Основной клинический диагноз\\" and prop.value != u\\"\\"}
4. Основной диагноз: <b>{currentAction[u\\"Основной клинический диагноз\\"].value if currentAction else ''}</b>
{end:}{end:}

{: currentAction = None}
{for: action in event.actions}
{if: action.code == \\"3_1_02\\"}{: currentAction = action}{end:}
{end:}

<table style=\\"font-family: Times New Roman; font-size: 10pt\\" border=\\"1\\" cellpadding=\\"0\\" cellspacing=\\"0\\" width=\\"100%\\">
<tr><td><b>Наименование:</b></td>
{:dt = currentAction.directionDate.date}
<td><b>{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
<td><b>{:dt = dt.addDays(1)}{dt.toString(\\"dd.MM\\")}</b></td>
</tr>

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Режим\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Режим:{currentAction[u\\"Режим\\"].value if currentAction else ''}</b>
        </td></tr>
        {end:}
        {if: action.name == u\\"Стол\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Стол:{currentAction[u\\"Стол\\"].value if currentAction else ''}</b></td>
        </tr>
        {end:}
    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Назначения\\"}{: currentAction = action}
        <tr>
        <td><b>{currentAction[u\\"Наименование\\"].value if currentAction else ''}</b>c {action.begDate.date.toString(\\"dd.MM.yyyy\\")} по {action.plannedEndDate.date.toString(\\"dd.MM.yyyy\\")}
        {currentAction[u\\"Доза\\"].value if currentAction else ''},{currentAction[u\\"Скорость введения\\"].value if currentAction else ''},
        {currentAction[u\\"Способ введения\\"].value if currentAction else ''}{currentAction[u\\"Примечания\\"].value if currentAction else '' :n}</td>
        </tr>

        {end:}

{if: action.code >= u\\"3_3\\" and action.code < u\\"3_4\\"}
<tr><td><b>{action.name}</b>{if: action.code != u\\"3_3_04\\" and action.code != u\\"3_3_06\\"}, назначено: {action[u\\"Количество процедур (назначено)\\"]}{end:}</td></tr>
{end:}

    {end:}
{end:}


{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инфузионная терапия\\"}{: currentAction = action}
                {for: prop in action}
                    {if: prop.value != \\"\\"}
                     <tr><td>{prop.value  :n}</td></tr>
                    {end:}
                {end:}
        {end:}
    {end:}
{end:}


{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инсулинотерапия\\"}{: currentAction = action}
            
<!--tr><td>c {action.begDate.date.toString(\\"dd.MM.yyyy\\")} г.<br/></td></tr-->
<tr><td><b>{currentAction[u\\"Наименование Инсулин 1\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 1\\"].value if currentAction else '' :n}</td></tr>
<tr><td><b>{currentAction[u\\"Наименование Инсулин 2\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 2\\"].value if currentAction else '' :n}</td></tr>
        {end:}
    {end:}
{end:}




<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
</table>
<br/><br/><br/>
<b>Медсестра:</b>_________________<b>/_______________/</b><br/>
<b>Врач:</b>_________________<b>/{tmpPerson}/</b>
</body>
</html>''',          
# новый лист назначений реанимации
'''\
<html>
<body STYLE=\\"font-family: Times New Roman; font-size: 12pt\\">
{setPageSize('A4')}
{setOrientation('L')}
{action.begDate.date.toString(\\"dd.MM.yyyy\\")}
{:date = action.directionDate.date}
<h2 align=\\"center\\"><b>ГУЗ \\"САРАТОВСКАЯ ОБЛАСТНАЯ ДЕТСКАЯ КЛИНИЧЕСКАЯ БОЛЬНИЦА\\"</b></h1>
<h3 align=\\"center\\"><b>ЛИСТ НАЗНАЧЕНИЙ
<br/>История болезни № {: currentAction = None}
{for: action in event.actions}
{if: action.name == u\\"Поступление\\"}{: currentAction = action}{end:}
{end:}<b>{currentAction[u\\"Номер ИБ\\"].value if currentAction else ''}</b></h2>

<hr/>
1. Ф.И.О.: <b>{client.fullName}</b><br/>
2. Дата рождения: <b>{client.birthDate} (возраст: {client.age})</b><br/>
3. Вес: 18:00 ______    Вес: 06:00 ______       В отделении: 
<br/><br/>

<table style=\\"font-family: Times New Roman; font-size: 12pt\\" border=\\"1\\" cellpadding=\\"0\\" cellspacing=\\"0\\" width=\\"100%\\">
<tr><td><b>Наименование:</b></td>
<td><b>12</b></td>
<td><b>13</b></td>
<td><b>14</b></td>
<td><b>15</b></td>
<td><b>16</b></td>
<td><b>17</b></td>
<td><b>18</b></td>
<td><b>19</b></td>
<td><b>20</b></td>
<td><b>21</b></td>
<td><b>22</b></td>
<td><b>23</b></td>
<td><b>24</b></td>
<td><b>&nbsp;1</b></td>
<td><b>&nbsp;2</b></td>
<td><b>&nbsp;3</b></td>
<td><b>&nbsp;4</b></td>
<td><b>&nbsp;5</b></td>
<td><b>&nbsp;6</b></td>
<td><b>&nbsp;7</b></td>
<td><b>&nbsp;8</b></td>
<td><b>&nbsp;9</b></td>
<td><b>10</b></td>
<td><b>11</b></td>
<td><b>12</b></td>
</tr>
{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Режим\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Режим:{currentAction[u\\"Режим\\"].value if currentAction else ''}</b>
        </td></tr>
        {end:}
        {if: action.name == u\\"Стол\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Стол:{currentAction[u\\"Стол\\"].value if currentAction else ''}</b></td>
        </tr>
        {end:}
    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Назначения\\"}{: currentAction = action}
        <tr>
        <td><b>{currentAction[u\\"Наименование\\"].value if currentAction else ''}</b>
        {currentAction[u\\"Доза\\"].value if currentAction else ''},{currentAction[u\\"Скорость введения\\"].value if currentAction else ''}
        {currentAction[u\\"Способ введения\\"].value if currentAction else ''}{currentAction[u\\"Примечания\\"].value if currentAction else '' :n}</td>
        </tr>
        {end:}
{if: action.code >= u\\"3_3\\" and action.code < u\\"3_4\\"}
<tr><td><b>{action.name}</b>{if: action.code != u\\"3_3_04\\" and action.code != u\\"3_3_06\\"}, назначено: {action[u\\"Количество процедур (назначено)\\"]}{end:}</td></tr>
{end:}

    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инфузионная терапия\\"}{: currentAction = action}
                {for: prop in action}
                    {if: prop.value != \\"\\"}
                     <tr><td>{prop.value  :n}</td></tr>
                    {end:}
                {end:}
        {end:}
    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инсулинотерапия\\"}{: currentAction = action}
            
<!--tr><td>c {action.begDate.date.toString(\\"dd.MM.yyyy\\")} г.<br/></td></tr-->
<tr><td><b>{currentAction[u\\"Наименование Инсулин 1\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 1\\"].value if currentAction else '' :n}</td></tr>
<tr><td><b>{currentAction[u\\"Наименование Инсулин 2\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 2\\"].value if currentAction else '' :n}</td></tr>
        {end:}
    {end:}
{end:}

<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
</table>
<br/><br/><br/>
<b>Врач:</b>____________________<b>/{action.person.shortName}/</b><br/>
<b>Медсестра:</b>___________________<b>/</b>________________<b>/</b>
</body>
</html>''',]
    c = conn.cursor()
    stmt = u"""UPDATE rbPrintTemplate SET `default`=\"%s\" where name=\"Лист назначений\"""" % templates[0]
    c.execute(stmt)
    stmt = u"""UPDATE rbPrintTemplate SET `default`=\"%s\" where name=\"Лист назначений_реанимация\"""" % templates[1]
    c.execute(stmt)


def downgrade(conn):
        templates = [
# старый лист назначений реанимации
'''\
<html>
<body STYLE=\\"font-family: Times New Roman; font-size: 12pt\\">
{setPageSize('A4')} {setOrientation('L')}
{setLeftMargin(30)} {setTopMargin(10)} {setBottomMargin(5)} {setRightMargin(10)}

{:tmpPerson = action.person.shortName}

{action.begDate.date.toString(\\"dd.MM.yyyy\\")} г.
<h2 align=\\"center\\"><b>ГУЗ \\"САРАТОВСКАЯ ОБЛАСТНАЯ ДЕТСКАЯ КЛИНИЧЕСКАЯ БОЛЬНИЦА\\"</b></h1>
<h3 align=\\"center\\"><b>ЛИСТ НАЗНАЧЕНИЙ
<br/>История болезни № 
{: currentAction = None}
{for: action in event.actions}
    {if: action.name == u\\"Поступление\\"}{: currentAction = action}{end:}
{end:}<b>{currentAction[u\\"Номер ИБ\\"].value if currentAction else ''}</b></h2>

<hr> 
1. Ф.И.О.: <b>{client.fullName}</b><br/>
2. Дата рождения: <b>{client.birthDate} г. (возраст: {client.age})</b><br/>
3. Рост: <b>{currentAction[u\\"Рост\\"].value if currentAction else ''} см.</b>, Вес: <b>{currentAction[u\\"Вес\\"].value if currentAction else ''} кг.</b><br/>
{: currentAction = None}
{for: action in event.actions}
{if: (action.code >= \\"1_1_01\\") and (action.code <= \\"1_1_17\\")}{: currentAction = action}{end:}
{end:}
{for: prop in currentAction}
{if: prop.name == u\\"Основной клинический диагноз\\" and prop.value != u\\"\\"}
4. Основной диагноз: <b>{currentAction[u\\"Основной клинический диагноз\\"].value if currentAction else ''}</b>
{end:}{end:}

{: currentAction = None}
{for: action in event.actions}
{if: action.code == \\"3_1_02\\"}{: currentAction = action}{end:}
{end:}

<table style=\\"font-family: Times New Roman; font-size: 10pt\\" border=\\"1\\" cellpadding=\\"0\\" cellspacing=\\"0\\" width=\\"100%\\">
<tr><td><b>Наименование:</b></td>
{:date = currentAction.directionDate.date}
<td><b>{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
<td><b>{:date = date.addDays(1)}{date.toString(\\"dd.MM\\")}</b></td>
</tr>

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Режим\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Режим:{currentAction[u\\"Режим\\"].value if currentAction else ''}</b>
        </td></tr>
        {end:}
        {if: action.name == u\\"Стол\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Стол:{currentAction[u\\"Стол\\"].value if currentAction else ''}</b></td>
        </tr>
        {end:}
    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Назначения\\"}{: currentAction = action}
        <tr>
        <td><b>{currentAction[u\\"Наименование\\"].value if currentAction else ''}</b>c {action.begDate.date.toString(\\"dd.MM.yyyy\\")} по {action.plannedEndDate.date.toString(\\"dd.MM.yyyy\\")}
        {currentAction[u\\"Доза\\"].value if currentAction else ''}x{currentAction[u\\"Количество раз в день\\"].value if currentAction else ''}р/д,
        {currentAction[u\\"Способ введения\\"].value if currentAction else ''}{currentAction[u\\"Время приема\\"].value if currentAction else '' :n}</td>
        </tr>

        {end:}

{if: action.code >= u\\"3_3\\" and action.code < u\\"3_4\\"}
<tr><td><b>{action.name}</b>{if: action.code != u\\"3_3_04\\" and action.code != u\\"3_3_06\\"}, назначено: {action[u\\"Количество процедур (назначено)\\"]}{end:}</td></tr>
{end:}

    {end:}
{end:}


{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инфузионная терапия\\"}{: currentAction = action}
                {for: prop in action}
                    {if: prop.value != \\"\\"}
                     <tr><td>{prop.value  :n}</td></tr>
                    {end:}
                {end:}
        {end:}
    {end:}
{end:}


{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инсулинотерапия\\"}{: currentAction = action}
            
<!--tr><td>c {action.begDate.date.toString(\\"dd.MM.yyyy\\")} г.<br/></td></tr-->
<tr><td><b>{currentAction[u\\"Наименование Инсулин 1\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 1\\"].value if currentAction else '' :n}</td></tr>
<tr><td><b>{currentAction[u\\"Наименование Инсулин 2\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 2\\"].value if currentAction else '' :n}</td></tr>
        {end:}
    {end:}
{end:}




<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
</table>
<br/><br/><br/>
<b>Медсестра:</b>_________________<b>/_______________/</b><br/>
<b>Врач:</b>_________________<b>/{tmpPerson}/</b>
</body>
</html>''',          
# новый лист назначений реанимации
'''\
<html>
<body STYLE=\\"font-family: Times New Roman; font-size: 12pt\\">
{setPageSize('A4')}
{setOrientation('L')}
{action.begDate.date.toString(\\"dd.MM.yyyy\\")}
{:date = action.directionDate.date}
<h2 align=\\"center\\"><b>ГУЗ \\"САРАТОВСКАЯ ОБЛАСТНАЯ ДЕТСКАЯ КЛИНИЧЕСКАЯ БОЛЬНИЦА\\"</b></h1>
<h3 align=\\"center\\"><b>ЛИСТ НАЗНАЧЕНИЙ
<br/>История болезни № {: currentAction = None}
{for: action in event.actions}
{if: action.name == u\\"Поступление\\"}{: currentAction = action}{end:}
{end:}<b>{currentAction[u\\"Номер ИБ\\"].value if currentAction else ''}</b></h2>

<hr/>
1. Ф.И.О.: <b>{client.fullName}</b><br/>
2. Дата рождения: <b>{client.birthDate} (возраст: {client.age})</b><br/>
3. Вес: 18:00 ______    Вес: 06:00 ______       В отделении: 
<br/><br/>

<table style=\\"font-family: Times New Roman; font-size: 12pt\\" border=\\"1\\" cellpadding=\\"0\\" cellspacing=\\"0\\" width=\\"100%\\">
<tr><td><b>Наименование:</b></td>
<td><b>12</b></td>
<td><b>13</b></td>
<td><b>14</b></td>
<td><b>15</b></td>
<td><b>16</b></td>
<td><b>17</b></td>
<td><b>18</b></td>
<td><b>19</b></td>
<td><b>20</b></td>
<td><b>21</b></td>
<td><b>22</b></td>
<td><b>23</b></td>
<td><b>24</b></td>
<td><b>&nbsp;1</b></td>
<td><b>&nbsp;2</b></td>
<td><b>&nbsp;3</b></td>
<td><b>&nbsp;4</b></td>
<td><b>&nbsp;5</b></td>
<td><b>&nbsp;6</b></td>
<td><b>&nbsp;7</b></td>
<td><b>&nbsp;8</b></td>
<td><b>&nbsp;9</b></td>
<td><b>10</b></td>
<td><b>11</b></td>
<td><b>12</b></td>
</tr>
{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Режим\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Режим:{currentAction[u\\"Режим\\"].value if currentAction else ''}</b>
        </td></tr>
        {end:}
        {if: action.name == u\\"Стол\\"}{: currentAction = action}
        <tr>
        <td>
        <b>Стол:{currentAction[u\\"Стол\\"].value if currentAction else ''}</b></td>
        </tr>
        {end:}
    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Назначения\\"}{: currentAction = action}
        <tr>
        <td><b>{currentAction[u\\"Наименование\\"].value if currentAction else ''}</b>
        {currentAction[u\\"Доза\\"].value if currentAction else ''}x{currentAction[u\\"Количество раз в день\\"].value if currentAction else ''}р/д,
        {currentAction[u\\"Способ введения\\"].value if currentAction else ''}{currentAction[u\\"Время приема\\"].value if currentAction else '' :n}</td>
        </tr>
        {end:}
{if: action.code >= u\\"3_3\\" and action.code < u\\"3_4\\"}
<tr><td><b>{action.name}</b>{if: action.code != u\\"3_3_04\\" and action.code != u\\"3_3_06\\"}, назначено: {action[u\\"Количество процедур (назначено)\\"]}{end:}</td></tr>
{end:}

    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инфузионная терапия\\"}{: currentAction = action}
                {for: prop in action}
                    {if: prop.value != \\"\\"}
                     <tr><td>{prop.value  :n}</td></tr>
                    {end:}
                {end:}
        {end:}
    {end:}
{end:}

{: currentAction = None}
{for: action in event.actions}
    {if: action.status < 2}
        {if: action.name == u\\"Инсулинотерапия\\"}{: currentAction = action}
            
<!--tr><td>c {action.begDate.date.toString(\\"dd.MM.yyyy\\")} г.<br/></td></tr-->
<tr><td><b>{currentAction[u\\"Наименование Инсулин 1\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 1\\"].value if currentAction else '' :n}</td></tr>
<tr><td><b>{currentAction[u\\"Наименование Инсулин 2\\"].value if currentAction else '' :n}</b><br/>{currentAction[u\\"Схема введения 2\\"].value if currentAction else '' :n}</td></tr>
        {end:}
    {end:}
{end:}

<tr></tr>
<tr></tr>
<tr></tr>
<tr></tr>
</table>
<br/><br/><br/>
<b>Врач:</b>____________________<b>/{action.person.shortName}/</b><br/>
<b>Медсестра:</b>___________________<b>/</b>________________<b>/</b>
</body>
</html>''',]
        c = conn.cursor()
        stmt = u"""UPDATE rbPrintTemplate SET `default`=\"%s\" where name=\"Лист назначений\"""" % templates[0]
        c.execute(stmt)
        stmt = u"""UPDATE rbPrintTemplate SET `default`=\"%s\" where name=\"Лист назначений_реанимация\"""" % templates[1]
        c.execute(stmt)
