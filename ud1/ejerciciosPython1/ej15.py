frase = input("Escribe una frase:")
frase = frase.lower()

palabras = frase.split()
print(palabras)

diccionario = {}

for i in palabras:
    if i in diccionario.keys():
        diccionario[i] += 1
    else:
        diccionario[i] = 1

print(diccionario)