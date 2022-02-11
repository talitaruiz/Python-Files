frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
print(junto)
inverso = junto[::-1]
print(inverso)
print('Você executou a frase {} e o inverso dela é {}'.format(frase, inverso))
if junto == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
print('-'*20,'FIM','-'*20)


