#Dado un numero, determine su longitud (numero de digitos)
#Entrada: es un numero entero
#Restricciones: es un entero positivo mayor a cero
#Salida: longitud de un numero
def cantidad_digitos(num):
    if isinstance (num, int) and (num > 0):
        return cantidad_digitos_total (abs (num))
    else:
        return "Error"
def cantidad_digitos_total (num):
    if (num == 0):
        return 0
    else:
        return 1 + cantidad_digitos_total (num // 10)
    
""" 1 + largo (78)
 1 + largo (78)
 1 + largo (7)
 1 + largo (0)
 return 0 """
