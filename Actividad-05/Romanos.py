#encoding:UTF-8
#Autor:Hector Manuel Takami Flores
#Calcula Numeros Romanos

def calculaARomanos(num):
    if num<=3:
       print(num*"I")
    elif num==4:
        print("IV")
    elif num==5:
        print("V")
    elif num>5 and num<=8:
        print("V"+((num%5)*("I")))
    elif num==9:
        print("IX")
    elif num==10:
        print("X")
    else:
        print("Error")

def main ():
    num = int(input("Ingrese el numero que desea convertir")) 
    rom=calculaARomanos(num)
    print(rom)
main()    