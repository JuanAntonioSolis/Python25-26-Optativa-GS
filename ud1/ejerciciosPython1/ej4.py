palabra = input("Escribe una palabra:")
vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
    if letra in vocales:
        contador+= 1

print(palabra, "tiene", contador, "vocales.")