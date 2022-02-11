lista = []
p = ' '
while True:
    n = int(input('Digite um valor:'))
    lista.append(n)
    p = str(input('Deseja parar?[S/N]'))
    if p in 'Ss':
        break

if 5 in lista:
    print('A lista contém o número 5.')
else:
    print('A lista não contém o número 5.')
lista.sort(reverse=True)
print(f'A quantidade de valores digitados foi {len(lista)}. A lista digitada foi {lista}.')
