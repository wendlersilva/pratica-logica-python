listaNomes = ["Bia", "Raquel", "Allan", "Mafalda"]

#for = para
for posicao in listaNomes:
    if posicao == "Allan":
        continue
    print(posicao)

print("\n")

#Contando de 0 até 10
for i in range(10):
    print(i)

print("\n")

#range (start, stop e step)

for posicao in range(1, 11, 1):
    print(posicao)

print("\n")

#Contar do 20 até 10

for i in range(20, 9, -1):
    print(i)
