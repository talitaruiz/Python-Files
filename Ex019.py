import random
n1 = str((input('Digite o nome do Primeiro aluno:')))
n2 = str((input('Digite o nome do Segundo aluno:')))
n3 = str((input('Digite o nome do Terceiro aluno: ')))
n4 = str(input('Digite o nome do Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))