"""Hacer una funcion que reciba un numero entero y elimine los digitos que son divisibles
entre 3"""
def elimMult3 (num):
    if isinstance (num, int):
        return verificar(num,0,0)
    else:
        return "Error no es un entero"
def verificar(num,resultado,pot):
    if num == 0:
        return resultado
    elif (num%10)%3 ==0:
        return verificar (num//10,resultado,pot)
    else:
        return verificar (num//10,resultado+(num%10)*10**pot,pot+1)
