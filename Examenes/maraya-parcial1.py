"""Ejercicio1................................................................"""
def formarLista(num):
    if isinstance(num,int) and (num>0):
        return crearLista(num)
    else:
        return"Error"

def crearLista(num):
    if num == 0:
        return []
    elif (num%10) % 2 == 0:
        return [num%10] + crearLista(num//10)
    else:
        return crearLista(num//10)

"""Ejercicio2................................................................"""
def palindromo (num):
    if isinstance (num,int) and (num>0):
        return verificar(num)
    else:
        return "Error"

def verificar(num):
    if num == numInvert(num):
        return True
    else:
        return False

def numInvert(num,contador (num)-1 = pot):
    if num == 0:
        return 0
    else:
        return (num%10)*10**pot + numInvert (num//10, pot-1)

def contador(num):
    if num == 0:
        return 0
    else:
        return 1 + contador(num//10)

"""Ejercicio3................................................................"""
def contarConsonantes(palabra):
    if isinstance (palabra, str):
        return verificar (palabra)
    else:
        return "Error"

def verificar(palabra):
    if palabra == "":
        return 0
    if palabra [0] == 'a' or 'e' or 'i' or 'o' or 'u':
        return 1 + verificar (palabra[1:])
    else:
        return verificar(palabra[1:])
"""Ejercicio4................................................................"""
def intercambiar (lista):
    if isinstance (lista,list):
        return nuevaLista(lista)
    else:
        return "Error"

def nuevaLista(lista2):
    if lista2 == [ ]:
        return [ ]
    else:
        return [lista2[1]]+[lista2[0]]+nuevaLista(lista2[2:])
