def suma_digitos (num):
    if (num==0): #Rojo
        return 0
    else : #verde
        return num % 10 + suma_digitos(num//10)
