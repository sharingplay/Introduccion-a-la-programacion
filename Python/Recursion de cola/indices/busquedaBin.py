"""Programe un función que realiza una búsqueda binaria de
elementos en una lista ordenada. Utilice recursión de cola e índices. """
def busquedaBin (num,lista):
    if isinstance (num,int) and (lista,list):
        return busqueda (num,lista,(len(lista))//2)
    else:
        return "Error"
def busqueda (num,lista,indice):
    if indice == len (lista) or indice < 0:
        return False
    if lista [indice] == num:
        return True
    elif lista [indice] > num:
        return busqueda (num,lista, indice-1)
    elif lista [indice] < num:
        return busqueda (num,lista, indice + 1)
        
