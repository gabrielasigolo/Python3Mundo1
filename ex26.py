from random import randint
from time import sleep


print('\033[0;33;40m-=-\033[m' * 20)
print('    TENTE DESCOBRIR O NÚMERO QUE O PC ESTÁ PENSANDO')
print('\033[0;33;40m-=-\033[m' * 20)
numero = int(input('\033[0;31mDigite um número inteiro entre 0 e 5: '))
numero_aleatorio = randint(0, 5)
print('\033[1;32mPROCESSANDO...')
sleep(2)

if numero == numero_aleatorio:
    print('\033[4;33mVenceu!')
else:
    print('\033[4;33mPerdeu!')
print('\033[0;36;40mO número era {}\033[m'.format(numero_aleatorio))
