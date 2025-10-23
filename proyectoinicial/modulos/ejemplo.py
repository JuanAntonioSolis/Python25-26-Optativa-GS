##Para importar todas las funciones del módulo
##import libreria

#Para importar sólo una función de un módulo
#Ya no hace falta poner el nombre del modulo delante al llamarlo
#as reverse, para poner alias a la funcion
from libreria import reverse_full_name as reverse 

#print( libreria.generate_full_name('Juan','Solis'))
#print(libreria.generate_greeting('Juan Antonio'))
print(reverse('Juan','Solis'))