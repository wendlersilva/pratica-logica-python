listaLetras = ["A", "B", "D", "C", "E", "F",]
listaLetras.sort()
print(listaLetras)

listaLetras.sort(reverse=True)
print(listaLetras)

#----------------------

listaNumeros = [4, 9, 5, 20, 10, 11]
listaNumeros.sort()
print(listaNumeros)

listaNumeros.sort(reverse=True)
print(listaNumeros)

#-----------------------

listaMaiMin = ["Sofá","casa", "Anel", "zebra"]
listaMaiMin.sort()
print(listaMaiMin)

listaMaiMin.sort(key=str.lower)
print(listaMaiMin)
