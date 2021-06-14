# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('How many kilometers have you traveled with the car? '))
days = int(input('How many days have you been with the car? '))

total = (days * 60) + (km * 0.15)


print('Total to pay: R$ {:.2f}'.format(total))


