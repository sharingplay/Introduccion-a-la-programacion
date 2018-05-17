#1................................................
def invertir (lista):
    if isinstance (lista,list) and lista != []:
        return inversa (lista, len(lista)-1,0,0)
    else:
        return "Error"

def inversa (lista,largo,indice,aux):
    if indice > largo:
        return lista
    else:
        aux = lista[indice]
        lista[indice] = lista [largo]
        lista[largo] = aux
        return inversa(lista,largo-1,indice+1,0)
#2.1...................................................
def cuadradoMagico(lista):
    if isinstance (lista,list):
        return consecutivos(lista,len(lista),len(lista[0]),0,0,len(lista)**2)
    else:
        return "Error"

def consecutivos(lista,cantFilas,cantCol,indiceFila,indiceCol,nDos):
    if indiceFila == cantFilas:
        return False
    elif nDos == 0:
        return True
    elif nDos != lista[indiceFila][indiceCol]:
        return consecutivos (lista,cantFilas,cantCol,indiceFila,indiceCol+1,nDos)
    elif indiceCol == cantCol:
        return consecutivos (lista,cantFilas,cantCol,indiceFila+1,0,nDos)
    elif nDos == lista [indiceFila][indiceCol]:
        return consecutivos (lista,cantFilas,cantCol,0,0,nDos -1)
#2.2...........................................................................
def cuadradoMagico(lista):
    if isinstance (lista,list):
        return validar(lista,0,0,len(lista),len(lista[0]),0,0)
    else:
        return "Error"
        
def validar(lista):
    if sumHor(lista,0,0,0,len(lista),len(lista[0])) == sumVert(lista,0,0,0,len(lista),len(lista[0]))
    and sumDiag (lista,0,0,0,len(lista),len(lista[0])) == sumAntD (lista,0,len(lista)-1,0,len(lista),len(lista[0]))
    and sumHor (lista,0,0,0,len(lista),len(lista[0])) == sumDiag (lista,0,0,0,len(lista),len(lista[0])):
        return True
    else:
        return False
    
def sumHor(lista,indFil,indCol,suma,cantFil,cantCol):
    if indFil == cantFil:
        return suma
    elif indCol < cantCol:
        return sumHor (lista,indFil,indCol + 1,suma + lista[indFil][indCol],cantFil,cantCol)
    else:
        return sumHor(lista,indFil + 1,indCol,suma,cantFil,cantCol):

def sumVert(lista,indFil,indCol,suma,cantFil,cantCol):
    if indiceCol == cantCol:
        return suma
    elif indiceFil < cantFil:
        return sumVert(lista,indFil + 1,indCol,suma + lista[indFil][indCol],cantFil,cantCol)
    else:
        return sumVert(lista,0,indCol + 1,suma,cantFil,cantCol)

def sumDiag(lista,indFil,indCol,suma,cantFil,cantCol):
    if indCol == cantCol:
        return suma
    else:
        return sumDiaf(lista,indFil + 1,indCol + 1,suma + lista[indFil][indCol],cantFil,cantCol)

def sumaAntD(lista,indFil,indCol,suma,cantFil,cantCol):
    if indCol < 0:
        return suma
    else:
        return sumaAntD (lista,indFil + 1 ,indCol - 1,suma + lista[indFil][indCol],cantFil,cantCol)

#3................................................................................

def girar(lista):
    if isinstance (lista,list):
        return rotar (lista,0,len(lista[0])-1,len(lista),len(lista[0]),[ ], [ ])
    else:
        return "Error"

def rotar (lista,indFil,indCol,suma,cantFil,cantCol,nueva,final):
    ir indCol < 0:
        return Final
    elif indFil == cantFil:
        return rotar (lista,0,indCol - 1,cantFil,cantCol, [ ], final + nueva)
    elif indFil < cantFil:
        return rotar(lista,indFil + 1,indCol,cantFil,cantCol, nueva + [lista[indFil][indCol]],final])
