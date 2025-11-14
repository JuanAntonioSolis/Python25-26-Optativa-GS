'''
Crea un módulo string_utils.py con las siguientes funciones:

invertir_texto(texto): Invierte el orden de los caracteres
contar_vocales(texto): Cuenta cuántas vocales hay
es_palindromo(texto): Verifica si es un palíndromo
capitalizar_palabras(texto): Capitaliza la primera letra de cada palabra
Importa y usa estas funciones en otro archivo.
'''

def invertir_texto(text):
    print(text[::-1])
    
def contar_vocales(text):
    text = text.lower()
    vocales = ["a","e","i","o","u"]
    contar_vocales = 0
    for letra in text:
        if letra in vocales:
            contar_vocales+=1
            
    print("En este texto hay", contar_vocales, "vocales")
    
def es_palindromo(text):
    
    text = text.lower()
    text = text.replace(" ", "")
    
    reves = text[::-1]
    
    if text == reves:
        return True
    else:
        return False

def capitalizar_palabras(text):
    text = text.title()
    
    print(text)
    
    
    
    