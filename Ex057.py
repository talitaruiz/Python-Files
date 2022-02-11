sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Digite novamente seu sexo [M/F]: ')).strip().upper()
print('Sexo registrado com sucesso!')
print('FIM')
