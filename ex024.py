frase = str(input("Digite uma frase qualquer: ")).strip().upper()

print("Sua frase tem {} letras A".format(frase.count("A")))
print("Ela aparece pela primeira vez na posição {}".format(frase.find("A")+1))
print("Ela aparece pela ultima vez na posição {}".format(frase.rfind("A")+1))


