"""Lista Par e Impar con While"""
def pares(num):
    if isinstance (num,int) and num >= 0:
        return pares_aux (num)

def pares_aux(num):
    listaPares = [ ]
    listaImpares = [ ]
    while num > 0:
        digi = num % 10
        if digi % 2 == 0:
            listaPares += [digi]
        else:
            listaImpares += [digi]
            num = num//10
    return listaPares, listaImpares

"""Lista Par e Impar con For"""
def pares_impares(lista):
    if isinstance (lista,list) and lista !=[ ]:
        return pares_impares_aux(lista)
def pares_impares_aux (lista):
    listaPares = [ ]
    listaImpares = [ ]
    for valor in lista:
        if (valor % 2 == 0):
            listaPares += [valor]
        else:
            listaImpares += [valor]
    return listaPares, listaImpares
