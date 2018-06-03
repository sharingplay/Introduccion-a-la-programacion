"""Desarrolle un programa que recibe como parametro una lista y la regresa en
orden invertido"""
def listaInverso (lista):
    if isinstance (lista,list):
        return inverso(lista)
    else:
        return "Error"
def inverso (lista): #suma el primer numero de la derecha y manda los demas
    if lista == []:  #como parametro de derecha a izquierda
        return []
    else:
        return [lista [-1]] + inverso (lista[:-1])

