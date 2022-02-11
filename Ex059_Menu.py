import time

valor1 = int(input('Digite um valor :'))
valor2 = int(input('Digite outro valor: '))
choice = 0
resultado = 0
while choice != 5:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa''')
    choice = int(input('Digite sua escolha de acordo com as opções abaixo: '))
    if choice == 1:
        resultado = valor1 + valor2
        time.sleep(1)
        print('Os números escolhidos foram {} e {} e o resultado da operação escolhida foi {}'.format(valor1, valor2, resultado))
    elif choice == 2:
        resultado = valor1 * valor2
        time.sleep(1)
        print('Os números escolhidos foram {} e {} e o resultado da operação escolhida foi {}'.format(valor1, valor2, resultado))
    elif choice == 3:
        if valor1 > valor2:
            resultado = valor1
            time.sleep(2)
            print('Os números escolhidos foram {} e {} e o maior valor digitado é {}'.format(valor1, valor2, resultado))
        else:
            resultado = valor2
            time.sleep(2)
            print('Os números escolhidos foram {} e {} e o maior valor digitado é {}'.format(valor1, valor2, resultado))
    elif choice == 4:
        time.sleep(2)
        valor1 = int(input('Digite valor novo: '))
        valor2 = int(input('Digite mais outro valor novo: '))
    elif choice == 5:
        print('Finalizando.....')
    else:
        time.sleep(2)
        print('Opção inválida, tente novamente!')
time.sleep(1)
print('Obrigada pela participação! Até a próxima!')



