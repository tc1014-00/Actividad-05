#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, A01377515
#Leer 2 colores primarios e imprimir el color de la mezcla de estos colores

#Funcion para realizar la mezcla de colores
def mezcla(c1,c2) :
    a = c1.lower()
    b = c2.lower()
    if ( a == "amarillo" or a == "azul" or a == "rojo" ) and ( b == "amarillo" or b == "azul" or b == "rojo" ) :
        if ( a == "amarillo" and b == "azul" ) or ( b == "amarillo" and a == "azul" ) :
            color = "Verde"
        elif ( a == "amarillo" and b == "rojo" ) or ( b == "amarillo" and a == "rojo" ) :
            color = "Naranja"
        elif (  a == "azul" and b == "rojo" ) or ( b == "azul" and a == "rojo" ) : 
            color = "Morado"
        elif a == b :
            color = a
    else :
        color = "un error"
    return color

def main() :
    color1 = input("Escribe un color")
    color2 = input("Escribe otro color")
    print( "El color que resultante es %s" %mezcla(color1,color2) )
    
    
main()