lista = list()

while len(lista) < 5:
    num = int(input("Escribe un número para la lista:"))
    lista.append(num)

print("Lista normal:", lista)
lista.reverse()
#lista[::-1] para no modificarla, sólo recorrer
print("Lista inversa: ", lista)
