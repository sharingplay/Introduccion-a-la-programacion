""" Dado un numero, encontrar
cuantas veces aparece un digito en ese numero"""
"""467544

4 -> 3 veces
aparece (num,digito)
"""
def conteo_num (num, digito):
    if isinstance (num, int) and (digito, int) and (num > 0) and (digito >= 0):
        return  cantidad_num(num,digito)
            
    else:
        return 0
def cantidad_num (num, digito):
    if num == 0:
        return 0
    if (num % 10) == digito: #sacar el ultimo digito
        return 1 + cantidad_num (num//10,digito) #Pasa el numero menos el ultimo digito
                                                 #de derecha a izquierda                              
    else:
        return cantidad_num(num//10,digito)
