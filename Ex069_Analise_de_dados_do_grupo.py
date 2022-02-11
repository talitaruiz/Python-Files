print('-'* 20, 'ANÁLISE DE DADOS DO GRUPO', '-' * 20)
mu = h = m = hm = 0
while True:
    idade = int(input('Digite sua idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo:')).strip().upper()[0]
    if sexo == 'M':
        h = h + 1
        if idade > 18:
            hm = hm + 1
    elif sexo == 'F':
        if idade < 20:
            mu = mu + 1
        elif idade > 18:
            m = m + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('Foram cadastrados {} pessoas maiores de 18 anos, {} homens foram cadastrados e {} mulheres foram cadastradas \n com menos de 20 anos.'.format(hm+m, h, mu))



