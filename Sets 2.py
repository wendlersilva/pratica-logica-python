setExemploNumeros = set()
setExemploNumeros.add(1)
setExemploNumeros.add(2)
setExemploNumeros.add(3)
setExemploNumeros.add(4)
setExemploNumeros.add(5)
setExemploNumeros.add("Wendler")

print(setExemploNumeros)
print("\n")


setLetras = {"A", "B", "C"}
print(setLetras)

print("\n")

set1 = {"Allan", "Berenice", "Roger"}
set2 = {39, 21, 45}

uniaoSets = set1.union(set2)
print(uniaoSets)


listaSet1 = {"Python", "C++", "Java"}
listaSet2 = {"VisualG", "Lógica", "Python"}

print("\n")
imprimindoOsDoisParaConferir = listaSet1.union(listaSet2)
print(imprimindoOsDoisParaConferir)

valorQueEstaEmAmbosOsSets = listaSet1.intersection(listaSet2)
print(valorQueEstaEmAmbosOsSets)


listaSet1.symmetric_difference_update(listaSet2)
print(listaSet1)


listaS1 = {"Python", "C++", "Java"}
listaS2 = {"VisualG", "Lógica", "Python"}

print("\n\n")
naoEstaoEmAmbos = listaS1.symmetric_difference(listaS2)
print(naoEstaoEmAmbos)


print("\n\n")


setNumero = {1, 2, 3, 4, 5, 6, 6, 7, 8}
print(setNumero)
print(len(setNumero))

setExemplo1 = {"A", "B", "C"}
setExemplo2 = {1, 2, 3}
setExemplo3 = {True, False, True}
setExemplo4 = {"Maça", 12, True}
setExemplo2.update(setExemplo1)

print("\n\n")
print(setExemplo1)
print(setExemplo2)
print(setExemplo3)
print(setExemplo4)


listaObjetos = {"Casa", "Moto", "Bicicleta", "Lancha"}

for item in listaObjetos:
    print(item)

listaObjetos.add("Carro")
print(listaObjetos)

listaObjetos.remove("Moto")
print(listaObjetos)

listaObjetos.pop()
print(listaObjetos)

print("Bicicleta" in listaObjetos)
