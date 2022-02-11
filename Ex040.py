n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Sua média é {}!'.format(media))
if media >= 6:
    print('Parabéns, você está\033[30;42m APROVADO!\033[m')
elif 5 <= media <= 6:
    print('Você está de \033[30;43m RECUPERAÇÃO!\033[m')
elif media < 5:
    print('Você está \033[30;41m REPROVADO!\033[m')
print('-'*20,'FIM','-'*20)
