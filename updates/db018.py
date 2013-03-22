# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


__doc__ = '''\
Изменение шаблона печати "Графическое отображение показателей больного"
'''

where = 'code="22" and name like "%Результат исследован%" and context="action21"'


def upgrade(conn):
    # Добавляем новые права
    sql = [
    '''\
UPDATE rbPrintTemplate
SET rbPrintTemplate.default = "<html>
<head>
<meta name=\\"qrichtext\\" content=\\"1\\" />
</head>
<body style=\\"font-family:'Times New Roman'\\">

{setPageSize('A4')}
{setOrientation('P')}
{setLeftMargin(5)} {setTopMargin(5)} {setBottomMargin(5)} {setRightMargin(5)}

{: plot_t = Plot(300,300,Plot.t(client.id)) }
{: plot_heart = Plot(300,300,Plot.heartRate(client.id)) }
{: plot_breath = Plot(300,300,Plot.respiratoryRate(client.id)) }
{: plot_pressure1 = Plot(300,300,Plot.systolicBloodPressure(client.id)) }
{: plot_pressure2 = Plot(300,300,Plot.diastolicBloodPressure(client.id)) }
{: plot_pressure = Plot(300,300,Plot.bloodPressure(client.id)) }


{if: plot_t.hasData }
<h7>Температура</h7>
<p>
<img align='center' src='canvas://plot_t' />
</p>
{end:}
{if: plot_heart.hasData }
<h7>ЧСС</h7>
<p>
<img align='center' src='canvas://plot_heart' />
</p>
{end:}
{if: plot_breath.hasData }
<h7>ЧД</h7>
<p>
<img align='center' src='canvas://plot_breath' />
</p>
{end:}
{if: plot_pressure1.hasData }
<h7>Систолическое АД</h7>
<p>
<img align='center' src='canvas://plot_pressure1' />
</p>
{end:}
{if: plot_pressure2.hasData }
<h7>Диастолическое АД</h7>
<p>
<img align='center' src='canvas://plot_pressure2' />
</p>
{end:}
{if: plot_pressure.hasData }
<h7>АД</h7>
<p>
<img align='center' src='canvas://plot_pressure' />
</p>
{end:}
</body>
</html>"
WHERE %s
    ''' % where
    ]
    # Исполнение 
    c = conn.cursor()
    for s in sql:
        c.execute(s)


def downgrade(conn):
    pass
