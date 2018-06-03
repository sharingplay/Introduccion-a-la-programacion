"""Suma valores de una lista"""
def suma (lista):
    #if type (lista) == list, tambien verifica que lista sea de tipo lista
    if isinstance (lista,list):
        return validarPar (lista)
    else:
        return "Error, el valor ingresado no es una lista"

def validarPar(lista): #separa los numero pares encontrados en la lista
    if lista == []:
        return 0
    elif lista [0] % 2 == 0:
        return lista [0]+ validarPar (lista[1:])
    else:
        return validarPar (lista [1:])
