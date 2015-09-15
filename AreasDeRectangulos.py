#encoding UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, A01377515
#Calcular area y perimetro de 2 rectangulos y dibujarlos

from Graphics import *

#Funcion para dibujar el rectanguo 1
def dibujarRectangulo1(ven,a1,b1) :
    lado1 = Line( (100,100), (100,100+a1) )
    lado2 = Line( (100,100+a1), (100+b1,100+a1) )
    lado3 = Line( (100+b1,100+a1), (100+b1,100) )
    lado4 = Line( (100+b1,100), (100,100) )
    lado1.draw(ven)
    lado2.draw(ven)
    lado3.draw(ven)
    lado4.draw(ven)
    lado1.setColor( Color("blue") )
    lado2.setColor( Color("blue") )
    lado3.setColor( Color("blue") )
    lado4.setColor( Color("blue") )
    
#Funcion para dibujar el rectangulo 2
def dibujarRectangulo2(ven,a2,b2) :
    lado1 = Line( (200,200), (200,200+a2) )
    lado2 = Line( (200,200+a2), (200+b2,200+a2) )
    lado3 = Line( (200+b2,200+a2), (200+b2,200) )
    lado4 = Line( (200+b2,200), (200,200) )
    lado1.draw(ven)
    lado2.draw(ven)
    lado3.draw(ven)
    lado4.draw(ven)
    lado1.setColor( Color("red") )
    lado2.setColor( Color("red") )
    lado3.setColor( Color("red") )
    lado4.setColor( Color("red") )
    
#Funcion para crear la ventana y dibujar los rectangulos en ella
def dibujarVentana(a1,b1,a2,b2) :
    ven = Window("Area y Perimetro",800,600)
    dibujarRectangulo1(ven,a1,b1)
    dibujarRectangulo2(ven,a2,b2)

#funcion para calcular el area de los rectangulos
def calcularArea(a,b) :
    return a*b
    
#Funcion para calcular el perimetro de los rectangulos
def calcularPer(a,b) :
    perimetro = 2*a + 2*b
    return perimetro
    
#Funcion para determinar el rectagulo con mayor area
def mayorArea(a1,a2) :
    if a1 > a2 :
        return "El primer rectagulo tiene mayor area"
    elif a2 > a1 :
        return "El segundo rectangulo tiene mayor area"
    else :
        return "El area de ambos rectangulos es igual"
    
def main() :
    alturaRec1 = int( input("Escribe la altura del primer rectangulo"))
    baseRec1 = int( input("Escribe la base del primer rectangulo"))
    alturaRec2 = int( input("Escribe la altura del segundo rectangulo"))
    baseRec2 = int( input("Escribe la base del segundo rectangulo"))
    a1 = calcularArea(alturaRec1,baseRec1)
    p1 = calcularPer(alturaRec1,baseRec1)
    a2 = calcularArea(alturaRec2,baseRec2)
    p2 = calcularPer(alturaRec2,baseRec2)    
    print( "El area del primer rectangulo es: %i y el perimetro es: %i" %(a1,p1))
    print( "El area del segundo rectangulo es: %i y el perimetro es: %i" %(a2,p2))
    print(mayorArea(a1,a2))
    dibujarVentana(alturaRec1,baseRec1,alturaRec2,baseRec2)

main()