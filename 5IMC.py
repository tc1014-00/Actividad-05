# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Calcula el IMC a partir del peso y la estatura

def calcularIMC(peso,estatura): #Calcula el IMC y devuelve el estado de la persona
    IMC = peso / estatura**2
    if (IMC < 18.5):
        estado = "Bajo peso"
    elif (IMC >= 18.5 and IMC <= 25):
        estado = "Peso normal"
    elif (IMC > 25):
        estado = "Sobrepeso"
    return (IMC,estado)
    

def main():
    peso = float (input ("¿Cuantos kilogramos pesa?"))
    estatura = float (input ("¿Cuantos metros mide?"))

    if (peso<=0 or estatura <= 0):
        print ("ERROR. Estatura o peso invalido")
    else:
        (IMC, estado) = calcularIMC(peso, estatura)
        
        print ("Peso:", format (peso, '.2f'))
        print ("Estatura:", format (estatura, '.2f'), "m")
        print ("IMC:", format (IMC, '.2f'))
        print ("Estado:", estado)

main()
