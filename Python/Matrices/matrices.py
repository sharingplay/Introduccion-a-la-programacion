def suma_matriz(elemento,matriz):
    if isinstance (matriz, int) and matriz !=[] and isinstance(elemento,int):
        return matriz_aux(elemento,matriz, len(matriz), len(matriz[0]),0,0)
    else: return "error"

def matriz_aux(elemento, matriz,num_filas,num_columnas,fila, columna):
    if fila == num_filas:
        return matriz
    elif columna == num_columnas:
        return matriz_aux (elemento,matriz,num_filas,num_columnas,fila+1,0)
    else:
        return matriz_aux (elemento,matriz[fila][columna]+elemento, num_filas,num_columnas,fila,columna+1)
