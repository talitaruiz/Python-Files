n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
if n1 > n2:
    print('O primeiro valor digitado {} é maior que o segundo valor digitado {}'. format(n1, n2))
elif n2 > n1:
    print('O segundo valor digitado {} é maior que o primeiro valor digitado {}'.format(n2,n1))
else:
    print('Os valores são iguais!')
