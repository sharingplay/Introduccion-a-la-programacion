def lista2 (lista):
    if isinstance (lista, list) and lista != []:
        return lista2_aux(lista,1, len(lista),1)
    else:
        return "error"

def lista2_aux(lista,resultado,largo, indice):
    if indice== largo:
        return resultado
    else:
        return lista2_aux(lista,largo, resultado* lista[indice], indice+1)
