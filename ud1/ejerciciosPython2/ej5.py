'''
Usa el módulo datetime para crear una función que:

Reciba una fecha de cumpleaños (día, mes, año)
Calcule cuántos días faltan para el próximo cumpleaños
Si ya pasó este año, calcule para el próximo año

'''

from datetime import *

def calcularCumple(fecha_cumple):
    hoy = date.today()
    diferencia = 0
    prox_cumple = date(hoy.year+1,fecha_cumple.month,fecha_cumple.day)
    
    if fecha_cumple <= hoy:
        diferencia = prox_cumple - hoy
        print("Quedan", diferencia.days, "dias para tu cumple")
    else:
        diferencia = fecha_cumple - hoy
        print("Quedan", diferencia.days, "dias para tu cumple")

cumple = date(2025,1,17)

calcularCumple(cumple)
                                                                                                                                                                                                                             