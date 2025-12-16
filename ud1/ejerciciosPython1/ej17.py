'''
Solicita dos listas de números de igual
longitud y calcula el producto escalar 
(sumando el producto de los elementos en la misma posición).
'''

lista1 = (10,8,6,4,2)
lista2 = (9,7,5,3,1)
producto_escalar = 0

for i in range (len(lista1)):
    producto_escalar += lista1[i] * lista2[i]
    

print("El producto escalar de las dos listas es:", producto_escalar)    








