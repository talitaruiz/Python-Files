salario = float(input('Digite seu salário atual:'))
if salario >= 1250:
    novo = salario * 1.10
else:
    novo = salario * 1.15
print('Seu novo salário será de {:.2f}'.format(novo))
print('-----FIM-----')
