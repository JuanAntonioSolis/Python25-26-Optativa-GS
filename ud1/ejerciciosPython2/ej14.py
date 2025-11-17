'''
Crea un programa que trabaje con coordenadas geográficas 
(latitud, longitud) utilizando desempaquetado de tuplas.

Función calcular_distancia_euclidiana(punto1, punto2) 
Recibe dos tuplas con coordenadas (latitud, longitud) 
Usa desempaquetado para extraer lat/lon de cada punto Calcula 
la distancia euclidiana simplificada: √((lat2-lat1)² + (lon2-lon1)²) Retorna la distancia

Función procesar_ruta(*puntos) Recibe una cantidad variable de 
puntos (mínimo 2) Separa el punto de origen, el destino, y 
todos los puntos intermedios Calcula la distancia total del 
recorrido (suma de distancias entre puntos consecutivos) 
Retorna un diccionario con: origen, destino, puntos_intermedios, y distancia_total
'''

from math import *

madrid = (40.4168, -3.7038)
barcelona = (41.3851, 2.1734)
valencia = (39.4699, -0.3763)
sevilla = (37.3891, -5.9845)

def calcular_distancia_euclidiana(punto1, punto2):
    latM, longM = punto1
    latB, longB = punto2
    
    distancia = sqrt( (pow(2,(latB-latM))) + pow(2,(longB-longM)))
    print("Distancia", punto1, "-",punto2, ":" , distancia)
        
    
calcular_distancia_euclidiana(madrid,barcelona)
    

    