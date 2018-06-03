"""Dado un numero determine cuantos de sus digitos son pares y cuantos son impares
Utilice funciones lambda"""

def parImpar (num):
    if isinstance (num, int):
        par = lambda digito: digito % 2 == 0
        impar = lambda digito: digito % 2
        print ("Pares: ",contar (num,par))
        print ("Impares: ",contar (num, impar))
    else:
        return "Error"
def contar (num,condicion):
    if  num == 0:
        return 0
    elif condicion (num%10):
        return 1 + contar (num//10,condicion)
    else:
        return contar (num//10,condicion)
    
