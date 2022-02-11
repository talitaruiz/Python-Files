print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual valor que deseja sacar?'))
div50 = div20 = div10 = rdi50 = rdi20 = rdi10 = 0
while True:
    div50 = valor//50
    rdi50 = valor%50
    div20 = rdi50//20
    rdi20 = rdi50%20
    div10 = rdi20//10
    rdi10 = rdi20%10
    break
print(f'Total de {div50} cédulas de 50 reais, {div20} cédulas de 20 reais, \n'
       f' {div10} cédulas de 10 reais e {rdi10} cédulas de 1 real. ')

