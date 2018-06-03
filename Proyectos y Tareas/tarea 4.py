"""Convertidor de binario a decimal"""
def convBinDec(num):
    if isinstance (num,int):
        return binDec (num, 0)
"""Convertidor de decimal a binario"""
def convDecBin(num):
    if isinstance (num,int):
        return decBin(num)
    
"""Convertidores"""
def binDec(num,cont): #convierte los numeros de la lista y los suma
    if (num%10 > 1) or (num%10 < 0):#verifica que el numero ingresado este
                                    #compuesto por 1 y 0
        return "Error el numero ingresado no esta en binario"
    if num == 0:
        return 0
    else: #Operacion para pasar de binario a decimal
        return (num % 10)*(2**cont) + binDec (num//10, cont+1)
    
def decBin(num):
    if num == 0:#Cuando el numero llega a 0 devuelve el resultado en forma de string
        return ""
    else:#convierte a string los resultados de las divisiones para concatenarlo.
        return str (decBin(num//2)) + str (num%2)
