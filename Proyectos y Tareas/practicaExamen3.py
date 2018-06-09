class Multiples:
    def __init__(self):
        pass
    def table(self):
        print("Ingrese un numero del 1 al 10 para ver la tabla de multiplicar")
        num = int(input("-->"))
        for i in range(1,11):
            print (str(num)+ " X " + str(i)+" = " + str(num*i))
                     
#..................................................................................

class Sequence:
    def __init__(self):
        pass
    def serie(self):
        print ("Ingrese dos numero, el primero menor que el segundo")
        print ("Para saber la suma de los numero que hay en medio")
        num1 = int(input("numero 1: "))
        num2 = int(input("numero 2: "))
        resultado = 0
        for i in range(num1,num2+1):
            resultado += i
        print ("La suma es: " + str(resultado))

#..................................................................................
class Collatz:
    def __init__(self):
        pass
    def conjeture(self):
        print ("Ingrese un numero para ver su secuencia de Collatz")
        num = int(input("numero: "))
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                print(num)
            else:
                num = num * 3 +1
                print (num)
#..................................................................................
class Imprimir:
    def __init__(self):
        pass
    def graficar(self):
        print("Ingrese un numero para graficar su secuencia de Collatz")
        matriz = []
        num = int(input("numero: "))
        grafico = ""
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                matriz.append(num)
            else:
                num = num * 3 +1
                matriz.append(num)
        for elemento in matriz:
            contador = 0
            while contador != elemento:
                grafico = grafico + "*"
                contador += 1
            print (grafico)
            grafico = ""


                
                
