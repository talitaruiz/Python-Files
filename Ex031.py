dist = int(input('Qual será a distância da sua viagem?'))
if dist <= 200:
    print('O custo da sua viagem será R$ {:.2f}'.format(dist * 0.50))
else:
    print('O custo da sua viagem será R$ {:.2f}'.format(dist * 0.45))
print('------FIM-----')


