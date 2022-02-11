n1 = total = count = maior = menor = 0
continuar = 'S'
while continuar != 'N':
    n1 = int(input('Digite um valor inteiro: '))
    continuar = str(input('Deseja continuar[S/N]?')).upper().strip()[0]
    count = count + 1
    total = total + n1
    if count == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
media = total/count
print('A quantidade de valores digitados foi de {} e a média entre eles é {}'.format(count, media))
print('O maior e o menor valor digitados são respectivamente {} e {}.'. format(maior, menor))
