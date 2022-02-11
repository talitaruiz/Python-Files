velho = 0
total = 0
mulhermenor = 0
for c in range(1,5):
    print('-'*10, 'Pessoa número', c, '-'*10)
    nome = str(input('Digite seu nome:')).strip()
    idade = int(input('Qual a sua idade?'))
    sexo = str(input('Qual o seu sexo (Feminino/Masculino)?')).upper().strip()
    if sexo == 'MASCULINO':
        if idade > velho:
            velho = idade
            nomevelho = nome
    else:
        if idade < 20:
            mulhermenor = mulhermenor + 1
    total = idade + total
print('A idade do homem mais velho é {} e seu nome é {}'.format(velho, nomevelho))
media = total/4
print('A média de todas as idades do grupo é {}'.format(media))
print('A quantidade de mulheres abaixo de 20 anos de idade é {}'.format(mulhermenor))
