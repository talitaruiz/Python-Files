print('--=--' * 20)
print('Validação de triângulos')
print('--=--'*20)
a = int(input('Digite o primeiro segmento:'))
b = int(input('Digite o segundo segmento:'))
c = int(input('Digite o terceiro segmento:'))
if b + c > a and a + c > b and a + b > c:
    print('Os valores digitados formam um triângulo!')
else:
    print('Os valores digitados não formam um triângulo!')
print('-------FIM---------')