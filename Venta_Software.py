#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Venta de software

def precio(paquetes):
    if 0<=paquetes<=9:
        precio=paquetes*1500
        return precio
    if 10<=paquetes<=19:
        precio=paquetes*(1500*0.80)
        return precio
    if 20<=paquetes<=49:
        precio=paquetes*(1500*0.70)
        return precio
    if 50<=paquetes<=99:
        precio=paquetes*(1500*0.60)
        return precio
    if 100<=paquetes:
        precio=paquetes*(1500*0.50)
        return precio
        
def cantidadDescontada(paquetes):
    if 0<=paquetes<=9:
        descontado=0
        return descontado
    if 10<=paquetes<=19:
        descontado=paquetes*(1500*0.20)
        return descontado
    if 20<=paquetes<=49:
        descontado=paquetes*(1500*0.30)
        return descontado
    if 50<=paquetes<=99:
        descontado=paquetes*(1500*0.40)
        return descontado
    if 100<=paquetes:
        descontado=paquetes*(1500*0.50)
        return descontado

def numerosNegativos(paquetes):
    if paquetes<0:
        cp='ERROR...(num.negativos)'
        return cp
        


def main():
    paquetes=int(input('Paquetes comprados'))
    p=precio(paquetes)
    descontado=cantidadDescontada(paquetes)
    error=numerosNegativos(paquetes)
    print(error)
    print('Cantidad descontada: $%.02f'%descontado)
    print('Total a pagar: $%.02f'%p)
main()