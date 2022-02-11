print('--------Programa das tabuadas ------')
valor = int(input('Digite um número:'))
print('A tabuada do valor digitado é:')
for c in range(1,11):
    tabuada = c * valor
    print('{:2} X {:2} = {} '.format(c,valor, tabuada))
print('FIM')
