#encoding:UTF-8
#Autor:Hector Manuel Takami Flores
#Calcula el total de una venta de Software

def totalDescuento(paquetes,costoSoftware):
    if paquetes<1:
        print("Error")
    elif paquetes<10:
       d= print("No hay descuento")
       t= print("El total es de:$",costoSoftware)
    elif paquetes<=19:
        d=print("Descuento: 20%")
        t=print("El total es de:$",(costoSoftware-(costoSoftware*.20)))
    elif paquetes<=49:
        d=print("Descuento: 30%")
        t=print("El total es de:$",(costoSoftware-(costoSoftware*.30)))
    elif paquetes<=99:
        d=print("Descuento: 40%")
        t=print("El total es de:$",(costoSoftware-(costoSoftware*.40))) 
    elif paquetes>=100:
        d=print("Descuento: 50%")
        t=print("El total es de:$",(costoSoftware-(costoSoftware*.50)))   
    else:
        print("")
        return t,d 

def main():
    costoSoftware=int(1500)
    paquetes=int(input("Numero de paquetes comprados"))
    total=totalDescuento(paquetes,costoSoftware)
    print(total)
main()  