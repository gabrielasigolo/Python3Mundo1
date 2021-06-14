salario = float(input('Digite seu salário: '))

aumento = 0.1
if salario > 1250:
    novo_salario = salario + (salario * aumento)
    print('O seu salário com um aumento de 10% será: R$ {:.2f}'.format(novo_salario))
else:
    aumento += 0.05 # 0.1 + 0.05 = 0.15 --> 15%
    novo_salario = salario + (salario * aumento)
    print('O seu salário com um aumento de 15% será: {:.2f}'.format(novo_salario))

