from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = (atual - nasc)
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade > 18:
    saldo = idade - 18
    print('O tempo de alistamento passou, aliste-se imediatamente! Já se passaram {} anos \n do tempo que deveria ter se alistado'. format(saldo))
    print('O ano que você deveria ter se alistado é {}'.format(atual - saldo))
elif idade == 18:
    print('Esse é o momento de se alistar, vá IMEDIATAMENTE a um quartel!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda não chegou a hora de se alistar, faltam {} anos ainda'.format(saldo))
    print('O ano em que você deverá se alistar será o ano de {}'.format(atual - saldo))
