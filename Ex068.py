from random import randint
from time import sleep
print('**** JOGO DO PAR OU ÍMPAR ****')
c = 0
b = 0
while True:
    n = int(input('Digite um valor inteiro:'))
    comp = randint(0, 10)
    total = n + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar[P/I]?')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {comp}. O total foi de {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÌMPAR')
    sleep(2)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            c = c + 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('Você ganhou!')
            b = b + 1
        else:
            print('Você perdeu!')
            break
totvi = c + b
print('O número total de vitórias foi de {} contra o computador.'.format(totvi))
