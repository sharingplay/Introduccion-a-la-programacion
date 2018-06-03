#realizar una matriz de tamaño nxn y llenarlo de "0" y "*"
#sin clases
#[['*','*','*','*',    '*'],
 #['*', 0, 0,   0,     '*'],
 #['*', 0, 0,   0,     '*'],
 #['*', 0, 0,   0,     '*'],
 #['*','*','*','*',    '*']]
class Matriz:
    def __init__(self):
        pass
    def matriz_n (self,n):
        if isinstance (n,int):
            return self.aux(n,[],[],0,0)
        else:
            return "error"

    def aux(self,n,matriz1,matriz2,fila,columna):
        if columna == n:
            return matriz2
        elif fila == n:
            return self.aux(n,[],matriz2+[matriz1],0,columna+1)
        elif fila == 0 or fila == n-1:
            return self.aux(n,matriz1 + ["*"],matriz2,fila+1,columna)
        elif columna == 0 or columna == n-1:
            return self.aux(n,matriz1 + ["*"],matriz2,fila+1,columna)
        else:
            return self.aux(n,matriz1 + [0],matriz2,fila+1,columna)
