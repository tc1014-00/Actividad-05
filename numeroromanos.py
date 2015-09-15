#Encoding:UTF-8
#Autor: Manuel Zavala Gómez
#Numeros romanos

def main():
    numero=int(input("Teclea tu número"))
    convertirRomano(numero)
    
def convertirRomano(numero):
    if numero <=3:
        print(numero*"I")
        
    elif numero >5 and numero<10:
        x = numero-5
        if x==4:
            print("IX")
        else:
            print("V",("I"*x))   
    else:
        if numero >5:
            print ("X")
        elif numero <5:
            print ("IV")
        else:
            print("V")     
main()        
            