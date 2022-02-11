vel = int(input('Informe a velocidade do carro:'))
if vel > 80:
    print('Você foi multado!')
    print('Você deve pagar uma multa de R$ {:.2f} reais'.format((vel-80)*7.00))
else:
    print('Você está andando na velocidade permitida!')
print('---FIM----')


