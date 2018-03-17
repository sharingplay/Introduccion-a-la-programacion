"""Sumatoria de todos los productos"""
def SumatoriaProductos(num):
  if isinstance (num, int) and num > 0:
    return sumatoria(num)
  else:
    return "Error"

def sumatoria(num):
  if num==0:
    return 0
  else:
    return producto (num) + sumatoria(num-1)

def producto(num):
  if num == 0:
    return 1
  else:
    return  (3*num**2-num)*producto(num-1)