n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
if m >= 6.0:
    print('Sua média {} está dentro do valor aceitável!'. format(m))
else:
    print('Sinal de perigo! Sua média está vermelha, abaixo de 6 que é o valor aceitável para passar de ano!')
    print('---Fim----')
