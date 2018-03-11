"""Un numero es primo si solo es divisible por si mismo y por 1. Si un numero
no es primo diremos que es compuesto. El 0 y el 1 son numeros especiales que
no se consideran primos ni compuestos. Haga un programa que determine si un
numero es primo, compuesto o especial. Debe crear la funcion de validacion
y puede usar varias funciones para obtener la respuesta"""
def validacionNum(num):
    if isinstance (num, int) and (num > 1): #valida que sea entero positivo
        return valNum(num,num-1)
    if num == 0 or num == 1: #Si es 0 o 1 es especial
        return "El numero es especial"
    else: #Si no es valido el numero, devuelve un error
        return "Error, numero invalido"
def valNum(num,div): #Asocia num-1 al divisor y comprueba los casos
    if div == 1:# Si div llego hasta 1 es que no encontro un valor para dividir
        return "Es primo"
    if num % div == 0:# Si el resultado es 0 es que encontro un divisor
        return "Es compuesto"
    else:
        return valNum(num,div-1)
