nome = str(input('Digite seu nome:')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))

