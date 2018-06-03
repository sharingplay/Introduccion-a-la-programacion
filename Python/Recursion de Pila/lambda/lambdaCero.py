"""Usando funciones lambda programe una funcion que indique si una lista tiene
al menos un cero. La funcion debe regresar True o False."""
def tieneCero(lista):
    if isinstance (lista, list):
        esCero = lambda digito: digito ==0
        return buscCero(lista,esCero)
    else:
        return "Error"
def buscCero(lista,condicion):
    if  lista == [ ]:
        return False
    elif condicion (lista[0]):
        return True
    else:
        return buscCero(lista[1:],condicion)
    
