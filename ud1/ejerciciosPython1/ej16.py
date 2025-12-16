'''
Pide al usuario ingresar varios números, guárdalos en una lista y muestra:

La lista original.
La lista ordenada ascendentemente.
La lista ordenada descendentemente.
'''
numeros = list()

for i in range(5):
    num = int(input("Escribe un número:"))
    numeros.append(num)

print("Lista original", numeros)

numeros.sort()
print("Lista ordenada ascendentemente:", numeros)

numeros.sort(reverse=True)
print("Lista ordenada descendentemente:", numeros)
