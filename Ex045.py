from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''JOGO PAPEL, PEDRA E TESOURA
-----------------OPÇÕES------------------
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada?''')
opcao = int(input('Digite sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[opcao]))
if opcao == computador:
    print('Houve EMPATE!')
elif computador == 0 and opcao == 2 or computador == 1 and opcao == 0 or computador == 2 and opcao == 1:
    print('O computador VENCEU!')
elif opcao == 0 and computador == 2 or opcao == 1 and computador == 0 or opcao == 2 and computador == 1:
    print('Você VENCEU!')
