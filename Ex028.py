import random
valor = int(input('Digite um valor de 0 a 5:'))
num = random.randint(0, 5)
if valor == num:
    print('Parabéns! Você acertou! O número escolhido pelo computador foi {} e o seu número foi {}'.format(num, valor ))
else:
    print('Você perdeu!O número escolhido pelo computador foi {} e o seu número foi {}'.format(num, valor ))
print('FIM')
print('-=-' * 20)



