import random
aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)
print('O aluno sorteado será: {}'.format(sorteado))

