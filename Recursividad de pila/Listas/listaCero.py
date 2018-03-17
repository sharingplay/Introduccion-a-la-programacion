"""Funcion que indica si una lista tiene al menos un cero.
La Funcion debe regresar True o False"""
def validar (lista):
    if isinstance (lista,list):
        return buscarCero (lista)
    else:
        return "Error"
def buscarCero (lista):
    if lista == []:
        return False
    elif lista [0] == 0:
        return True
    else: 
        return buscarCero (lista [1: ])

