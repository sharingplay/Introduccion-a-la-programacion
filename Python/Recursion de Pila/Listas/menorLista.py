"""Hacer una funcion que encuentre el valor minimo en una lista"""
def menorLista(lista):
    if isinstance (lista, list):
        print ("El menor numero encontrado es", menor(lista))
    else:
        return "Error"
def menor(lista):
    if len(lista) == 1: #condicion de parada cuando la lista tenga 1 numero
        return lista[0]

    elif lista [1] < lista [0]: #compara el segundo de la lista con el primero
        return menor (lista[1:])#Si el segundo es menor que el primero regresa 
                                #la lista a partir del segundo numero sin contar
                                #el primero
    else:
        return menor ([lista[0]]+ lista[2:])
"""De lo contrario devolver la lista con el primer numero, y los demas a
partir del tercero, sin contar el segundo ya que no es menor que el primero"""
