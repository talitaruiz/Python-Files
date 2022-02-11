import math
ca = float(input('Digite o valor do cateto oposto:'))
co = float(input('Digite o valor do cateto adjacente'))
h = math.sqrt(pow(ca,2)+pow(co,2))
print('O valor da hipotenusa é {:.2f} :'. format(h))
