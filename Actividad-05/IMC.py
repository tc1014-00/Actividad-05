#encoding:UTF-8
#Autor:Hector Manuel Takami Flores
#Calcula el IMC y da aservaciones sobre el peso de la persona

def calculaIMC(peso,estatura):
    
    imc=(peso/(estatura*estatura))
    return imc
    
def determinaPesoPersona(peso,estatura):
    iMc=calculaIMC(peso,estatura)
    if iMc<=0:
        iMc="Error"
        
    elif iMc<=18.5:
        iMc="Bajo de peso"
        
    elif iMc<=25:
        iMc="Peso Normal"
        
    elif iMc>25:
        iMc="Sobrepeso"
    else:
        iMc= ""
        
    return iMc
        

def main():
    peso=float(input("Introduzca el peso (Kg)"))
    estatura=float(input("Introduzca la estatura (Mtrs)"))
    iMC=calculaIMC(peso,estatura)
    print("IMC= %f"%iMC)
    pesoImc=determinaPesoPersona(peso,estatura)
    print(pesoImc)
    
    
    
main()