def sumaListas(lista):
    if isinstance (lista, list):
        print("La sumatoria de la lista es", sumatoriaListas (lista))
    else:
        return "Error"
    
def sumatoriaListas (lista):
    if lista == [ ]:
        return 0
    if isinstance (lista[0],list):
        return sumatoriaListas(sacarLista(lista[0])+ lista[1:])
    else:
        return lista[0] + sumatoriaListas (lista[1:])

def sacarLista (lista2):
    if lista2 == [ ]:
        return [ ]
    else:
        return [lista2[0]] + sacarLista (lista2[1:])
