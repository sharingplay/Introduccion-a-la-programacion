"""Sume los valores de la diagonal de una matriz cuadrada de n*n"""
def sumaDiagonalMatriz (matriz):
    if isinstance (matriz,list) and len (matriz)== len(matriz[0]):
        return sacarDiagonal (matriz,0,len (matriz),0)
    else:
        return "Error no es una lista"

def sacarDiagonal (matriz,indice,largo,suma):
    if indice == largo:
        return suma
    else: 
        return sacarDiagonal (matriz,indice+1,largo,suma + matriz[indice][indice])
        
