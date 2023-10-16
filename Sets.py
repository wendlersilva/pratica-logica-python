setExemploNumeros = set()
setExemploNumeros.add(1)
setExemploNumeros.add(2)
setExemploNumeros.add(3)
setExemploNumeros.add(4)
setExemploNumeros.add(5)
setExemploNumeros.add("Wendler")

print(setExemploNumeros)


setLetras = {"A", "B", "C"}
print(setLetras)

set1 = {"Wendler", "Silva"}
set2 = {23, 12, 4}
uniaoSets = set1.union(set2)
print(uniaoSets)

listaSet1 = {"Python", "Java", "C#"}
listaSet2 = {"Visual G", "Lógica", "Python"}
paraConferir = listaSet1.union((listaSet2))
print(paraConferir)

valorAmbos = listaSet1.intersection(listaSet2)
print(valorAmbos)


