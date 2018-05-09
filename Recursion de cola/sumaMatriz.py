"""Calcular la suma de todos los valores de una matriz de n x m y determinar el valor promedio
de estos"""
def sumaMatriz (lista):
    if isinstance (lista,list):
        return promedio (lista,0,0,len (lista),len (lista[0]),0)
    else:
        return "Error"

def promedio (lista,indiceFila,indiceCol,cantFila,cantCol,prom):
    if indiceFila == cantFila:
        return prom/(cantFila*cantCol)
    elif indiceCol <  cantCol -1:
        return promedio (lista,indiceFila,indiceCol + 1,cantFila,cantCol,prom + lista[indiceFila][indiceCol])
    elif indiceCol == cantCol-1:
        return promedio (lista, indiceFila + 1, 0, cantFila, cantCol,prom + lista[indiceFila][indiceCol])
