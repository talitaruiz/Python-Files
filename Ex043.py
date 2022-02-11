peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f}, logo você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu imc é {:.2f}. Parabéns! Seu peso é ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}, logo você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f}, logo você está com obesidade.')
else:
    print('Seu IMC é de {:.2f}, logo você está com obesidade mórbida.'.format(imc))
print(20*'X_','FIM',20*'-X')