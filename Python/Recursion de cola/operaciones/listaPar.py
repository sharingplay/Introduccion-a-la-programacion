"""Usando recursion de cola programe una funcion que recibe una lista y obtenga otra lista
con los numeros pares, utilizando indices."""
def listaPar (lista):
    if isinstance (lista,list):
        return nuevaLista(lista, len (lista), 0, [ ])
    else:
        return "Error"
def nuevaLista (lista, largo, indice,nueva):
    if largo == indice:
        return nueva
    elif isinstance (lista[indice],list): #en caso de que hayan listas dentro de otras
        return nuevaLista(lista[indice],len (lista[indice]),0,[ ]) + nuevaLista (lista, largo, indice + 1, nueva)
    elif lista[indice] % 2 == 0:
        return nuevaLista (lista, largo, indice +1, nueva + [lista [indice]])
    else:
        return nuevaLista (lista, largo, indice +1, nueva)
