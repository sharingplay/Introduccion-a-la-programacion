"""Calcular la serie de Fibonacci para un numero.
Se debe validar que el numero es un entero positivo"""
def Fib(num):
  if isinstance (num,int):
    return fib_aux(num)
  else:
    return "Error"
def fib_aux(num):
  if num == 0:
    return 1
  elif num == 1:
    return 1
  else: 
    print ((num - 1)+(num - 2))
    return fib_aux (num - 1) + fib_aux (num - 2)