#Encoding: UTF-8
#Autor: Manuel Zavala Gomez
#Areas de Rectangulos

from Graphics import*

def main():
    altura= int(input("Altura"))
    base= int(input("Base"))
    altura2= int(input("Altura"))
    base2= int(input("Base"))
    
    window = Window("Rectangulos", 300,300)
    dibujarRectangulo(window,base,altura,"red")
    dibujarRectangulo2(window,base2,altura2,"yellow") 
    
    calcularPerimetro (altura,base,altura2,base2)
    calcularArea(altura,base,altura2,base2)
    
def dibujarRectangulo(window,base,altura,color):
    x2 = 50+base
    y2 = 100+altura
    shape = Rectangle ((50,100),(x2,y2))   
    shape.fill = Color(color) 
    shape.draw(window) 
    
def dibujarRectangulo2(window,base2,altura2,color):
    x2 = 50+base2
    y2 = 100+altura2
    shape = Rectangle ((100,50),(x2,y2))   
    shape.fill = Color(color) 
    shape.draw(window)     
      
def calcularPerimetro (altura,base,altura2,base2):
    p1= (altura*2)+(base*2)
    p2= (altura2*2)+(base2*2)
    print ("Tu primer perímetro es:",p1)
    print ("Tu segundo perímetro es:" ,p2)
    
def calcularArea(altura,base,altura2,base2):
    a1= (altura*base)
    a2= (altura2*base2)
    print ("Tu primer area es:", a1 )
    print ("Tu segunda area es:", a2)   
    if a1 > a2 :
        print ("El rectangulo 1 tiene mayor area")
    elif a1 < a2:
        print("El rectangulo 2 tiene mayor area")
    elif a1== a2:
        print("Las dos areas son iguales")
        
def dibujarRectangulo(window,base,altura,color):
    x2 = 50+base
    y2 = 100+altura
    shape = Rectangle ((50,100),(x2,y2))   
    shape.fill = Color(color) 
    shape.draw(window)       
main()