valor = int(input('Digite um valor:'))
tot = 0
for c in range(1, valor + 1):
    if valor % c == 0:
        print('\033[34m', end = ' ')
        tot = tot + 1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format(c), end = ' ')
print('O número {} foi divisível {} vezes'.format(valor, tot))
if tot == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')


