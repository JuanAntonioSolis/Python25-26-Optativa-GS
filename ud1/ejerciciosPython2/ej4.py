from string_utils import *

texto = "dabale arroz a la zorra el abad"

contar_vocales(texto)
invertir_texto(texto)
if es_palindromo(texto):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    
capitalizar_palabras(texto)