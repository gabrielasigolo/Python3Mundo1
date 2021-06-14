from math import sin, cos, tan, radians
ângulo = float(input('Digite um ângulo: '))
sin = sin(radians(ângulo))
cos = cos(radians(ângulo))
tan = tan(radians(ângulo))

print('O seno desse ângulo será {:.2f}, o cosseno {:.2f} e o tangente será {:.2f}'.format(sin, cos, tan))
