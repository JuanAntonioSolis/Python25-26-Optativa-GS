#El primer carácter el mayúsculas
challenge = 'tres dias de phyton'
print(challenge.capitalize())

#Número de ocurrencias de un caracter en una cadena
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

#Si termina en un substring específico
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# Devuelve el índice de una primera ocurrencia de un substring
#rfind para última ocurrencia
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error

