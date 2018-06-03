"""Suma valores de una lista"""
def suma (lista):
    #if type (lista) == list, tambien verifica que lista sea de tipo lista
    if isinstance (lista,list):
        return suma_aux (lista)
    else:
        return "Error, el valor ingresado no es una lista"

def suma_aux (lista):
    if lista == []:
        return 0
    else:
        return lista [0] + suma_aux (lista[1:]) #saca al primer numero y continua con los demas
