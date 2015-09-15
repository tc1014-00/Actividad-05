#enconding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, A01377515
#Calcula el Indice de Masa Corporal y determina si alguien tiene sobrepeso o bajo peso

#Funcion que calcula el IMC
def calcularIMC(p,e) :  
    if p >= 0 and e > 0 :
        imc = p / e **2
    else :
        imc = 0
    return imc
    
#Funcion para indicar si la persona tiene un peso correcto
def verificarPesoCorrecto(p,e) :
    if p >= 0 and e > 0 :
        if calcularIMC(p,e) < 18.5 : 
            peso = "bajo peso"
        elif calcularIMC(p,e) >= 18.5 and calcularIMC(p,e) <= 25 :
            peso = "peso normal"
        else :
            peso = "sobre peso"
    else :
        peso = "error"
    return peso
    
#Funcion principal
def main() :
    peso = int( input("Dame tu pedo en kg"))
    estatura = float( input("Dame tu estatura en metros"))
    print("Tu IMC es de: %.2f" %calcularIMC(peso, estatura) )
    print("Tienes un",verificarPesoCorrecto(peso,estatura))
    

main()