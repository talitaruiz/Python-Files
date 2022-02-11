print('='*20)
print('        10 TERMOS DE UMA PA        ')
print('='*20)
prim = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
decimo = prim + (10 - 1) * razao
for c in range(prim, decimo+razao ,razao):
    print('{}'.format(c), end = ' - ')
print('ACABOU')
