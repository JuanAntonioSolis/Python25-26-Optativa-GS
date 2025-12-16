'''
Escribe una función que valide si una contraseña cumple los siguientes criterios:

Al menos 8 caracteres
Al menos una letra mayúscula
Al menos una letra minúscula
Al menos un número
Al menos un carácter especial (@, #, $, %, etc.)
La función debe retornar True si cumple todos los criterios, False en caso contrario.
'''
import string

def validatePassword(passwd):
    caracteres = string.punctuation
    nums = string.digits
    minus = string.ascii_lowercase
    mayus = string.ascii_uppercase
    tieneCarac = False
    tieneNums = False
    tieneMinus = False
    tieneMayus = False
    
    if len(passwd) < 8:
        print("La contraseña debe tener más de 8 carácteres.")
        return False
    
    for char in passwd:
        if char in mayus:
            tieneMayus = True
        elif char in minus:
            tieneMinus = True
        elif char in caracteres:
            tieneCarac = True
        elif char in nums:
            tieneNums = True
            
    if tieneNums and tieneMinus and tieneCarac and tieneMayus:
        return True
    else:
        if not tieneCarac:
            print("La contraseña debe contener al menos un carácter especial")
        if not tieneNums:
            print("La contraseña debe contener al menos un número")
        if not tieneMayus:
            print("La contrasena debe contener al menos una mayúscula")
        if not tieneMinus:
            print("La contraseña debe contener al menos una mínscula")
        return False
    
password = "AA123A?12a"
validatePassword(password)