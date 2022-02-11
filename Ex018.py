import math
ang = float(input('Digite o valor do ângulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno desse ângulo é: {:.2f}, o cosseno desse ângulo é:{:.2f} e a tangente desse ângulo é:{:.2f}'. format(sen, cos, tan))


