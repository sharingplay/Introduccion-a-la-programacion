"""Busqueda lineal de elementos:
dado un elemento, recorra una lista para determinar si este se encuentra
en la lista. Busqueda lineal de elementos. Utilice indices"""
def busquedaLineal (num,lista):
    if isinstance (num, int) and (lista,list):
        return buscar (num,lista,0,len (lista))
    else:
        return "Error"

def buscar (num,lista,indice,largo):
    if indice == largo:
        return False
    elif num == lista [indice]:
        return True
    else:
        return buscar (num,lista,indice+1,largo)
"""Busqueda lineal con slicing..............................................."""

def busquedaSlice(num,lista):
    if isinstance (num, int) and (lista,list):
        return busqueda(num,lista)
    else:
        return "Error"

def busqueda (num,lista):
    if lista == [ ]:
        return False
    elif num == lista [0]:
        return True
    else:
        return busqueda (num,lista[1:])
