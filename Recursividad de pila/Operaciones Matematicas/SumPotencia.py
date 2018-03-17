"""Sumatoria de potencias"""
def SumPotencia(num):
  if isinstance (num, int) and num > 0:
    return suma_mult(num)
  else:
    return "Error"
def suma_mult(num):
  if num==0:
    return 0
  else:
    return (num*num**3)+suma_mult(num-1)
