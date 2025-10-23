frase = input("Escribe una frase:")
frase = frase.lower()
letras = {}

for letra in frase:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1
        
print(letras)