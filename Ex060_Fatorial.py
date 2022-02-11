n = int(input('Digite um número para cálculo do fatorial:'))
f = 1
c = n
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end= '')
    f = f * c
    c = c - 1
print(f)

