# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Da un descuento dependiendo de la cantidad de paquetes vendidos.

def calcularDescuento (paquetes): #Calcula el descuento dependiendo de la cant. de paquetes comprados
    if   (paquetes < 10 ):
        desc = 0
    elif (paquetes >= 10 and paquetes < 20):
        desc = 0.2
    elif (paquetes >= 20 and paquetes < 50):
        desc = 0.3
    elif (paquetes >= 50 and paquetes < 100):
        desc = 0.4
    elif (paquetes >= 100):
        desc = 0.5
    return desc

def main():
    numeroPaquetes = int (input ("¿Cuantos paquetes quiere?"))

    if (numeroPaquetes<0):
        print ("ERROR. Cantidad de paquetes invalida.")
    else:
        subtotal = numeroPaquetes * 1500
        descuento = calcularDescuento (numeroPaquetes) * subtotal
        total = subtotal - descuento
        print ("Numero de paquetes:", format (numeroPaquetes, ',.0f'))
        print ("Subtotal: $", format (subtotal, ',.2f'))
        print ("Decuento: $", format (descuento, ',.2f'))
        print ("Total: $"   , format (total, ',.2f'))

main()
