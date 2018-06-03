"""Sume los valores de la antidiagonal de una matriz cuadrada de n*n"""
def sumaDiagonalMatriz (matriz):
    if isinstance (matriz,list) and len (matriz)== len(matriz[0]):
        return sacarDiagonal (matriz,0,len (matriz)-1,-1,0)
    else:
        return "Error no es una lista"

def sacarDiagonal (matriz,indice,indice2,limite,suma):
    if indice2 == limite:
        return suma
    else: 
        return sacarDiagonal (matriz,indice+1,indice2-1,limite,suma + matriz[indice][indice2])
        
