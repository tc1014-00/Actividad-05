#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, A0177515
#Aplica un descuento segun la cantidad de paquetes adquiridos

#Funcion para calcular el descuento aplicado
def calcularDesc(num) : 
    if num >= 0 :
        if num >= 10 and num <=19 : 
            desc = (num*1500) * .20
        elif num >= 20 and num <= 49 :
            desc = (num*1500) * .30
        elif num >= 50 and num <= 99 :
            desc = (num*1500) * .40
        elif num >= 100 : 
            desc = (num*1500) * .50
        else : 
            desc = 0
    else :
        desc = 0
    return desc 
    
#Funcion que calcula el total a pagar
def calcularTotal(num) :
    if num >= 0 :
        total = num*1500 - calcularDesc(num)
    else : 
        total = "Error"
    return total

#Funcion principal
def main() :
    numPaquetes = int( input("Cuantos paquetes se compraron?"))
    print("La cantidad descontada es %.1f y el total es:" %(calcularDesc(numPaquetes)),calcularTotal(numPaquetes) )
    
main()