# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Calcula el IMC y checa que tan sano estas

def calcularIMC(peso,estatura):
    imc=peso/(estatura*estatura)
    return imc

def determinarSaludPersona(imc):
    if imc<18.5:
        salud="Bajo peso"
    elif imc>=18.5 and imc<=25:
        salud="Peso normal" 
    else:
        salud="Sobrepeso"
    return salud

def main():
    peso=float(input("Cual es tu peso en kg"))
    estatura=float(input("Cual es tu estatura en mtrs"))
    if peso<=0 or estatura<=0:
        print("Eror: Uno de los valores no es valido")
    else:
        imc=calcularIMC(peso,estatura)
        salud=determinarSaludPersona(imc)
        print("Su IMC es de:",imc," y por tanto usted tiene:",salud)  
main()      