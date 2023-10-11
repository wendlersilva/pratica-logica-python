lista1 = ["A", "B", "C"]
lista2 = ["D", "E", "F"]

lista1.extend(lista2)
print(lista1)

lista1.remove("E")
print(lista1)

lista1.pop(2)
print(lista1)

lista1.pop()
print(lista1)

del lista1[0]
print(lista1)

lista1.clear()
print(lista1)

lista1.append("Maça")
print(lista1)

lista1.insert(1, "Banana")
print(lista1)

lista1.insert(1, "Uva")
print(lista1)

lista1.insert(1, "Damasco")
print(lista1)

if "Uva" in lista1:
    print("Sim a Uva existe na lista")
else:
    print("Não encontramos a fruta")

if "Damasco" in lista1:
    print("Sim o Damasco existe na lista")
else:
    print("Não encontramos Damasco na lista")

if "Laranja" in lista1:
    print("Sim a Laranja existe na lista")
else:
    print("Não encontramos Laranja na lista")

lista1[2] = "Melancia"
print(lista1)

lista1[1:2] = ["A", "B"]
print(lista1)
