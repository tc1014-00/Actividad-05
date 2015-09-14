# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Obtiene el area de dos rectangulos a partir de sus medidas, compara las areas y dibuja los rectangulos

#NOTAS: Profesor, tengo problemas con el Calico de mi maquina
#por lo que use estos comandos para un compilador estandar.
#Si gusta, puede probarlo con el IDLE de python.

import turtle 

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

def dibujarRectangulo (x, y): #Utiliza Turtle para dibujar un rectangulo a partir de su base y altura
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left (90)

    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left (90)

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

    turtle.pen (pencolor = "red")
    dibujarRectangulo(xUno, yUno)

    turtle.pen (pencolor = "blue")
    dibujarRectangulo(xDos, yDos)

main()



        
