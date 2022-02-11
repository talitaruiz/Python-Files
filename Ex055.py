maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o seu peso atual:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi {} e o menor peso digitado foi {}'.format(maior, menor))

