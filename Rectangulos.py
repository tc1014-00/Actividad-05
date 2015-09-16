#Encoding:UTF-8
#Autor:Paola Castillo Nacif
#El programa mostrara dos rectangulos asi como su perimetro y area

from Graphics import*

def calcularAreaUno(b1,h1):
    areaUno=(b1*h1)
    return areaUno
    
def calcularPerimetroUno(b1,h1):
    perimetroUno=((b1*2)+(h1*2))
    return perimetroUno
    
def calcularAreaDos(b2,h2):
    areaDos=(b2*h2)
    return areaDos
    
def calcularPerimetroDos(b2,h2):
    perimetroDos=((b2*2)+(h2*2))
    return perimetroDos
    
def calcularAreaM(areaRec1,areaRec2):
    am=""
    if (areaRec1>areaRec2):
        am="El area del rectangulo 1 es mayor"
    elif (areaRec1==areaRec2):
        am="El area es igual para los dos rectangulos"
    else:
        am="El area del rectangulo 2 es mayor"
        
    return am
    
def calcularPerM(perRec1,perRec2):
    pm=""
    if (perRec1>perRec2):
        pm="El perimetro del rectangulo 1 es mayor"
    elif (perRec1==perRec2):
        pm="El perimetro es igual para los dos rectangulos"
    else:
        pm="El perimetro del rectangulo 2 es mayor"
    return pm
    
def dibujarRectangulos(baseR1,alturaR1,baseR2,alturaR2):
    ventana=Window("Rectangulos",1200,1000)
    
    rectanguloUno=Arrow((200,200),0)
    rectanguloUno.draw(ventana)
    rectanguloUno.penDown()
    rectanguloUno.forward(baseR1)
    rectanguloUno.rotate(90)
    rectanguloUno.forward(alturaR1)
    rectanguloUno.rotate(90)
    rectanguloUno.forward(baseR1)
    rectanguloUno.rotate(90)
    rectanguloUno.forward(alturaR1)
    rectanguloUno.rotate(90)
    
    rectanguloDos=Arrow((500,500),0)
    rectanguloDos.setColor(Color("red"))
    rectanguloDos.draw(ventana)
    rectanguloDos.penDown()
    rectanguloDos.setColor(Color("red"))
    rectanguloDos.forward(baseR2)
    rectanguloDos.rotate(90)
    rectanguloDos.setColor(Color("red"))
    rectanguloDos.forward(alturaR2)
    rectanguloDos.rotate(90)
    rectanguloDos.setColor(Color("red"))
    rectanguloDos.forward(baseR2)
    rectanguloDos.rotate(90)
    rectanguloDos.setColor(Color("red"))
    rectanguloDos.forward(alturaR2)
    rectanguloDos.rotate(90)

def main(): 
    b1=int(input("Inserte medida de la base del rectangulo uno"))
    h1=int(input("Inserte medida de la altura del rectangulo uno"))
    b2=int(input("Inserte medida de la base del rectangulo dos"))
    h2=int(input("Inserte medida de la altura del rectangulo dos"))
    areaRec1=calcularAreaUno(b1,h1)
    perRec1=calcularPerimetroUno(b1,h1)
    areaRec2=calcularAreaDos(b2,h2)
    perRec2=calcularPerimetroDos(b2,h2)
    areaMayor=calcularAreaM(areaRec1,areaRec2)
    perimetroMayor=calcularPerM(perRec1,perRec2)
    print("El area del primer rectangulo es:",areaRec1)
    print("El perimetro del primer rectangulo es:",perRec1)
    print("El area del segundo rectangulo es:",areaRec2)
    print("El perimetro del segundo rectangulo es:",perRec2)
    print(areaMayor)
    print(perimetroMayor)
    baseR1=b1
    alturaR1=h1
    baseR2=b2
    alturaR2=h2
    dibujarRectangulos(baseR1,alturaR1,baseR2,alturaR2)
main()
    