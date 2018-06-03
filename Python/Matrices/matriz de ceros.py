#realizar una matriz de tamaño nxn y llenarlo de "0" y "*"
#sin clases
#[['*','*','*','*',    '*'],
 #['*', 0, 0,   0,     '*'],
 #['*', 0, 0,   0,     '*'],
 #['*', 0, 0,   0,     '*'],
 #['*','*','*','*',    '*']]

def matriz_n (n):
    if isinstance (n,int):
        return aux(n,[],[],0,0)
    else:
        return "error"

def aux(n,matriz1,matriz2,fila,columna):
    if columna == n:
        return matriz2
    elif fila == n:
        return aux(n,[],matriz2+[matriz1],0,columna+1)
    elif fila == 0 or fila == n-1:
        return aux(n,matriz1 + ["*"],matriz2,fila+1,columna)
    elif columna == 0 or columna == n-1:
        return aux(n,matriz1 + ["*"],matriz2,fila+1,columna)
    else:
        return aux(n,matriz1 + [0],matriz2,fila+1,columna)
        
