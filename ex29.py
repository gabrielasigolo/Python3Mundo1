km = float(input('Digite a distância da viagem: '))
valor_a_pagar = km * 0.50 if km <= 200 else km * 0.45 #maneira simplificada
'''
if km <= 200: --> maneira normal
    valor_a_pagar = km * 0.50
else:
    valor_a_pagar = km * 0.45
'''
print('Total a pagar: R$ {:.2f}'.format(valor_a_pagar))

