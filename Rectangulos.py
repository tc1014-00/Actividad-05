#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Dimensiones de dos rectangulos

from Graphics import*

def calculaPerimetro(a,l):
    P=(a*2)+(l*2)
    return P
    
def calculaArea(a,l):
    A=a*l
    return A
    

def comparaRectangulos(A,A2):
    if (A>A2):
        return 'El area del primer rectangulo es mayor'
    elif(A<A2):
        return 'El area del segundo rectangulo es mayor'
    else:
        return 'Las areas de los rectangulos son iguales'

def dibujar(a,l,a2,l2):
    v=Window('Rectangulos',800,600)
    dibujar1(v,a,l)
    dibujar2(v,a2,l2)
    
def dibujar1(v,a,l):
    fig1=Line((0,0),(a,0))
    fig2=Line((a,0),(a,l))
    fig3=Line((a,l),(0,l))
    fig4=Line((0,l),(0,0))
    fig1.draw(v)
    fig2.draw(v)
    fig3.draw(v)
    fig4.draw(v)
    
def dibujar2(v,a,l):
    fig1=Line((0,0),(a,0))
    fig2=Line((a,0),(a,l))
    fig3=Line((a,l),(0,l))
    fig4=Line((0,l),(0,0))
    fig1.setColor(Color('red'))
    fig2.setColor(Color('red'))
    fig3.setColor(Color('red'))
    fig4.setColor(Color('red'))
    fig1.draw(v)
    fig2.draw(v)
    fig3.draw(v)
    fig4.draw(v)

def main():
    ancho=int(input('Ancho del primer rectangulo'))
    ancho2=int(input('Ancho del segundo rectangulo'))
    largo=int(input('Largo del primer rectangulo'))
    largo2=int(input('Largo del segundo rectangulo'))
    perimetro=calculaPerimetro(ancho,largo)
    perimetro2=calculaPerimetro(ancho2,largo2)
    area=calculaArea(ancho,largo)
    area2=calculaArea(ancho2,largo2)
    mayor=comparaRectangulos(area,area2)
    print('El perimetro del primer rectangulo es: ',perimetro,)
    print('El area del primer rectangulo es: ',area)
    print('El perimetro del segundo rectangulo es: ',perimetro2)
    print('El area del segundo rectangulo es: ',area2)
    print('El rectangulo mas grande es: ',mayor)
    dibujar(ancho,largo,ancho2,largo2)
main()