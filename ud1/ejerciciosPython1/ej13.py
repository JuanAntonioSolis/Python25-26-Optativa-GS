matriz = list()
for i in range(0,2):
    #Crear los elementos antes de acceder a ellos
    matriz.append(list(range(3)))
    for j in range(0,3):
        num = int(input("Escribe un número"))
        matriz[i][j] = num
        
print(matriz)
suma = 0
for fila in matriz:
    suma += sum(fila)

print(suma)
