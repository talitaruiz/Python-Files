frase = str(input('Digite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na sua frase'.format(frase.count('A')))
print('A primeira ocorrência da letra A ocorre na posição {}'. format(frase.find('A')+1))
print('A última ocorrência da letra A ocorre na posição {}:' . format(frase.rfind('A')+1))
