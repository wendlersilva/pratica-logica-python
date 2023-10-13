listaNome = ["Wendler", "Silva", "Juliana"]
for posicao in listaNome:
    print(posicao)

print("\n")

[print(item) for item in listaNome]

print("\n")

contador = 0

while contador < len(listaNome):
    print(listaNome[contador])
    contador = contador + 1

#-----------------------

listaNomeC = []

for item in listaNome:
    if "w" in item:
        listaNomeC.append(item)

print(listaNomeC)
