'''
Crea una función que reciba un texto y retorne un diccionario con la frecuencia de cada palabra 
(ignorando mayúsculas/minúsculas y signos de puntuación).
'''

from statistics import *

def contar_palabras(text):
    text = texto.lower()
    text = text.replace(".","")
    text = text.split()
    
    conteos = {}
    
    for palabra in text:
        conteos[palabra] = conteos.get(palabra, 0) +1 
    
    print(conteos)
    
    
texto = "Python es genial. Python es poderoso y Python es versátil."
contar_palabras(texto)