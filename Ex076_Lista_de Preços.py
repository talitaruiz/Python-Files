print('='*40)
print(f'{"Listagem de Preços":^40}')
print('='*40)
listagem = ('Borracha', 0.70,
            'Apagador', 3.50,
            'Caderno', 12.60,
            'Lapiseira', 12.90,
            'Estojo', 4.70,
            'Lápis', 3.50,
            'Giz de Cera', 7.10,
            'Guache', 5.30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
print('='*40)