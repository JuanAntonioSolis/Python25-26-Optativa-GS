'''
Crea dos diccionarios con claves y valores numéricos, y combina ambos en uno solo:

Si una clave se repite, suma los valores.
Si no, simplemente añade la clave y su valor.
'''

dicc1 = {"Edad": 23, "Altura":180, "Pie":29, "Ojos":2}
dicc2 = {"Ojos":1,"Brazos":2,"Altura":50,"Manos":1}
dicc_combinado = {}

for clave in dicc1:
    dicc_combinado[clave] = dicc1[clave]
    
for clave in dicc2:
    if clave in dicc1:
        dicc_combinado[clave] += dicc2[clave]
    else:
        dicc_combinado[clave] = dicc2[clave]
    
print(dicc_combinado)
