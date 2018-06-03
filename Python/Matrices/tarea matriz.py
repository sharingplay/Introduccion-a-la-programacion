
"""multiplica los primeros numeros de una columna contra los numeros de
una fila"""
def multiplicacionMatriz(lista1,lista2):
    if isinstance (lista1,list) and (lista2,list):
        return matrices(lista1,lista2,0,0,0,0,[],[])
    else:
        return "Error"

def matrices (lista1,lista2,contCol_1,contCol_2,contFila_1,contFila_2,nueva,final):
    if contFila_1 == len(lista1) and contCol_2 == len (lista2[0]):
        return final

    elif contCol_1 < len(lista1[0]):
        return matrices (lista1,lista2,contCol_1 + 1,contCol_2,contFila_1,contFila_2 + 1,nueva + [(lista1[contFila_1][contCol_1]) * (lista2[contFila_2][contCol_2])],final)

    elif contCol_1 == len(lista1[0]):
        return matrices (lista1,lista2,0,contCol_2 + 1,contFila_1 + 1,0,[],final + [nueva])


    
    #multiplicacionMatriz([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]])
    #continuar pensando la logica

def multiplicacionMatriz(lista1,lista2):
    if isinstance (lista1,list) and (lista2,list):
        return matrices(lista1,lista2,0,0,0,0,[],[])
    else:
        return "Error"

"""def matrices (lista1,lista2,contCol_1,contCol_2,contFila_1,contFila_2,nueva,final):
    if contFila_1 == len(lista1) and contCol_2 == len (lista2[0]):
        return final

    elif contCol_1 < len(lista1[0]):
        return matrices (lista1,lista2,contCol_1 + 1,contCol_2,contFila_1,contFila_2 + 1,nueva + [(lista1[contFila_1][contCol_1]) * (lista2[contFila_2][contCol_2])],final)

    elif contCol_1 == len(lista1[0]):
        return matrices (lista1,lista2,0,contCol_2 + 1,contFila_1 + 1,0,[],final + [nueva[0]])"""
