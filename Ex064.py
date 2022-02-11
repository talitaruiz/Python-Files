n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]:'))
    s = n + s
    cont = cont + 1
    if n == 999:
        s = s - 999
        cont = cont - 1
print('A soma de todos os valores digitados foi {} . Você digitou {} valores.'.format(s, cont))

