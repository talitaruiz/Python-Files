print('x-'*20, 'LOJAS DA TALITA', 20*'x_')
preço = float(input('Digite o valor total das suas compras:'))
print('''Formas de Pagamento Disponíveis')
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal 
[4] 3x ou mais no cartão: 20% de juros''')
opção = int(input('Qual é a opção desejada de pagamento?'))
if opção == 1:
    valor = preço * 0.9
    print('Na opção de pagamento à vista, você pagará R$ {:.2f}'.format(valor))
elif opção == 2:
    valor = preço * 0.95
    print('Na opção de pagamento à vista no cartão, você pagará R$ {:.2f}'.format(valor))
elif opção == 3:
    valor = preço / 2
    print('Na opção 3, você pagará duas parcelas de R$ {} '.format(valor))
elif opção == 4:
    parcelas = int(input('Digite o número de parcelas desejado: '))
    valor = (preço * 1.20) / parcelas
    print('Na opção 4, você pagará {} vezes de R$ {:.2f}'.format(parcelas, valor))
print('------------------- FIM ---------------------')


