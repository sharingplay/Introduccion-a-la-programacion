"""Suma valores pares e impares de una lista"""
def suma (lista):
    #if type (lista) == list, tambien verifica que lista sea de tipo lista
    if isinstance (lista,list):
        print "Suma pares: " , validarPar (lista)
        print "Suma impares: ",validarImpar(lista)
    else:
        return "Error, el valor ingresado no es una lista"

def validarPar(lista): #separa los numero pares encontrados en la lista
    if lista == []:
        return 0
    elif lista [0] % 2 == 0:
        return lista [0]+ validarPar (lista[1:])
    else:
        return validarPar (lista [1:])
    
def validarImpar(lista): #separa y cuenta los numero impares encontrados
    if lista == []:
        return 0
    elif lista [0] % 2 != 0:
        return lista [0]+ validarImpar (lista[1:])
    else:
        return validarImpar (lista [1:])
