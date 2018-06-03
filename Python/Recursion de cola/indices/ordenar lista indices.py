"""Dada una lista, crear una funcion para ordenar sus elemntos. utilice recursion de cola y listas"""
def ordenar (lista):
    if isinstance (lista,list) and lista != [ ]:
        return  ordenar_aux(lista,0,0)
    else:
        return "Error"

def ordenar_aux (lista,indice1,indice2):
    if indice2 == len(lista)-1: # cantidad de comparaciones
         return lista
    elif indice1 == len (lista) - 1:
        return ordenar_aux(lista,0,indice2 + 1)
    elif lista [indice1] > lista [indice1+1]:
        aux = lista[indice1]
        lista [indice1] = lista[indice1 + 1]
        lista [indice1 +1] = aux
        return ordenar_aux (lista, indice1 + 1,indice2)
    else:
        return ordenar_aux (lista, indice1 + 1,indice2)
