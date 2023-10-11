listaMinMax = [5, 10, 20, 100, 50]
print(min(listaMinMax))
print(max(listaMinMax))

#-----------------------

listaNumeros1ate10 = [posicao for posicao in range(100)]
print(listaNumeros1ate10)

#-----------------------

listaDoisEmDois = list(range(0, 100, 2))
print(listaDoisEmDois)

#-----------------------

listaOriginal = ["Carro", "Moto", "Bicicleta", "Lancha"]
listaCopiada = listaOriginal.copy()
print(listaCopiada)

#-----------------------

lista1Letras = ["A", "B", "C"]
lista2Numeros = [1, 2, 3]

listaJoin = lista1Letras + lista2Numeros
print(listaJoin)

#-----------------------

l1 = ["a1", "b1", "c1"]
l2 = [11, 12, 13]

for item in l2:
    l1.append(item)
print(l1)


