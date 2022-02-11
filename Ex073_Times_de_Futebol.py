times = ('Santos', 'Palmeiras', 'Botafogo', 'Fluminense','São Paulo',
         'Corinthians','Grêmio',
         'Internacional', 'Cruzeiro', 'Flamengo','Sport', 'Bahia', 'Brasil de Pelotas',
         'Cuiabá',
         'São Caetano', 'Chapecoense', 'Ceará','Paraná','Coritiba','Ponte Preta')
print('-=' * 65)
print(f'Lista de times: {times}')
print('-=' * 65)
print(f'Os 4 primeiro colocados do Brasileirão são: {times[0:4]}')
print('-=' * 65)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 65)
print(f'Times em ordem alfabética:{sorted(times)}')
print('-=' * 65)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição.')
print('-=' * 65)