#encoding:UTF-8
#Autor:Ernesto Cruz López A01169052
#Calcular el IMC

def dividir(kg,m):
    IMC=((kg)/(m**2))
    return IMC
    
def calcularValor(iMC):
    peso=""
    if iMC<=18.4:
        peso="Bajo peso"
    elif 18.5<=iMC and iMC<=25:
        peso="Peso normal"
    else:
        peso="Sobre peso"
                 
    
    return peso
         
def main():
    kg= float(input("Peso en kg"))
    m= float(input("Altura en m"))
    
    if m<=0 or kg<0:
        print("Error")
    else:
        iMC =dividir(kg,m)
        estado=calcularValor(iMC)
        print ("Indice de Masa Corporal: %.02f"%iMC)
        print ("Tu estado es:",estado)
main()