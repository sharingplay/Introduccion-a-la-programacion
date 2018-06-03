"""Hacer una funcion que multiplica los elementos de una lista por el resultado de
multiplicaciones previas usando slicing"""
def multPrevias(lista):
    if isinstance (lista,list):
        return operacion(lista,1)
    else:
        return "Error no es una lista"

def operacion (lista,resultado):
    if lista == [ ]:
        return resultado
    else:
        return operacion(lista[:-1],lista[-1]*resultado)
