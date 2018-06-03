"""Programe una funcion que indique cuantas veces se repite un digito en una lista
Utilice la funcion lambda"""
def cantVeces(lista,num):
    if isinstance (lista,list) and (num, int):
        repite = lambda digito, num: num == digito
        return conteo (lista,num,repite)
    else:
        return "Error"

def conteo (lista, num, condicion):
    if lista == [ ]:
        return 0
    elif condicion (lista [0],num):
        return 1 + conteo (lista[1:],num,condicion)
    else:
        return conteo (lista[1:],num,condicion)
