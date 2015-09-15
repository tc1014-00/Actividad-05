# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Obtiene el area de dos rectangulos a partir de sus medidas, compara las areas y dibuja los rectangulos

from Graphics import *


def obtenerArea (x,y): #Obtiene el area de un rectangulo a partir de su base y altura
    area = x * y
    return area

def obtenerPerimetro (x, y): #Obtiene el perimetro de un rectangulo
    perimetro = 2*x + 2*y
    return perimetro

def checarMayorArea (uno, dos): #Checa de dos areas cual es mayor o si son iguales
    if (uno<dos):
        mayor = "dos"
    elif (uno>dos):
        mayor = "uno"
    else :
        mayor = "igual"
    return mayor

def dibujarRectangulo (turtle, x, y):#Utiliza Turtle para dibujar un rectangulo a partir de su base y altura
    turtle.forward (x)
    turtle.rotate (90)
    turtle.forward (y)
    turtle.rotate (90)
    turtle.forward (x)
    turtle.rotate (90)
    turtle.forward (y)
    turtle.rotate (90)
    
def main():
    xUno = float (input ("Dame el largo del primer rectangulo"))
    yUno = float (input ("Dame la altura del primer rectangulo"))
    xDos = float (input ("Dame el largo del segundo rectangulo"))
    yDos = float (input ("Dame la altura del segundo rectangulo"))
    

    areaUno = obtenerArea (xUno, yUno)
    areaDos = obtenerArea (xDos, yDos)
    print ("El area del rectangulo uno es: %.2f unidades cuadradas" % areaUno)
    print ("El area del rectangulo dos es: %.2f unidades cuadradas" % areaDos)


    
    perimetroUno = obtenerPerimetro (xUno, yUno)
    perimetroDos = obtenerPerimetro (xDos, yDos)
    print ("El perimetro del rectangulo uno es: %.2f unidades" % perimetroUno)
    print ("El perimetro del rectangulo dos es: %.2f unidades" % perimetroDos)
    

    mayor = checarMayorArea (areaUno, areaDos)
    if (mayor == "igual"):
        print ("El area de los rectangulos es igual")
    else:
        print ("El area mayor es la del rectangulo", mayor)

    ventana = Window ("Ventana",800,400)
    tortu = Turtle ((400, 200),0) #Crea la tortuga y la centra en la ventana. Inicia en 0 grados
    tortu.draw (ventana)
    tortu.penDown()

    tortu.pen.color = Color("red")
    dibujarRectangulo(tortu, xUno, yUno)
    
    tortu.penUp()
    tortu.penDown()
    tortu.pen.color = Color("blue")
    dibujarRectangulo(tortu, xDos, yDos)

main()



        
