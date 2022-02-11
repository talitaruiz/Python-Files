aluno = list()
continuar = ''
while True:
    nome = str(input('Digite o nome do aluno:'))
    nota1 = float(input('Digite a primeira nota:'))
    nota2 = float(input('Digite a segunda nota:'))
    media = (nota1 + nota2)/2
    aluno.append([nome, nota1, nota2, media])
    continuar = str(input('Deseja continuar? [S/N)]'))
    if continuar in 'Nn':
        break
print(aluno)
print(f'{"No.":<4}{"NOME":<10} {"MÉDIA":>8}')
print('-'* 30)
for i, c in enumerate(aluno):
    print(f'{i:<4}{c[0]:<10}{c[3]:>8.1f}')
while True:
    n = int(input('Deseja saber as notas de qual aluno[Digite o No. dele]?'))
    print(f'As notas do aluno {aluno[n][0]} foram {nota1} e {nota2}.')
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'Obrigado pela participação!')





