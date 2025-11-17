'''
Crea una función que:

Reciba una lista de strings
Intente convertir cada elemento a entero
Ignore los valores que no se puedan convertir
Retorne una lista con los números convertidos y otra con los errores encontrados
'''

datos = ["10", "20", "abc", "30", "xyz", "40"]

def convertir(lista):
    lista2 = []
    listaErrores = []
    
    for dato in lista:
        try:
            num = int(dato)
            lista2.append(num)
        except ValueError:
            listaErrores.append(f"{dato} no se pudo convertir")
        
    
    lista2.append(listaErrores)
    print(lista2)
    
convertir(datos)
    