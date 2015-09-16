#Encoding:UTF-8
#Autor:Paola Castillo Nacif
#Descripcion:El programa imprimira el IMC de una persona

def calcularIMC(peso,est):
    if peso<=0 or est<=0:
        IMC="Error"
    else:
        IMC=peso/(est**2)
    return IMC
    
def pesoIdeal(imc):
    peso=""
    if imc=="Error":
        peso="Error"
    elif imc<18.5:
        peso="Bajo peso"
    elif imc>=18.5 and imc<=25:
        peso="Peso normal"
    elif imc>25:
        peso="Sobrepeso"
    return peso
    
def main():
    peso=float(input("Peso"))
    est=float(input("Estatura"))
    imc=calcularIMC(peso,est)
    pesoR=pesoIdeal(imc)
    print("El IMC es:",imc)
    print ("De acuerdo a tu IMC tienes:",pesoR)
main()