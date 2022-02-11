par = []
impar = []
for c in range(1,8):
    valor = (int(input(f'Digite o {c}º valor:')))
    if valor % 2 == 0:
            par.append(valor)
    else:
            impar.append(valor)
par.sort()
impar.sort()
print(f'A lista de números pares é: {par}.')
print(f'A lista de números ímpares é: {impar}.')

