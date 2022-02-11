lista = []
for c in range(0,5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[len(lista) - 1]:
        lista.append(n)
    else:
        pos = 0
        while pos <len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos = pos + 1
print(f' Os valores em ordem crescente digitados foi : {lista}')
