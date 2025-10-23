'''
Crea un programa que simule un pequeño 
inventario de productos mediante un diccionario:

Cada clave es el nombre de un producto, y el valor, la cantidad disponible.
Permite al usuario añadir productos, modificar cantidades y mostrar el inventario final.
'''

inventario = {}

def añadir(inv):
    producto = input("Escribe qué producto quieres añadir:")
    cantidad = input("Escribe qué cantidad tenemos del producto:")
    inv[producto] = cantidad

def modif_cant(inv):
    prod = input("De qué producto quieres modificar la cantidad?:")
    cant = input("Qué cantidad deseas establecer?:")
    if prod in inv:
        inv[prod] = cant

        

añadir(inventario)
añadir(inventario)


modif_cant(inventario)
print(inventario)

