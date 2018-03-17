"""Calcular el factorial de un numero"""
def factorial(num):
    if isinstance (num, int) and (num >0):
        return calculo_factorial(num)
    else:
        return "Error, el numero debe ser mayor a 0"
def calculo_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculo_factorial(num-1)
