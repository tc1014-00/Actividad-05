# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Lee un numero y lo imprime como numero romano

def convertirARomano(numero):
    if numero<=3:
        return numero*"I"
    elif numero>3 and numero<6:
        return (((numero%5)%3)*"I")+"V"
    elif numero>=6 and numero<=8:
        return "V"+((numero%5)*"I")
    else :
        return (((numero%10)%8)*"I")+"X"
    
        
def main():
    numero=int(input("Que numero quiere convertir"))
    if numero>0 and numero<11 :
        numRomano=convertirARomano(numero)
        print ("El numero ",numero," en romano es:",numRomano)
    else:
        print("ERROR: el numero debe estar entre el rango[1,10]") 
        
main()   