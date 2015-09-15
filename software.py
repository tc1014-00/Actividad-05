# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Calcula el descuento en una compañia

def calcularDescuento(paquetes):
    if paquetes<10:
        descuento=0
    elif paquetes>=10 and paquetes<20:
        descuento=(1500*0.2)*paquetes
    elif paquetes>=20 and paquetes<50:
        descuento=(1500*0.3)*paquetes
    elif paquetes>=50 and paquetes<100:
        descuento=(1500*0.4)*paquetes
    else:
        descuento=(1500*.5)*paquetes
    return descuento            

def calcularPago(descuento,paquetes):
    if paquetes<10:
        pago=paquetes*1500
    elif paquetes>=10 and paquetes<20:
        pago=(paquetes*1500)-descuento
    elif paquetes>=20 and paquetes<50:
        pago=(paquetes*1500)-descuento
    elif paquetes>=50 and paquetes<100:
        pago=(paquetes*1500)-descuento
    else:
        pago=(paquetes*1500)-descuento
    return pago

def main():
    paquetes=int(input("Cuantos paquetes desea comprar"))
    
    if paquetes<1 :
        print("Usted no ha puesto una cantidad valida")
    else :
        desc=calcularDescuento(paquetes)
        pago=calcularPago(desc,paquetes)
        print("Usted comprara:",paquetes," paquetes")
        print("Con lo que ahorrara: $",desc)
        print("Y solo pagará: $",pago)
main()  