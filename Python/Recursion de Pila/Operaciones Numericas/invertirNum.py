"""Escriba un programa que recibe un numero conformado por una cantidad par de
digitos los cuales son procesados en parejas. Los digitos que conforman cada
pareja son intercambiados, el numero no puede contener 0
Ej: 185412 devuelve 814521"""
def invertirNum(num):
    if isinstance(num,int):
        return cambio(num)
    else:
        return "Error"
def cambio(num,pot=0):
    if num == 0:
        return 0
    else:
        return invertir(num % 100)*10**pot + cambio(num//100,pot+2)
def invertir (num,pot=0):
    if num == 0:
        return 0
    else:
        return (num//10)*10**pot + (num%10)*10**(pot+1)
