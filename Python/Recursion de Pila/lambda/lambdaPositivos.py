"""Hacer una funcion que indique si todos los elementos de una lista son positivos.
La funcion debe regresar True o False."""
def lambdaPositivos(lista):
    if isinstance (lista, list):
        positivo = lambda digito: digito < 0
        return validarPositivos(lista,positivo)
    else:
        return "Error"
def validarPositivos(lista,condicion):
    if  lista == [ ]:
        return True
    elif condicion (lista[0]):
        return False
    else:
        return validarPositivos (lista[1:],condicion)
    
