prim = int(input('Digite o primeiro valor:'))
seg = int(input('Digite o segundo valor diferente do primeiro valor:'))
ter = int(input('Digite o terceiro valor diferente dos anteriores:'))
if prim > seg and prim > ter:
    print('O primeiro valor digitado {} é o maior'.format(prim))
if seg > prim and seg > prim:
    print('O segundo valor digitado {} é o maior'.format(seg))
if ter > prim and ter > seg:
    print('O terceiro valor digitado {} é o maior'.format(ter))
if prim < seg and prim < ter:
    print('O primeiro valor digitado é o menor {}'.format(prim))
if seg < prim and seg < ter:
    print('O segundo valor digitado é o menor {}'.format(seg))
if ter < prim and ter < seg:
    print('O terceiro valor digitado é o menor {}'.format(ter))
print('----FIM-----')