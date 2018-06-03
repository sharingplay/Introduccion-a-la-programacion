"""Programar una funcion que recibe como parametros una lista de numeros,
determinar cuales numeros son primos y regresar una lista que contiene
solo los numeros primos. Utilice una funcion para verificar la entrada, otra
para determinar cuando un numero es primo y otra para devolver la lista
con el resultado"""
def validarPrimos (lista): #valida que el parametro sea de tipo list
    if isinstance (lista, list):
        print ("Los numeros primos de la lista son:", verificarPrimo(lista))
    else:
        return "Error"
 
def verificarPrimo(lista): #verificar si el numero es primo y lo agrega a
    if lista == [ ]:
        return [ ]
    if primo (lista[0],lista[0]-1) == True:
        return [lista[0]]+ verificarPrimo (lista[1:])
    else:
        return verificarPrimo (lista[1:])

def primo(num,div): #Asocia num-1 al divisor y comprueba los casos
    if num == 0 or num == 1 or num == 2 or num == 3:
        return True
    if div == 1:# Si div llego hasta 1 es que no encontro un valor para dividir
        return True
    if num % div == 0:# Si el resultado es 0 es que encontro un divisor
        return False
    else:
        return primo(num,div-1)





