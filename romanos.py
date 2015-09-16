#encoding: UTF-8
#Autor= Ernesto Cruz López  
#Convertir arabigos a romanos.

def convertirTres(num):
    x=num*"I"
    return x
def convertirOcho(num):
    y=(num-5)*"I"
    return y
def convertir(num):
    numero=""
    if num == 1 or num== 2 or num == 3:
         numero= convertirTres(num)
    elif num== 4:
         numero="IV"
    elif num==5 or num== 6 or num==7 or num==8:
         numero= "V"+(convertirOcho(num))
    elif num==9:
         numero="IX"
    elif num==10:
         numero="X"
    else:
        numero="No existe"
    return numero
    

def main():
    num= int(input("Escribe un número"))
    numeroRomano = convertir(num)
    print("Tu número en romano es",numeroRomano)
main()