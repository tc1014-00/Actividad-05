#encoding: UTF-8
# Autor: Mauricio Medrano 
# Descripcion: Calcular la mezcla de colores. 

def ColorCorrecto(colorUno): 
    if colorUno == "rojo" or colorUno == "azul" or colorUno =="amarillo":
        return 1
    else :
        return 0
def calcularColorNuevo(uno, dos): 
    if colorUno == "rojo" and ColorDos == "azul" or colorUno == "azul" and colorDos == "rojo":
        colorNuevo="morado"
    elif colorUno == "rojo" and colorDos == "amarillo" or colorUno == "amarillo" and colorDos == "rojo":
        colorNuevo = "naranja"
    elif colorUno == "azul" and colorDos == "amarillo" or colorUno == "amarillo" and colorDos == "azul":
        colorNuevo = "verde"
    elif colorUno==coloDos:
        coloNuevo = colorUno
        
    return colorNuevo
    
def main():
    colorUno = input ("Dame el primer color primario")
    colorDos = input ("Dame el segundo color primario")

    colorUno = colorUno.lower()
    colorDos = colorDos.lower()

    if ( colorCorrecto(colorUno)== 0 or colorColorCorrecto(colorDos)== 0):
        print ("Color ingresado no es un color valido")

    else:
        colorNuevo = calcularColorNuevo(colorUno, colorDos)
       print ("El color que resulta de mezclar %s y %s es %s" % (colorUno, colorDos, colorNuevo))
main()