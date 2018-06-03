"""Sumatoria de los todos los digitos hasta el ingresado"""
def Sumatoria(num):
  if isinstance (num, int) and num > 0:
    return suma(num)
  else:
    return "Error"
def suma(num):
  if num==0:
    return 0
  else:
    return (num)+suma(num-1) #devuelve los valores ingresados en tiempo real