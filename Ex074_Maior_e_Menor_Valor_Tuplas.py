import random
c = 1
n= (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),
random.randint(1,10))
d = sorted(n)
print(f'A tupla sorteada foi {n}.')
print('O maior valor da tupla é {}, e o menor valor da tupla é {} .'.format(d[4],d[0]))