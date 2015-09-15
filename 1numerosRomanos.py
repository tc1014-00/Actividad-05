# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Regresa un numero en numeros romanos

def cambiarNumero(n):           #Cambia el numero a numeros romanos
    if (n <= 3 and n>=1):
        r = n*"I"
    elif (n == 4):
        r = "IV"
    elif (n >=5 and n<=8):
        r = "V"+ "I"*(n%5)
    elif (n == 9):
        r = "I" + "X"
    elif (n == 10):
        r = "X"
    else:
        r = "ERROR"
    return r
    
def main():
    numero = int (input("Dame el numero"))
    numeroRomano = cambiarNumero (numero)
    print ("El numero %i en romano es" %numero, numeroRomano)   

main()
