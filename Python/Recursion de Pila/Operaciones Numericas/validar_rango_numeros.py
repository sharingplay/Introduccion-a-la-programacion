"""Verifica que todos los digitos del numero se encuentren entre 0 y 4"""
def rango_digito (num):
    if isinstance (num,int) and (num >= 0):
        return scanNum(num)
    else:
        return "Error"
def scanNum (num):
    if num == 0:
        return True
    if (num%10 >=0) and (num%10<=4):
        return scanNum (num//10)
    else:
        return False
        
