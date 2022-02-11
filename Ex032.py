from datetime import date
ano = int(input('Que ano você quer analisar?'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0 ) or ano % 400 == 0:
    print('É ano bissexto')
else:
    print('Não é ano bissexto')
print('---FIM---')
