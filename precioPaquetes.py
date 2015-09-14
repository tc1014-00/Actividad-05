#encoding: UTF-8
# Jorge Daniel Juarez Ruiz
# Calcular el precio total dependiendo del descuento por no. de paquetes


def calcularPrecio(p): 
    if 0<=p<=9:
        precio=p*1500
        return precio
    if 10<=p<=19:
        precio=p*1500*0.80
        return precio
    if 20<=p<=49:
        precio=p*1500*0.70
        return precio
    if 50<=p<=99:
        precio=p*1500*0.60
        return precio
    if p>=100:
        precio=p*1500*0.50
        return precio
    if p<0:
        precio=0
        return precio
        
def descontarCantidad(p):
    if 0<=p<=9:
        cd=0
        return cd
    if 10<=p<=19:
        cd=(p*1500*0.20)
        return cd
    if 20<=p<=49:
        cd=(p*1500*0.30)
        return cd
    if 50<=p<=99:
        cd=(p*1500*0.40)
        return cd
    if p>=100:
        cd=(p*1500*0.50)
        return cd
    if p<0:
        cd=0
        return cd
def marcarError(p):
    if p<0:
        a="ERROR (num.negativos)"
        return a
    else: 
        b=""
        return b
        

def main():
    paquetes=int(input("Numero de paquetes"))
    p=calcularPrecio(paquetes)
    cd=descontarCantidad(paquetes)
    e=marcarError(paquetes)
    print (e)
    print("Cantidad descontada: $%.02f" %(cd))
    print ("Total a pagar: $%.02f" %(p))
    

main()