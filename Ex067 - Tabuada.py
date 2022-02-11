print('-'*20,'PROGRAMA DE TABUADA', '-'*20)
n = int(input('Digite um número:'))
while n > 0:
    for c in range(1,11):
        print('{} X {} = {}'.format(n,c,c*n))
        if n < 0:
            break
    print('-'*800)
    n = int(input('Se deseja continuar digite outro número para tabuada.'))
print('Obrigado pela participação! ')




