class Invertir:
    def __init__(self):
        pass

    def invertir_lista(self,lista):
        if isinstance (lista,list):
            return self.invertir_lista_aux (lista)
        else: return "Error: el valor ingresado no es una lista"

    def invertir_lista_aux(self,lista): #IZQUIERDA A DERECHA
        if lista == []: #rojo
            return []
        else: return self.invertir_lista_aux(lista[1:])+ [lista[0]]

    def invertir_lista_index (self,lista): #DERECHA A IZQUIERDA
        if lista == []: #rojo
            return []
        else: return [lista[-1]]+ self.invertir_lista_index(lista[:-1])
"""Para llamarlo hay que hacer
inv = Invertir()
inv.invertir_lista([1,2,3,4,5])"""

