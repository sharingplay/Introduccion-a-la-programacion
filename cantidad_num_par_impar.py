"""Crear una funcion para determinar cuantos digitos pares tiene un numero.
Recuerde crear la funcion de validacion para verificar que los valores del
digito se encuentran entre 0 y 9."""
def numeros_pares (num):
    if isinstance (num, int) and (num >= 0):
        print ("Cantidad de impares:", num_par(num))
        print ("Cantidad de impares", num_impar(num))
    else:
        return "Error"
def num_impar(num):
    if num == 0:
        return 0
    if ((num%10)%2) == 1:
        return 1+num_impar(num//10)
    else:
        return num_impar (num//10)
def num_par (num):
    if num == 0:
        return 0
    if ((num%10)%2)==0:
        return 1+num_par(num//10)
    else:
        return num_par(num//10)
