num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digte o terceiro número: '))

maiorNumero = num1
if num2 > maiorNumero:
    maiorNumero = num2
if num3 > maiorNumero:
    maiorNumero = num3

menorNumero = num1
if num2 < menorNumero:
    menorNumero = num2
if num3 < menorNumero:
    menorNumero = num3
print('Maior número: {}'.format(maiorNumero))
print('Menor número: {}'.format(menorNumero))
