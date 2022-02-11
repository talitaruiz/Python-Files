lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Deseja continuar[S/N]?'))
    if continuar in 'Sn':
        break
print(f'A lista de números digitados foi {lista}.')
print(f'Os números pares digitados foram {par}. ')
print(f'Os números ímpares digitados foram {impar}.')

