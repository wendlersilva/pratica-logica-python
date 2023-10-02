nome = "Wendler Silva"
print(nome)
print("Total de caracteres: " + str(len(nome)))

print(nome[0])
print(nome[0:7])
print(nome[8:13])
print(nome[0:13])
print(nome[0:])

#Upper deixa todas as letras em maiúscula
frase = "Curso de Lógica de PROGRAMAção python"
print(frase.upper())

#Lower deixa tudo em minúscula
print(frase.lower())

#Subistitui algo
notaProva = "Tirei nota cinco na prova"
print(notaProva.replace("cinco", "dez"))

cpf = "123.456.545-22"
cpfPartes = cpf.split(".")
print(cpfPartes)
print(cpfPartes[0])
