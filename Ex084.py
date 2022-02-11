galera = []
dados = []
continuar = ' '
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome:')))
    dados.append(int(input('Digite o peso:')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar[S/N]?'))
    if continuar in 'Nn':
        break
print(f' A lista de pessoas digitadas foi: {galera}.')
print(f'E a quantidade de pessoas digitadas foi {len(galera)}.')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}.', end = '')
print(f'O maior peso foi de {maior}.', end='')
print()
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}.', end = '')
print(f'O menor peso foi de {menor}.', end='')
print()

