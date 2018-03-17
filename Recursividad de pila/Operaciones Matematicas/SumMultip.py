"""Multiplicacion de una operacion dada"""
def SumMultip(num):
  if isinstance (num, int) and num > 0:
    return operacion(num)
  else:
    return "Error"
def operacion(num):
  if num == 0:
    return 1
  else:
    return (3*num-2) * operacion(num-1)
