velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Velocidade ultrapassada, você foi multado!')
    multa = (velocidade - 80) * 7
    print('Valor da multa: R$ {:.2f}'.format(multa))
else:
    print('Você está na velocidade certa!')
