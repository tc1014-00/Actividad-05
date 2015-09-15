# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Calcula los perimetros y areas de dos rectangulos y los compara

from Graphics import*

def calcularPerimetro1(r1b,r1h):
    pr1=(2*r1b)+(2*r1h)
    return pr1

def calcularPerimetro2(r2b,r2h):
    pr2=(2*r2b)+(2*r2h)
    return pr2
    
def calcularArea1(r1b,r1h):
    ar1=r1b*r1h
    return ar1
    
def calcularArea2(r2b,r2h):
    ar2=r2b*r2h
    return ar2

def compararAreas(ar1,ar2):
    if ar1>ar2:
        return "El primer rectangulo es el de mayor area"
    elif ar2>ar1:
        return "El segundo rectangulo es el de mayor area"    
    elif ar1==ar2:
        return "Las areas de ambos rectangulos son iguales"

def dibujarRectangulos(r1b,r1h,r2b,r2h):
    v=Window("Rectangulos",800,800)
    r1=Arrow((10,400),0)
    r1.draw(v)
    r1.penDown()
    r1.forward(r1b)
    r1.rotate(90)
    r1.forward(r1h)
    r1.rotate(90)
    r1.forward(r1b)
    r1.rotate(90)
    r1.forward(r1h)
    
    r2=Arrow((400,400),0)
    r2.draw(v)
    r2.penDown()
    r2.forward(r2b)
    r2.rotate(90)
    r2.forward(r2h)
    r2.rotate(90)
    r2.forward(r2b)
    r2.rotate(90)
    r2.forward(r2h)
    r2.color=Color("Red")
    
    

def main():
    r1b=int(input("Ingrese la medida de la base del rectangulo 1(cm)"))
    r1h=int(input("Ingrese la medida de la altura del rectangulo 1(cm)"))
    r2b=int(input("Ingrese la medida de la base del rectangulo 2(cm)"))
    r2h=int(input("Ingrese la medida de la altura del rectangulo 2(cm)"))
    pr1=calcularPerimetro1(r1b,r1h)
    pr2=calcularPerimetro2(r2b,r2h)
    ar1=calcularArea1(r1b,r1h)
    ar2=calcularArea2(r2b,r2h)
    print("Perimetro del primer rectangulo:",pr1,"cm")
    print("Area del primer rectangulo:",ar1,"cm")
    print("Perimetro del segundo rectangulo:",pr2,"cm")
    print("Area del segundo rectangulo:",ar2,"cm")
    print(compararAreas(ar1,ar2))
    dibujarRectangulos(r1b,r1h,r2b,r2h)
    
main()