'''
Crea una función division_segura(a, b) que divida dos números y 
maneje las siguientes excepciones:

- ZeroDivisionError: Si se intenta dividir por cero
- ValueError: Si los valores no son numéricos
- TypeError: Si los tipos de datos son incorrectos
La función debe retornar el resultado o un mensaje de error apropiado.
'''

def division_segura(a,b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except ValueError:
        return "Los valores deben ser numéricos"
    except TypeError:
        return "Tipo de dato incorrecto"
    except Exception as e:
        return "Error inesperado:", {e}

print(division_segura(10,2))
        
    
