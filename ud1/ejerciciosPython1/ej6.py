lista = list()

while len(lista) < 5:
    num = int(input("Escribe un número para la lista:"))
    lista.append(num)

print("El número más pequeño de la lista es: ", min(lista))
print("El número más grande de la lista es: ", max(lista))
