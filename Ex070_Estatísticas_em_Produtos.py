valortotal = c = vmenor = cont = 0
prodmenor = ' '
while True:
    produto = str(input('Produto que deseja comprar:')).strip()
    preço = float(input('Preço R$:'))
    cont = cont + 1
    if preço > 1000:
        c = c + 1
    if cont == 1:
        vmenor = preço
        prodmenor = produto
    else:
        if preço < vmenor:
            vmenor = preço
            prodmenor = produto
    valortotal = preço + valortotal
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]?')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O valor total da compra foi de {valortotal:.2f}.')
print('Foram comprados {} produtos de valor acima de R$ 1000,00.'.format(c))
print(f'O produto de menor valor comprado foi {prodmenor} no valor de {vmenor:.2f}. ')
print('{:-^40}'.format('VOLTE SEMPRE'))





