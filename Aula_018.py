teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Carlos'
teste[1] = 32
galera.append(teste)
print(galera)