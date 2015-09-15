#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, Matricula: A01377515
#Este programa convierte numeros enteros del 1 al 10 a numeros romanos

#Funcion que recibe un numero entero y lo tranforma a romano
def convertir(n) :
    if n >= 1 and n <=3 :
        numeroRomano = n*"I"
    elif n == 4 or n == 5 :
        numeroRomano = (5-n)*"I"+"V"
    elif n >= 6 and  n <= 8 :
        numeroRomano = "V"+(n-5)*"I"
    elif n == 9 or n == 10 :
        numeroRomano = (10-n)*"I"+"X"
    else :
        numeroRomano = "inexistente"
    return numeroRomano
    
#Funcion principal donde se leen y se imprimen resultados
def main() :
    numero = int( input("Ingresa un numero entre 1 y 10"))
    print( "%i en romano es %s" %(numero, convertir(numero) ))
   
main()