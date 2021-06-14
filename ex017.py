from math import hypot
catetoOP = float(input('Digite o comprimento do cateto oposto do triângulo: '))
catetoADJ = float(input('Digiteo o comprimento do cateto adjacente do triângulo: '))

hipotenusa = hypot(catetoOP, catetoADJ)
print('A hipotenusa do triângulo será: {:.2f}'.format(hipotenusa))
