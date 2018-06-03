def busqueda_binaria (x,lista):
    if isinstance (x,int) and (lista,list):
        return busqueda_aux (x,lista,len(lista)// 2)
    else:
        return "error"

def busqueda_aux (x,lista,mitad):
    if lista == []:
        return False
    elif lista[mitad] == x:
        return True
    if lista[mitad] < x:
        return busqueda_aux (x,lista[(mitad+1):], (len(lista[(mitad+1):])-1)//2)
    else:
        return busqueda_aux (x,lista[:mitad], (len(lista[:mitad])-1)//2)
