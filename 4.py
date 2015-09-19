#encoding: UTF-8 
#David Salvador Ruiz Roa
#Venta de software

def descuento(a):
    t = ""
    if a < 0:
        t = "error"
    elif a > 9 and a < 20:
        t = "20%"
    elif a > 19 and a <50:
        t = "30%"
    elif a > 49 and a <100:
        t = "40%"
    elif a > 100:
        t = "50%"
    else:
        t = "Error"
    return t


def main():
    paquetesC = int(input("Ingrese la cantidad de paquetes comprados"))
    total = descuento(paquetesC)
    print("Cantidad de paquetes : ",paquetesC)
    print("Descuento aplicado : ",total)
    
    
    
    
main()
