import math #importa la libreria de matematica
def sumaRaiz(lista):
    if isinstance (lista,list):
        print ("La suma de las raices es: ", raiz(lista))
    else:
        return "Error"
def raiz (lista):
    if lista == []:
        return 0
    else:
        return math.sqrt(lista[0]) + raiz (lista[1:])

