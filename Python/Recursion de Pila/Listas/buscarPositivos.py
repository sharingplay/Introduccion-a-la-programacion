"""Funcion que indica si todos los elementos de una lista son positivos,
Si todos los elementos son positivos debe regresar True, sino False"""
def numEnteros (lista):
    if isinstance (lista, list):
        return buscarPositivos (lista)
    else:
        return "Error"
def buscarPositivos (lista):
    if lista == []:
        return True
    elif lista [0] < 0:
        return False
    else: return buscarPositivos (lista [1: ])

