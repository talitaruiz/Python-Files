n = int(input('Digite um valor para cálculo do fatorial:'))
c = n
f = 1
for c in range(1, n+1):
    f = c * f
    c = c - 1
print('O fatorial para o valor {} é {}'.format(n, f))
