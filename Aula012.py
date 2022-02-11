nome = str(input('Digite seu nome:'))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Fábio' or nome == 'Pedro' or nome == 'Patrícia' or nome == 'Juliana' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Marco Talita Marcelo Priscila Ricardo Otávio Carolina':
    print('Belo nome você tem!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia!')