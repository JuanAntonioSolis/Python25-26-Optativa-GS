#Creacion 
lista = list()
lista2 = []
lista3 = [1,2,3,4,5]
lista4 = ['Python','JavaScript','Java','C++']

print(len(lista3))
print(lista4)
print(lista4[3])
print(lista3[-1])

#Desempaquetado de listas !!
len1, len2, len3, len4 = lista4
print(len1,len2,len3,len4)

#Modificar listas
lista4[1] = 'PhP'
print(lista4)

#Añadir elementos por el final
lista4.append('HTML5')
lista4.append(69)
print(lista4)

#Insertar elementos en una posicion concreta -> resto de elementos se desplazan a la derecha
lista4.insert(1,2)
print(lista4)

#Eliminar elementos por valor -> Elimina el primero que encuentra
lista4.remove(2)
lista4.remove(69)
print(lista4)

#Eliminar por posicion
eliminado = lista4.pop()
print(lista4)
print("Se eliminó", eliminado)
lista4.pop(0)
print(lista4)

#Copiar listas
lista3_copia = lista3.copy()
print(lista3_copia)
#NO ES COPIA:
lista5 = lista3
lista5.remove(2)
print(lista5)

#Unir listas
lista6 = lista3 + lista5
print(lista6)

#Nº de veces que aparece un elemento en una lista
print(lista6.count(3))
