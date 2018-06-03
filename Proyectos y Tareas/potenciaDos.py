"""Potencias de Dos"""
def validar (exp):
    if isinstance (exp, int) and (exp > 0):
        return potencias (exp)
    else:
        return "Error"
def potencias(exp):
    if exp == 0:
        print (2 ** exp, end = ",") #comando para imprimir en la misma linea
        return 0
    else:
        print (2 ** exp, end = ",")
        return potencias (exp - 1)
