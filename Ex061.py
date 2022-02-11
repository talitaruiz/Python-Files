prim = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
cont = 1
while cont <= 10:
    print(prim, ' - ', end='')
    prim = prim + razao
    cont = cont + 1
print('FIM')