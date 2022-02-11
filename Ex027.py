nome = str(input('Digite seu nome completo:')).strip()
div = nome.split()
print('Seu primeiro nome é {}'.format(div[1]))
print('Seu segundo nome é {}'.format(div[len(div)-1]))

