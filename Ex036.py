salario = float(input('Digite seu salário:'))
casa = float(input('Digite o valor da casa:'))
tempo = int(input('Em quantos anos deseja pagar o imóvel?'))
prazo = tempo * 12
prestacao = casa / prazo
if prestacao > salario * 0.3:
    print('O empréstimo foi negado.')
else:
    print('A prestação que vocÊ vai pagar será de {:.2f}'.format(prestacao))
print('Obrigada pela atenção!')
