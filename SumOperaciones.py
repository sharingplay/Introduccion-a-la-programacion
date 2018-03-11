"""Sumatoria de operaciones"""
def SumOperaciones(num):
  if isinstance (num, int) and num > 0:
    return operacion(num)
  else:
    return "Error"
def operacion(num):
  if num==0:
    return 0
  else:
    return num + 5*((num*num)**2) + operacion(num-1)
