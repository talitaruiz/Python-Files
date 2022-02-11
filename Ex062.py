prim = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
termo = prim
cont = 1
extra = 10
total = 0
while extra != 0:
    total = total + extra
    while cont <= total:
        print(termo, ' - ', end='')
        termo = termo + razao
        cont = cont + 1
    extra = int(input('Quantos termos você deseja mostrar a mais?'))
print('O total de termos mostrados foram:{}'.format(termo))
print('FIM')