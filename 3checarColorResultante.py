# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Mezcla dos colores e imprime el color resultante

def checarColorValido(color): #Checa si el color ingresado es un color primario
    if ((color == "rojo") or (color == "azul") or (color =="amarillo")):
        return 1
    else :
        return 0
def calcularColorResultante(uno, dos): #Calcula el resultante de la mezcla de dos colores
    if ( (uno == "rojo" and dos == "azul") or (uno == "azul" and dos == "rojo")):
        resultante="morado"
    elif ( (uno == "rojo" and dos == "amarillo") or (uno == "amarillo" and dos == "rojo") ):
        resultante = "naranja"
    elif ( (uno == "azul" and dos == "amarillo") or (uno == "amarillo" and dos == "azul") ):
        resultante = "verde"
    elif (uno==dos):
        resultante = uno
        
    return resultante
    
def main():
    colorUno = input ("Dame el primer color primario")
    colorDos = input ("Dame el segundo color primario")

    colorUno = colorUno.lower()
    colorDos = colorDos.lower()

    if ( checarColorValido(colorUno)== 0 or checarColorValido(colorDos)== 0):
        print ("Color ingresado no es un color valido")

    else:
        colorResultante = calcularColorResultante(colorUno, colorDos)
        print ("El color que resulta de mezclar %s y %s es %s" % (colorUno,colorDos, colorResultante))

main()
