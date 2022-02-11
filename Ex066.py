s = n = c = 0
while True: #looping infinito
    n = int(input('Digite um valor inteiro [999 para parar]:'))
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'A quantidade de valores digitados foram de {c} e a somatória dos valores foram {s}.')

