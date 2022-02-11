import time
import random
import emoji

computador = random.randint(1, 10)

tentativas = 0
jogador = ''
print(emoji.emojize('\033[34mSou seu computador \033[m :sunglasses: ', use_aliases=True))
print('Acabei de pensar em um número entre 1 e 10. Tente adivinhar...')
print('===' *21)
while jogador != computador:
    tentativas += 1
    jogador = int(input('Qual seu palpite? '))
    print('Processando.....')
    time.sleep(2)
    if jogador != computador:
        print('\033[31mErrado! Tente outra vez!\033[m')
        if computador > jogador:
            print('O computador escolheu um número MAIOR')
        elif computador < jogador:
            print('O computador escolheu um número MENOR')
    print('==='*21)
print('Parabéns! Você Acertou com {} tentativas.'.format(tentativas))

