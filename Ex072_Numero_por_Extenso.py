cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print('O número digitado foi {}.'. format(cont[num]))
    print('Tente novamente.', end = ' ')
    continuar = str(input('Deseja continuar[S/N]?')).upper().strip()[0]
    while continuar not in 'NS':
        continuar = str(input('Que continuar?[S/N]<insira uma resposta válida>')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Obrigado pela participação.')