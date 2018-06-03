"""Desarrolle un programa en python que recibe como entrada una lista de
numeros de longitud n, los cuales son elevados a una potencia y sumados.
Si la lista contiene sublistas como elementos, debe procesar cada elemento
de estas elevandolos a la potencia correspondiente y sumando el valor obtenido"""
def sumPotLista (lista):
    if isinstance (lista,list):
        return sumaLista(lista,0)
    else:
        return "El objeto ingresado no es una lista"

def sumaLista(lista,pot):
    if lista == [ ]:
        return 0
    elif isinstance (lista[0],list):
        return sumaLista(lista[0],pot) + sumaLista(lista[1:],pot+len(lista[0]))
    #return sumaLista(lista[0]+lista[1:]) tambien sirve
    else:
        return lista[0]**(pot+1) + sumaLista(lista[1:],pot + 1)
""""""
