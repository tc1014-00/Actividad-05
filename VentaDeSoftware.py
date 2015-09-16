#Encoding:UTF-8
#Autor: Paola Castillo Nacif
#Descripcion:El programa mostrara el descuento realizado en la compra de cierta cantidad de paquetes de Software

def calcularNeg(paq):
    mensaje=""
    if paq<0:
        mensaje="error"
    else:
        mensaje=""
    return mensaje

def calcularDesc(paq):
    if paq>=0 and paq<10:
        desc=0
    elif paq>=10 and paq<=19:
        desc=(paq*1500)*0.20
    elif paq>=20 and paq<=49:
        desc=(paq*1500)*0.30
    elif paq>=50 and paq<=99:
        desc=(paq*1500)*0.40
    elif paq>=100:
        desc=(paq*1500)*0.50
    return desc

def calcularCosto(paq):
    if paq>=0 and paq<10:
        costo=(paq*1500)
    elif paq>=10 and paq<=19:
        costo=(paq*1500)-((paq*1500)*0.20)
    elif paq>=20 and paq<=49:
        costo=(paq*1500)-((paq*1500)*0.30)
    elif paq>=50 and paq<=99:
        costo=(paq*1500)-((paq*1500)*0.40)
    elif paq>=100:
        costo=(paq*1500)-((paq*1500)*0.50)
    return costo

    
def main():
    paq=int(input("Inserte cantidad de paquetes de Software a comprar"))
    errorn=calcularNeg(paq)
    desc=calcularDesc(paq)
    totalp=calcularCosto(paq)
    print(errorn)
    print("su descuento es de:","$","%.2f"%desc)
    print("Su total es de:","$","%.2f"%totalp)
main()
    