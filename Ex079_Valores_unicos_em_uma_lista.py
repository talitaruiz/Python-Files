lista = []
c = 0
while True:
    n = int(input(f'Digite um valor inteiro:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso....')
    else:
        print('Valor já contém na lista, não é possível adicionar novamente.')
    pergunta = str(input('Deseja continuar?[S/N]')).upper()
    if pergunta in 'N':
        break
lista.sort()
print(f'A lista digitada foi {lista}.')

