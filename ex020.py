nome = str(input("Digite seu nome completo: ")).strip()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(" ", "")))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
