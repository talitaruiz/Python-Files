n = (int(input('Digite o primeiro valor:')),
int(input('Digite o primeiro valor:')),
int(input('Digite o primeiro valor:')),
int(input('Digite o primeiro valor:')))
print(f'A tupla formada com os valores digitados é {n}.')
print(f'O número 9 aparece {n.count(9)} vezes.')
if 3 in n:
    print(f'O primeiro valor 3 foi digitado na {n.index(3)+1}  posição. ')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
print(f'Os valores pares digitados foram:', end = ' ')
for c in n:
    if c % 2 == 0:
        print(c , end =' ')
