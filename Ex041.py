from datetime import date
atual = date.today().year
atleta = str(input('Digite o nome do atleta:')).strip()
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print('A categoria do atleta {} é MIRIM, pois tem {} anos'. format(atleta, idade))
elif 9 < idade <= 14:
    print('A categoria do atleta {} é INFANTIL, pois tem {} anos'.format(atleta, idade))
elif 14 < idade <= 19:
    print('A categoria do atleta {} é JÚNIOR, pois tem {} anos'.format(atleta, idade))
elif 19 < idade <=25:
    print('A categoria do atleta {} é SÊNIOR, pois tem {} anos'.format(atleta, idade))
else:
    print('A categoria do atleta {} é MASTER pois tem {} anos'.format(atleta, idade))
print('X-'*20,'FIM','X-'*20)
