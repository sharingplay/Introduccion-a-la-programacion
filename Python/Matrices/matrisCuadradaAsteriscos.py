"""Programe una clase que tenga varios metodos para analizar lo siguiente:
* Crear una matriz de n x n, en donde el usuario solo debe especificar el valor
de n como parametro.
* Rellenar con asteriscos la primera y la ultima fila.
* Rellenar con asteriscos la primera y ultima columna."""
class Matriz:
    def __init__(self):
        pass
    def crearMatriz (self,n):
        if isinstance (n, int) and n > 0:
            return self.crearMatriz_aux (n,[],[],0,0)
        else:
            return "Error"

    def crearMatriz_aux (self,n,matriz,fila,indiceFila,indiceColumna):
        if indiceFila == n:
            return matriz
        elif indiceColumna == n:
            return self.crearMatriz_aux (n, matriz + [fila], [ ], indiceFila + 1, 0)
        elif indiceFila == 0 or indiceFila == n-1:
            return self.crearMatriz_aux(n, matriz,fila + ["*"],indiceFila, indiceColumna)
        elif indiceColumna == 0 or indiceColumna == n-1:
            return self.crearMatriz_aux(n, matriz,fila + ["*"],indiceFila,indiceColumna)
        else:
            return crearMatriz_aux (n, matriz, fila + [0], indiceFila, indiceColumna + 1)
