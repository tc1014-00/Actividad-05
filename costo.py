#encoding: UTF-8
#Autor: Ernrsto Cruz Lopez
#Descuentos

def sinDescuento(numPaquetes):
    uno=(1500*numPaquetes)*(0)
    return uno
def descuentoVeinte(numPaquetes):
    vente=(1500*numPaquetes)*(.20)
    return vente
def descuentoTreinta(numPaquetes):
    trenta=(1500*numPaquetes)*(.30)
    return trenta
def descuentoCuarenta(numPaquetes):
    cuaren=(1500*numPaquetes)*(.40)
    return cuaren
def descuentoCincuenta(numPaquetes):
    cinco =(1500*numPaquetes)*(.50)
    return cinco
    
def descuento(numPaquetes):
    numpaquetes=""
    
    if numPaquetes<=9:
       desc=sinDescuento(numPaquetes)
    
    elif numPaquetes>=10 and 19>=numPaquetes:
        desc=descuentoVeinte(numPaquetes)
        
    elif numPaquetes>=20 and numPaquetes<=49:
         desc=descuentoTreinta(numPaquetes)
         
             
    elif numPaquetes>=50 and  numPaquetes<=99:
         desc=descuentoCuarenta(numPaquetes)
         
        
    elif numPaquetes>=100:
         desc=descuentoCincuenta(numPaquetes)
                 
    
    return desc

def costo(numPaquetes):
    cost=((1500*numPaquetes)-descuento(numPaquetes))
    return cost
         
def main():
    numPaquetes= int(input("Numero de paquetes comprados"))
    
    if numPaquetes<0:
        print("Error")
    else:
        des =descuento(numPaquetes)
        cos =costo(numPaquetes)
        print ("Total a pagar: $%0.2f" % cos)
        print ("Cantidad descontanda: $%0.2f" % des)
main()