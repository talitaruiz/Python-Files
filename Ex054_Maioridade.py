from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    ano = int(input('Digite seu ano de nascimento:'))
    idade = atual - ano
    print('Sua idade é {}'.format(idade))
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor =+ 1
print('O número de pessoas maior de idade foi de {} e o número de pessoas menores \n de idade foram {}'.format(totmaior, totmenor))
print('Obrigada pela presença!')
