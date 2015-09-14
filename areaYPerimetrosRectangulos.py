#encoding: UTF-8
# Jorge Daniel Juarez Ruiz
# Calcular el area y perimetro de dos rectangulos, decir cual area es mayor y dibujarlos

from Graphics import*

def calcularPerimetro(a,l):
    p=(2*a)+(2*l)
    return p
    
def calcularArea(a,l):
    ar=a*l
    return ar
    
def compararRectangulos(a1,a2):
    if a1<a2:
        return "El area del rectangulo 2 es mayor"
    elif a2<a1:
        return "El area del rectangulo 1 es mayor"
    else: 
        return "Las areas son iguales"

def dibujar(a1,l1,a2,l2):
    v= Window ("Rectangulos",800,600)
    dibujarA(v, a1,l1)
    dibujarB(v, a2,l2)
    
def dibujarA(v,a,l):
    figa= Line((0,0), (a,0))
    figb= Line((a,0), (a,l))
    figc= Line((a,l), (0,l))
    figd= Line((0,l),(0,0))
    figa.draw(v)
    figb.draw(v)
    figc.draw(v)
    figd.draw(v)
    
def dibujarB(v,a,l):
    fig1= Line((0,0), (a,0))
    fig2= Line((a,0), (a,l))
    fig3= Line((a,l), (0,l))
    fig4= Line((0,l),(0,0))
    fig1.setColor(Color("blue"))
    fig2.setColor(Color("blue"))
    fig3.setColor(Color("blue"))
    fig4.setColor(Color("blue"))
    fig1.draw(v)
    fig2.draw(v)
    fig3.draw(v)
    fig4.draw(v)
    

def main():
    ancho1=int(input("Ancho rectangulo 1"))
    largo1=int(input("Largo rectangulo 1"))
    ancho2=int(input("Ancho rectangulo 2"))
    largo2=int(input("Largo rectangulo 2"))
    perimetro1=calcularPerimetro(ancho1,largo1)
    perimetro2=calcularPerimetro(ancho2,largo2)
    area1=calcularArea(ancho1,largo1)
    area2=calcularArea(ancho2,largo2)
    mayor=compararRectangulos(area1,area2)
    print("El perimetro del rectangulo 1 es:", perimetro1)
    print("El perimetro del rectangulo 2 es:", perimetro2)
    print("El area del rectangulo 1 es:", area1)
    print("El area del rectangulo 2 es:", area2)
    print (mayor)
    dibujar(ancho1,largo1,ancho2,largo2)
    
main()